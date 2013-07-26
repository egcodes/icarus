# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowhost.ui'
#
# Created: Thu Jul 25 02:47:39 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1200, 635)
        Form.setMinimumSize(QtCore.QSize(1200, 635))
        Form.setMaximumSize(QtCore.QSize(1200, 635))
        Form.setStyleSheet(_fromUtf8("\n"
"QRadioButton\n"
"{\n"
"    color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #cccccc;\n"
"    border: 0px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"QRadioButton::indicator:checked\n"
"{\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(79, 79, 79, 255), stop:0.530928 rgba(125, 125, 125, 255), stop:0.659794 rgba(220, 220, 220, 255), stop:1 rgba(207, 207, 207, 255));\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"\n"
"QCheckBox\n"
"{\n"
"    color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked, QCheckBox::indicator:unchecked\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #cccccc;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 3px;\n"
"}\n"
"QCheckBox::indicator:checked\n"
"{\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.4, fx:0.5, fy:0.5, stop:0 rgba(79, 79, 79, 255), stop:0.530928 rgba(125, 125, 125, 255), stop:0.659794 rgba(220, 220, 220, 255), stop:1 rgba(207, 207, 207, 255));\n"
"}\n"
"QCheckBox::indicator\n"
"{\n"
"    border-radius: 3px;\n"
"}\n"
"QCheckBox::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"    color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    background-color: rgb(240, 240, 240); \n"
"   border:1px solid;\n"
"    border-color: #cecece;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: rgb(150, 150, 150);\n"
"    border-radius: 2px;\n"
"    width: 10px;\n"
"    margin: 1px;\n"
"}\n"
"QPushButton\n"
"{\n"
"    color: #000000;\n"
"   border: 1px;\n"
"    border-color: rgb(162, 162, 162);\n"
"   border-style: solid;\n"
"    border-bottom-right-radius: 5;\n"
"    border-bottom-left-radius: 5;\n"
"    border-top-right-radius: 5;\n"
"    background-color: qlineargradient(spread:pad, x1:0.486, y1:1, x2:0.486631, y2:0.3925, stop:0 rgba(227, 227, 227, 255), stop:0.909091 rgba(250, 250, 250, 255));\n"
"    border-top-left-radius: 5;\n"
"\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    background-color: rgb(214, 214, 214);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: rgb(204, 204, 204);\n"
"}\n"
"            \n"
"QTabBar::tab {\n"
"    padding-left: 150px;\n"
"    padding-right: 150px;\n"
"    padding-top: 5px;\n"
"\n"
"    border-style: solid;\n"
"    border-top-left-radius: 5;\n"
"    border-top-right-radius: 5;\n"
"    border-width: 1px;\n"
"    border-color: #aeaeae;\n"
"    background-color: rgb(230, 230, 230);\n"
"}"))
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1181, 611))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(990, 10, 85, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        self.pushButton_3.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(900, 10, 85, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabWidget = QtGui.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(1, 110, 1179, 500))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.pushButtonKillProcess = QtGui.QPushButton(self.tab_6)
        self.pushButtonKillProcess.setEnabled(False)
        self.pushButtonKillProcess.setGeometry(QtCore.QRect(350, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        self.pushButtonKillProcess.setFont(font)
        self.pushButtonKillProcess.setObjectName(_fromUtf8("pushButtonKillProcess"))
        self.checkBoxProcessListOtherUser = QtGui.QCheckBox(self.tab_6)
        self.checkBoxProcessListOtherUser.setGeometry(QtCore.QRect(520, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        self.checkBoxProcessListOtherUser.setFont(font)
        self.checkBoxProcessListOtherUser.setObjectName(_fromUtf8("checkBoxProcessListOtherUser"))
        self.refreshProcess = QtGui.QPushButton(self.tab_6)
        self.refreshProcess.setGeometry(QtCore.QRect(300, 20, 41, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        self.refreshProcess.setFont(font)
        self.refreshProcess.setText(_fromUtf8(""))
        self.refreshProcess.setObjectName(_fromUtf8("refreshProcess"))
        self.tableWidgetProcessList = QtGui.QTableWidget(self.tab_6)
        self.tableWidgetProcessList.setGeometry(QtCore.QRect(0, 80, 1171, 389))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        self.tableWidgetProcessList.setFont(font)
        self.tableWidgetProcessList.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidgetProcessList.setObjectName(_fromUtf8("tableWidgetProcessList"))
        self.tableWidgetProcessList.setColumnCount(0)
        self.tableWidgetProcessList.setRowCount(0)
        self.tableWidgetProcessList.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetProcessList.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidgetProcessList.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetProcessList.horizontalHeader().setStretchLastSection(True)
        self.label_10 = QtGui.QLabel(self.tab_6)
        self.label_10.setGeometry(QtCore.QRect(950, 44, 54, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEditSearchProcess = QtGui.QLineEdit(self.tab_6)
        self.lineEditSearchProcess.setGeometry(QtCore.QRect(1010, 40, 161, 25))
        self.lineEditSearchProcess.setText(_fromUtf8(""))
        self.lineEditSearchProcess.setObjectName(_fromUtf8("lineEditSearchProcess"))
        self.tableWidgetProcessStatus = QtGui.QTableWidget(self.tab_6)
        self.tableWidgetProcessStatus.setGeometry(QtCore.QRect(10, 10, 271, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetProcessStatus.sizePolicy().hasHeightForWidth())
        self.tableWidgetProcessStatus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidgetProcessStatus.setFont(font)
        self.tableWidgetProcessStatus.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidgetProcessStatus.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidgetProcessStatus.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidgetProcessStatus.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidgetProcessStatus.setWordWrap(False)
        self.tableWidgetProcessStatus.setObjectName(_fromUtf8("tableWidgetProcessStatus"))
        self.tableWidgetProcessStatus.setColumnCount(5)
        self.tableWidgetProcessStatus.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetProcessStatus.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../../../Projects/hermes/images/services.png")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon2)
        self.tableWidgetProcessStatus.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setIcon(icon2)
        self.tableWidgetProcessStatus.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setIcon(icon2)
        self.tableWidgetProcessStatus.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setIcon(icon2)
        self.tableWidgetProcessStatus.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetProcessStatus.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidgetProcessStatus.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetProcessStatus.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetProcessStatus.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetProcessStatus.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidgetProcessStatus.setItem(0, 4, item)
        self.tableWidgetProcessStatus.horizontalHeader().setDefaultSectionSize(55)
        self.tableWidgetProcessStatus.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidgetProcessStatus.verticalHeader().setVisible(False)
        self.pushButtonKillWindow = QtGui.QPushButton(self.tab_6)
        self.pushButtonKillWindow.setEnabled(True)
        self.pushButtonKillWindow.setGeometry(QtCore.QRect(430, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        self.pushButtonKillWindow.setFont(font)
        self.pushButtonKillWindow.setObjectName(_fromUtf8("pushButtonKillWindow"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("images/process.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_6, icon3, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.pushButtonServiceStop = QtGui.QPushButton(self.tab_5)
        self.pushButtonServiceStop.setEnabled(False)
        self.pushButtonServiceStop.setGeometry(QtCore.QRect(280, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonServiceStop.setFont(font)
        self.pushButtonServiceStop.setObjectName(_fromUtf8("pushButtonServiceStop"))
        self.tableWidgetServices = QtGui.QTableWidget(self.tab_5)
        self.tableWidgetServices.setGeometry(QtCore.QRect(0, 80, 1171, 389))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidgetServices.setFont(font)
        self.tableWidgetServices.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidgetServices.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidgetServices.setObjectName(_fromUtf8("tableWidgetServices"))
        self.tableWidgetServices.setColumnCount(3)
        self.tableWidgetServices.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetServices.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetServices.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetServices.setHorizontalHeaderItem(2, item)
        self.tableWidgetServices.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetServices.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidgetServices.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetServices.horizontalHeader().setStretchLastSection(True)
        self.pushButtonServiceRestart = QtGui.QPushButton(self.tab_5)
        self.pushButtonServiceRestart.setEnabled(False)
        self.pushButtonServiceRestart.setGeometry(QtCore.QRect(380, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonServiceRestart.setFont(font)
        self.pushButtonServiceRestart.setObjectName(_fromUtf8("pushButtonServiceRestart"))
        self.pushButtonServiceStart = QtGui.QPushButton(self.tab_5)
        self.pushButtonServiceStart.setEnabled(False)
        self.pushButtonServiceStart.setGeometry(QtCore.QRect(180, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonServiceStart.setFont(font)
        self.pushButtonServiceStart.setObjectName(_fromUtf8("pushButtonServiceStart"))
        self.refreshServices = QtGui.QPushButton(self.tab_5)
        self.refreshServices.setGeometry(QtCore.QRect(130, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.refreshServices.setFont(font)
        self.refreshServices.setText(_fromUtf8(""))
        self.refreshServices.setObjectName(_fromUtf8("refreshServices"))
        self.lineEditSearchServices = QtGui.QLineEdit(self.tab_5)
        self.lineEditSearchServices.setGeometry(QtCore.QRect(1010, 40, 161, 25))
        self.lineEditSearchServices.setText(_fromUtf8(""))
        self.lineEditSearchServices.setObjectName(_fromUtf8("lineEditSearchServices"))
        self.label_7 = QtGui.QLabel(self.tab_5)
        self.label_7.setGeometry(QtCore.QRect(945, 48, 61, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tableWidgetServicesStatus = QtGui.QTableWidget(self.tab_5)
        self.tableWidgetServicesStatus.setGeometry(QtCore.QRect(10, 10, 111, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetServicesStatus.sizePolicy().hasHeightForWidth())
        self.tableWidgetServicesStatus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidgetServicesStatus.setFont(font)
        self.tableWidgetServicesStatus.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidgetServicesStatus.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidgetServicesStatus.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidgetServicesStatus.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidgetServicesStatus.setShowGrid(False)
        self.tableWidgetServicesStatus.setWordWrap(False)
        self.tableWidgetServicesStatus.setObjectName(_fromUtf8("tableWidgetServicesStatus"))
        self.tableWidgetServicesStatus.setColumnCount(2)
        self.tableWidgetServicesStatus.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetServicesStatus.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../../../Projects/hermes/images/computer.jpg")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon4)
        self.tableWidgetServicesStatus.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setIcon(icon4)
        self.tableWidgetServicesStatus.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidgetServicesStatus.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetServicesStatus.setItem(0, 1, item)
        self.tableWidgetServicesStatus.horizontalHeader().setDefaultSectionSize(55)
        self.tableWidgetServicesStatus.horizontalHeader().setMinimumSectionSize(55)
        self.tableWidgetServicesStatus.verticalHeader().setVisible(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("images/services.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_5, icon5, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.textBrowserScreenshot = QtGui.QTextBrowser(self.tab)
        self.textBrowserScreenshot.setGeometry(QtCore.QRect(0, 0, 1175, 469))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.textBrowserScreenshot.setFont(font)
        self.textBrowserScreenshot.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(170, 255, 0);"))
        self.textBrowserScreenshot.setObjectName(_fromUtf8("textBrowserScreenshot"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("images/screenshot.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon6, _fromUtf8(""))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(5, 10, 81, 61))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(55, 30, 61, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(1080, 10, 85, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        self.pushButton.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("images/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox_2 = QtGui.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(430, 10, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.labelInfo_3 = QtGui.QLabel(self.groupBox_2)
        self.labelInfo_3.setGeometry(QtCore.QRect(10, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelInfo_3.setFont(font)
        self.labelInfo_3.setObjectName(_fromUtf8("labelInfo_3"))
        self.labelTasks_4 = QtGui.QLabel(self.groupBox_2)
        self.labelTasks_4.setGeometry(QtCore.QRect(10, 60, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelTasks_4.setFont(font)
        self.labelTasks_4.setObjectName(_fromUtf8("labelTasks_4"))
        self.labelMachineName_2 = QtGui.QLabel(self.groupBox_2)
        self.labelMachineName_2.setGeometry(QtCore.QRect(10, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelMachineName_2.setFont(font)
        self.labelMachineName_2.setObjectName(_fromUtf8("labelMachineName_2"))
        self.progressBarLoad5 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBarLoad5.setGeometry(QtCore.QRect(150, 42, 111, 16))
        self.progressBarLoad5.setProperty("value", 0)
        self.progressBarLoad5.setObjectName(_fromUtf8("progressBarLoad5"))
        self.progressBarLoad15 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBarLoad15.setGeometry(QtCore.QRect(150, 63, 111, 16))
        self.progressBarLoad15.setProperty("value", 0)
        self.progressBarLoad15.setInvertedAppearance(False)
        self.progressBarLoad15.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBarLoad15.setObjectName(_fromUtf8("progressBarLoad15"))
        self.progressBarLoad1 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBarLoad1.setGeometry(QtCore.QRect(150, 22, 111, 16))
        self.progressBarLoad1.setProperty("value", 0)
        self.progressBarLoad1.setObjectName(_fromUtf8("progressBarLoad1"))
        self.labelLoad1 = QtGui.QLabel(self.groupBox_2)
        self.labelLoad1.setGeometry(QtCore.QRect(110, 21, 41, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.labelLoad1.setFont(font)
        self.labelLoad1.setText(_fromUtf8(""))
        self.labelLoad1.setObjectName(_fromUtf8("labelLoad1"))
        self.labelLoad5 = QtGui.QLabel(self.groupBox_2)
        self.labelLoad5.setGeometry(QtCore.QRect(110, 41, 41, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.labelLoad5.setFont(font)
        self.labelLoad5.setText(_fromUtf8(""))
        self.labelLoad5.setObjectName(_fromUtf8("labelLoad5"))
        self.labelLoad15 = QtGui.QLabel(self.groupBox_2)
        self.labelLoad15.setGeometry(QtCore.QRect(110, 61, 41, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.labelLoad15.setFont(font)
        self.labelLoad15.setText(_fromUtf8(""))
        self.labelLoad15.setObjectName(_fromUtf8("labelLoad15"))
        self.line_4 = QtGui.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(0, 90, 1211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line_4.setFont(font)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(140, 10, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.labelMachineName_7 = QtGui.QLabel(self.groupBox)
        self.labelMachineName_7.setGeometry(QtCore.QRect(10, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelMachineName_7.setFont(font)
        self.labelMachineName_7.setObjectName(_fromUtf8("labelMachineName_7"))
        self.labelInfo_2 = QtGui.QLabel(self.groupBox)
        self.labelInfo_2.setGeometry(QtCore.QRect(10, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelInfo_2.setFont(font)
        self.labelInfo_2.setObjectName(_fromUtf8("labelInfo_2"))
        self.labelTasks_3 = QtGui.QLabel(self.groupBox)
        self.labelTasks_3.setGeometry(QtCore.QRect(10, 60, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelTasks_3.setFont(font)
        self.labelTasks_3.setObjectName(_fromUtf8("labelTasks_3"))
        self.labelMachineName = QtGui.QLabel(self.groupBox)
        self.labelMachineName.setGeometry(QtCore.QRect(100, 20, 201, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.labelMachineName.setFont(font)
        self.labelMachineName.setText(_fromUtf8(""))
        self.labelMachineName.setObjectName(_fromUtf8("labelMachineName"))
        self.labelNodeId = QtGui.QLabel(self.groupBox)
        self.labelNodeId.setGeometry(QtCore.QRect(100, 40, 201, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.labelNodeId.setFont(font)
        self.labelNodeId.setText(_fromUtf8(""))
        self.labelNodeId.setObjectName(_fromUtf8("labelNodeId"))
        self.labelUptimeUsers = QtGui.QLabel(self.groupBox)
        self.labelUptimeUsers.setGeometry(QtCore.QRect(100, 60, 201, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.labelUptimeUsers.setFont(font)
        self.labelUptimeUsers.setText(_fromUtf8(""))
        self.labelUptimeUsers.setObjectName(_fromUtf8("labelUptimeUsers"))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Icarus v1.0", None))
        self.frame.setProperty("class", _translate("Form", "MainFrame", None))
        self.pushButton_3.setText(_translate("Form", "About", None))
        self.pushButton_2.setText(_translate("Form", "Help", None))
        self.pushButtonKillProcess.setText(_translate("Form", "Kill Process", None))
        self.checkBoxProcessListOtherUser.setText(_translate("Form", "List of non-root", None))
        self.tableWidgetProcessList.setSortingEnabled(True)
        self.label_10.setText(_translate("Form", "Search", None))
        item = self.tableWidgetProcessStatus.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Total", None))
        item = self.tableWidgetProcessStatus.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Running", None))
        item = self.tableWidgetProcessStatus.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Sleeping", None))
        item = self.tableWidgetProcessStatus.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Stopped", None))
        item = self.tableWidgetProcessStatus.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Zombie", None))
        __sortingEnabled = self.tableWidgetProcessStatus.isSortingEnabled()
        self.tableWidgetProcessStatus.setSortingEnabled(False)
        self.tableWidgetProcessStatus.setSortingEnabled(__sortingEnabled)
        self.pushButtonKillWindow.setText(_translate("Form", "Kill Window", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "Process", None))
        self.pushButtonServiceStop.setText(_translate("Form", "Stop", None))
        self.tableWidgetServices.setSortingEnabled(True)
        item = self.tableWidgetServices.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name", None))
        item = self.tableWidgetServices.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Status", None))
        item = self.tableWidgetServices.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Info", None))
        self.pushButtonServiceRestart.setText(_translate("Form", "Restart", None))
        self.pushButtonServiceStart.setText(_translate("Form", "Start", None))
        self.label_7.setText(_translate("Form", "Search", None))
        item = self.tableWidgetServicesStatus.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Up", None))
        item = self.tableWidgetServicesStatus.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Down", None))
        __sortingEnabled = self.tableWidgetServicesStatus.isSortingEnabled()
        self.tableWidgetServicesStatus.setSortingEnabled(False)
        self.tableWidgetServicesStatus.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Services", None))
        self.textBrowserScreenshot.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Terminal", None))
        self.label_5.setText(_translate("Form", "ICARUS", None))
        self.pushButton.setText(_translate("Form", "Exit", None))
        self.groupBox_2.setTitle(_translate("Form", "Load Average", None))
        self.labelInfo_3.setText(_translate("Form", "Last 5 minutes    :", None))
        self.labelTasks_4.setText(_translate("Form", "Last 15 minutes  :", None))
        self.labelMachineName_2.setText(_translate("Form", "Last 1 minutes    :", None))
        self.groupBox.setTitle(_translate("Form", "Host Information", None))
        self.labelMachineName_7.setText(_translate("Form", "Host Name         :", None))
        self.labelInfo_2.setText(_translate("Form", "Host Ip                 :", None))
        self.labelTasks_3.setText(_translate("Form", "Uptime - Users  :", None))

