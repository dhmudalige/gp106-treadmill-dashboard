import sys
import platform
from datetime import datetime

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import sqlite3

from gui.splashscreen import Ui_SplashScreen

from gui.datainput import Ui_DataInput

from gui.dashboard_testing import Ui_Dashboard

import functions.treadmill as tm

## GLOBAL VARIABLES
counter = 0

global rpm
global radius

radius = 0.25
rpm = 60


## DASHBOARD
class Dashboard(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)            

        global display_speed
        global display_distance
        global display_calories
        global display_steps        

        treadmill_operation = tm.TreadmillParameters(rpm,radius)
        treadmill_operation.get_user(1,weight,height)
        treadmill_operation.get_time(time)
        treadmill_operation.start()

        display_speed = treadmill_operation.speed
        display_distance = treadmill_operation.distance
        display_calories = treadmill_operation.calories
        display_steps = treadmill_operation.steps

        #Define the action corresponding to the pushbutton "Start"
        self.ui.pushButtonStart.clicked.connect(self.mytimer)

        #Define the action corresponding to the pushbutton "Stop"
        self.ui.pushButtonStop.clicked.connect(self.pause)

        self.ui.lcdNumberSteps.display(int(display_steps))
        self.ui.lcdNumberCalories.display(display_calories)
        self.ui.lcdNumberSpeed.display(display_speed)
        self.ui.lcdNumberDistance.display(display_distance)
        self.ui.lcdNumberTime.display(time)

        self.ui.comboBoxDistance.activated[str].connect(self.distanceUnitsChanged) 
        self.ui.comboBoxSpeed.activated[str].connect(self.speedUnitsChanged) 


    def speedUnitsChanged(self, text):
        if text == "m/s":
            self.ui.lcdNumberSpeed.display(display_speed)
        elif text == "km/h":
            self.ui.lcdNumberSpeed.display(display_speed * 3.6)
        elif text == "mph":
            self.ui.lcdNumberSpeed.display(display_speed * 2.23694) 

    def distanceUnitsChanged(self, text):
        if text == "m":
            self.ui.lcdNumberDistance.display(display_distance)
        elif text == "km":
            self.ui.lcdNumberDistance.display(display_distance / 1000)
        elif text == "miles":
            self.ui.lcdNumberDistance.display(display_distance / 1609.344)


    def pause(self):
        print("Pause")

    def mytimer(self):

        print("Current date and time :- " , datetime.now())

        try:
            def count():
                global mytimestamp
                global total_seconds

                mytimestamp = 66600
                total_seconds = 0
                
                while True:
                    # To manage the intial delay. 
                    if mytimestamp == 66600:
                        display="Starting..."
                    else:
                        tt = datetime.fromtimestamp(mytimestamp)
                        display = tt.strftime("%H:%M:%S")
                        total_seconds = int(tt.hour)*3600 + int(tt.minute)*60 + int(tt.second)
                                    
                    print(display)
                    return total_seconds

                    mytimestamp += 1                        

            # Triggering the start of the count. 
            count()
            
        except KeyboardInterrupt:
            pause()
            

## DATA INPUT
class DataInput(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_DataInput()
        self.ui.setupUi(self)
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #Define the action corresponding to the pushbutton "Enter"
        self.ui.pushButtonEnter.clicked.connect(self.submit)

    # Create Submit function for database
    def submit(self):

        global weight
        global height
        global time

        weight = int(self.ui.plainTextEditWeight.toPlainText())
        height = int(self.ui.plainTextEditHeight.toPlainText())
        time = int(self.ui.plainTextEditTime.toPlainText())
        
        # SHOW DASHBOARD WINDOW
        self.dashboardwindow = Dashboard()
        self.dashboardwindow.show()

        # CLOSE DATA INPUT WINDOW
        self.close()

        # Connect to the database
        conn = sqlite3.connect('treadmillapplication_testing.db')
        # Create cursor
        c = conn.cursor()

        # Insert Into Table
        c.execute("INSERT INTO users(first_name, last_name, gender, age, height, weight, total_time, total_distance, total_calories_burnt, total_number_of_steps) VALUES (:f_name, :l_name, :gender, :age, :height, :weight, :total_time, :distance, :calories, :steps)",
                {
                    'f_name': self.ui.plainTextEditFname.toPlainText(),
                    'l_name': self.ui.plainTextEditLname.toPlainText(),
                    'gender': self.ui.plainTextEditGender.toPlainText(),
                    'age': self.ui.plainTextEditAge.toPlainText(),
                    'height': self.ui.plainTextEditHeight.toPlainText(),
                    'weight': self.ui.plainTextEditWeight.toPlainText(),
                    'total_time': self.ui.plainTextEditTime.toPlainText(),
                    'distance': display_distance,
                    'calories': display_calories,
                    'steps': int(display_steps)
                })

        #Commit Changes
        conn.commit()
        # Close Connection 
        conn.close()

## SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI (INTERFACE CODES)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW (SPLASH SCREEN)
        self.show()
        ### END ###

    ## APP FUNCTIONS

    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW DATA INPUT WINDOW
            self.datainputwindow = DataInput()
            self.datainputwindow.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splashscreenwindow = SplashScreen()

    # datainputwindow = DataInput()
    # dashboardwindow = Dashboard()

    sys.exit(app.exec_())