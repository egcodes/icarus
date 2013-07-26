#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, atexit
from datetime import datetime

from PyQt4 import QtCore, Qt
from PyQt4 import QtGui

from mainwindowhost import Ui_Form


class XTerm(QtGui.QX11EmbedContainer): #XTerm -> Terminal ekrani icin kullanilan class'dir. Windows'da bu class calistirilmadan once yorum satirlari ile  iptal edilmelidir. Cunku Windows'da X bulunmamaktadir.
	def __init__(self, parent, xterm_cmd="xterm", ip=0):
		QtGui.QX11EmbedContainer.__init__(self, parent)
		self.ip = ip
		self.xterm_cmd = xterm_cmd
		self.process = QtCore.QProcess(self)
		self.show_term()
		self.connect(self.process, Qt.SIGNAL("finished(int, QProcess::ExitStatus)"), self.on_term_close)
		atexit.register(self.kill)

	def kill(self):
		try:
			self.process.kill()
			self.process.waitForFinished()
		except Exception, error:
			self.printErrorMessage("Warning", "kill", error)
			
		
	def show_term(self):
		if self.ip == 0:
			args = [
			"-into",
			str(self.winId()),
			"-bg",
			"#000000", # self.palette().color(QPalette.Background).name(), 
			"-fg",
			"#7fff00", #self.palette().color(QPalette.Foreground).name(), 
			# border 
			"-b", "0",
			"-w", "0",
			# blink cursor 
			"-bc",
			]
		else:
			args = [
			"-into",
			str(self.winId()),
			"-bg",
			"#000000", # self.palette().color(QPalette.Background).name(), 
			"-fg",
			"#7fff00", #self.palette().color(QPalette.Foreground).name(), 
			# border 
			"-b", "0",
			"-w", "0",
			# blink cursor 
			"-bc",
			"-e", "ssh root@%s"%str(self.ip)
			]
			
		self.process.start(self.xterm_cmd, args)
		if self.process.error() == Qt.QProcess.FailedToStart:
			self.printErrorMessage("Warning", "show_term", "Xterm not installed")

	def on_term_close(self, exit_code, exit_status):
		self.close()

	def printErrorMessage(self, errorMessage, functionName, message): # hata mesaji basmasini ve loglamasini saglayan fonksiyon
		today = datetime.now()
		with open("logHermes", "a") as f:
			f.writelines("%s --> %s: XTerm.%s() -> %s\n"%(today, errorMessage, functionName, message))
		print "%s --> %s: %s() -> XTerm.%s\n"%(today, errorMessage, functionName, message)
		

class MainWindow(QtGui.QMainWindow, Ui_Form):
	def __init__(self):	
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		
		if os.name == "posix":
			xTerm = XTerm(self.textBrowserScreenshot)
			xTerm.setGeometry(0, 0 , 1165, 450)
			
		#Buton ve sinyal baglantilari
		self.checkBoxProcessListOtherUser.clicked.connect(self.listProcessNonRoot)
		self.refreshProcess.clicked.connect(self.getProcessList)
		self.refreshServices.clicked.connect(self.getServicesList)
		self.pushButtonServiceStart.clicked.connect(self.startService)
		self.pushButtonServiceStop.clicked.connect(self.stopService)
		self.pushButtonServiceRestart.clicked.connect(self.restartService)
		self.pushButtonKillProcess.clicked.connect(self.killProcess)
		self.pushButtonKillWindow.clicked.connect(self.killWindow)
		self.pushButton.clicked.connect(self.shutdownWindow)
		self.lineEditSearchProcess.textChanged.connect(self.searchProcess)
		self.tableWidgetServices.itemClicked.connect(self.enableServiceButton)
		self.tableWidgetProcessList.itemClicked.connect(self.enableProcessButton)

		#Logo ve buton resimleri
		self.setLogoAndIcon()
		
		#Process ve Servis sayisi
		self.processCount = 0
		self.servicesCount = 0	

		#Servis listesi alininmasi
		self.getServicesList(click=0)
		
		#Process list "top" komutunun ciktisi ile alinmasi
		self.getProcessList(click=0)

		#Klasik bilgilerin alinmasi
		self.updateHostInfo()

		self.startTimer(30000)
	
		self.statusBar().showMessage("%s is ready"%self.hostname)

	def timerEvent(self, e):
		#Servis listesi alininmasi
		self.getServicesList(click=0)
		
		#Process list "top" komutunun ciktisi ile alinmasi
		self.getProcessList(click=0)

		#Klasik bilgilerin alinmasi
		self.updateHostInfo()

	def setLogoAndIcon(self):
		logo = QtGui.QPixmap("images/icarus.gif")
		self.label.setPixmap(logo)
		icon = Qt.QIcon(Qt.QPixmap("images/refresh.png"))
		self.refreshProcess.setIcon(icon)
		self.refreshServices.setIcon(icon)
		
	def updateHostInfo(self):
		#Host bilgilerinin labellara yazilmasi
		self.hostname = os.popen("hostname").read().strip()
		self.labelMachineName.setText(self.hostname)
		for i in os.popen("ifconfig").readlines():
			if i.find('inet addr') != -1:
				ip = i.split()[1][5:]
				if ip != "127.0.0.1":
					self.labelNodeId.setText(ip)
	

		#Uptime ve Users
		str1 = self.listInfo[0][6:]
		self.labelUptimeUsers.setText(str1[:str1.find('user') + 4])
		
		#Load average
		items = str1[str1.rfind(':') + 1:].split(',')
		self.progressBarLoad1.setValue(float(items[0]))
		self.labelLoad1.setText(items[0].strip())
		self.progressBarLoad5.setValue(float(items[1]))
		self.labelLoad5.setText(items[1].strip())
		self.progressBarLoad15.setValue(float(items[2]))
		self.labelLoad15.setText(items[2].strip())
	
	
	def getServicesList(self, click=1):
		servicesCountUp = 0
		servicesCountDown = 0
		widgetTableName = self.tableWidgetServices

		widgetTableName.setRowCount(0)
		widgetTableName.clearContents()
		listInfo = os.popen("service --status-all").readlines()

		OsSystem = os.popen("cat /etc/*release").read().split()[0]

		if OsSystem == "CentOS":
			listInfo2= []
			for i in listInfo:
				if i.find("running") != -1:
					status = "+"
					serviceName = i.split()[0]
					listInfo2.append(' [ ' + status + ' ]' + '  ' + serviceName + '\n')
				elif i.find("stopped") != -1:
					status = "-"
					serviceName = i.split()[0]
					listInfo2.append(' [ ' + status + ' ]' + '  ' + serviceName + '\n')
				else:
					status = "?"
					serviceName = i.split()[0]
					listInfo2.append(' [ ' + status + ' ]' + '  ' + serviceName + '\n')
			del listInfo
			listInfo = listInfo2

		for i, tableRow in enumerate(listInfo):
			widgetTableName.insertRow(i)
			items = tableRow.split()
			
			#Service name
			QtItem = QtGui.QTableWidgetItem()
			QtItem.setText(str(items[3]).capitalize())
			brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
			brush.setStyle(QtCore.Qt.SolidPattern)
			QtItem.setBackground(brush)
			QtItem.setCheckState(QtCore.Qt.Unchecked)
			icon = QtGui.QIcon("images/computer.png")
			QtItem.setIcon(icon)
			widgetTableName.setItem(i, 0, QtItem)
			
			#Service durumu
			QtItem = QtGui.QTableWidgetItem()
			if items[1] == "+":
				brush = QtGui.QBrush(QtGui.QColor(160, 255, 0))
				brush.setStyle(QtCore.Qt.SolidPattern)
				QtItem.setBackground(brush)
				QtItem.setText("Up")
				servicesCountUp += 1
			elif items[1] == "-":
				brush = QtGui.QBrush(QtGui.QColor(255, 60, 0))
				brush.setStyle(QtCore.Qt.SolidPattern)
				QtItem.setBackground(brush)
				QtItem.setText("Down")
				servicesCountDown += 1
			else:
				brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
				brush.setStyle(QtCore.Qt.SolidPattern)
				QtItem.setBackground(brush)
				QtItem.setText("Unknown")
				servicesCountDown += 1
			widgetTableName.setItem(i, 1, QtItem)

			
			#Service output
			QtItem = QtGui.QTableWidgetItem()
			QtItem.setText(listInfo[i])
			widgetTableName.setItem(i, 2, QtItem)


		self.servicesCount = i + 1
		
		#Servisler Up/Down durumu
		QtItem = QtGui.QTableWidgetItem()
		brush = QtGui.QBrush(QtGui.QColor(160, 255, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		QtItem.setBackground(brush)
		QtItem.setText(str(servicesCountUp))
		self.tableWidgetServicesStatus.setItem(0, 0, QtItem)

		QtItem = QtGui.QTableWidgetItem()
		brush = QtGui.QBrush(QtGui.QColor(255, 60, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		QtItem.setBackground(brush)
		QtItem.setText(str(servicesCountDown))
		self.tableWidgetServicesStatus.setItem(0, 1, QtItem)

	def getProcessList(self, click=1):
		if not click:
			stdout = os.popen("top -n 1 -b").readlines()
			self.infoProcess = stdout
			
		widgetTableName = self.tableWidgetProcessList
		
		widgetTableName.setColumnCount(0)
		widgetTableName.setRowCount(0)
		widgetTableName.clear()
	
		if self.infoProcess == "empty":
			self.statusBar().showMessage("Unsuccessfull: Processes not received...")
			return	
		self.listInfo = self.infoProcess
		
		self.listTop = []
		for i, j in enumerate(self.listInfo):
			self.listTop.append(j)
			if i == 4:
				break
		
		#Sutun isimleri
		widgetTableName.setColumnCount(len(self.listInfo[6].split()))
		for i, columnName in enumerate(self.listInfo[6].split()):
			item = QtGui.QTableWidgetItem(str(columnName))
			item.setText(str(columnName))
			widgetTableName.setHorizontalHeaderItem(i, item)
		
		self.listInfo.pop()
		for i, tableRow in enumerate(self.listInfo):
			if i < 7:
				continue
			widgetTableName.insertRow(i - 7)
			for substring in tableRow.split('"'):
				items = substring.split()
				for l, item in enumerate(items):
					QtItem = QtGui.QTableWidgetItem()
					if item.isdigit():
						QtItem.setData(0, int(item))
					else:
						try:
							num = float(item)
							QtItem.setData(0, num)
						except:
							QtItem.setText(item)
					if l == 0 or l == 1:
						brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
						brush.setStyle(QtCore.Qt.SolidPattern)
						QtItem.setBackground(brush)
					if l == 0:
						QtItem.setCheckState(QtCore.Qt.Unchecked)
						icon = QtGui.QIcon("images/computer.png")
						QtItem.setIcon(icon)
					widgetTableName.setItem(i - 7, l, QtItem)
					
		self.processCount = i - 6

		#Proses Total/Zombie durumlari
		tasks = self.listTop[1][7:]
		item = tasks.split(',')
		processTotal = item[0].split()[0]
		processRunning = item[1].split()[0]
		processSleeping = item[2].split()[0]
		processStopped = item[3].split()[0]
		processZombie = item[4].split()[0]
		
		QtItem = QtGui.QTableWidgetItem()
		brush = QtGui.QBrush(QtGui.QColor(160, 255, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		QtItem.setBackground(brush)
		QtItem.setText(processTotal)
		self.tableWidgetProcessStatus.setItem(0, 0, QtItem)
		
		QtItem = QtGui.QTableWidgetItem()
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		QtItem.setBackground(brush)
		QtItem.setText(processRunning)
		self.tableWidgetProcessStatus.setItem(0, 1, QtItem)
		
		QtItem = QtGui.QTableWidgetItem()
		brush = QtGui.QBrush(QtGui.QColor(160, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		QtItem.setBackground(brush)
		QtItem.setText(processSleeping)
		self.tableWidgetProcessStatus.setItem(0, 2, QtItem)
		
		QtItem = QtGui.QTableWidgetItem()
		brush = QtGui.QBrush(QtGui.QColor(255, 160, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		QtItem.setBackground(brush)
		QtItem.setText(processStopped)
		self.tableWidgetProcessStatus.setItem(0, 3, QtItem)
		
		QtItem = QtGui.QTableWidgetItem()
		brush = QtGui.QBrush(QtGui.QColor(255, 60, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		QtItem.setBackground(brush)
		QtItem.setText(processZombie)
		self.tableWidgetProcessStatus.setItem(0, 4, QtItem)
		
		self.updateHostInfo()
		
			
	def startService(self):
		self.statusBar().showMessage("Service is starting, please wait...")
		for i in range(self.servicesCount):
			item = self.tableWidgetServices.item(i, 0)
			if item.checkState():
				serviceName = str(self.tableWidgetServices.item(i, 0).text()).lower()
				os.popen("service %s start"%serviceName.strip())
				output = os.popen("service %s status"%serviceName.strip()).read()
				if output.find("running"):
					QtItem = Qt.QTableWidgetItem()
					QtItem.setText(output)
					self.tableWidgetServices.setItem(i, 2, QtItem)

					QtItem = Qt.QTableWidgetItem()
					brush = QtGui.QBrush(QtGui.QColor(160, 255, 0))
					brush.setStyle(QtCore.Qt.SolidPattern)
					QtItem.setBackground(brush)
					QtItem.setText("Up")					
					self.tableWidgetServices.setItem(i, 1, QtItem)
					self.statusBar().showMessage("Successfull: The service has been started...")
				else:
					self.statusBar().showMessage("Unsuccessfull: The service could not be started...")

	def stopService(self):
		self.statusBar().showMessage("Service is stopping, please wait...")

		for i in range(self.servicesCount):
			item = self.tableWidgetServices.item(i, 0)
			if item.checkState():
				serviceName = str(self.tableWidgetServices.item(i, 0).text()).lower()
				output = os.popen("service %s stop"%serviceName.strip()).read()
				if output.find("stopped"):
					QtItem = Qt.QTableWidgetItem()
					QtItem.setText(output)
					self.tableWidgetServices.setItem(i, 2, QtItem)

					QtItem = Qt.QTableWidgetItem()
					brush = QtGui.QBrush(QtGui.QColor(255, 60, 0))
					brush.setStyle(QtCore.Qt.SolidPattern)
					QtItem.setBackground(brush)
					QtItem.setText("Down")					
					self.tableWidgetServices.setItem(i, 1, QtItem)
					self.statusBar().showMessage("Successfull: The service has been stopped...")
				else:
					self.statusBar().showMessage("Unsuccessfull: The service could not be stopped...")
					self.thread1.terminate()

	def restartService(self):
		self.statusBar().showMessage("Service is restarting, please wait...")
		for i in range(self.servicesCount):
			item = self.tableWidgetServices.item(i, 0)
			if item.checkState():
				serviceName = str(self.tableWidgetServices.item(i, 0).text()).lower()
				output = os.popen("service %s restart"%serviceName.strip()).read()
				if output.find("running"):
					QtItem = Qt.QTableWidgetItem()
					QtItem.setText(output)
					self.tableWidgetServices.setItem(i, 2, QtItem)

					QtItem = Qt.QTableWidgetItem()
					brush = QtGui.QBrush(QtGui.QColor(160, 255, 0))
					brush.setStyle(QtCore.Qt.SolidPattern)
					QtItem.setBackground(brush)
					QtItem.setText("Up")					
					self.tableWidgetServices.setItem(i, 1, QtItem)
					self.statusBar().showMessage("Successfull: The service has been restarted...")
				else:
					self.statusBar().showMessage("Unsuccessfull: The service could not be restarted...")
				
	def searchServices(self):
		searchText = self.lineEditSearchServices.text()
		count = self.servicesCount
		for i in range(count):
			self.tableWidgetServices.hideRow(i)
			for j in range(3):
				if str(Qt.QTableWidgetItem(self.tableWidgetServices.item(i, j)).text()).find(searchText) != -1:
					self.tableWidgetServices.showRow(i)
					
	def searchProcess(self):
		searchText = self.lineEditSearchProcess.text()
		count = self.processCount
		for i in range(count):
			self.tableWidgetProcessList.hideRow(i)
			for j in range(12):
				if str(Qt.QTableWidgetItem(self.tableWidgetProcessList.item(i, j)).text()).find(searchText) != -1:
					self.tableWidgetProcessList.showRow(i)
		
	def killProcess(self):
		for i in range(self.processCount):
			item = self.tableWidgetProcessList.item(i, 0)
			if item:
				if item.checkState():
					output = os.system("kill %s"%str(self.tableWidgetProcessList.item(i, 0).text()).strip())
					if not output:
						self.tableWidgetProcessList.removeRow(i)
						self.statusBar().showMessage("Successfull: The process has been kill...")
						self.processCount -= 1
					else:
						self.statusBar().showMessage("Unsuccessfull: The process could not be kill...")
	
	def killWindow(self):
		QtCore.QTimer.singleShot(3000, self.killWindowCmd)
		QtGui.QMessageBox().information(self, 'ICARUS', 
			'Click a window to kill its process 3 seconds later.')
		
	
	def killWindowCmd(self):
		os.system('xkill')

	def listProcessNonRoot(self):
		if self.checkBoxProcessListOtherUser.isChecked():
			for i in range(self.processCount):
				if Qt.QTableWidgetItem(self.tableWidgetProcessList.item(i, 1)).text() == "root":
					self.tableWidgetProcessList.hideRow(i)
		else:
			for i in range(self.processCount):
				self.tableWidgetProcessList.showRow(i)
	
	def enableServiceButton(self):
		for i in range(self.servicesCount):
			item = self.tableWidgetServices.item(i, 0)
			if item.checkState():
				self.pushButtonServiceStart.setEnabled(True)
				self.pushButtonServiceStop.setEnabled(True)
				self.pushButtonServiceRestart.setEnabled(True)
				break
			else:
				self.pushButtonServiceStart.setEnabled(False)
				self.pushButtonServiceStop.setEnabled(False)
				self.pushButtonServiceRestart.setEnabled(False)
		
	def enableProcessButton(self):
		for i in range(self.processCount):
			item = self.tableWidgetProcessList.item(i, 0)
			if item.checkState():
				self.pushButtonKillProcess.setEnabled(True)
				break	
			else:
				self.pushButtonKillProcess.setEnabled(False)
		
	def shutdownWindow(self):
		self.close()

			
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	mainWindow = MainWindow()
	mainWindow.show()
	app.exec_()
