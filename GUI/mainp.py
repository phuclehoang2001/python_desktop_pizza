
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMessageBox
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
        self.ui.pushButton_45.clicked.connect(self.find_order_btn)##Id_only
        ##Load_Value 
        self.auto_get_value_group()
        self.auto_get_value_category()
        self.auto_get_value_Size()
        self.auto_get_value_Base()
        self.auto_get_order_value()
        ##Deletecategory
        self.ui.pushButton_26.clicked.connect(self.deleteCategory)
        self.ui.pushButton_38.clicked.connect(self.deleteBase)
        self.ui.pushButton_32.clicked.connect(self.deleteSize)
        self.ui.Groupacc_delete.clicked.connect(self.deleteGroupacc)
        ##Fix
        self.ui.pushButton_24.clicked.connect(self.update_category)
        self.ui.GroupAcc_fix.clicked.connect(self.update_group)
        self.ui.pushButton_30.clicked.connect(self.update_size)
        self.ui.pushButton_36.clicked.connect(self.update_Base)
        ##reload Function
        self.ui.pushButton_22.clicked.connect(self.auto_get_value_category)
        self.ui.GroupAcc_info.clicked.connect(self.auto_get_value_group)
        self.ui.pushButton_28.clicked.connect(self.auto_get_value_Size)
        self.ui.pushButton_34.clicked.connect(self.auto_get_value_Base)
        self.ui.pushButton_46.clicked.connect(self.auto_get_order_value)
        ###Function for order
        self.ui.pushButton_50.clicked.connect(self.cancel_order)
        self.ui.pushButton_47.clicked.connect(self.check_order)
        self.ui.pushButton_48.clicked.connect(self.handler_order)

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
    #Update
    def update_group(self):
        row=self.ui.tableWidget.currentRow()
        id=self.ui.tableWidget.item(row,0).text()
        display=self.ui.tableWidget.item(row,1).text()
        grp=Group()
        grp.setId(id)
        grp.setDisplay(display)
        grpBus=GroupBUS()
        grpBus.updateGroup(grp)
    def update_category(self):
        row=self.ui.tableWidget_3.currentRow()
        id=self.ui.tableWidget_3.item(row,0).text()
        display=self.ui.tableWidget_3.item(row,1).text()
        cate=Category()
        cate.setId(id)
        cate.setDisplay(display)
        print(cate.getDisplay())
        catebus=CategoryBUS()
        catebus.updateCategory(cate)
    def update_size(self):
        row=self.ui.tableWidget_4.currentRow()
        id=self.ui.tableWidget_4.item(row,0).text()
        display=self.ui.tableWidget_4.item(row,1).text()
        priority=self.ui.tableWidget_4.item(row,2).text()
        sz=Size()
        sz.setId(id)
        sz.setDisplay(display)
        sz.setPriority(priority)
        szBus=SizeBUS()
        szBus.updateSize(sz)
    def update_Base(self):
        row=self.ui.tableWidget_5.currentRow()
        id=self.ui.tableWidget_5.item(row,0).text()
        display=self.ui.tableWidget_5.item(row,1).text()
        bse=Base()
        bse.setId(id)
        bse.setDisplay(display)
        bsebl=BaseBUS()
        bsebl.updateBase(bse)
      
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
    def auto_get_order_value(self):
        self.ui.tableWidget_7.clearContents()
        Orderbl=OrderBUS()
        Orderbl.readListOrder()
        list=Orderbl.showAllOrder()
        self.ui.tableWidget_7.setRowCount(len(Orderbl.listOrder))
        count=0
        for order in list:
            orderId=QtWidgets.QTableWidgetItem(str(order["OrderId"]))
            status_display=QtWidgets.QTableWidgetItem()
            
            if(order["EndStatus"].getId()>6):
                status_display.setBackground(QColor(255, 52, 52))
            elif(order["EndStatus"].getId()<6):
                status_display.setBackground(QColor(255, 255, 127))
            else:
                status_display.setBackground(QColor(5, 255, 109))
            status_display.setText(str(order["EndStatus"].getDisplay()))
            time_order=QtWidgets.QTableWidgetItem(str(order["StartStatusDetail"].getTimeCreated()))
            last_process=QtWidgets.QTableWidgetItem(str(order["EndStatusDetail"]))
            customer=QtWidgets.QTableWidgetItem(order["CustomerUsername"])
            employee=QtWidgets.QTableWidgetItem(order["HandlerUsername"])
            totalprice=QtWidgets.QTableWidgetItem(str(order["TotalPrice"]))
            amount=QtWidgets.QTableWidgetItem(str(order["Quantity"]))

            self.ui.tableWidget_7.setItem(count,0,orderId)
            self.ui.tableWidget_7.setItem(count,1,status_display)
            self.ui.tableWidget_7.setItem(count,2,time_order)
            self.ui.tableWidget_7.setItem(count,3,last_process)
            self.ui.tableWidget_7.setItem(count,4,customer)
            self.ui.tableWidget_7.setItem(count,5,employee)
            self.ui.tableWidget_7.setItem(count,6,totalprice)
            self.ui.tableWidget_7.setItem(count,7,amount)
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
    def find_order_btn(self):
        find_str=self.ui.Line_edit_findOrder.text()
        Orderbl=OrderBUS()
        Orderbl.readListOrder()
        list=Orderbl.findOrderById(int(find_str))
        print(len(list))
        count=0
        self.ui.tableWidget_7.clearContents()
        for items in list:
            orderId=QtWidgets.QTableWidgetItem(str(items.getId()))
            status_display=QtWidgets.QTableWidgetItem()
            if Orderbl.getLastStatusDetail(items.getId()).getStatusId()>6:
                status_display.setBackground(QColor(255, 0, 0))
            elif Orderbl.getLastStatusDetail(items.getId()).getStatusId()<6:
                status_display.setBackground(QColor(255, 255, 127))
            else:
                status_display.setBackground(QColor(5, 255, 109))
            status_display.setText(Orderbl.getLastStatus(items.getId()).getDisplay())
            time_order=QtWidgets.QTableWidgetItem(str(Orderbl.getFirstStatusDetail(items.getId()).getTimeCreated()))
            last_process=QtWidgets.QTableWidgetItem(str(Orderbl.getLastStatusDetail(items.getId()).getTimeCreated()))
            customer=QtWidgets.QTableWidgetItem(items.getCustomer())
            employee=QtWidgets.QTableWidgetItem(items.getHandler())
            totalprice=QtWidgets.QTableWidgetItem(str(items.getTotalPrice()))
            amount=QtWidgets.QTableWidgetItem(str(items.getQuantity()))


            self.ui.tableWidget_7.setItem(count,0,orderId)
            self.ui.tableWidget_7.setItem(count,1,status_display)
            self.ui.tableWidget_7.setItem(count,2,time_order)
            self.ui.tableWidget_7.setItem(count,3,last_process)
            self.ui.tableWidget_7.setItem(count,4,customer)
            self.ui.tableWidget_7.setItem(count,5,employee)
            self.ui.tableWidget_7.setItem(count,6,totalprice)
            self.ui.tableWidget_7.setItem(count,7,amount)
            count+=1
    ####################Order function
    def cancel_order(self):
        odbl=OrderBUS()
        row=self.ui.tableWidget_7.currentRow()
        id=self.ui.tableWidget_7.item(row,0).text()
        txt=odbl.cancelOrder(id)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(txt)
        msgBox.setWindowTitle("Hủy đơn hàng")
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()
    def check_order(self):
        odbl=OrderBUS()
        row=self.ui.tableWidget_7.currentRow()
        id=self.ui.tableWidget_7.item(row,0).text()
        list=odbl.getInfoOrder(id)
        fullname=list["FullName"]
        address=list["Address"]
        phone=list["Phone"]
        payment=list["DisplayPayment"]
        time=list["DisplayTime"]
        Note=list["Note"]
        total=list["Total"]
        ####
        str_7=""

        for i in range(len(list["ListStatusDetail"])):
            displayStatus = list["ListStatus"][i].getDisplay()
            if list["ListStatusDetail"][i] is not None: 
                new=(displayStatus + "\t" * 3 +str(list["ListStatusDetail"][i].getTimeCreated()))+'\n'
                str_7+=new
            else:
                new=(displayStatus + "\t" * 3 + "Trống")+'\n'
                str_7+=new
        ###
        str8="***CHI TIẾT ĐƠN HÀNG***"
        ###
        str_9="Pizza" + "\t" * 4 + "Giá"+'\n'
        for orderDetail in list["OrderDetails"]:
            str_9+=(orderDetail["DisplayPizza"] +" x " + str(orderDetail["Quantity"]) +"\t" * 4 + str(orderDetail["Amount"]))
        str10="Tổng tiền:" + "\t" * 4 + str(list["Total"])
        ###
        str_1="Họ tên khách hàng: "+list["FullName"]
        str2="Địa chỉ giao hàng: "+ list["Address"]
        str3="Số điện thoại liên lạc: "+ list["Phone"]
        str4="Phương thức thanh toán: "+ list["DisplayPayment"]
        str5="Thời gian giao hàng: "+ list["DisplayTime"]
        str6="***TRẠNG THÁI ĐƠN HÀNG***"
        txt=str_1+'\n'+str2+'\n'+str3+'\n'+str4+'\n'+str5+'\n'+str6+'\n'+str_7+'\n'+str8+"\n"+str_9+'\n'+str10
        #txt='FullName:\t{}\nAddress:\t{}\nPhone\t{}\nPayment:\t{}\nTime:\t{}\nNote:\t{}\nTotal:\t{}'.format(fullname,address,phone,payment,time,Note,total)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(txt)
        msgBox.setWindowTitle("Chi tiết đơn hàng")
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()
    def handler_order(self):
        odbl=OrderBUS()
        row=self.ui.tableWidget_7.currentRow()
        id=self.ui.tableWidget_7.item(row,0).text()
        txt=odbl.handleOrder(id)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(txt)
        msgBox.setWindowTitle("Message box pop up window")
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()




        
        


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

