from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication , QLCDNumber
import sys , os
import webbrowser
import random
import string


class Ui_MainWindow ( object ) :
    def setupUi (self , MainWindow) :
        MainWindow.setObjectName ( "MainWindow" )
        MainWindow.resize ( 546 , 268 )
        self.centralwidget = QtWidgets.QWidget ( MainWindow )
        self.centralwidget.setObjectName ( "centralwidget" )
        self.layoutWidget = QtWidgets.QWidget ( self.centralwidget )
        self.layoutWidget.setGeometry ( QtCore.QRect ( 1 , 1 , 541 , 222 ) )
        self.layoutWidget.setObjectName ( "layoutWidget" )
        self.gridLayout = QtWidgets.QGridLayout ( self.layoutWidget )
        self.gridLayout.setContentsMargins ( 0 , 0 , 0 , 0 )
        self.gridLayout.setObjectName ( "gridLayout" )
        self.label_length = QtWidgets.QLabel ( self.layoutWidget )
        sizePolicy = QtWidgets.QSizePolicy ( QtWidgets.QSizePolicy.Expanding , QtWidgets.QSizePolicy.Preferred )
        sizePolicy.setHorizontalStretch ( 100 )
        sizePolicy.setVerticalStretch ( 100 )
        sizePolicy.setHeightForWidth ( self.label_length.sizePolicy ().hasHeightForWidth () )
        self.label_length.setSizePolicy ( sizePolicy )
        font = QtGui.QFont ()
        font.setPointSize ( 10 )
        font.setBold ( False )
        font.setWeight ( 50 )
        self.label_length.setFont ( font )
        self.label_length.setObjectName ( "label_length" )
        self.gridLayout.addWidget ( self.label_length , 5 , 1 , 1 , 1 )
        spacerItem = QtWidgets.QSpacerItem ( 20 , 40 , QtWidgets.QSizePolicy.Minimum , QtWidgets.QSizePolicy.Expanding )
        self.gridLayout.addItem ( spacerItem , 1 , 7 , 5 , 1 )
        self.lineEdit_password = QtWidgets.QLineEdit ( self.layoutWidget )
        sizePolicy = QtWidgets.QSizePolicy ( QtWidgets.QSizePolicy.Expanding , QtWidgets.QSizePolicy.Fixed )
        sizePolicy.setHorizontalStretch ( 100 )
        sizePolicy.setVerticalStretch ( 100 )
        sizePolicy.setHeightForWidth ( self.lineEdit_password.sizePolicy ().hasHeightForWidth () )
        self.lineEdit_password.setSizePolicy ( sizePolicy )
        self.lineEdit_password.setMinimumSize ( QtCore.QSize ( 100 , 40 ) )
        self.lineEdit_password.setObjectName ( "lineEdit_password" )
        self.gridLayout.addWidget ( self.lineEdit_password , 2 , 1 , 1 , 6 )
        self.checkBox_more = QtWidgets.QCheckBox ( self.layoutWidget )
        sizePolicy = QtWidgets.QSizePolicy ( QtWidgets.QSizePolicy.Expanding , QtWidgets.QSizePolicy.Fixed )
        sizePolicy.setHorizontalStretch ( 100 )
        sizePolicy.setVerticalStretch ( 100 )
        sizePolicy.setHeightForWidth ( self.checkBox_more.sizePolicy ().hasHeightForWidth () )
        self.checkBox_more.setSizePolicy ( sizePolicy )
        font = QtGui.QFont ()
        font.setBold ( True )
        font.setWeight ( 75 )
        self.checkBox_more.setFont ( font )
        self.checkBox_more.setLayoutDirection ( QtCore.Qt.LeftToRight )
        self.checkBox_more.setAutoFillBackground ( False )
        self.checkBox_more.setChecked ( True )
        self.checkBox_more.setAutoExclusive ( False )
        self.checkBox_more.setObjectName ( "checkBox_more" )
        self.gridLayout.addWidget ( self.checkBox_more , 5 , 6 , 1 , 1 )
        self.checkBox_0_9 = QtWidgets.QCheckBox ( self.layoutWidget )
        sizePolicy = QtWidgets.QSizePolicy ( QtWidgets.QSizePolicy.Expanding , QtWidgets.QSizePolicy.Fixed )
        sizePolicy.setHorizontalStretch ( 100 )
        sizePolicy.setVerticalStretch ( 100 )
        sizePolicy.setHeightForWidth ( self.checkBox_0_9.sizePolicy ().hasHeightForWidth () )
        self.checkBox_0_9.setSizePolicy ( sizePolicy )
        font = QtGui.QFont ()
        font.setBold ( True )
        font.setWeight ( 75 )
        self.checkBox_0_9.setFont ( font )
        self.checkBox_0_9.setChecked ( True )
        self.checkBox_0_9.setObjectName ( "checkBox_0_9" )
        self.gridLayout.addWidget ( self.checkBox_0_9 , 5 , 5 , 1 , 1 )
        self.label_name = QtWidgets.QLabel ( self.layoutWidget )
        sizePolicy = QtWidgets.QSizePolicy ( QtWidgets.QSizePolicy.Expanding , QtWidgets.QSizePolicy.Preferred )
        sizePolicy.setHorizontalStretch ( 0 )
        sizePolicy.setVerticalStretch ( 0 )
        sizePolicy.setHeightForWidth ( self.label_name.sizePolicy ().hasHeightForWidth () )
        self.label_name.setSizePolicy ( sizePolicy )
        self.label_name.setMinimumSize ( QtCore.QSize ( 0 , 0 ) )
        font = QtGui.QFont ()
        font.setPointSize ( 17 )
        font.setBold ( False )
        font.setWeight ( 50 )
        self.label_name.setFont ( font )
        self.label_name.setTextFormat ( QtCore.Qt.AutoText )
        self.label_name.setAlignment ( QtCore.Qt.AlignCenter )
        self.label_name.setObjectName ( "label_name" )
        self.gridLayout.addWidget ( self.label_name , 0 , 1 , 1 , 6 )
        self.pushButton_generate = QtWidgets.QPushButton ( self.layoutWidget )
        sizePolicy = QtWidgets.QSizePolicy ( QtWidgets.QSizePolicy.Expanding , QtWidgets.QSizePolicy.Fixed )
        sizePolicy.setHorizontalStretch ( 100 )
        sizePolicy.setVerticalStretch ( 100 )
        sizePolicy.setHeightForWidth ( self.pushButton_generate.sizePolicy ().hasHeightForWidth () )
        self.pushButton_generate.setSizePolicy ( sizePolicy )
        self.pushButton_generate.setMinimumSize ( QtCore.QSize ( 50 , 30 ) )
        font = QtGui.QFont ()
        font.setPointSize ( 11 )
        font.setBold ( True )
        font.setWeight ( 75 )
        self.pushButton_generate.setFont ( font )
        self.pushButton_generate.setObjectName ( "pushButton_generate" )
        self.gridLayout.addWidget ( self.pushButton_generate , 1 , 1 , 1 , 6 )
        spacerItem1 = QtWidgets.QSpacerItem ( 20 , 40 , QtWidgets.QSizePolicy.Minimum ,
                                              QtWidgets.QSizePolicy.Expanding )
        self.gridLayout.addItem ( spacerItem1 , 1 , 0 , 5 , 1 )
        self.horizontalSlider_1_30 = QtWidgets.QSlider ( self.layoutWidget )
        sizePolicy = QtWidgets.QSizePolicy ( QtWidgets.QSizePolicy.Expanding , QtWidgets.QSizePolicy.Fixed )
        sizePolicy.setHorizontalStretch ( 100 )
        sizePolicy.setVerticalStretch ( 100 )
        sizePolicy.setHeightForWidth ( self.horizontalSlider_1_30.sizePolicy ().hasHeightForWidth () )
        self.horizontalSlider_1_30.setSizePolicy ( sizePolicy )
        self.horizontalSlider_1_30.setMaximum ( 30 )
        self.horizontalSlider_1_30.setOrientation ( QtCore.Qt.Horizontal )
        self.horizontalSlider_1_30.setInvertedAppearance ( True )
        self.horizontalSlider_1_30.setInvertedControls ( False )
        self.horizontalSlider_1_30.setTickPosition ( QtWidgets.QSlider.NoTicks )
        self.horizontalSlider_1_30.setTickInterval ( 0 )
        self.horizontalSlider_1_30.setObjectName ( "horizontalSlider_1_30" )
        self.gridLayout.addWidget ( self.horizontalSlider_1_30 , 4 , 1 , 1 , 6 )
        self.pushButton_coppy = QtWidgets.QPushButton ( self.layoutWidget )
        sizePolicy = QtWidgets.QSizePolicy ( QtWidgets.QSizePolicy.Expanding , QtWidgets.QSizePolicy.Fixed )
        sizePolicy.setHorizontalStretch ( 100 )
        sizePolicy.setVerticalStretch ( 100 )
        sizePolicy.setHeightForWidth ( self.pushButton_coppy.sizePolicy ().hasHeightForWidth () )
        self.pushButton_coppy.setSizePolicy ( sizePolicy )
        self.pushButton_coppy.setMinimumSize ( QtCore.QSize ( 30 , 30 ) )
        font = QtGui.QFont ()
        font.setPointSize ( 10 )
        font.setBold ( True )
        font.setWeight ( 75 )
        self.pushButton_coppy.setFont ( font )
        self.pushButton_coppy.setObjectName ( "pushButton_coppy" )
        self.gridLayout.addWidget ( self.pushButton_coppy , 3 , 1 , 1 , 6 )
        self.checkBox_a_z = QtWidgets.QCheckBox ( self.layoutWidget )
        sizePolicy = QtWidgets.QSizePolicy ( QtWidgets.QSizePolicy.Expanding , QtWidgets.QSizePolicy.Fixed )
        sizePolicy.setHorizontalStretch ( 100 )
        sizePolicy.setVerticalStretch ( 100 )
        sizePolicy.setHeightForWidth ( self.checkBox_a_z.sizePolicy ().hasHeightForWidth () )
        self.checkBox_a_z.setSizePolicy ( sizePolicy )
        font = QtGui.QFont ()
        font.setBold ( True )
        font.setWeight ( 75 )
        self.checkBox_a_z.setFont ( font )
        self.checkBox_a_z.setChecked ( True )
        self.checkBox_a_z.setAutoRepeat ( False )
        self.checkBox_a_z.setAutoExclusive ( False )
        self.checkBox_a_z.setObjectName ( "checkBox_a_z" )
        self.gridLayout.addWidget ( self.checkBox_a_z , 5 , 4 , 1 , 1 )
        spacerItem2 = QtWidgets.QSpacerItem ( 40 , 20 , QtWidgets.QSizePolicy.Expanding ,
                                              QtWidgets.QSizePolicy.Minimum )
        self.gridLayout.addItem ( spacerItem2 , 5 , 3 , 1 , 1 )
        self.label_length_number = QtWidgets.QLabel ( self.layoutWidget )
        font = QtGui.QFont ()
        font.setPointSize ( 10 )
        self.label_length_number.setFont ( font )
        self.label_length_number.setAlignment ( QtCore.Qt.AlignCenter )
        self.label_length_number.setObjectName ( "label_length_number" )
        self.gridLayout.addWidget ( self.label_length_number , 5 , 2 , 1 , 1 )
        MainWindow.setCentralWidget ( self.centralwidget )
        self.menubar = QtWidgets.QMenuBar ( MainWindow )
        self.menubar.setGeometry ( QtCore.QRect ( 0 , 0 , 546 , 21 ) )
        self.menubar.setObjectName ( "menubar" )
        self.menufile = QtWidgets.QMenu ( self.menubar )
        self.menufile.setObjectName ( "menufile" )
        MainWindow.setMenuBar ( self.menubar )
        self.statusbar = QtWidgets.QStatusBar ( MainWindow )
        self.statusbar.setObjectName ( "statusbar" )
        MainWindow.setStatusBar ( self.statusbar )
        self.actionsave_to_cv = QtWidgets.QAction ( MainWindow )
        self.actionsave_to_cv.setObjectName ( "actionsave_to_cv" )
        self.menufile.addAction ( self.actionsave_to_cv )
        self.menubar.addAction ( self.menufile.menuAction () )

        self.retranslateUi ( MainWindow )
        QtCore.QMetaObject.connectSlotsByName ( MainWindow )

        # generate password pushbutton
        self.pushButton_generate.clicked.connect ( self.generate_password )
        # coppy password pushbutton
        self.pushButton_coppy.clicked.connect ( self.coppy_password )

    # def generate password
    def generate_password (self) :
        if not self.checkBox_a_z.isChecked () and not self.checkBox_0_9.isChecked () and not self.checkBox_more.isChecked () :
            QtWidgets.QMessageBox.warning ( self.centralwidget , "Error" , "Please select at least one character set!" )
            return

        chars = ''

        if self.checkBox_a_z.isChecked () :
            chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        if self.checkBox_0_9.isChecked () :
            chars += "0123456789"
        if self.checkBox_more.isChecked () :
            chars += "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
        # همیشه حروف کوچک را هم اضافه کن

        if not chars :
            self.lineEdit_password.setText ( "no character selected" )

        length = self.horizontalSlider_1_30.value ()
        password = ''.join ( random.choice ( chars ) for _ in range ( length ) )
        self.lineEdit_password.setText ( password )
        self.label_length_number.setText ( str ( length ) )

    # def coppy password
    def coppy_password (self) :
        self.lineEdit_password.selectAll ()
        self.lineEdit_password.copy ()
        self.statusbar.showMessage ( 'Password copied to clipboard ' , 3000 )

    def retranslateUi (self , MainWindow) :
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle ( _translate ( "MainWindow" , "MainWindow" ) )
        self.label_length.setText ( _translate ( "MainWindow" , "character length : " ) )
        self.checkBox_more.setText ( _translate ( "MainWindow" , "!@#" ) )
        self.checkBox_0_9.setText ( _translate ( "MainWindow" , "0-9" ) )
        self.label_name.setText ( _translate ( "MainWindow" , "password generator" ) )
        self.pushButton_generate.setText ( _translate ( "MainWindow" , "generate" ) )
        self.pushButton_coppy.setText ( _translate ( "MainWindow" , "coppy" ) )
        self.checkBox_a_z.setText ( _translate ( "MainWindow" , "A-Z" ) )
        self.label_length_number.setText ( _translate ( "MainWindow" , "30" ) )
        self.menufile.setTitle ( _translate ( "MainWindow" , "file" ) )
        self.actionsave_to_cv.setText ( _translate ( "MainWindow" , "save to .csv" ) )


if __name__ == "__main__" :
    import sys

    app = QtWidgets.QApplication ( sys.argv )
    MainWindow = QtWidgets.QMainWindow ()
    ui = Ui_MainWindow ()
    ui.setupUi ( MainWindow )
    MainWindow.show ()
    sys.exit ( app.exec_ () )
