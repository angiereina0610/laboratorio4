# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazlab2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 869)
        MainWindow.setStyleSheet("background-color: rgb(83, 132, 170);")
        
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 240, 451, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 232, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setStyleSheet("background-image: url(escuela.png);")
        self.frame.setObjectName("frame")
        
        
        
        
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.captura = QtWidgets.QComboBox(self.groupBox)
        self.captura.setGeometry(QtCore.QRect(50, 80, 351, 41))
        self.captura.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.captura.setObjectName("captura")
        self.captura.addItem("")
        self.captura.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 100, 881, 101))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(600, 240, 461, 511))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(290, 80, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 391, 16))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 261, 16))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 261, 16))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 120, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(40, 160, 391, 16))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 261, 16))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 210, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 250, 261, 16))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 250, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(40, 300, 391, 16))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 340, 261, 16))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 380, 261, 16))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 340, 113, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(290, 380, 113, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(60, 540, 451, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.reportes = QtWidgets.QComboBox(self.groupBox_3)
        self.reportes.setGeometry(QtCore.QRect(50, 100, 351, 41))
        self.reportes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.reportes.setObjectName("reportes")
        self.reportes.addItem("")
        self.reportes.addItem("")
        self.reportes.addItem("")
        self.reportes.addItem("")
        
        
        
   
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1116, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "CAPTURA DE DATOS "))
        self.captura.setItemText(0, _translate("MainWindow", "Escoger momento de captura"))
        self.captura.setItemText(1, _translate("MainWindow", "Escoger momento de capura con grafica en tiempo real "))
        self.label.setText(_translate("MainWindow", "BIENVENIDO AL LABORATORIO DE MONITOR DE TEMPERATURA"))
        self.groupBox_2.setTitle(_translate("MainWindow", "CONFIGURACI??N DE PARAMETROS"))
        self.label_2.setText(_translate("MainWindow", "PARA VALORES DE TEMPERATURA EN ESTADO DE   HIPOTERMIA"))
        self.label_3.setText(_translate("MainWindow", "Diligencie por favor el valor m??nimo"))
        self.label_4.setText(_translate("MainWindow", "Diligencie por favor el valor m??ximo"))
        self.label_5.setText(_translate("MainWindow", "PARA VALORES DE TEMPERATURA EN ESTADO   NORMAL"))
        self.label_6.setText(_translate("MainWindow", "Diligencie por favor el valor m??nimo"))
        self.label_7.setText(_translate("MainWindow", "Diligencie por favor el valor m??ximo"))
        self.label_8.setText(_translate("MainWindow", "PARA VALORES DE TEMPERATURA EN ESTADO   DE FIEBRE"))
        self.label_9.setText(_translate("MainWindow", "Diligencie por favor el valor m??nimo"))
        self.label_10.setText(_translate("MainWindow", "Diligencie por favor el valor m??ximo"))
        self.groupBox_3.setTitle(_translate("MainWindow", "REPORTES "))
        self.reportes.setItemText(0, _translate("MainWindow", "Ver grafica de los datos capturados"))
        self.reportes.setItemText(1, _translate("MainWindow", "Valor maximo"))
        self.reportes.setItemText(2, _translate("MainWindow", "Valor minimo"))
        self.reportes.setItemText(3, _translate("MainWindow", "Promedio de temperatura"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
