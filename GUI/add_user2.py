# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_user2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from BUS import GroupBUS,UserBUS
from DTO import User
class add_user_dia(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 329)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 190, 47, 16))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(40, 260, 62, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 290, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 160, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(40, 290, 24, 16))
        self.label_10.setObjectName("label_10")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 160, 32, 16))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 52, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(41, 90, 46, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(130, 130, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setMinimumWidth(100)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 130, 27, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 260, 113, 20))
        self.lineEdit_4.setMaxLength(10)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 230, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(130, 190, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 230, 32, 16))
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 0, 91, 31))
        self.label.setObjectName("label")
        self.pushbutton=QtWidgets.QPushButton(Dialog)
        self.pushbutton.setGeometry(QtCore.QRect(250, 290, 60, 20))
        self.pushbutton.setText("ADD")
        self.pushbutton.clicked.connect(self.add_user)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def add_item(self):
        grbus=GroupBUS()
        grbus.readListGroup()
        for grp in grbus.listGroup:
            self.comboBox.addItem(grp.getDisplay())
    def add_user(self):
        if self.lineEdit.text()=='' or self.lineEdit_2.text()=='':
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText("Xin hãy nhập đầy đủ các trường")
            msgBox.setWindowTitle("ERROR")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            returnValue = msgBox.exec()
        else:
            grbus=GroupBUS()
            grbus.readListGroup()
            userBUS =UserBUS()
            userBUS.readListUser()
            usr=User()
            usr.setUsername(self.lineEdit.text())
            password=self.lineEdit_2.text()
            usr.setFullname(self.lineEdit_6.text())
            usr.setAddress(self.lineEdit_3.text())
            for item in grbus.findGroupByName(self.comboBox.currentText()):
                usr.setGroupId(item.getId())
            usr.setBirth(self.dateEdit.date().toPyDate())
            usr.setPhone(self.lineEdit_4.text())
            usr.setEmail(self.lineEdit_5.text())
            if userBUS.addUser(usr,password):
                print("OK")
            else:
                print("Not ok")



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "Ngày sinh"))
        self.label_9.setText(_translate("Dialog", "Số điện thoại"))
        self.label_10.setText(_translate("Dialog", "Email"))
        self.label_5.setText(_translate("Dialog", "Họ tên"))
        self.label_2.setText(_translate("Dialog", "User Name*"))
        self.label_3.setText(_translate("Dialog", "Password*"))
        self.label_8.setText(_translate("Dialog", "Nhóm*"))
        self.label_7.setText(_translate("Dialog", "Địa chỉ"))
        self.label.setText(_translate("Dialog", "Thêm người dùng"))
        self.add_item()
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = add_user_dia()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
