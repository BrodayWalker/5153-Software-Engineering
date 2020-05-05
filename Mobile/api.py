#!/usr/bin/env python3

import json
import urllib.parse
from pprint import pprint
from pymongo import MongoClient, ReturnDocument

class Api:
    '''
    The API class implements the Innoventory API which is used to interact
    with the backend MongoDB instance. 
    '''
    authenUsername = urllib.parse.quote("AuthenTest")
    authenPassword = urllib.parse.quote("test")
    authenConnectionString = f"mongodb+srv://{authenUsername}:{authenPassword}@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority"
    
    customerUsername = urllib.parse.quote("customer")
    customerPassword = urllib.parse.quote("gIcgQXd4prd1C3yk")
    customerConnectionString = f"mongodb+srv://{customerUsername}:{customerPassword}@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority"
    
    employeeUsername = urllib.parse.quote("employee")
    employeePassword = urllib.parse.quote("h57pnEeTXY299LDx")
    employeeConnectionString = f"mongodb+srv://{employeeUsername}:{employeePassword}@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority"

    emptyUser = {'username': '', 'password': ''}

    # connect to a database using a valid connection string and return client
    def connect(self, connectionString=""):
        self.connectionString = connectionString
        client = MongoClient(connectionString)
        return client    

    # search the product collection for a specific item
    def search(self, term):
        self.term = term
        client = self.connect(self.customerConnectionString)
        db = client.Innoventory

        # will hold all documents from queries
        result = []

        # Find best result
        search_one = db.Products.find_one(self.term)

        # Add the result if item was found
        if search_one != None:
            result.append([search_one])

        # find more general results
        # split the search term by whitespace
        new_search = self.term["item"].split()

        # search database by each word in term
        for word in new_search:
            # mini_result = db.Products.find({ "item": "/"+word+"/" })
            # result.append(mini_result)
            result.append(list(db.Products.find({ "item": {'$regex': word }})))
        return result

    # a simple print function for item names
    def display_results(self, search_result):
        for doc in search_result:
            for result in doc:
                print(result['item'])

    # Returns an unordered set of item names from a search
    def parse_results(self, search_result):
        # Use a set to avoid duplicate results
        items = set()
        if search_result != None:
            for doc in search_result:
                for result in doc:
                    items.add(result['item'])
        return items

# Employee class offers the two operations an Innoventory employee can perform:
# change any product's availability and quantity
class Employee(Api):
    '''
    The Employee class provides the functionality to to modify product quantity and availability
    '''
    def __init__(self):
        client = self.connect(self.employeeConnectionString)
        db = client.Innoventory
        self.collection = db.Products
    
    '''
    The change_quantity method updates the quantity of item, identified by the dictionary
    ``item``, to the value in ``quantity``.
    Returns the updated quantity from the database itself to prove the change has been made
    '''
    def change_quantity(self, item={}, quantity=1):
        return self.collection.find_one_and_update(
            filter=item,
            update={'$set': {'quantity': quantity}},
            return_document=ReturnDocument.AFTER
        )['quantity']

    '''
    The change_availability method updates the availability of item, identified by the dictionary
    ``item``, to the value in ``avail``.
    Returns the updated availability from the database itself to prove the change has been made.
    '''
    def change_availability(self, item={}, avail=bool):
        return self.collection.find_one_and_update(
            filter=item,
            update={'$set': {'availability': avail}},
            return_document=ReturnDocument.AFTER
        )['availability']

class Login(Api):
    '''
    The Login class provides the functionality to query the MongoDB instance
    to authenticate a user.
    '''

    '''
    The checkPassword method accepts a dictionary containing the username and password
    of the user to be authenticated. If the username and password are valid and correct,
    the user's information is returned as a dictionary. If the username and/or password
    are not correct, an Api.emptyUser dictionary is returned.
    '''
    def authenticate(self, user={'username': '', 'password': '', 'isCustomer': ''}):
        self.user = user
        validPassword = False
        # Get connection to database
        client = self.connect(Api.authenConnectionString)
        # Switch to Authen database
        db = client.Authen
        # Switch to Users collection in Authen database
        collection = db.Users
        # search for user
        # returns a single document or None if there is no match
        userInfo = collection.find_one({'username':self.user['username']})

        #########################################################################
        login_success = False
        customer = False
        #########################################################################

        # if found, check to see if password matches
        if userInfo != None:
            # check password retrieved from database vs input password
            if userInfo['password'] == self.user['password']:
                validPassword = True

            # Password tests
            if validPassword:
                # print("Valid username, valid password")
                login_success = True
                customer = userInfo['isCustomer']
            else:
                # print("Valid username, invalid password")
                userInfo = Api.emptyUser
        else:
            userInfo = Api.emptyUser

        return userInfo, login_success, customer

    '''
    The login method accepts a user dictionary containing the username and password.
    The password is checked and the userInfo object is returned.
    '''
    def login(self, user={'username': '', 'password': ''}):
        self.user = user
        # returns the userInfo dictionary and a boolean, login_success
        return self.authenticate(self.user)

    
class UserManager(Api):
    '''
    The UserManager class contains methods for creating users and modifying
    '''

    # Connects to the Authen database and switches to the Users collection
    def connectToAuthen(self):
        # Get connection to MongoDB instance as the authen user
        client = self.connect(Api.authenConnectionString)
        # Connect to Authen db
        db = client.Authen
        # Switch to Users collection
        collection = db.Users      

        return collection 

    # The createUser method creates a new user if the given username is not already in use
    def createUser(self, data={}):
        self.data = data
        status = False

        collection = self.connectToAuthen()

        # Make sure username does not already exist
        # find_one returns None if the username is not in the Users collection
        userExists = collection.find_one({'username': self.data['username']})
        
        # If the username does not already exist, it is safe to create the new user
        if userExists == None:
            # all users who create an account from the app are customers (isCustomer = True)
            # Employees are only added by database admins directly through the Mongo Atlas (isCustomer = False)
            self.data['isCustomer'] = True
            collection.insert_one(self.data)
            status = True

            # create the user's shopping cart in the 'Shopping_Cart' collection
            ShoppingCart({'username': self.data['username']}).createCart()
        
        # Return true for successful user creation, false for user creation failure
        return status

    # The removeUser function removes a user account from the Users collection if it exists
    # The number of documents removed is returned as an integer value
    def removeUser(self, data={}):
        self.data = data
        status = 0
        
        collection = self.connectToAuthen()

        # If the username exists, remove it from the Users collection
        result = collection.delete_one(self.data)

        # remove user's shopping cart
        ShoppingCart(self.data).eraseUser()

        status = result.deleted_count

        return status

    # Modifies a user password.
    def changePassword(self, oldData = {}, newData = {}):
        self.data = oldData
        self.data2 = newData

        # If the data authenticates, change the user's password 
        collection = self.connectToAuthen()
        
        return collection.update_one(self.data, {'$set':self.data2}).acknowledged

# This class represents all the shopping cart functionality
# See __main__ for example code
class ShoppingCart(Api):
    '''
    The ShoppingCart class contains methods for creating, accessing, and modifying
    a customer's shopping cart.
    For security reasons, do not pass passwords in the ``user`` dictionary,
    only the user's name.
    Per-customer Schema: 
    "_id": {
        "$oid": #########
    },
    "username": <customer's username>,
    "cart": [
        {},
        {},
        ...
    ]
    '''
    def __init__(self, user={'username': ''}):
        client = self.connect(Api.authenConnectionString)
        # Connect to Authen db
        db = client.Authen
        # Switch to Users collection
        self.collection = db.Shopping_Cart
        self.user = user

    '''
    The createCart method inserts a document in the Shopping Cart collection
    for the customer
    '''
    def createCart(self):
        # create an empty array for cart items
        # Returns true if insertion was successful
        return self.collection.insert_one({'username': self.user['username'], 'cart': []}).acknowledged

    ''' 
    The addCart method will add an item to the user's cart by appending the dictionary ``item``
    to the ``cart`` list 
    Example:
          shop_cart.addCart({'username': 'bwalker'}, {'item':'Dr. Pepper','quantity':1,'available':True})
    '''
    def addCart(self, item={}):
        self.item = item
        return self.collection.update_one(
                self.user, 
                {'$push': {'cart': {'$each': [ self.item ]}}}
        ).acknowledged

    ''' 
    The removeCart method will remove an item from the user's cart by dropping
    the ``item`` document from the ``cart`` list. 
    Example:
          shop_cart.removeCart({'username': 'bwalker'}, {'item':'Dr. Pepper'})
    '''  
    def removeCart(self, item={}):
        self.item = item
        return self.collection.update_one(
            self.user, 
            {'$pull': {'cart': self.item }}
        ).acknowledged
    
    ''' 
    The changeQuan method will update ``item`` in the customer's shopping cart to 
    have quantity ``quantity``
    Example:
          shop_cart.removeCart({'item':'Dr. Pepper'}, 5)
    '''  
    def changeQuan(self, item={}, quantity=1):
        self.item = item
        self.quantity = quantity
        return self.collection.update_one(
            filter=self.user,
            update={'$set': {f"cart.$[element].quantity": self.quantity}},
            array_filters=[{'element': self.item}]
        ).acknowledged
    
    ''' 
    The readShoppingcart method will return the customer's shopping cart contents
    as a list of dictionaries
    '''  
    def readShoppingcart(self):
        return dict(self.collection.find_one(filter=self.user))['cart']

    ''' 
    The emptyCart method will empty the ``cart`` list of a customer
    '''      
    def emptyCart(self):
        return self.collection.find_one_and_update(self.user, {'$set' : {'cart': []}})

    ''' 
    The eraseUser method will completely delete the user and their shopping cart
    from the Shopping Cart collection
    '''  
    def eraseUser(self):
        return self.collection.delete_one(self.user).acknowledged

# If api.py is run on its own, all tests will be run and the results will be shown
if __name__ == "__main__":

    # Requirement 2.1 Tests - Login 
    ###############################

    print("Requirement 2.1 - Login\n----------------------------------")
    validTestCustomer = {'username':'bwalker', 'password':'GC2020'}
    validTestEmployee = {'username':'cmatamoros', 'password':'GC2030'}
    invalidPassword = {'username':'bwalker', 'password':'wrong'}
    invalidUsername = {'username':'bwekrlkd', 'password':'doesntmatter'}

    # Get an instance of the Login class to test login functionality
    loginTest = Login()
    
    # Valid username and password test for customer
    user, login_success, user_type = loginTest.login(validTestCustomer)
    if login_success:
        print('TC01: Passed')
    else:
        print('TC01: Failed')
    
    # Valid username and password test for employee
    user, login_success, user_type = loginTest.login(validTestEmployee)
    if not user_type:
        print('TC02: Passed')
    else:
        print('TC02: Failed')

    # Valid username, invalid password test
    user, login_success, user_type = loginTest.login(invalidPassword)
    if not login_success:
        print('TC03: Passed')
    else:
        print('TC03: Failed')

    # Invalid username, Invalid password
    user, login_success, user_type = loginTest.login(invalidUsername)
    if not login_success:
        print('TC04: Passed')
    else:
        print('TC04: Failed')

    # No login information given
    user, login_success, _ = loginTest.login()
    if not login_success:
        print('TC05: Passed')
    else:
        print('TC05: Failed')

    # Create user account
    userTest = UserManager()

    # Create a user that doesn't exist
    result = userTest.createUser({'username': 'test', 'password': 'test'})
    if result == True:
        print('TC06: Passed')
    else:
        print('TC06: Failed')

    # Remove the user that was just created
    result = userTest.removeUser({'username': 'test'})
    if result == True:
        print('TC07: Passed')
    else:
        print('TC07: Failed')

    # Try to create a user using a username that is taken already
    result = userTest.createUser({'username': 'bwalker', 'password' : 'random'})
    if result == False:
        print('TC08: Passed')
    else:
        print('TC08: Failed')

    # Try to delete a user that doesn't exist
    result = userTest.removeUser({'username': 'test'})
    if result == False:
        print('TC09: Passed')
    else:
        print('TC09: Failed')

    print('\n')

    # Requirement 2.2 Tests - Item Search and Discovery
    ###################################################

    print("Requirement 2.2 - Item Search and Discovery\n----------------------------------")
    # Get an instance of the Api class for querying the database
    api = Api()

    # Connection test
    # Returns an instance of a connection with the MongoDB database
    connection = api.connect(api.customerConnectionString)
    if connection:
        print('TC01: Passed')
    else:
        print('TC01: Failed')

    # Search for a known available item
    testSearch = api.search({'item':'red pepper paste'})
    parsed = api.parse_results(testSearch)
    if 'red pepper paste' in parsed:
        print('TC02: Passed')
    else:
        print('TC02: Failed')
    
    print('\n')

    # Requirement 2.3 Tests - Item Selection and Purchase
    #####################################################

    # Create a shopping cart for a user, add some items to it, remove items from it, erase the user's cart completely
    print("Requirement 2.3 - Item selection and purchase\n----------------------------------\n")
    shop_cart = ShoppingCart({'username': 'cmat'})

    # create a customer's cart
    if shop_cart.createCart():
        print("TC01: Passed")
    else:
        print("TC01: Failed")

    # add an item to the cart
    if shop_cart.addCart({'item':'coke','quantity':1234,'available':True}) and shop_cart.addCart({'item':'Sprite','quantity':12,'available':False}) and shop_cart.addCart({'item':'Dr. Pepper','quantity':1,'available':True}):
        print("TC02: Passed")
    else:
        print("TC02: Failed")

    # change the quantity of an item in the cart
    if shop_cart.changeQuan({'item':'coke','quantity':1234,'available':True}, 1235):
        print("TC03: Passed")
    else:
        print("TC03: Failed")
    
    # remove items from the cart
    if shop_cart.removeCart({'item':'coke'}) and shop_cart.removeCart({'item':'Dr. Pepper'}):
        print("TC04: Passed")
    else:
        print("TC04: Failed")

    # return the items in the shopping cart as a list of dicts
    asdf = shop_cart.readShoppingcart()
    if asdf == []:
        print("TC05: Failed")
    else:
        print("TC05: Passed | Shopping Cart Contents:", asdf)

    # empty user's cart
    if shop_cart.emptyCart() == None:
        print("TC06: Failed")
    else:
        print("TC06: Passed")

    # erase the user
    if shop_cart.eraseUser():
        print("TC07: Passed")
    else:
        print("TC07: Failed")