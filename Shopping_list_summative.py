#-------------------------------------------------------------------------------
# Name:        Shoppping List
# Purpose:
#
# Author:      kenny.coons
#
# Created:     11/10/2019
# Copyright:   (c) kenny.coons 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Imports
import time


#-----------Lists------------


dessert_list = ["Ice Cream", "Pie", "cheese cake" ]

#-----------------Shopping List/Dictionary-----------
breakfast = {}
dinner = {}
supper = {}

# breakfast Functions----------
def add_items_b():
    stop = False
    while stop == False:
        items = input("what do you want to add to your breakfast list").lower()
        if items == "stop":
            stop = True
        elif items != "stop":
            value = input("how much of that would you like to add")
            print ("adding", value, items)
            breakfast[items] = value

def remove_items_b():
    stop = False
    while stop == False:
        items = input("what would you like to remove from your list").lower()
    if items == "stop":
        stop = True
    elif items != "stop":
        if items in breakfast:
            print ("removing", items)
            del breakfast[items]


def view_items_b():
    stop = False
    for(items, value) in breakfast.items():
        print ("You have", value, items, "in your list")


def main_b():
    play = 1
    print("Time to go shopping")
    while play == 1:
        time.sleep(1)
        choice = input("Would you like to add or remove items, view the list or stop?").lower()
        if choice == "add":
            add_items_b()
        elif choice == "remove":
            remove_items_b()
        elif choice == "view":
            view_items_b()
        elif choice == "stop":
            stop_stuff()
            play = 0
            print("dinner time")
        else:
            print("i am sorry, i didn't understand that")

#Dinner Functions
def add_items_d():
    stop = False
    while stop == False:
        items = input("what do you want to add to your dinner list").lower()
        if items == "stop":
            stop = True
        elif items != "stop":
            value = input("how much of that would you like to add")
            print ("adding", value, items)
            dinner[items] = value

def remove_items_d():
    stop = False
    while stop == False:
        items = input("what would you like to remove from your list").lower()
    if items == "stop":
        stop = True
    elif items != "stop":
        if items in dinner:
            print ("removing", items)
            del dinner[items]


def view_items_d(): #dinner function
    stop = False
    for(items, value) in dinner.items():
        print ("You have", value, items, "in your list")


def main_d(): #main dinner function
    play = 1
    print("Time to go shopping")
    while play == 1:
        time.sleep(1)
        choice = input("Would you like to add or remove items, view the list or stop?").lower()
        if choice == "add":
            add_items_d()
        elif choice == "remove":
            remove_items_d()
        elif choice == "view":
            view_items_d()
        elif choice == "stop":
            stop_stuff()
            play = 0
            print("Onto supper")
        else:
            print("i am sorry, i didn't understand that")


#Supper Functions
def add_items_s(): #adds supper items
    stop = False
    while stop == False:
        items = input("what do you want to add to your supper list").lower()
        if items == "stop":
            stop = True
        elif items != "stop":
            value = input("how much of that would you like to add")
            print ("adding", value, items)
            supper[items] = value

def remove_items_s(): #removes supper items
    stop = False
    while stop == False:
        items = input("what would you like to remove from your supper list").lower()
    if items == "stop":
        stop = True
    elif items != "stop":
        if items in supper:
            print ("removing", items)
            del supper[items]


def view_items_s(): #supper function
    stop = False
    for(items, value) in supper.items():
        print ("You have", value, items, "in your list")


def main_s():  #main supper function
    play = 1
    print("Time to go shopping")
    while play == 1:
        time.sleep(1)
        choice = input("Would you like to add or remove items, view the list or stop?").lower()
        if choice == "add":
            add_items_s()
        elif choice == "remove":
            remove_items_s()
        elif choice == "view":
            view_items_s()
        elif choice == "stop":
            stop_stuff()
            play = 0
            print("onto dessert")
        else:
            print("i am sorry, i didn't understand that")


#Dessert Functions
def choose_dessert():  #Allows the user to add or remove from the shopping list they have for desserts, an then view the length of the lis
    dessert_list = input("You have already added ice cream, pie and cheesecake, would you like to add or delete an item").lower
    if dessert_list == "add":
        added_dessert = input("what you like to add").lower
        append.added_dessert
    elif dessert_list == "delete":
        removed_dessert = input("what desert would you like to remove?").lower
        if removed_dessert == "cheesecake":
            dessert_list.remove("cheesecake")
        elif removed_dessert == "ice cream":
            dessert_list.remove("ice cream")
        elif removed_dessert == "pie":
            dessert_list.remove("pie")
    print(dessert_list)






def stop_stuff():
    stop = True

def eating_time():
    print ("you have eaten", breakfast, "for breakfast")
    print ("you have eaten", dinner, "for dinner")
    print ("you have eaten", supper, "for supper")
    dessert_time = input("What would you like to have for dessert you can choose anything from", dessert_list)





#Main Code#
main_b()#calls function
main_d()#calls function
main_s()#calls function
choose_dessert()#calls function
eating_time()

