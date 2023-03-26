
from PyQt5 import QtCore, QtGui, QtWidgets
from load_screen import Ui_LoadScreen
import sys
import time
from main_window import Ui_MainWindow
#Globals
COUNTER=0
#MAIN WINDOW
class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.GroupAccount_btn.clicked.connect(self.click_groupAccount_btn)
        self.ui.Account_btn.clicked.connect(self.click_Account_btn)
        self.ui.Category_btn.clicked.connect(self.click_Category_btn)
        self.ui.Size_btn.clicked.connect(self.click_Size_btn)
        self.ui.Base_btn.clicked.connect(self.click_PizzaBase_btn)
        self.ui.pizza_btn.clicked.connect(self.click_Pizza_btn)
        self.ui.Order_btn.clicked.connect(self.click_Order_btn)
        self.ui.Stastical_btn.clicked.connect(self.click_Stastical_btn)
    def click_groupAccount_btn(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def click_Account_btn(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def click_Category_btn(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def click_Size_btn(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    def click_PizzaBase_btn(self):
        self.ui.stackedWidget.setCurrentIndex(4)
    def click_Pizza_btn(self):
        self.ui.stackedWidget.setCurrentIndex(5)
    def click_Order_btn(self):
        self.ui.stackedWidget.setCurrentIndex(6)
    def click_Stastical_btn(self):
        self.ui.stackedWidget.setCurrentIndex(7)

class handler(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui=Ui_LoadScreen()
        self.ui.setupUi(self)
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ##Hide background
        self.ui.background.setMaximumHeight(0)
        ##Intialize Animation
        self.logo_anim()
        self.describ_anim()
        self.start_anm()
        
        #QTIMER
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        
        #Timeer
        self.timer.start(35)
        

        ##Animated
    def logo_anim(self):
        opacity_eff=QtWidgets.QGraphicsOpacityEffect(self.ui.logoimage)
        self.ui.logoimage.setGraphicsEffect(opacity_eff)
        self.logo_opacity_animation=QtCore.QPropertyAnimation(
            opacity_eff,b'opacity',duration=1500,startValue=0,endValue=1
        )
        self.logo_opacity_animation.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        #self.logo_opacity_animation.start()
    def describ_anim(self):
        opacity_eff=QtWidgets.QGraphicsOpacityEffect(self.ui.background)
        self.ui.background.setGraphicsEffect(opacity_eff)

        geometry_anim=QtCore.QPropertyAnimation(
            self.ui.background,
            b'maximumHeight',
            duration=1000,
            startValue=0,
            endValue=228
        )
        geometry_anim.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        opacity_anim=QtCore.QPropertyAnimation(
            opacity_eff,b'opacity',duration=500,startValue=0,endValue=1
        )
        self.describ_anim=QtCore.QParallelAnimationGroup(self.ui.background)
        self.describ_anim.addAnimation(geometry_anim)
        self.describ_anim.addAnimation(opacity_anim)
        #self.describ_anim.start()
    def start_anm(self):
        self.anim_grp=QtCore.QSequentialAnimationGroup(self)
        self.anim_grp.addAnimation(self.logo_opacity_animation)
        self.anim_grp.addAnimation(self.describ_anim)
        self.anim_grp.start()
    ##Progess
    def progress(self):
        global COUNTER

        #Set value to progress bar
        self.ui.progressBar.setValue(int(COUNTER))
        self.ui.percentage.setText(f"{int(COUNTER)}%")

        #Close loadScreen and open app
        if COUNTER > 100:
            #stop timer
            self.timer.stop()

            #Show main window
            self.main=mainwindow()
            self.main.show()

            #CLose loading screen
            self.close()
        ##Increase COUNTER
        COUNTER+=0.5





if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    Loading = handler()
    Loading.show()
    sys.exit(app.exec_())

