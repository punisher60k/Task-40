from tabulate import tabulate

#========The beginning of the class==========
class Shoes:

    def __init__(self, country, code, product, cost:int, quantity:int):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        #returns the cost of shoes
        return self.cost

    def get_quantity(self):
        #returns the quanity of shoes
        return self.quantity

    def __str__(self):
        return f"{self.product} shoe from {self.country}(code {self.code}). It costs £{self.cost} and there are {self.quantity} in stock."


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        with open("inventory.txt", "r") as file:

            for index, entry in enumerate(file):
                #to skip first line which contains header data
                if index == 0:
                    continue
                else:
                    #initially treat data to remove whitespace and split into a list under "temp"
                    temp = entry.strip()
                    temp = temp.split(",")

                    #create a Shoe object and append to "Shoe_list"
                    shoe_list.append(Shoes(temp[0],temp[1],temp[2],int(temp[3]),int(temp[4])))
            print("Import success")

    except FileNotFoundError:
        return "File not found"

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    #request user input
    input_country = input("Country of origin: ")
    input_code = input("Product code: ")
    input_product = input("Product name: ")
    input_cost = int(input("Product cost: "))
    input_quantity = int(input("Product quantity: "))

    #create a Shoe object and append to "Shoe_list"
    shoe_list.append(Shoes(input_country,input_code,input_product,input_cost,input_quantity))


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    #will be a list of lists
    main_list = []

    for i in shoe_list:
        #extract attributes from each Shoe object in shoe_list and add as a list to main_list
        temp_list = []
        temp_list.append(i.country)
        temp_list.append(i.code)
        temp_list.append(i.product)
        temp_list.append(i.cost)
        temp_list.append(i.quantity)
        main_list.append(temp_list)

    #use tabulate library to output main_list
    print(tabulate(main_list, headers=["Country","Code", "Product","Cost (£)","Quantity"], tablefmt='grid'))

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    
    index_tracker = 0 #position in shoe_list with smallest quantity
    for i in range(1, len(shoe_list)): #start at position 1 as no need to comparison first value against itself
        #compares each item in shoe_list in terms of quantity, if smaller then position in list is stored in index_tracker
        if shoe_list[i].get_quantity() < shoe_list[index_tracker].get_quantity():
            index_tracker = i

    lowest_quantity_product = shoe_list[index_tracker].product
    lowest_quantity_num = shoe_list[index_tracker].get_quantity()

    #output to user which product has smallest quantity
    user_input = input((f"{lowest_quantity_product} shoes have the smallest stock count of {lowest_quantity_num}, do you want to restock? (Y/N) "))

    test = True
    while test:
        #give user a choice over whether they wish to increase quantity of lowest quantity shoe or not
        if user_input.lower() == "y":
            user_restock_value = int(input(f"How many {lowest_quantity_product} will you add? "))
            shoe_list[index_tracker].quantity += user_restock_value
            new_quantity = shoe_list[index_tracker].get_quantity()
            print(f"You now have {new_quantity} {lowest_quantity_product} in stock.")
            
            #allows exit of while loop
            test = False

        elif user_input.lower() == "n":
            print(f"{lowest_quantity_product} shoes will not be restocked.")

            #allows exit of while loop
            test = False

        else:
            #as "test" is still True, while loop will continually ask for correct input
            user_input = input("Invalid input. Please confirm \"y\" or \"n\". " )


def search_shoe(shoe_code):
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

    output = None #placeholder for Shoe object which matches "shoe_code"

    #loops through entire shoe_list for matching "code"
    for i in shoe_list:
        if i.code == shoe_code:
            output = i #assumes no duplicate Shoe "code"

    #to capture instances where user input doesn't match anything
    if output == None:
        print("No shoe was found with that value.")
    else:
        print(output)

        
def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    total_stock_value = 0

    for i in shoe_list:
        total_stock_value+= (i.get_cost() * i.get_quantity())

    print(f"The total value of stock is £{total_stock_value:,}.") #use of "," to add thousands separator to "total_stock_value"


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

    highest_tracker = 0 #position in shoe_list with smallest quantity
    for i in range(1, len(shoe_list)): #start at position 1 as no need to comparison first value against itself

        if shoe_list[i].get_quantity() > shoe_list[highest_tracker].get_quantity():
            highest_tracker = i

    highest_quantity_product = shoe_list[highest_tracker].product
    highest_quantity_num = shoe_list[highest_tracker].get_quantity()
    print(f"{highest_quantity_product} shoes have the highest stock count of {highest_quantity_num} and should be put on sale.")
    

#==========Main Menu=============

#Program will continually ask the user to provide one of 3 valid options
while True:
    try:
        choice = int(input('''Please choose one of the following options:
1 - Import inventory data
2 - Create a new Shoe product
3 - View all shoes in stock
4 - Find lowest stock item
5 - Find highest stock item
6 - Search based on product code
7 - Calculate current stock value
8 - Quit program
> '''))

        if choice == 1:
            read_shoes_data()
            print("\n")
        elif choice == 2:
            capture_shoes()
            print("\n")
        elif choice == 3:
            view_all()
            print("\n")
        elif choice == 4:
            re_stock()
            print("\n")           
        elif choice == 5:
            highest_qty()
            print("\n")
        elif choice == 6:
            user_search = input("What is the product code of the shoe? ")
            search_shoe(user_search)
            print("\n")
        elif choice == 7:
            value_per_item()
            print("\n")
        elif choice == 8:
            break
        #if user writes a number that isn't 1,2 or 3 then provides below output
        else:
            print("Invalid option try again.\n")

    #to catch text versions of numbers
    except ValueError:
        print("Please enter a digit version of your choice.\n")