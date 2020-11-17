import os
import datetime

def print_menu():
    print("-" * 52)
    print("  Welcome to Warehouse PyControl [" + get_date_time() +"]")
    print("-" * 52)

    print('[1] - Add Product to Catalog')
    print('[2] - Display catalog')
    print('[3] - Display products out of stock')
    print('[4] - Total Stock Value')
    print('[5] - Cheapest Product')
    print('[6] - Delete Product')
    print('[7] - Update Product Price')
    print('[8] - Update Product stock')
    print('[10] - 3 most expensive products')
    print('[11] - Disctinct categories')

    print('[s] - Save changes')
    print('[x] - Exit')

def get_date_time():
    now = datetime.datetime.now()
    return now.strftime("%d/%b/%Y %H:%M")

def print_header(text):
    clear()
    print('-' * 76)
    print(text)
    print('-' * 76)

def print_product_info(prod):
    print(
            str(prod.id).rjust(3) + " | " + 
            prod.title.ljust(25) + " | " + 
            prod.category.ljust(12) + " | " + 
            str (prod.stock).rjust(7) + " | $ " + 
            str (prod.price).rjust(12) + " |"
            )


def clear():
    if(os.name == 'nt'):
        return os.system('cls')
    else:
        return os.system('clear')
    
    #return os.system('cls' if os.name == 'nt' else 'clear')