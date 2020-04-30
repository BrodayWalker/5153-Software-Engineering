

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QPalette
from PyQt5.QtCore import Qt
from api import Api, Login, Employee, UserManager, ShoppingCart
import sys

class Ui_MainWindow(object):
    def __init__(self, start):
        self.start = start
        self.prompt_confirm = False
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 621)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 401, 601))
        self.stackedWidget.setObjectName("stackedWidget")
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(16)

        # login page code (page 1)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.stackedWidget.addWidget(self.page_1)
        self.groupBoxLI = QtWidgets.QGroupBox(self.page_1)
        self.groupBoxLI.setGeometry(QtCore.QRect(10,10,381,581))
        self.groupBoxLI.setObjectName("groupBoxLI")
        self.username_textbox = QtWidgets.QLineEdit(self.groupBoxLI)
        self.username_textbox.setGeometry(QtCore.QRect(120, 180, 141, 31))
        self.username_textbox.setObjectName("username_textbox")
        self.password_textbox = QtWidgets.QLineEdit(self.groupBoxLI)
        self.password_textbox.setGeometry(QtCore.QRect(120, 260, 141, 31))
        self.password_textbox.setObjectName("password_textbox")
        self.password_textbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.username_label = QtWidgets.QLabel(self.groupBoxLI)
        self.username_label.setGeometry(QtCore.QRect(120, 130, 141, 41))
        self.username_label.setFont(font)
        self.username_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.groupBoxLI)
        self.password_label.setGeometry(QtCore.QRect(120, 210, 141, 41))
        self.password_label.setFont(font)
        self.password_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.login_button = QtWidgets.QPushButton(self.groupBoxLI)
        self.login_button.setGeometry(QtCore.QRect(144, 310, 91, 23))
        self.login_button.setObjectName("login_button")
        self.create_account_button = QtWidgets.QPushButton(self.groupBoxLI)
        self.create_account_button.setGeometry(QtCore.QRect(144, 350, 91, 23))
        self.create_account_button.setObjectName("create_account_button")
        self.label = QtWidgets.QLabel(self.groupBoxLI)
        self.label.setGeometry(QtCore.QRect(50, 430, 281, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/login_shaq.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.logo = QtWidgets.QLabel(self.page_1)
        self.logo.setGeometry(QtCore.QRect(90, 20, 220, 120))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../images/Inno.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.failure_notif = QtWidgets.QLabel(self.groupBoxLI)
        self.failure_notif.setGeometry(QtCore.QRect(120, 390, 141, 31))
        self.failure_notif.setText("")
        self.failure_notif.setAlignment(QtCore.Qt.AlignCenter)
        self.failure_notif.setObjectName("failure_notif")

        # create account code (page 1.5)
        self.page_1_5 = QtWidgets.QWidget()
        self.page_1_5.setObjectName("page_1_5")
        self.stackedWidget.addWidget(self.page_1_5)
        self.groupBoxCA = QtWidgets.QGroupBox(self.page_1_5)
        self.groupBoxCA.setGeometry(QtCore.QRect(10,190,381,381))
        self.groupBoxCA.setObjectName("groupBoxCA")
        self.Username = QtWidgets.QLabel(self.groupBoxCA)
        self.Username.setGeometry(QtCore.QRect(30,40,91,16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)     
        self.Username.setFont(font)
        self.Username.setObjectName("Username")
        self.UserInput = QtWidgets.QLineEdit(self.groupBoxCA)
        self.UserInput.setGeometry(QtCore.QRect(160,40,211,31))
        self.UserInput.setObjectName("UserInput")
        self.Password = QtWidgets.QLabel(self.groupBoxCA)
        self.Password.setGeometry(QtCore.QRect(30,150,91,16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        self.Passinput = QtWidgets.QLineEdit(self.groupBoxCA)
        self.Passinput.setGeometry(QtCore.QRect(160,150,211,31))
        self.Passinput.setObjectName("Passinput")
        self.Passinput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CancelButton = QtWidgets.QPushButton(self.groupBoxCA)
        self.CancelButton.setGeometry(QtCore.QRect(10,260,121,31))
        self.CancelButton.setObjectName("CancelButton")
        self.CreateButton = QtWidgets.QPushButton(self.groupBoxCA)
        self.CreateButton.setGeometry(QtCore.QRect(250,260,121,31))
        self.CreateButton.setObjectName("CreateButton")
        self.Instructions = QtWidgets.QLabel(self.groupBoxCA)
        self.Instructions.setGeometry(QtCore.QRect(10,200,331,41))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.Instructions.setFont(font)
        self.Instructions.setObjectName("Instructions")
        self.photo = QtWidgets.QLabel(self.page_1_5)
        self.photo.setGeometry(QtCore.QRect(110,10,181,171))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../images/Charles_Barkley.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        # search page code (page 2)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.search_prompt_label = QtWidgets.QLabel(self.page_2)
        self.search_prompt_label.setGeometry(QtCore.QRect(90, 200, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(16)
        self.search_prompt_label.setFont(font)
        self.search_prompt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.search_prompt_label.setObjectName("search_prompt_label")
        self.no_results_notif = QtWidgets.QLabel(self.page_2)
        self.no_results_notif.setGeometry(QtCore.QRect(146, 353, 101, 31))
        self.failure_notif.setText("")
        self.no_results_notif.setAlignment(QtCore.Qt.AlignCenter)
        self.no_results_notif.setObjectName("no_results_notif")
        self.search_button = QtWidgets.QPushButton(self.page_2)
        self.search_button.setGeometry(QtCore.QRect(150, 310, 91, 23))
        self.search_button.setObjectName("search_button")
        self.search_box = QtWidgets.QLineEdit(self.page_2)
        self.search_box.setGeometry(QtCore.QRect(60, 250, 271, 41))
        self.search_box.setObjectName("search_box")

        # search results code (page 3)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.search_listWidget = QtWidgets.QListWidget(self.page_3)
        self.search_listWidget.setGeometry(QtCore.QRect(10, 10, 381, 521))
        self.search_listWidget.setObjectName("search_listWidget")
        self.search_back_button = QtWidgets.QPushButton(self.page_3)
        self.search_back_button.setGeometry(QtCore.QRect(10, 540, 101, 31))
        self.search_back_button.setObjectName("search_back_button")

        # item page code (page 4)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.item_back_button = QtWidgets.QPushButton(self.page_4)
        self.item_back_button.setGeometry(QtCore.QRect(10, 540, 101, 31))
        self.item_back_button.setObjectName("item_back_button")
        self.addbutton = QtWidgets.QPushButton(self.page_4)
        self.addbutton.setGeometry(QtCore.QRect(280, 540, 101, 31))
        self.addbutton.setObjectName("addbutton")
        self.addbutton.setEnabled(True)
        self.name = QtWidgets.QLabel(self.page_4)
        self.name.setGeometry(QtCore.QRect(10, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.price = QtWidgets.QLabel(self.page_4)
        self.price.setGeometry(QtCore.QRect(140, 370, 81, 31))
        self.price_label = QtWidgets.QLabel(self.page_4)
        self.price_label.setGeometry(QtCore.QRect(10, 370, 121, 31))
        self.price_label.setFont(font)
        self.price_label.setObjectName("price_label")
        self.quantity = QtWidgets.QLabel(self.page_4)
        self.quantity.setGeometry(QtCore.QRect(10, 330, 121, 31))
        self.quantity.setFont(font)
        self.quantity.setObjectName("quantity")
        self.numitems = QtWidgets.QLabel(self.page_4)
        self.numitems.setGeometry(QtCore.QRect(140, 330, 81, 31))
        self.available_label = QtWidgets.QLabel(self.page_4)
        self.available_label.setGeometry(QtCore.QRect(10, 410, 121, 31))
        self.available_label.setFont(font)
        self.available_label.setObjectName("available_label")
        self.itemdescription = QtWidgets.QLabel(self.page_4)
        self.itemdescription.setGeometry(QtCore.QRect(10, 210, 121, 41))
        self.itemdescription.setFont(font)
        self.itemdescription.setObjectName("itemdescription")
        self.description_text = QtWidgets.QLabel(self.page_4)
        self.description_text.setGeometry(QtCore.QRect(140, 220, 251, 101))
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.item_name = QtWidgets.QLabel(self.page_4)
        self.item_name.setGeometry(QtCore.QRect(140, 160, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.price.setFont(font)
        self.price.setObjectName("price")
        self.item_name.setFont(font)
        self.item_name.setScaledContents(True)
        self.item_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.item_name.setWordWrap(True)
        self.item_name.setObjectName("item_name")
        self.available_status = QtWidgets.QLabel(self.page_4)
        self.available_status.setGeometry(QtCore.QRect(140, 410, 81, 31))
        self.available_status.setFont(font)
        self.available_status.setObjectName("available_status")
        self.description_text.setFont(font)
        self.description_text.setScaledContents(True)
        self.description_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_text.setWordWrap(True)
        self.description_text.setObjectName("description_text")
        self.item_line = QtWidgets.QFrame(self.page_4)
        self.item_line.setGeometry(QtCore.QRect(0, 130, 401, 16))
        self.item_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.item_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.item_line.setObjectName("item_line")
        self.item_line_2 = QtWidgets.QFrame(self.page_4)
        self.item_line_2.setGeometry(QtCore.QRect(0, 450, 401, 16))
        self.item_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.item_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.item_line_2.setObjectName("item_line_2")
        self.photo = QtWidgets.QLabel(self.page_4)
        self.photo.setGeometry(QtCore.QRect(90,10,220,120))
        self.photo.setFrameShape(QtWidgets.QFrame.Box)
        self.photo.setLineWidth(2)
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../images/surprise_shaq.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.numitems.setFont(font)
        self.numitems.setObjectName("numitems")
        self.info_label = QtWidgets.QLabel(self.page_4)
        self.info_label.setGeometry(QtCore.QRect(130, 540, 131, 31))
        self.info_label.setText("")
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setObjectName("info_label")

        # shopping cart page code (page 5)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.page_5.setFont(font)
        self.remove_button = QtWidgets.QPushButton(self.page_5)
        self.remove_button.setGeometry(QtCore.QRect(270, 430, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remove_button.setFont(font)
        self.remove_button.setObjectName("remove_button")
        self.cart_back_button = QtWidgets.QPushButton(self.page_5)
        self.cart_back_button.setGeometry(QtCore.QRect(20, 530, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cart_back_button.setFont(font)
        self.cart_back_button.setObjectName("cart_back_button")
        self.cart_listWidget = QtWidgets.QListWidget(self.page_5)
        self.cart_listWidget.setGeometry(QtCore.QRect(20, 69, 360, 241))
        self.cart_listWidget.setObjectName("cart_listWidget")
        self.users_sc = QtWidgets.QLabel(self.page_5)
        self.users_sc.setGeometry(QtCore.QRect(20, 15, 360, 40))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(26)
        self.users_sc.setFont(font)
        self.users_sc.setAlignment(QtCore.Qt.AlignCenter)
        self.users_sc.setObjectName("users_sc")
        self.total_label = QtWidgets.QLabel(self.page_5)
        self.total_label.setGeometry(QtCore.QRect(30, 320, 41, 31))
        self.total_label.setObjectName("total_label")
        self.sc_line = QtWidgets.QFrame(self.page_5)
        self.sc_line.setGeometry(QtCore.QRect(0, 355, 400, 16))
        self.sc_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.sc_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sc_line.setObjectName("sc_line")
        self.cost_label = QtWidgets.QLabel(self.page_5)
        self.cost_label.setGeometry(QtCore.QRect(150, 320, 100, 31))
        self.cost_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cost_label.setObjectName("cost_label")
        self.item_prompt = QtWidgets.QLabel(self.page_5)
        self.item_prompt.setGeometry(QtCore.QRect(0, 360, 400, 70))
        self.item_prompt.setAlignment(QtCore.Qt.AlignCenter)
        self.item_prompt.setObjectName("item_prompt")
        # self.item_page_button = QtWidgets.QPushButton(self.page_5)
        # self.item_page_button.setGeometry(QtCore.QRect(140, 430, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        # self.item_page_button.setFont(font)
        # self.item_page_button.setObjectName("item_page_button")
        self.chng_quan_button = QtWidgets.QPushButton(self.page_5)
        self.chng_quan_button.setGeometry(QtCore.QRect(20, 430, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chng_quan_button.setFont(font)
        self.chng_quan_button.setObjectName("chng_quan_button")
        self.checkout_button = QtWidgets.QPushButton(self.page_5)
        self.checkout_button.setGeometry(QtCore.QRect(270, 530, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkout_button.setFont(font)
        self.checkout_button.setObjectName("checkout_button")
        self.quantity_spin = QtWidgets.QSpinBox(self.page_5)
        self.quantity_spin.setGeometry(QtCore.QRect(50, 470, 42, 22))
        self.quantity_spin.setObjectName("quantity_spin")
        self.quantity_spin.setMinimum(1)
        self.quantity_spin.setValue(1)
        self.sc_line_2 = QtWidgets.QFrame(self.page_5)
        self.sc_line_2.setGeometry(QtCore.QRect(0, 500, 400, 16))
        self.sc_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.sc_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sc_line_2.setObjectName("sc_line_2")

####################################################################################################

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuYour_Shopping_Cart = QtWidgets.QMenu(self.menuBar)
        self.menuYour_Shopping_Cart.setObjectName("menuYour_Shopping_Cart")
        self.menuUpdate_Credentials = QtWidgets.QMenu(self.menuYour_Shopping_Cart)
        self.menuUpdate_Credentials.setObjectName("menuUpdate_Credentials")
        MainWindow.setMenuBar(self.menuBar)
        self.actionShopping_Cart = QtWidgets.QAction(MainWindow)
        self.actionShopping_Cart.setObjectName("actionShopping_Cart")
        self.actionChange_Username = QtWidgets.QAction(MainWindow)
        self.actionChange_Username.setObjectName("actionChange_Username")
        self.actionChange_Password = QtWidgets.QAction(MainWindow)
        self.actionChange_Password.setObjectName("actionChange_Password")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        self.menuUpdate_Credentials.addAction(self.actionChange_Username)
        self.menuUpdate_Credentials.addAction(self.actionChange_Password)
        self.menuYour_Shopping_Cart.addAction(self.actionShopping_Cart)
        self.menuYour_Shopping_Cart.addAction(self.menuUpdate_Credentials.menuAction())
        self.menuYour_Shopping_Cart.addAction(self.actionLogout)
        self.menuBar.addAction(self.menuYour_Shopping_Cart.menuAction())

        # set all the menu buttons to disabled until a user logs in
        self.actionShopping_Cart.setEnabled(False)
        self.actionChange_Username.setEnabled(False)
        self.actionChange_Password.setEnabled(False)
        self.actionLogout.setEnabled(False)

        self.retranslateUi(MainWindow)

        # sets the starting page to index 0 when app is started
        self.stackedWidget.setCurrentIndex(self.start)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # when login button is pressed, call login method
        self.login_button.clicked.connect(self.login)

        # when the user clicks the 'create account' button from the main page
        self.create_account_button.clicked.connect(self.switch_to_create_acc)

        # Connect the createuser button with the createAcc function
        self.CreateButton.clicked.connect(self.createAcc)

        # Return user to login screen
        self.CancelButton.clicked.connect(lambda: self.switch_page(0))
                
        # when button is pressed, call search method
        self.search_button.clicked.connect(self.search_products)

        # logs a user out
        self.actionLogout.triggered.connect(self.logout)

        # if an item is clicked, go to item's page
        self.search_listWidget.itemClicked.connect(self.display_item_page)

        # adds an item the user's shopping cart
        self.addbutton.clicked.connect(self.add_to_shoppingcart)

        # navigate to the user's shopping cart
        self.actionShopping_Cart.triggered.connect(self.initialize_shoppingcart)

        # go back to the search results page from the shopping cart
        self.cart_back_button.clicked.connect(lambda: self.switch_page(2))

        # removes an item from the user's cart
        self.remove_button.clicked.connect(self.remove_item)

        # updates an item's quantity to what is designated in quantity box
        self.chng_quan_button.clicked.connect(self.change_quan)

        # asks the user if they want to purchase items
        self.checkout_button.clicked.connect(self.checkout)

        # # displays an item's page by performing a query on the database,
        # # that way, the item page displays current info
        # self.item_page_button.clicked.connect(self.cart_display_page)

        # # when back buttons are pressed, call switch to previous page
        self.item_back_button.clicked.connect(lambda: self.switch_page(self.stackedWidget.currentIndex()-1))
        self.search_back_button.clicked.connect(lambda: self.switch_page(self.stackedWidget.currentIndex()-1))

        # self.prepEmployee()
#######################################################################################################

    def prepEmployee(self):
        # add the Change Quantity buttons and spin box and the Make Available button
        self.item_quan_spinBox = QtWidgets.QSpinBox(self.page_4)
        self.item_quan_spinBox.setGeometry(QtCore.QRect(11,470,101,22))
        self.item_quan_spinBox.setObjectName("item_quan_spinBox")
        self.item_quan_spinBox.setMinimum(1)
        self.item_quan_spinBox.setMaximum(999999)
        self.item_chng_quan = QtWidgets.QPushButton(self.page_4)
        self.item_chng_quan.setGeometry(QtCore.QRect(10, 500, 101, 31))
        self.item_chng_quan.setObjectName("item_chng_quan")
        self.item_mk_avail_button = QtWidgets.QPushButton(self.page_4)
        self.item_mk_avail_button.setGeometry(QtCore.QRect(280, 500, 101, 31))
        self.item_mk_avail_button.setObjectName("item_mk_avail_button")
        # put text into the buttons
        _translate = QtCore.QCoreApplication.translate
        self.item_chng_quan.setText(_translate("MainWindow", "Change Quantity"))
        self.item_mk_avail_button.setText(_translate("MainWindow", "Make Available"))
        # employees do not add items to their carts since they don't have any
        self.addbutton.setEnabled(False)
        # create the employee object
        self.employee_object = Employee()
        # add functionality to employee buttons
        self.item_chng_quan.clicked.connect(self.employee_change_quan)
        self.item_mk_avail_button.clicked.connect(self.employee_change_avail)

        # change the color of the background
        self.page_2.setAutoFillBackground(True)
        self.page_3.setAutoFillBackground(True)
        self.page_4.setAutoFillBackground(True)
        p2 = self.page_2.palette()
        p3 = self.page_3.palette()
        p4 = self.page_4.palette()
        p2.setColor(self.page_2.backgroundRole(), Qt.darkRed)
        p3.setColor(self.page_3.backgroundRole(), Qt.darkRed)
        p4.setColor(self.page_4.backgroundRole(), Qt.darkRed)
        self.page_2.setPalette(p2)
        self.page_3.setPalette(p3)
        self.page_4.setPalette(p4)

        print("Fully prepped for employee")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Innoventory"))
        self.search_prompt_label.setText(_translate("MainWindow", "What are you looking for?"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.create_account_button.setText(_translate("MainWindow", "Create Account"))
        # self.groupBoxCA.setTitle(_translate("MainWindow", "Input field"))
        self.Username.setText(_translate("MainWindow", "Username"))
        self.Password.setText(_translate("MainWindow", "Password"))
        self.CancelButton.setText(_translate("MainWindow", "Cancel"))
        self.CreateButton.setText(_translate("MainWindow", "Create User"))
        self.Instructions.setText(_translate("MainWindow", "Please enter the username and password for your new account."))
        self.item_back_button.setText(_translate("MainWindow", "Back"))
        self.search_back_button.setText(_translate("MainWindow", "Back"))
        self.addbutton.setText(_translate("MainWindow", "Add to Cart"))
        self.name.setText(_translate("MainWindow", "Name:"))
        self.item_name.setText(_translate("MainWindow", ""))
        self.itemdescription.setText(_translate("MainWindow", "Description:"))
        self.description_text.setText(_translate("MainWindow", "Description"))
        self.quantity.setText(_translate("MainWindow", "Quantity: "))
        self.numitems.setText(_translate("MainWindow", ""))
        self.remove_button.setText(_translate("MainWindow", "Remove Item"))
        self.cart_back_button.setText(_translate("MainWindow", "Back"))
        self.users_sc.setText(_translate("MainWindow", "Your Shopping Cart"))
        self.total_label.setText(_translate("MainWindow", "Total: "))
        self.cost_label.setText(_translate("MainWindow", "cost"))
        self.item_prompt.setText(_translate("MainWindow", "Click an item to iteract"))
        # self.item_page_button.setText(_translate("MainWindow", "Go to item page"))
        self.chng_quan_button.setText(_translate("MainWindow", "Update Quantity"))
        self.checkout_button.setText(_translate("MainWindow", "Checkout"))
        self.menuYour_Shopping_Cart.setTitle(_translate("MainWindow", "Your Account"))
        self.menuUpdate_Credentials.setTitle(_translate("MainWindow", "Update Credentials"))
        self.actionShopping_Cart.setText(_translate("MainWindow", "Shopping Cart"))
        self.actionChange_Username.setText(_translate("MainWindow", "Change Username"))
        self.actionChange_Password.setText(_translate("MainWindow", "Change Password"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))
        self.price_label.setText(_translate("MainWindow", "Price:"))
        self.price.setText(_translate("MainWindow", "$"))
        self.available_label.setText(_translate("MainWindow", "Available?"))
        self.available_status.setText(_translate("MainWindow", "Yes/No"))

###################################################################################################################################

    # attempt to log in to Innoventory with username and password offered
    def login(self, MainWindow):
        if self.username_textbox.text() != "" and self.password_textbox.text() != "":
            self.username_password = {  'username': self.username_textbox.text(), 
                                        'password': self.password_textbox.text()
                                    }
            user = Login()
            _, login_success, self.userType = user.login(self.username_password)
            self.login_result(login_success)

    # allow user in if credentials are verified; block otherwise
    def login_result(self, login_success):
        # if the user logged in successfully and they are a customer
        if login_success and self.userType:
            # create the shopping cart object for shopping cart additions, removals, and modifications
            self.shopping_cart_object = ShoppingCart({'username': self.username_password['username']})
            # create a shopping cart copy to prevent multiple database queries (like when checking if an item is already in the cart before adding it)
            self.shopping_cart_list = self.shopping_cart_object.readShoppingcart()
            # re-enable menu bar buttons
            self.actionShopping_Cart.setEnabled(True)
            # self.actionChange_Username.setEnabled(True)
            # self.actionChange_Password.setEnabled(True)
            self.actionLogout.setEnabled(True)
            self.username_textbox.setText("")
            self.password_textbox.setText("")
            self.switch_page(2)
        # if the login was successful and the user is not a customer (i.e. an employee)
        elif login_success and not self.userType:
            # prepares the app for viewing by a employee
            self.prepEmployee()
            self.username_textbox.setText("")
            self.password_textbox.setText("")
            self.actionLogout.setEnabled(True)
            self.switch_page(2)
        else:
            self.failure_notif.setText("Failed attempt.\nPlease try again.")

    # log the user out and return them to the login page       
    def logout(self):
        if self.userType:
            self.actionShopping_Cart.setEnabled(False)
            self.actionChange_Username.setEnabled(False)
            self.actionChange_Password.setEnabled(False)
        self.actionLogout.setEnabled(False)
        self.switch_page(0)

    # If the user does something weird, tell them off.
    def error(self, cause):
        self.photo.setPixmap(QtGui.QPixmap("../images/Mad_Charlie.jpg"))

        if cause == 1:
            self.Instructions.setText("Error: Please enter a value for username and password")
            self.Instructions.adjustSize()
        
        elif cause == 2:
            self.Instructions.setText("Error: That username has already been taken.")
            self.Instructions.adjustSize()

    def switch_to_create_acc(self):
        self.UserInput.setText("")
        self.Passinput.setText("")
        self.switch_page(1)


    # Once the user has filled in the input fields, check to see if they are
    # compatible. If everything works out, then upload their information into the
    # "users" collection.
    def createAcc(self):
        username = self.UserInput.text()
        password = self.Passinput.text()

        # If the user is lazy
        if username == '' or password == '':
            self.error(1)
        
        # Upload the requested info into our database
        else:
            creation = UserManager()
            if creation.createUser({'username': username, 'password': password}):
                self.Instructions.setText("Success! Your account has been created!")
                self.Instructions.adjustSize()

                self.gif = QMovie('../images/Success.gif')
                self.photo.setMovie(self.gif)
                self.gif.start()

                self.CancelButton.setText("Login")
            else:
                self.error(2)

    # readjusts label sizes so text inside will not overflow
    def update(self, widget):
        widget.adjustSize()

    # run an item search using the API
    def search_products(self):
        if self.search_box.text() != "":
            search_string = self.search_box.text()
            self.search_attempt = Api()
            # 'self.search_result' is now an unordered set of all the search results
            self.search_result = self.parse_results(self.search_attempt.search({'item': search_string}))
            if self.search_result != []:
                self.switch_page(3)
                self.display_results()
            else:
                self.no_results_notif.setText("No results found")

    # Returns an unordered set of item names from a search
    def parse_results(self, result):
        # Use a set to avoid duplicate results
        items = {}
        counter = 0
        for doc in result:
            for item in doc:
                if item != None:
                    items[str(counter)] = item
                    counter += 1
        return items

    # print search results to a list widget
    def display_results(self):
        self.search_listWidget.clear()
        for count in range(0,len(self.search_result)):
            item_string = self.search_result[str(count)]["item"] + " "
            # if "details" in result:
            #     for num in range(0,len(result["details"])):
            #         item_string += str(result["details"]["name" + str(num)]) + " "
            item = QtWidgets.QListWidgetItem(item_string)
            self.search_listWidget.addItem(item)

    # will switch to widget representing page 'next_page'
    def switch_page(self, next_page):
        self.next_page = next_page
        # if the argument 'next_page' is an integer, 
        if isinstance(self.next_page, int):
            self.stackedWidget.setCurrentIndex(self.next_page)
        else:
            self.stackedWidget.setCurrentWidget(self.next_page)
    
    def display_item_page(self, item):
        # print("Item in row", self.search_listWidget.row(item), "was clicked!")
        self.item = item
        # 'index'  is the product the user clicked on ('item') found in the 'self.search_result' list 
        product = self.search_result[str(self.search_listWidget.row(self.item))]
        # print item name
        self.item_name.setText(product["item"])
        # print item details
        detail_string = ""
        if "details" in product:
            for num in range(0,len(product["details"])):
                detail_string += str(product["details"]["name" + str(num)]) + "\n"
        else:
            detail_string = '-'
        self.description_text.setText(detail_string)
        # print product quantity
        if "quantity" in product:
            self.numitems.setText(str(product["quantity"]))
        else:
            self.numitems.setText("-")
        # print product availability
        if product['availability']:
            self.available_status.setText("Yes")
        else:
            self.available_status.setText("No")
        # print product price
        self.price.setText('$' + str(product['price']))
        self.update(self.item_name)
        self.update(self.description_text)
        self.info_label.setText("")
        if not self.userType:
            if product['availability']:
                self.item_mk_avail_button.setText("Make Unavailable")
            else:
                self.item_mk_avail_button.setText("Make Available")
        self.switch_page(4)
        # print(item.text())

    # change the quantity of an item
    def employee_change_quan(self):
        product = self.search_result[str(self.search_listWidget.row(self.item))]
        # some items don't have a quantity field
        if 'quantity' in product:
            # changes the quantity of the product, returns the updated quantity, and updates quantity on item page
            new_quan = self.employee_object.change_quantity(product,self.item_quan_spinBox.value())
            self.numitems.setText(str(new_quan))
            self.search_result[str(self.search_listWidget.row(self.item))]['quantity'] = new_quan

    # change the quantity of an item
    def employee_change_avail(self):
        product = self.search_result[str(self.search_listWidget.row(self.item))]
        # if product is available, make it not
        if product['availability']:
            # change availability of product to false
            self.employee_object.change_availability(product,False)
            self.search_result[str(self.search_listWidget.row(self.item))]['availability'] = False
            self.available_status.setText("No")
            self.item_mk_avail_button.setText("Make Available")
        # if product is not available, make it available
        else:
            # change availability of product to true
            self.employee_object.change_availability(product,True)
            self.search_result[str(self.search_listWidget.row(self.item))]['availability'] = True
            self.item_mk_avail_button.setText("Make Unavailable")
            self.available_status.setText("Yes")

    def add_to_shoppingcart(self):
        product = self.search_result[str(self.search_listWidget.row(self.item))]
        if product['item'] not in self.shopping_cart_list:
            product['quantity'] = 1
            self.shopping_cart_object.addCart(product)
            self.shopping_cart_list.append(product)
            self.info_label.setText("Added to cart!")
            self.findPrice()
        else:
            self.info_label.setText("Already in cart!")
    
    # will fill the list widget on the shopping cart page with all the items in the 
    # user's shopping cart
    def initialize_shoppingcart(self):
        self.cart_listWidget.clear()
        for product in self.shopping_cart_list:
            item = QtWidgets.QListWidgetItem("Item: " + product['item'] + ", Count: " + str(product['quantity']) + ", Price: " + str(product['price']))
            self.cart_listWidget.addItem(item)
        self.findPrice()
        self.item_prompt.setText("Click an item to interact")
        self.switch_page(5)
    
    def findPrice(self):
        total_price = 0
        for item in self.shopping_cart_list:
            total_price += item['price'] * item['quantity']
        self.cost_label.setText(str(total_price))

    def remove_item(self):
        if self.cart_listWidget.count():
            item = self.cart_listWidget.currentRow()
            # remove the item from the database shopping cart
            self.shopping_cart_object.removeCart(self.shopping_cart_list[item])
            # remove the item from the local shopping cart variable (database shopping cart copy)
            self.shopping_cart_list.pop(item)
            # get rid of the item from the list widget
            self.cart_listWidget.takeItem(item)
            self.findPrice()

    def change_quan(self):
        if self.cart_listWidget.count():
            self.shopping_cart_object.changeQuan(self.shopping_cart_list[self.cart_listWidget.currentRow()], self.quantity_spin.value())
            self.findPrice()
            item = self.shopping_cart_list[(self.cart_listWidget.currentRow())]
            item['quantity'] = self.quantity_spin.value()

    def checkout(self):
        if self.cart_listWidget.count():
            if self.prompt_confirm == False:
                self.checkout_button.setText("Are you sure?")
                self.prompt_confirm = True
            else:
                self.prompt_confirm = False
                self.item_prompt.setText("Thank you for your purchase!\nPress \"Back\" to return to search")
                self.cart_listWidget.clear()
                self.shopping_cart_list = []
                self.shopping_cart_object.emptyCart()

    # def cart_display_page(self):
    #     # 'index'  is the product the user clicked on ('item') found in the 'self.search_result' list 
    #     # add a function to API called quick search that lets you search for one document
    #     product = {}
    #     detail_string = ""
    #     self.switch_page(4)
    #     self.item_name.setText(product["item"])
    #     if "details" in product:
    #         for num in range(0,len(product["details"])):
    #             detail_string += str(product["details"]["name" + str(num)]) + "\n"
    #     else:
    #         self.description_text.setText("-")
    #     self.description_text.setText(detail_string)
    #     if "quantity" in product:
    #         self.numitems.setText(str(product["quantity"]))
    #     else:
    #         self.numitems.setText("-")
    #     self.update(self.item_name)
    #     self.update(self.description_text)
    #     # print(item.text())

###########################################################################################################################

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(0)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())