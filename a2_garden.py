"""
CP5639 2020-1 Assignment 2
Market Garden Simulator
Student Name: Jishnu Maharshi Yalamarthi
Date Started: 25/05/20

Pseudocode:

Pseudocode for main function

function main_market_garden_simulator()
    garden_plants = ["plants"]
    day_count = 0
    total_produce = 0
    print main menu
    print daily_update(day_count, total_produce, garden_plants)
    get input_choice
    while input_choice != "Q"
        if input_choice == "W"
            increase day count by 1
            total_produce = simulate_one_day(total_produce, garden_plants)
        else if input_choice == "D"
            display_plants(garden_plants)
        else if input_choice == "A"
            total_produce = plant_addition(total_produce, garden_plants)
        else
            print invalid choice
        print daily_update(day_count, total_produce, garden_plants)
        get input_choice
    print daily_update (day_count, total_produce, garden_plants)
    display_final_details

Pseudocode for simulate_one_day

function simulate_one_day(produce, garden_plants)
    rainfall =  random integer between minimum_rainfall and maximum_rainfall
    print ( rainfall )
    if rainfall < ideal_amount_of_rain
        dead_plant = random_plant(garden_plants)
        delete dead_plant from garden_plants
        print 'Sadly your dead_plant has died.'
    rain_percent = rainfall/100
    rain_half_percent = (rainfall/2)/100
    for every plant in garden_plants
        produce = random_rain_percent * len(plant)
        print 'This plant's produce'
        add produce to total_produce
    return produce

Pseudocode for adding a new plant

function add_new_plant(produce_at_hand, garden_plants)
    if produce_at_hand > ideal_produce_for_purchase
        new_plant = get_valid_plant_name()
        while plant_name exists in plants_list
            print 'plant already exists'
            new_plant = get_valid_plant_name()
        new_plant_name_length = length(new_plant)
        produce_at_hand = produce_at_hand - new_plant_name_length
        append the new_plant to garden_plants
        return produce_at_hand
    display error "You can't add plants yet"
    return produce_at_hand

"""

import random

RAINFALL_UPPER_LIMIT = 100
RAINFALL_LOWER_LIMIT = 0
MINIMUM_RAIN_REQUIRED = 30
IDEAL_PRODUCE_FOR_PURCHASE = 10
NEW_PLANT_NAME_LIMIT = 10


def main_market_garden_simulator():
    """Main function for the Market Garden Simulator"""
    day_count = 0
    total_produce = 0
    garden_plants = ["Parsley", "Sage", "Rosemary", "Thyme"]
    # Main Menu options
    your_options = "(W)ait\n(D)isplay Plants\n(A)dd new plant\n(Q)uit"
    print("Welcome to the Market Garden Simulator!\nPlants cost and generate produce according to their name length("
          "e.g. Sage plants cost 4)\nYou can buy new plants with the produce your garden generates\nLet's hope it "
          "rains.. a lot!\nYour start with these plants:")
    display_plants(garden_plants)
    display_daily_update(day_count, total_produce, garden_plants)  # This displays everyday status in the Market Garden
    print(your_options)
    main_menu_choice = input("Choose: ").upper()
    # Main Menu repeats until user wants to (Q)uit
    while main_menu_choice != "Q":
        if main_menu_choice == "W":
            day_count += 1
            # total produce is brought back from function call to display at the daily update
            total_produce = simulate_one_day(total_produce, garden_plants)
        elif main_menu_choice == "D":
            if len(garden_plants) > 1:
                print("You have these plants: ")
                display_plants(garden_plants)
            else:
                print(f"You have this plant: {garden_plants[0]}")
        elif main_menu_choice == "A":
            # The function for adding new plant is called with arguments of 'total produce' we hold and the variable
            # for amount of ideal produce required to purchase new plant
            total_produce = add_new_plant(total_produce, garden_plants)
        else:
            print("Invalid choice")
        display_daily_update(day_count, total_produce, garden_plants)
        print(your_options)
        main_menu_choice = input("Choose: ").upper()
    if len(garden_plants) > 0:
        print("You finished with these plants:")
        display_plants(garden_plants)
    else:
        print("You finished with no plants")
    display_daily_update(day_count, total_produce, garden_plants)
    print("Thank you for simulating. Now go and enjoy a real garden.")


def display_plants(garden_plants):
    """Function to display all plants in Market Garden"""
    for plant in garden_plants:
        print(plant, end=", ")


def display_daily_update(day_count, produce, garden_plants):
    """Function to display daily update status"""
    if day_count > 1:
        if len(garden_plants) > 1:
            print(f"\nAfter {day_count} days, you have {len(garden_plants)} plants and your total produce is {produce}")
        else:
            print(f"\nAfter {day_count} days, you have {len(garden_plants)} plant and your total produce is {produce}")
    else:
        if len(garden_plants) > 1:
            print(f"\nAfter {day_count} day, you have {len(garden_plants)} plants and your total produce is {produce}")
        else:
            print(f"\nAfter {day_count} day, you have {len(garden_plants)} plant and your total produce is {produce}")


def get_valid_plant_name():
    """Function to get a valid new plant name"""
    new_plant = input("Plant name (1-10 Characters): ").title()
    # Plant names that are greater than 10 characters or empty strings are invalid input until correct input is given
    while new_plant == "" or len(new_plant) > NEW_PLANT_NAME_LIMIT:
        print("Invalid plant name length.")
        new_plant = input("Plant name(1-10 Characters): ").title()
    return new_plant


def add_new_plant(produce, garden_plants):
    """Function to add a new plant into Market Garden"""
    # We can only purchase new plant if the produce at hand is greater than ideal amount of produce
    if produce >= IDEAL_PRODUCE_FOR_PURCHASE:
        new_plant = get_valid_plant_name()
        # If the plant already exists in the Market Garden, error is displayed asking for a different plant name
        while new_plant in garden_plants:
            print(f"You already have {new_plant} plant. Get a different one.")
            new_plant = get_valid_plant_name()
        plant_purchase_expense = len(new_plant)
        produce -= plant_purchase_expense
        garden_plants.append(new_plant)
        return produce
    print("You can't afford any new plants yet. Just (W)ait.")
    return produce


def simulate_one_day(produce, garden_plants):
    """Function to simulate one day in the Market Garden"""
    rain_fall = random.randint(RAINFALL_LOWER_LIMIT, RAINFALL_UPPER_LIMIT)  # Generate random rainfall
    print(f"Rainfall: {rain_fall}mm")
    rainfall_percent = rain_fall/100    # Calculate rainfall percentage
    half_rainfall_percent = (rain_fall/2)/100   # Calculate half percentage of rainfall for using in produce generation
    if rain_fall <= MINIMUM_RAIN_REQUIRED:
        dead_plant = random.choice(garden_plants)   # A random plant is chosen from garden_plants list and deleted
        print(f"Sadly, your {dead_plant} plant has died.")
        garden_plants.remove(dead_plant)
    for plant in garden_plants:
        # Produce by each plant is generated using the provided formula
        each_plant_produce = int(random.uniform(half_rainfall_percent, rainfall_percent) * len(plant))
        print(f"{plant} produced {each_plant_produce}", end=", ")
        produce += each_plant_produce
    return produce


main_market_garden_simulator()
