
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        if not Dashboard.objectName():
            Dashboard.setObjectName(u"Dashboard")
        Dashboard.resize(600, 725)
        self.centralwidget = QWidget(Dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {	\n"
"	background-color: rgb(56, 58, 89);	\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.lcdNumberCalories = QLCDNumber(self.frame)
        self.lcdNumberCalories.setObjectName(u"lcdNumberCalories")
        self.lcdNumberCalories.setGeometry(QRect(220, 480, 141, 71))
        self.lcdNumberSpeed = QLCDNumber(self.frame)
        self.lcdNumberSpeed.setObjectName(u"lcdNumberSpeed")
        self.lcdNumberSpeed.setGeometry(QRect(220, 190, 141, 71))
        self.lcdNumberDistance = QLCDNumber(self.frame)
        self.lcdNumberDistance.setObjectName(u"lcdNumberDistance")
        self.lcdNumberDistance.setGeometry(QRect(220, 380, 141, 71))
        self.lcdNumberTime = QLCDNumber(self.frame)
        self.lcdNumberTime.setObjectName(u"lcdNumberTime")
        self.lcdNumberTime.setGeometry(QRect(200, 80, 351, 71))
        self.lcdNumberTime.setFrameShape(QFrame.StyledPanel)
        self.lcdNumberTime.setLineWidth(1)
        self.lcdNumberSteps = QLCDNumber(self.frame)
        self.lcdNumberSteps.setObjectName(u"lcdNumberSteps")
        self.lcdNumberSteps.setGeometry(QRect(220, 280, 141, 71))
        self.labelGroupName = QLabel(self.frame)
        self.labelGroupName.setObjectName(u"labelGroupName")
        self.labelGroupName.setGeometry(QRect(60, 600, 471, 61))
        self.labelGroupName.setStyleSheet(u"color: rgb(170, 0, 255);")
        self.label_time = QLabel(self.frame)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setGeometry(QRect(60, 80, 141, 71))
        self.label_time.setStyleSheet(u"color:rgb(85, 255, 255);")
        self.label_speed = QLabel(self.frame)
        self.label_speed.setObjectName(u"label_speed")
        self.label_speed.setGeometry(QRect(70, 190, 141, 71))
        self.label_speed.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.label_steps = QLabel(self.frame)
        self.label_steps.setObjectName(u"label_steps")
        self.label_steps.setGeometry(QRect(70, 280, 141, 71))
        self.label_steps.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.label_distance = QLabel(self.frame)
        self.label_distance.setObjectName(u"label_distance")
        self.label_distance.setGeometry(QRect(50, 380, 141, 71))
        self.label_distance.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.label_calories = QLabel(self.frame)
        self.label_calories.setObjectName(u"label_calories")
        self.label_calories.setGeometry(QRect(50, 480, 141, 71))
        self.label_calories.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.comboBoxSpeed = QComboBox(self.frame)
        self.comboBoxSpeed.setObjectName(u"comboBoxSpeed")
        self.comboBoxSpeed.setGeometry(QRect(390, 210, 81, 41))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxSpeed.setFont(font)
        self.comboBoxSpeed.addItem("m/s")
        self.comboBoxSpeed.addItem("km/h")
        self.comboBoxSpeed.addItem("mph")
        self.comboBoxDistance = QComboBox(self.frame)
        self.comboBoxDistance.setObjectName(u"comboBoxDistance")
        self.comboBoxDistance.setGeometry(QRect(390, 400, 81, 41))
        self.comboBoxDistance.setFont(font)
        self.comboBoxDistance.addItem("m")
        self.comboBoxDistance.addItem("km")
        self.comboBoxDistance.addItem("miles")
        self.label_cal = QLabel(self.frame)
        self.label_cal.setObjectName(u"label_cal")
        self.label_cal.setGeometry(QRect(390, 480, 51, 71))
        self.label_cal.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.frame)

        Dashboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dashboard)

        QMetaObject.connectSlotsByName(Dashboard)
    # setupUi

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"Dashboard", None))
        self.labelGroupName.setText(QCoreApplication.translate("Dashboard", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Group 76 - Treadmill Dashboard</span></p></body></html>", None))
        self.label_time.setText(QCoreApplication.translate("Dashboard", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">Time</span></p></body></html>", None))
        self.label_speed.setText(QCoreApplication.translate("Dashboard", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Speed</span></p></body></html>", None))
        self.label_steps.setText(QCoreApplication.translate("Dashboard", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Steps</span></p></body></html>", None))
        self.label_distance.setText(QCoreApplication.translate("Dashboard", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Distance</span></p></body></html>", None))
        self.label_calories.setText(QCoreApplication.translate("Dashboard", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Calories</span></p></body></html>", None))
        self.comboBoxSpeed.setPlaceholderText("")
        self.comboBoxDistance.setPlaceholderText("")
        self.label_cal.setText(QCoreApplication.translate("Dashboard", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">cal</span></p></body></html>", None))
    # retranslateUi

