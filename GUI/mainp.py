
from PyQt5 import QtCore, QtGui, QtWidgets
from load_screen import Ui_LoadScreen
import sys
import time
from main_window import Ui_MainWindow
import sys
sys.path.insert(0,".")
from BUS import*
from DTO import *
from DAO import CategoryDAO
from add_category import add_category_dialog,QtWidgets
from add_group import add_group_dia
from add_size import add_size_dia
from add_base import add_base_dia
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
        
        
        
        
        ##Can nhac nut nay##Mở dialog add
        self.ui.pushButton_23.clicked.connect(self.open_add_category_btn)
        self.ui.GroupAcc_add.clicked.connect(self.open_add_group_btn)
        self.ui.pushButton_29.clicked.connect(self.open_add_size_dialog)
        self.ui.pushButton_35.clicked.connect(self.open_add_base_dialog)
        #find function//
        self.ui.pushButton_21.clicked.connect(self.find_category_btn)
        self.ui.GroupAcc_search.clicked.connect(self.find_group_btn)
        self.ui.pushButton_27.clicked.connect(self.find_size_btn)
        self.ui.pushButton_33.clicked.connect(self.find_base_btn)
        ##Load_Value 
        self.auto_get_value_group()
        self.auto_get_value_category()
        self.auto_get_value_Size()
        self.auto_get_value_Base()
        ##Deletecategory
        self.ui.pushButton_26.clicked.connect(self.deleteCategory)
        self.ui.pushButton_38.clicked.connect(self.deleteBase)
        self.ui.pushButton_32.clicked.connect(self.deleteSize)
        self.ui.Groupacc_delete.clicked.connect(self.deleteGroupacc)
        ##reload Function
        self.ui.pushButton_22.clicked.connect(self.auto_get_value_category)
        self.ui.GroupAcc_info.clicked.connect(self.auto_get_value_group)
        self.ui.pushButton_28.clicked.connect(self.auto_get_value_Size)
        self.ui.pushButton_34.clicked.connect(self.auto_get_value_Base)
    #Delete##########################
    def deleteCategory(self):
        row=self.ui.tableWidget_3.currentRow()
        col=self.ui.tableWidget_3.currentColumn()
        id=self.ui.tableWidget_3.item(row,col).text()
        cate=Category()
        cate.setId(id)
        Catebus=CategoryBUS()
        Catebus.readListCategory()
        if Catebus.deleteCategory(cate):
            print("ok")
            self.auto_get_value_category()
    def deleteBase(self):
        row=self.ui.tableWidget_5.currentRow()
        col=self.ui.tableWidget_5.currentColumn()
        id=self.ui.tableWidget_5.item(row,col).text()
        base=Base()
        base.setId(id)
        basebl=BaseBUS()
        basebl.readListBase()
        if basebl.deleteBase(base):
            print("ok")
            self.auto_get_value_Base()
    def deleteSize(self):
        row=self.ui.tableWidget_4.currentRow()
        col=self.ui.tableWidget_4.currentColumn()
        id=self.ui.tableWidget_4.item(row,col).text()
        print(id)
        size=Size()
        size.setId(id)
        sizebl=SizeBUS()
        sizebl.readListSize()
        if sizebl.deleteSize(size):
            print("ok")
            self.auto_get_value_Size()
    def deleteGroupacc(self):
        row=self.ui.tableWidget.currentRow()
        col=self.ui.tableWidget.currentColumn()
        id=self.ui.tableWidget.item(row,col).text()
        print(id)
        group=Group()
        group.setId(id)
        groupbl=GroupBUS()
        groupbl.readListGroup()
        if groupbl.deleteGroup(group):
            print("ok")
            self.auto_get_value_group()

    #############################################    
        #AutoGetValue#############################################
   

    def auto_get_value_category(self):
        self.ui.tableWidget_3.clearContents()
        catebus= CategoryBUS()
        catebus.readListCategory()
        self.ui.tableWidget_3.setRowCount(len(catebus.listCategory))
        count=0
        
        for category in catebus.listCategory:
            idITEM=QtWidgets.QTableWidgetItem(str(category.getId()))
            displayITEM=QtWidgets.QTableWidgetItem(category.getDisplay())
            self.ui.tableWidget_3.setItem(count,0,idITEM)
            self.ui.tableWidget_3.setItem(count,1,displayITEM)
            count+=1
   
    def auto_get_value_group(self):
        group_Bus= GroupBUS()
        group_Bus.readListGroup()
        self.ui.tableWidget.setRowCount(len(group_Bus.listGroup))
        count=0
        for group in group_Bus.listGroup:
            idITEM=QtWidgets.QTableWidgetItem(str(group.getId()))
            displayITEM=QtWidgets.QTableWidgetItem(group.getDisplay())
            self.ui.tableWidget.setItem(count,0,idITEM)
            self.ui.tableWidget.setItem(count,1,displayITEM)
            count+=1
   
    def auto_get_value_Size(self):
        self.ui.tableWidget_4.clearContents()
        SizeBus=SizeBUS()
        SizeBus.readListSize()
        self.ui.tableWidget_4.setRowCount(len(SizeBus.listSize))
        count=0
        for sizeItem in SizeBus.listSize:
            idITEM=QtWidgets.QTableWidgetItem(str(sizeItem.getId()))
            displayITEM=QtWidgets.QTableWidgetItem(sizeItem.getDisplay())
            sizeItem=QtWidgets.QTableWidgetItem(str(sizeItem.getPriority()))
            self.ui.tableWidget_4.setItem(count,0,idITEM)
            self.ui.tableWidget_4.setItem(count,1,displayITEM)
            self.ui.tableWidget_4.setItem(count,2,sizeItem)
            count+=1
    def auto_get_value_Base(self):
        self.ui.tableWidget_5.clearContents()
        baseBl=BaseBUS()
        baseBl.readListBase()
        self.ui.tableWidget_5.setRowCount(len(baseBl.listBase))
        count=0
        for Items in baseBl.listBase:
            idITEM=QtWidgets.QTableWidgetItem(str(Items.getId()))
            displayITEM=QtWidgets.QTableWidgetItem(Items.getDisplay())
            self.ui.tableWidget_5.setItem(count,0,idITEM)
            self.ui.tableWidget_5.setItem(count,1,displayITEM)
            count+=1

    #####################################################
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
        ###Create add_cattegory_dialog
        ########
    def open_add_category_btn(self):
        Dialog = QtWidgets.QDialog()
        ui = add_category_dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
    def open_add_group_btn(self):
        Dialog = QtWidgets.QDialog()
        ui = add_group_dia()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
    def open_add_size_dialog(self):
        Dialog = QtWidgets.QDialog()
        ui = add_size_dia()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
    def open_add_base_dialog(self):
        Dialog = QtWidgets.QDialog()
        ui = add_base_dia()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

        ###############################
    def find_category_btn(self):
        find_str=self.ui.LineEdit_find_category.text()
        catebus=CategoryBUS()
        catebus.readListCategory()
        list=catebus.findCategoriesByName(find_str)
        self.ui.tableWidget_3.clearContents()
        count=0
        for category in list:
            idITEM=QtWidgets.QTableWidgetItem(str(category.getId()))
            displayITEM=QtWidgets.QTableWidgetItem(category.getDisplay())
            self.ui.tableWidget_3.setItem(count,0,idITEM)
            self.ui.tableWidget_3.setItem(count,1,displayITEM)
            count+=1
    def find_group_btn(self):
        find_str=self.ui.LineEdit_find_group.text()
        groupbus=GroupBUS()
        groupbus.readListGroup()
        list=groupbus.findGroupByName(find_str)
        self.ui.tableWidget.clearContents()
        count=0
        for group in list:
            idITEM=QtWidgets.QTableWidgetItem(str(group.getId()))
            displayITEM=QtWidgets.QTableWidgetItem(group.getDisplay())
            self.ui.tableWidget.setItem(count,0,idITEM)
            self.ui.tableWidget.setItem(count,1,displayITEM)
            count+=1
    def find_size_btn(self):
        find_str=self.ui.Line_edit_findSize.text()
        sizebus=SizeBUS()
        sizebus.readListSize()
        list=sizebus.findSizesByName(find_str)
        count=0
        self.ui.tableWidget_4.clearContents()
        for sizeItem in list:
            idITEM=QtWidgets.QTableWidgetItem(str(sizeItem.getId()))
            displayITEM=QtWidgets.QTableWidgetItem(sizeItem.getDisplay())
            sizeItem=QtWidgets.QTableWidgetItem(str(sizeItem.getPriority()))
            self.ui.tableWidget_4.setItem(count,0,idITEM)
            self.ui.tableWidget_4.setItem(count,1,displayITEM)
            self.ui.tableWidget_4.setItem(count,2,sizeItem)
            count+=1
    def find_base_btn(self):
        find_str=self.ui.Line_edit_findBase.text()
        basebl=BaseBUS()
        basebl.readListBase()
        list=basebl.findBasesByName(find_str)
        count=0
        self.ui.tableWidget_5.clearContents()
        for Items in list:
            idITEM=QtWidgets.QTableWidgetItem(str(Items.getId()))
            displayITEM=QtWidgets.QTableWidgetItem(Items.getDisplay())
            self.ui.tableWidget_5.setItem(count,0,idITEM)
            self.ui.tableWidget_5.setItem(count,1,displayITEM)
            count+=1
    ####################


        
        


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
        COUNTER+=2





if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    Loading = handler()
    Loading.show()
    sys.exit(app.exec_())

