#!/usr/bin/python3

"""
Keychain app v.1.0 release on 12.01.2020
-------------------------------------------------
About
This is console app that remembers login profiles.
Most of them are from web application.
--------------------------------------------------
Main propose
Never forget profile info.
Full crd manage on profiles.
-------------------------------------------------
"""

import sys
import os

# GLOBALS
FILE_NAME = 'data.txt'
FILE_READ = 'r'
FILE_WRITE = 'w+'
FILE_APPEND = 'a+'


def logo():
    print("""
| | _____ _   _  ___| |__   __ _(_)_ __  
| |/ / _ \ | | |/ __| '_ \ / _` | | '_ \ 
|   <  __/ |_| | (__| | | | (_| | | | | |
|_|\_\___|\__, |\___|_| |_|\__,_|_|_| |_|
          |___/                          by nanorocks""")


def menu_input():
    print("""
    1. View all profiles
    2. Add new profile
    3. Delete profile
    4. Abort
    """)
    try:
        value = int(input("Enter number: "))
    except ValueError:
        print('Invalid input. Abort')
        sys.exit()
    return value


def data_file(call_menu=1, return_type=0):
    try:
        with open(FILE_NAME, FILE_READ) as f:
            if os.stat(FILE_NAME).st_size == 0:
                print('Storage is empty!')
                f.close()
                if return_type:
                    print('Abort')
                    sys.exit()
                if call_menu:
                    menu()
            else:
                print("\n", f.read())
                f.close()
                if return_type:
                    return 1
                if call_menu:
                    menu()
    except IOError:
        with open(FILE_NAME, FILE_WRITE) as create_file:
            print('New storage is created!')
            data_file()
            create_file.close()
    f.close()


def view_profiles():
    data_file()


def add_new_profile():
    try:
        profile_name = input("Enter profile name ex. (FB, SLACK, EMAIL): ")
        username = input("Enter username: ")
        password = input("Enter password: ")

    except ValueError:
        print("Invalid input")
        sys.exit()
    try:
        with open(FILE_NAME, FILE_APPEND) as f:
            f.write(profile_name + " " + username + " " + password + "\n")
            print('Profile stored!')
            f.close()
            menu()
    except IOError:
        print('There was an error. Storage not created.')
    f.close()


def delete_profile():
    data_file(0, 1)
    profile_flag = input('Enter profile name to delete: ')
    storage = []
    with open(FILE_NAME, FILE_READ) as f:
        for line in enumerate(f):
            line_set = str(tuple(line)[1]).split(' ')
            first_arg = line_set[0]
            if str(first_arg) == str(profile_flag):
                continue
            storage.append(' '.join(line_set))
    f.close()

    with open(FILE_NAME, FILE_WRITE) as f:
        f.writelines(storage)
    f.close()
    data_file()


def abort():
    print('Abort.')


def menu():
    number = menu_input()
    if number == 1:
        view_profiles()
    elif number == 2:
        add_new_profile()
    elif number == 3:
        delete_profile()
    elif number == 4:
        abort()
    else:
        print('Invalid input. Abort')


if __name__ == '__main__':
    logo()
    menu()
