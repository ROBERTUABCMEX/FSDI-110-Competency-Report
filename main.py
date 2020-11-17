"""
Program: Warehouse control
Author: Roberto Valdes
Date: Nov. 2020
Functionally:
    - Register products
        - id (auto generated)
        - title
        - category
        - stock
        - price
        

"""
# imports
from menu import clear, print_menu, print_header, print_product_info
from product import Product
import pickle

# global vars
catalog = []
next_id = 1


# functions

def serialize_data():
    try:
        writer = open('warehouse.data', 'wb') # wb = write binary
        pickle.dump(catalog, writer)
        writer.close()
        print("** Data serialized!!")
    except:
        Print("** Error, data ")

def deserialize_data():
    try:
        global next_id
        reader = open('warehouse.data', 'rb') # rb = read binary
        temp_list = pickle.load(reader)
        reader.close()

        for prod in temp_list:
            catalog.append(prod)
        
        # get the last used id, and increase by 1
        last = catalog[-1]
        next_id = last.id + 1

        how_many = len(catalog)
        print("** Read: " + str(how_many) + " products")

    except:
        print("** Error, no data file found")


def register_product():
    try:
        global next_id
        print_header("Register new Product")
        title = input('Please provide te Title: ')
        cat = input('Please provide the Category: ')
        stock = int(input("Please provide initial Stock: "))
        price = float(input("Please provide the Price: "))


        # validations
        if(len(title) < 1):
            print("Error: Title should not be empty")

        product = Product(next_id, title, cat, stock, price)
        next_id += 1
        catalog.append(product)
    except:
        print("** Error, try again")

def display_catalog():
    print_header("Current Catalog")
    for prod in catalog:
        print_product_info(prod)

def display_no_stock():
    print_header("Products out of stock")
    for prod in catalog:
        if(prod.stock == 0):
            print_product_info(prod)




def total_stock_value():
    print_header("Total Atock value")
    total = 0
    for prod in catalog:
        total += (prod.price * prod.stock)
    
    print("Total stock value: $" + str(total))


def cheapest_product():
    print_header("Print the cheapest product")


    cheapest = catalog[0]
    for prod in catalog:
        if(prod.price < cheapest.price):
            cheapest = prod
    
    print("Cheapest product is:")
    print_product_info(cheapest)


def delete_product():
    display_catalog()
    id = int(input("ID of item to delete: "))

    found = False
    for prod in catalog:
        if(prod.id == id):
            found = True
            catalog.remove(prod)
            print("** Item removed")
    
    if(not found):
        print("** Incorrect id, try again")


def update_product_price():
    print_header("Update product price")
    display_catalog()

    try:
        id = int (input("id of the product to update: "))

        found = False
        for prod in catalog:
            if (prod.id == id):
                found = True
                price = float(input("Please provide the new price: $ "))
                prod.price = price
                print("** Price update")
        

        if(not found):
            print("** Incorrect id, try again")
        
        return found # true if catalog was modified, False otherwise
    except:
        print("** Unexpected error!")
        return False


def most_expensive_items():
    print_header(" 3 most expensive product prices")
    # creat an array of prices (numbers only)
    prices = []
    for prod in catalog:
        prices.append(prod.price)

    # sort the array
    prices.sort(reverse=True)

    # print
    print(prices[0]) # find  a product with the same price, and print_item (that product)
    print(prices[1]) 
    print(prices[2])


        

# instructions

deserialize_data()
input("Press Enter to contunue.....")

opc = ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input('Please select an option: ')

    if(opc == '1'):
        register_product()
        serialize_data()
    elif(opc == '2'):
        display_catalog()
    elif(opc == '3'):
        display_no_stock()
    elif(opc == '4'):
        total_stock_value()
    elif(opc == '5'):
        cheapest_product()
    elif(opc == 's'):
        serialize_data()
    elif(opc == '6'):
        delete_product()
        serialize_data()
    elif(opc == '7'):
        if(update_product_price()):
            serialize_data()
    elif(opc == '10'):
        most_expensive_items()


    input('Press Enter to continue...')

print('Good byte!')