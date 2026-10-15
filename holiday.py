#This imports random module
'''
2. Your task will be to calculate a user’s total holiday cost, which includes the plane cost, hotel cost, and car rental cost.

3. First, get the following user inputs:
● city_flight: The city they will be flying to (you can create some options for them. Remember, each city will have different fl ight costs).
● num_nights: The number of nights they will be staying at a hotel.
● rental_days: The number of days for which they will be hiring a car.

4. Next, create the following four functions:
● hotel_cost(): This function will take num_nights as an argument and return a total cost for the hotel stay (you can choose the price per night charged at the hotel).
● plane_cost(): This function will take city_flight as an argument and return a cost for the fl ight. Hint: use if/else statements in the function to retrieve a price based on the chosen city.
● car_rental(): This function will take rental_days as an argument and return the total cost of the car rental (you can choose the daily rental cost).
● holiday_cost(): This function takes three arguments: num_nights, city_flight, and rental_days. Using these three arguments, call the hotel_cost(), plane_cost(), and car_rental() functions with their respective arguments, and fi nally return the total cost for the holiday.

5. Print out all the details about the holiday in a way that is easy to read.
Try running your program with different combinations of input to show its compatibility with different options.

'''

 # this uses the random import with a method called choice   

city_flight = input("Which city are you flying to? Madrid, Paris, Berlin: ").capitalize()
num_nights = int(input("Please input how many nights you will be staying at the hotel? E.g 1, 2: "))
rental_days = int(input("Please input the number of days you will be hiring a car? E.g 1, 2:  "))

def hotel_cost(num_nights):
    
    cost_hotel_stay = num_nights * 40

    return cost_hotel_stay

def plane_cost(city_flight):
    
    if city_flight == "Madrid":
        ticket = 99
    elif city_flight == "Paris":
        ticket = 50
    elif city_flight == "Berlin":
        ticket = 70
    else:
        ticket =0

    return ticket

def car_rental(rental_days):
    
     cost_car_days = rental_days * 20
     
     return cost_car_days

def holiday_cost():
     
     total_cost = hotel_cost(num_nights)+ plane_cost(city_flight)+ car_rental(rental_days)
     
     return total_cost


print(f"The total cost of the holiday is £{holiday_cost()}")






