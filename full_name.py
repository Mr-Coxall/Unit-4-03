# Created by: Mr. Coxall
# Created on: Aug 2016
# Created for: ICS3U
# This program shows optional and named parameters

def print_name(first, initial = '', last = ''):
    # print name
    if initial == '':
        print(first + ' ' + last)
    else:
        print(first + ' ' + initial + ' ' + last)

first_name = raw_input("Enter your first name: ")
last_name = raw_input("Enter your last name: ")
initial_choice = raw_input("Do you want to enter your initials?(y/n): ")
if initial_choice == 'y':
    initial_name = raw_input("Enter your initials: ")
    print_name(first_name, initial = initial_name, last = last_name)
else:
    print_name(first_name, last = last_name)
