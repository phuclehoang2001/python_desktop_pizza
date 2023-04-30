
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMessageBox
from load_screen import Ui_LoadScreen
from login import Login_window
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
from add_user2 import add_user_dia
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

#Globals
COUNTER=0
Role=0
FullName=""
UserName=""
counting=0
counting2=0
#MAIN WINDOW
class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        global Role
        global FullName
        global UserName
        if UserName!="admin":
            self.ui.pushButton_passchange.setEnabled(False)
            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.Account_btn.setHidden(True)
            self.ui.GroupAccount_btn.setHidden(True)
        self.ui.pushButton_info.setText(FullName)
        self.statictical_category(0)
        self.statstical_pizza(0)
        self.ui.pushButton_info.clicked.connect(self.doubleclicklable)
        self.ui.GroupAccount_btn.clicked.connect(self.click_groupAccount_btn)
        self.ui.Account_btn.clicked.connect(self.click_Account_btn)
        self.ui.Category_btn.clicked.connect(self.click_Category_btn)
        self.ui.Size_btn.clicked.connect(self.click_Size_btn)
        self.ui.Base_btn.clicked.connect(self.click_PizzaBase_btn)
        self.ui.pizza_btn.clicked.connect(self.click_Pizza_btn)
        self.ui.Order_btn.clicked.connect(self.click_Order_btn)
        self.ui.Stastical_btn.clicked.connect(self.click_Stastical_btn)
        
        ####
        self.ui.pushButton_passchange.clicked.connect(self.change_pass)
        self.ui.pushButton_18.clicked.connect(self.change_info)
        self.ui.lock.clicked.connect(self.lock_open_user)
        self.ui.combobox1.currentIndexChanged.connect(self.statictical_category)
        self.ui.combobox2.currentIndexChanged.connect(self.statstical_pizza)
        #####Info
        self.ui.pushButton_20.clicked.connect(self.info_account)
        #logout
        self.ui.Setting_btn.clicked.connect(self.logout)
        ##Phan quyen
        self.ui.GroupAcc_menu.clicked.connect(self.phanquyen)
        ##Can nhac nut nay##Mở dialog add
        self.ui.pushButton_23.clicked.connect(self.open_add_category_btn)
        self.ui.GroupAcc_add.clicked.connect(self.open_add_group_btn)
        self.ui.pushButton_29.clicked.connect(self.open_add_size_dialog)
        self.ui.pushButton_35.clicked.connect(self.open_add_base_dialog)
        self.ui.pushButton_17.clicked.connect(self.open_add_user)
        #find function//
        self.ui.pushButton_21.clicked.connect(self.find_category_btn)
        self.ui.GroupAcc_search.clicked.connect(self.find_group_btn)
        self.ui.pushButton_27.clicked.connect(self.find_size_btn)
        self.ui.pushButton_33.clicked.connect(self.find_base_btn)
        self.ui.pushButton_45.clicked.connect(self.find_order_btn)##Id_only
        self.ui.pushButton_15.clicked.connect(self.find_account)
        ##Load_Value 
        self.auto_get_value_group()
        self.auto_get_value_account()
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
        self.ui.pushButton_16.clicked.connect(self.auto_get_value_account)
        ###Function for order
        self.ui.pushButton_50.clicked.connect(self.cancel_order)
        self.ui.pushButton_47.clicked.connect(self.check_order)
        self.ui.pushButton_48.clicked.connect(self.handler_order)
        global Role
        print(Role)

        ####logout
    def logout(self):
        self.main=wth()
        self.main.show()
        self.close()

    ########################user info
    ###
    def doubleclicklable(self):
        usrbl=UserBUS()
        global UserName
        infoUser=usrbl.getInfo(UserName)
        print("Heelo")
        print(infoUser["address"])
        dialog =QtWidgets.QDialog()
        dialog.setMinimumHeight(100)
        dialog.setMinimumWidth(250)
        dialog.setWindowTitle("Thông tin tài khoản")
        layout = QtWidgets.QVBoxLayout()
        dialog.setLayout(layout)
        form_layout =QtWidgets.QFormLayout()
        layout.addLayout(form_layout)
        label_ttk=QtWidgets.QLabel("Tên tài khoản: "+infoUser["fullname"])
        label_ntk=QtWidgets.QLabel("Nhóm tài khoản: "+infoUser["groupName"])
        label_hoten=QtWidgets.QLabel("Họ tên: "+infoUser["fullname"])
        label_dob=QtWidgets.QLabel("Ngày sinh: "+str(infoUser["birthday"]))
        label_address=QtWidgets.QLabel("Địa chỉ: "+infoUser["address"])
        label_number=QtWidgets.QLabel("Số điện thoại: "+infoUser["phone"])
        label_mail=QtWidgets.QLabel("Email: "+infoUser["email"])
        form_layout.addRow(label_ttk)
        form_layout.addRow(label_ntk)
        form_layout.addRow(label_hoten)
        form_layout.addRow(label_hoten)
        form_layout.addRow(label_dob)
        form_layout.addRow(label_address)
        form_layout.addRow(label_number)
        form_layout.addRow(label_mail)
        
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok)
        button_box.accepted.connect(dialog.accept)
        layout.addWidget(button_box)
        response = dialog.exec_()


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
    def auto_get_value_account(self):
        self.ui.tableWidget_2.clearContents()
        userbl=UserBUS()
        userbl.readListUser()
        self.ui.tableWidget_2.setRowCount(len(userbl.listUser))
        print("Chieu dai ",len(userbl.listUser))
        count=0
        for account in userbl.listUser:
            username=QtWidgets.QTableWidgetItem(str(account.getUsername()))
            groupname=QtWidgets.QTableWidgetItem(userbl.getGroupName(account))
            self.ui.tableWidget_2.setItem(count,0,username)
            self.ui.tableWidget_2.setItem(count,1,groupname)
            if userbl.hasPermission(account.getUsername(),"lock"):
                status=QtWidgets.QTableWidgetItem("Khóa")
                self.ui.tableWidget_2.setItem(count,2,status)
            else:
                status=QtWidgets.QTableWidgetItem("Mở khóa")
                self.ui.tableWidget_2.setItem(count,2,status)
            
            count+=1
            

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
        self.resize(1050,729)
    def click_Account_btn(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.resize(1050,729)
    def click_Category_btn(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.resize(1050,729)
    def click_Size_btn(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.resize(1050,729)
    def click_PizzaBase_btn(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.resize(1050,729)
    def click_Pizza_btn(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.resize(1050,729)
    def click_Order_btn(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        self.resize(1050,729)
    def click_Stastical_btn(self):
        self.ui.stackedWidget.setCurrentIndex(7)
        self.resize(1400,729)
        ###Create add_cattegory_dialog
        ########
    def open_add_user(self):
        Dialog = QtWidgets.QDialog()
        ui = add_user_dia()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

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
    def find_account(self):
        find_str=self.ui.Line_edit_User.text()
        userbl=UserBUS()
        userbl.readListUser()
        list=userbl.findUserByUsername(find_str)
        self.ui.tableWidget_2.clearContents()
        count=0
        for account in list:
            username=QtWidgets.QTableWidgetItem(str(account.getUsername()))
            groupname=QtWidgets.QTableWidgetItem(userbl.getGroupName(account))
            self.ui.tableWidget_2.setItem(count,0,username)
            self.ui.tableWidget_2.setItem(count,1,groupname)
            if userbl.hasPermission(account.getUsername(),"lock"):
                status=QtWidgets.QTableWidgetItem("Khóa")
                self.ui.tableWidget_2.setItem(count,2,status)
            else:
                status=QtWidgets.QTableWidgetItem("Mở khóa")
                self.ui.tableWidget_2.setItem(count,2,status)
            
            count+=1
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
                new=(displayStatus + "\t" +str(list["ListStatusDetail"][i].getTimeCreated()))+'\n'
                str_7+=new
            else:
                new=(displayStatus + "\t"+ "Trống")+'\n'
                str_7+=new
        ###
        str8="***CHI TIẾT ĐƠN HÀNG***"
        ###
        str_9="Pizza" + "\t" + "Giá"+'\n'
        for orderDetail in list["OrderDetails"]:
            str_9+=(orderDetail["DisplayPizza"] +" x " + str(orderDetail["Quantity"]) +"\t" * 4 + str(orderDetail["Amount"]))+'\n'
        str10="Tổng tiền:" + "\t" + str(list["Total"])
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
        ##################Phan quyen
    def phanquyen(self):
        permission_dict = {
            "admin.login": "Đăng nhập trang quản trị",
            "admin.group": "Quản lý nhóm tài khoản",
            "admin.user": "Quản lý tài khoản",
            "admin.category": "Quản lý danh mục bánh",
            "admin.topping": "Quản lý nhân bánh",
            "admin.size": "Quản lý kích thước bánh",
            "admin.base": "Quản lý đế bánh",
            "admin.pizza": "Quản lý bánh pizza",
            "admin.order": "Quản lý đơn hàng",
            "admin.statistic": "Thống kê báo cáo"}
        row=self.ui.tableWidget.currentRow()
        Group_id=self.ui.tableWidget.item(row,0).text()
        perMissonBl=GroupBUS()
        perMissonBl.readListGroup()




        dialog =QtWidgets.QDialog()
        layout = QtWidgets.QVBoxLayout()
        dialog.setLayout(layout)
        form_layout =QtWidgets.QFormLayout()
        layout.addLayout(form_layout)

        dialog.setWindowTitle("Phân Quyền")
        for key,value in permission_dict.items():
            per1=perMissonBl.isSet(Group_id,key)
            if per1==True:
                check=QtWidgets.QCheckBox()
                check.setText(value)
                check.setChecked(True)
                form_layout.addRow(check)
            else:
                check=QtWidgets.QCheckBox()
                check.setText(value)
                check.setChecked(False)
                form_layout.addRow(check)
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)
        response = dialog.exec_()
        if response == QtWidgets.QDialog.Accepted:
            count=0
            for key,value in permission_dict.items():
                checkbox_item = form_layout.itemAt(count, QtWidgets.QFormLayout.FieldRole)
                checkbox_widget = checkbox_item.widget()
                if checkbox_widget.isChecked():
                    vari=1
                    perMissonBl.setPermission(Group_id,key,vari)
                else:
                    vari=0
                    perMissonBl.setPermission(Group_id,key,vari)
                count+=1
    def info_account(self):
        usrbl=UserBUS()
        row=self.ui.tableWidget_2.currentRow()
        col=self.ui.tableWidget_2.currentColumn()
        user_name=self.ui.tableWidget_2.item(row,col).text()
        print(user_name)
        infoUser=usrbl.getInfo(user_name)
        print(infoUser["address"])
        dialog =QtWidgets.QDialog()
        dialog.setMinimumHeight(100)
        dialog.setMinimumWidth(250)
        dialog.setWindowTitle("Thông tin tài khoản")
        layout = QtWidgets.QVBoxLayout()
        dialog.setLayout(layout)
        form_layout =QtWidgets.QFormLayout()
        layout.addLayout(form_layout)
        label_ttk=QtWidgets.QLabel("Tên tài khoản: "+infoUser["fullname"])
        label_ntk=QtWidgets.QLabel("Nhóm tài khoản: "+infoUser["groupName"])
        label_hoten=QtWidgets.QLabel("Họ tên: "+infoUser["fullname"])
        label_dob=QtWidgets.QLabel("Ngày sinh: "+str(infoUser["birthday"]))
        label_address=QtWidgets.QLabel("Địa chỉ: "+infoUser["address"])
        label_number=QtWidgets.QLabel("Số điện thoại: "+infoUser["phone"])
        label_mail=QtWidgets.QLabel("Email: "+infoUser["email"])
        form_layout.addRow(label_ttk)
        form_layout.addRow(label_ntk)
        form_layout.addRow(label_hoten)
        form_layout.addRow(label_hoten)
        form_layout.addRow(label_dob)
        form_layout.addRow(label_address)
        form_layout.addRow(label_number)
        form_layout.addRow(label_mail)
        
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok)
        button_box.accepted.connect(dialog.accept)
        layout.addWidget(button_box)
        response = dialog.exec_()
    def change_info(self):
        row=self.ui.tableWidget_2.currentRow()
        col=self.ui.tableWidget_2.currentColumn()
        user_name=self.ui.tableWidget_2.item(row,col).text()
        usrbl=UserBUS()
        usrbl.readListUser()
        info=usrbl.getInfo(user_name)
        dialog =QtWidgets.QDialog()
        dialog.setMinimumHeight(100)
        dialog.setMinimumWidth(250)
        dialog.setWindowTitle("Thông tin tài khoản")
        layout = QtWidgets.QVBoxLayout()
        dialog.setLayout(layout)
        form_layout =QtWidgets.QFormLayout()
        layout.addLayout(form_layout)

        label_1 =QtWidgets.QLabel("Tên tài khoản")
        Line_Usr=QtWidgets.QLineEdit()
        Line_Usr.setText(user_name)
        Line_Usr.setEnabled(False)
        #
        label_2=QtWidgets.QLabel("Nhóm")
        combobox=QtWidgets.QComboBox()
        grbus=GroupBUS()
        grbus.readListGroup()
        for grp in grbus.listGroup:
            combobox.addItem(grp.getDisplay())
        combobox.setCurrentText(info["groupName"])
        #
        label_3=QtWidgets.QLabel("Họ tên")
        line_fullname=QtWidgets.QLineEdit()
        line_fullname.setText(info["fullname"])
        #
        label_4=QtWidgets.QLabel("Ngày sinh")
        datetime=QtWidgets.QDateEdit()
        datetime.setDate((info["birthday"]))
        #
        label_5=QtWidgets.QLabel("Địa chỉ")
        line_address=QtWidgets.QLineEdit()
        line_address.setText(info["address"])
        #
        label_6=QtWidgets.QLabel("số diện thoại")
        line_phone=QtWidgets.QLineEdit()
        line_phone.setText(info["phone"])
        #
        label_7=QtWidgets.QLabel("Email")
        line_mail=QtWidgets.QLineEdit()
        line_mail.setText(info["email"])
        form_layout.addWidget(label_1)
        form_layout.addWidget(Line_Usr)
        #
        form_layout.addWidget(label_2)
        form_layout.addWidget(combobox)
        #
        form_layout.addWidget(label_3)
        form_layout.addWidget(line_fullname)
        #
        form_layout.addWidget(label_4)
        form_layout.addWidget(datetime)
        #
        form_layout.addWidget(label_5)
        form_layout.addWidget(line_address)
        #
        form_layout.addWidget(label_6)
        form_layout.addWidget(line_phone)
        #
        form_layout.addWidget(label_7)
        form_layout.addWidget(line_mail)
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)
        response = dialog.exec_()
        if response == QtWidgets.QDialog.Accepted:
            usr=User()
            usr.setUsername(user_name)
            usr.setAddress(line_address.text())
            usr.setBirth(datetime.date().toPyDate())
            usr.setEmail(line_mail.text())
            usr.setFullname(line_fullname.text())
            usr.setPhone(line_phone.text())
            for item in grbus.findGroupByName(combobox.currentText()):
                usr.setGroupId(item.getId())
            usrbl.updateUser(usr)
        else:
            pass
    def change_pass(self):
        row=self.ui.tableWidget_2.currentRow()
        col=self.ui.tableWidget_2.currentColumn()
        usr_name=self.ui.tableWidget_2.item(row,col).text()
        global UserName
        usrbl=UserBUS()
        dialog =QtWidgets.QDialog()
        dialog.setMinimumHeight(100)
        dialog.setMinimumWidth(250)
        dialog.setWindowTitle("Đổi mật khẩu")
        layout = QtWidgets.QVBoxLayout()
        dialog.setLayout(layout)
        form_layout =QtWidgets.QFormLayout()
        layout.addLayout(form_layout)
        ###
        label_1=QtWidgets.QLabel("Mật khẩu mới")
        form_layout.addWidget(label_1)
        line_edit_1=QtWidgets.QLineEdit()
        form_layout.addWidget(line_edit_1)
        label_2=QtWidgets.QLabel("Nhập lại mật khẩu")
        form_layout.addWidget(label_2)
        line_edit_2=QtWidgets.QLineEdit()
        form_layout.addWidget(line_edit_2)
        ####
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)
        response = dialog.exec_()
        if response == QtWidgets.QDialog.Accepted:
            if UserName=="admin":
                if usrbl.updatePassword(usr_name,line_edit_1.text()):
                    print("Sửa thành công")
        else:
            pass        
    def lock_open_user(self):
        usrbl=UserBUS()
        usrbl.readListUser()
        row=self.ui.tableWidget_2.currentRow()
        col=self.ui.tableWidget_2.currentColumn()
        usr_name=self.ui.tableWidget_2.item(row,col).text()
        dialog =QtWidgets.QDialog()
        dialog.setMinimumHeight(100)
        dialog.setMinimumWidth(250)
        dialog.setWindowTitle("Mở/Khóa tài khoản")
        layout = QtWidgets.QVBoxLayout()
        dialog.setLayout(layout)
        
        flag=0
        if usr_name=="admin":
            label=QtWidgets.QLabel("Không thể khóa tài khoản Admin")
            layout.addWidget(label)
        else:
            checklock=usrbl.hasPermission(usr_name,"lock")
            if checklock:
                label=QtWidgets.QLabel("Tài khoản đã khóa,xác nhận mở khóa?")
                layout.addWidget(label)
                flag=1
            else:
                label=QtWidgets.QLabel("Tài khoản chưa khóa,xác nhận khóa?")
                layout.addWidget(label)
                flag=2
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)
        response = dialog.exec_()
        if response == QtWidgets.QDialog.Accepted:
            if flag==1:
                usrbl.unclockUser(usr_name)
            elif flag==2:
                usrbl.clockUser(usr_name)
        else:
            pass
    def statictical_category(self,index):
        fig = plt.Figure()
        canvas = FigureCanvas(fig)
        canvas.setFixedSize(1300,400)
        ax = fig.add_subplot(111)
        global counting
        if self.ui.combobox1.currentText()=="Doanh thu- Dự kiến / Thực tế":
            statis_bl=StatisticBUS
            tk_category=statis_bl.category()
            lst_of_cate=[]
            lst_of_dttt=[]
            lst_of_dtdk=[]
            
            for index, value in enumerate(tk_category["Categories"]):
                if int(tk_category["ActualRevenue"][index])!=0 or int(tk_category["ExpectedRevenue"][index])!=0:
                    lst_of_cate.append(value.getDisplay())
                    lst_of_dttt.append(tk_category["ActualRevenue"][index])
                    lst_of_dtdk.append(tk_category["ExpectedRevenue"][index])
            ax.bar( lst_of_cate, lst_of_dttt, label='Doanh thu thực tế')
            ax.bar( lst_of_cate, lst_of_dtdk,bottom=lst_of_dttt, label='Doanh thu dự kiến')
        
            ax.set_xlabel('Danh mục')
            ax.set_ylabel('Số liệu')
            ax.set_title('Biểu đồ số liệu Doanh thu của danh mục')
            ax.legend()
           
            if counting >=1:
                self.ui.layout.itemAt(1).widget().deleteLater()
                print(counting)
                self.ui.layout.addWidget(canvas)
                print(self.ui.layout.count())
                
            else:

                self.ui.layout.addWidget(canvas)
                counting+=1 
        elif self.ui.combobox1.currentText()=="Bán ra- Dự kiến / Thực tế":
            statis_bl=StatisticBUS
            tk_category=statis_bl.category()
            lst_of_cate=[]
            lst_of_brtt=[]
            lst_of_brdk=[]
            fig = plt.Figure()
            canvas = FigureCanvas(fig)
            canvas.setFixedSize(1300,400)
            ax = fig.add_subplot(111)
            for index, value in enumerate(tk_category["Categories"]):
                if int(tk_category["ActualSales"][index])!=0 or int(tk_category["ExpectedSales"][index])!=0:
                    lst_of_cate.append(value.getDisplay())
                    lst_of_brtt.append(tk_category["ActualSales"][index])
                    lst_of_brdk.append(tk_category["ExpectedSales"][index])
            ax.bar( lst_of_cate, lst_of_brtt, label='Bán ra thực tế')
            ax.bar( lst_of_cate, lst_of_brdk,bottom=lst_of_brtt, label='Bán ra dự kiến')
        
            ax.set_xlabel('Danh mục')
            ax.set_ylabel('Số liệu')
            ax.set_title('Biểu đồ số liệu Bán ra của danh mục')
            ax.legend()
            if counting >=1:
                self.ui.layout.itemAt(1).widget().deleteLater()
                print(counting)
                
                self.ui.layout.addWidget(canvas)
                print(self.ui.layout.count())
            else:
                counting+=1
                self.ui.layout.addWidget(canvas)
        elif self.ui.combobox1.currentText()=="Tổng doanh thu- Dự kiến / Thực tế":
            statis_bl=StatisticBUS
            tk_category=statis_bl.category()
            tongdtbanra=tk_category["TotalActualRevenue"]
            tongdtdukien=tk_category["TotalExpectedRevenue"]
            ax.bar( ["Tổng doanh thu thực tế"], tongdtbanra, label='Tổng Doanh thu thực tế')
            ax.bar( ["Tổng doanh thu dự kiến"], tongdtdukien, label='Tổng Doanh thu dự kiến')
        
            ax.set_ylabel('Số liệu')
            ax.set_title('Biểu đồ số liệu Tổng doanh thu')
            ax.legend()
           
            if counting >=1:
                self.ui.layout.itemAt(1).widget().deleteLater()
                print(counting)
                self.ui.layout.addWidget(canvas)
                print(self.ui.layout.count())
                
            else:

                self.ui.layout.addWidget(canvas)
                counting+=1 
        elif self.ui.combobox1.currentText()=="Tổng Bán ra- Dự kiến / Thực tế":
            statis_bl=StatisticBUS
            tk_category=statis_bl.category()
            tongdtbanra=tk_category["TotalActualSales"]
            tongdtdukien=tk_category["TotalExpectedSales"]
            ax.bar( ["Tổng số lượng bán ra thực tế"], tongdtbanra, label='Tổng số lượng bán ra thực tế')
            ax.bar( ["Tổng số lượng bán ra dự kiến"], tongdtdukien, label='Tổng số lượng bán ra dự kiến')
        
            ax.set_ylabel('Số liệu')
            ax.set_title('Biểu đồ số liệu Tổng số lượng bán ra')
            ax.legend()
           
            if counting >=1:
                self.ui.layout.itemAt(1).widget().deleteLater()
                print(counting)
                self.ui.layout.addWidget(canvas)
                print(self.ui.layout.count())
                
            else:

                self.ui.layout.addWidget(canvas)
                counting+=1 
    def statstical_pizza(self,index):
        fig = plt.Figure()
        canvas = FigureCanvas(fig)
        canvas.setFixedSize(1300,400)
        ax = fig.add_subplot(111)
        global counting2
        if self.ui.combobox2.currentText()=="Doanh thu- Dự kiến / Thực tế":
            statis_bl=StatisticBUS
            tk_category=statis_bl.pizza()
            lst_of_cate=[]
            lst_of_dttt=[]
            lst_of_dtdk=[]
            
            for index, value in enumerate(tk_category["Pizzas"]):
                if int(tk_category["ActualRevenue"][index])!=0 or int(tk_category["ExpectedRevenue"][index])!=0:
                    lst_of_cate.append(value.getDisplay())
                    lst_of_dttt.append(int(tk_category["ActualRevenue"][index]))
                    lst_of_dtdk.append(int(tk_category["ExpectedRevenue"][index]))
            ax.bar( lst_of_cate, lst_of_dttt, label='Doanh thu thực tế')
            ax.bar( lst_of_cate, lst_of_dtdk,bottom=lst_of_dttt, label='Doanh thu dự kiến')
        
            ax.set_xlabel('Pizza')
            ax.set_ylabel('Số liệu')
            ax.set_title('Biểu đồ số liệu Doanh thu của pizza')
            ax.legend()
            if counting2 >=1:
                self.ui.layout2.itemAt(1).widget().deleteLater()
                print(counting2)
                self.ui.layout2.addWidget(canvas)
                
            else:
                self.ui.layout2.addWidget(canvas)
                counting2+=1
        elif self.ui.combobox2.currentText()=="Bán ra- Dự kiến / Thực tế":
            statis_bl=StatisticBUS
            tk_category=statis_bl.pizza()
            lst_of_cate=[]
            lst_of_brtt=[]
            lst_of_brdk=[]
            
            for index, value in enumerate(tk_category["Pizzas"]):
                if int(tk_category["ActualSales"][index])!=0 or int(tk_category["ExpectedSales"][index])!=0:
                    lst_of_cate.append(value.getDisplay())
                    lst_of_brtt.append(int(tk_category["ActualSales"][index]))
                    lst_of_brdk.append(int(tk_category["ExpectedSales"][index]))
            ax.bar( lst_of_cate, lst_of_brtt, label='Bán ra thực tế')
            ax.bar( lst_of_cate, lst_of_brdk,bottom=lst_of_brtt, label='Bán ra dự kiến')
        
            ax.set_xlabel('Pizza')
            ax.set_ylabel('Số liệu')
            ax.set_title('Biểu đồ số liệu bán ra của Pizza')
            ax.legend()
            if counting2 >=1:
                self.ui.layout2.itemAt(1).widget().deleteLater()
                print(counting2)
                self.ui.layout2.addWidget(canvas)
                
            else:
                self.ui.layout2.addWidget(canvas)
                counting2+=1
        elif self.ui.combobox2.currentText()=="Tổng doanh thu- Dự kiến / Thực tế":
            statis_bl=StatisticBUS
            tk_category=statis_bl.pizza()
            tongdtbanra=tk_category["TotalActualRevenue"]
            tongdtdukien=tk_category["TotalExpectedRevenue"]
            ax.bar( ["Tổng doanh thu thực tế"], tongdtbanra, label='Tổng Doanh thu thực tế')
            ax.bar( ["Tổng doanh thu Dự kiến"], tongdtdukien, label='Tổng Doanh thu dự kiến')
        
            ax.set_ylabel('Số liệu')
            ax.set_title('Biểu đồ số liệu Tổng doanh thu')
            ax.legend()
           
            if counting2 >=1:
                self.ui.layout2.itemAt(1).widget().deleteLater()
                self.ui.layout2.addWidget(canvas)
                
            else:

                self.ui.layout2.addWidget(canvas)
                counting2+=1 
        elif self.ui.combobox2.currentText()=="Tổng Bán ra- Dự kiến / Thực tế":
            statis_bl=StatisticBUS
            tk_category=statis_bl.pizza()
            tongdtbanra=tk_category["TotalActualSales"]
            tongdtdukien=tk_category["TotalExpectedSales"]
            ax.bar( ["Tổng số lượng bán ra thực tế"], tongdtbanra, label='Tổng số lượng bán ra thực tế')
            ax.bar( ["Tổng số lượng bán ra Dự kiến"], tongdtdukien, label='Tổng số lượng bán ra dự kiến')
        
            ax.set_ylabel('Số liệu')
            ax.set_title('Biểu đồ số liệu Tổng số lượng bán ra')
            ax.legend()
           
            if counting2 >=1:
                self.ui.layout2.itemAt(1).widget().deleteLater()
                self.ui.layout2.addWidget(canvas)
                
            else:

                self.ui.layout2.addWidget(canvas)
                counting2+=1 
        






        

##LOGin
class wth(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui=Login_window()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)
    def click(self):
        self.main=handler()
        self.main.show()
        self.close()
    def login(self):
        usr=self.ui.LineEdit.text()
        print(usr)
        pss=self.ui.LineEdit_2.text()
        userBUS = UserBUS()
        res=userBUS.checkLogin(usr,pss)
        print(res)
        if res=="OK":
            if userBUS.hasPermission(usr,"lock"):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Tài khoản đã bị khóa xin vui lòng liên hệ quản trị viên")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.show()
                msgBox.exec()
            else:
                info=userBUS.getInfo(usr)
                global Role
                global FullName
                global UserName
                FullName=info["fullname"]
                Role=info["groupId"]
                UserName=info["username"]
                print(info)
                self.click()

        elif res=="Sai thông tin đăng nhập":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("SAI THÔNG TIN ĐĂNG NHẬP")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.show()
            msgBox.exec()
        elif res=="Tài khoản đã bị khóa!":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Tài khoản đã bị khóa!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.show()
            msgBox.exec()
        elif res=="Không có quyền đăng nhập trang quản trị":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Không có quyền đăng nhập trang quản trị")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.show()
            msgBox.exec()
        elif res=="Vui lòng nhập đủ thông tin":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Vui lòng nhập đủ thông tin")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.show()
            msgBox.exec()
    




        

        
        


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
    Loading = wth()
    Loading.show()
    sys.exit(app.exec_())

