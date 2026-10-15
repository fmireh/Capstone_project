
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return (
            f"Country: {self.country}, "
            f"Code: {self.code}, "
            f"Product: {self.product}, "
            f"Cost: {self.cost}, "
            f"Quantity: {self.quantity}"
        )


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
            lines = file.readlines()

        for line in lines[1:]:
            data = line.strip().split(",")

            country = data[0]
            code = data[1]
            product = data[2]
            cost = float(data[3])
            quantity = int(data[4])

            shoe = Shoe(
                        country,
                        code,
                        product,
                        cost,
                        quantity
                    )
            shoe_list.append(shoe)

        print("Inventory data successfully loaded.")

    except FileNotFoundError:
        print("Error: inventory.txt could not be found.")


    
def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    country = input("What is the country? ")
    code = input("What is the code? ")
    product = input("What is the product name? ")
    cost = float(input("What is the cost of product? "))
    quantity = int(input("What is quantity? "))

    shoe_object = Shoe(
            country,
            code,
            product,
            cost,
            quantity
        )

    shoe_list.append(shoe_object)

    print("Shoe successfully added.")
    
    

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    if not shoe_list:
        print("There are no shoes in the inventory.")
        return
    
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    if not shoe_list:
        print("There are no shoes in the inventory.")
        return
    
    lowest_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)
    
    print("\nShoe with the lowest quantity:")
    print(lowest_shoe)

    low_quantity = input("Do you want to restock? (yes/no): ").lower()

    if  low_quantity == "yes":

        amount = int(input("How many shoes would you like to add? (integers only): "))
        
        lowest_shoe.quantity += amount

        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")

            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},"
                    f"{shoe.cost},{shoe.quantity}\n"
                )
        print("Shoe successfully restocked.")
    else:
        print("No restocking shoes.")

def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    shoe_code = input("What is the shoe code ")

    for shoe in shoe_list:
        if shoe.code == shoe_code:
            print(shoe)
            return shoe
    print("Shoe not found.")

    return None    

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
    print(
            f"{shoe.product}: "
            f"Cost = {shoe.cost}, "
            f"Quantity = {shoe.quantity}, "
            f"Total value = {value}"
        )

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

    highest_shoe = max(
        shoe_list,
        key=lambda shoe: shoe.quantity
    )
    print(highest_shoe)
    print("This shoe is for sale! ")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:

    print("1. Read File")
    print("2. Add Shoe")
    print("3. View Shoes")
    print("4. Restock")
    print("5. Search")
    print("6. Value Per Item")
    print("7. Highest Quantity")
    print("8. Exit")

    choice = input("Please select an option: ")

    for i in choice:

        if choice == "1":
            read_shoes_data()

        elif choice == "2":
            capture_shoes()

        elif choice == "3":
            view_all()

        elif choice == "4":
            re_stock()

        elif choice == "5":
            search_shoe()

        elif choice == "6":
            value_per_item()

        elif choice == "7":
            highest_qty()

        elif choice == "8":
            print("Goodbye!")
        break
    else:
        print("Print invalid choice ")