import os, csv, io
from os import path
import os
import pandas as pd
from Tools.scripts.dutree import display

list1 = []                                                                  # list of all projects

class Preview:
    def __init__(self, lst1=[]):
        self.lst1 = lst1

    def set_view(self, lst1):
        self.lst1 = lst1

    def view2(self):
        print(self.lst1[0], "\t       ", self.lst1[1], "\t\t\t   ", self.lst1[2], "\t\t\t\t  ", self.lst1[3])


class OtherFunctions:
    def iteration(self, filename):
        data = pd.read_csv(filename)

        df = pd.DataFrame(data)
        left_aligned_df = df.style.set_properties(**{'text-align': 'left'})
        display(self, left_aligned_df)


    def is_empty(self, x):
        with open(x, 'r') as csvfile:                                       # check queue if empty or not
            csv_dict = [row for row in csv.DictReader(csvfile)]
            if len(csv_dict) == 0:
                self.o = False
                return self.o
            else:
                self.o = True
                return self.o

    def try_again(self, ques, msg, loc):
        while True:
            try:
                choice = int(input('\n{} YES(1) or NO(0): '.format(ques)))
                if choice == 1:
                    if loc == 1:
                        input_module_details()
                    elif loc == 2:
                        view_module()
                    elif loc == 3:
                        schedule_module()
                    elif loc == 4:
                        get_a_module()
                elif choice == 0:
                    self.restart()
                else:
                    raise ValueError
            except ValueError:
                print(msg)

    def restart(self):
        while True:
            try:
                choice = int(input('\nGo back to main menu? YES(1) or NO(0): '))
                if choice == 1:
                    main()
                elif choice == 0:
                    quit()
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input.")

    def input_validation(self, x, y):
        if y == 1:
            while True:
                try:
                    i = int(input(x))
                    if (type(i) is not int) or (i < 0): raise ValueError
                except ValueError:
                    print('Invalid input.', '\n')
                else:
                    return i
        elif y == 2:
            while True:
                try:
                    i = input(x)
                    if i == " " : raise ValueError
                    else:
                        return i
                except ValueError:
                    print('Invalid input.', '\n')
                else:
                    return i


def clear():
    os.system('cls')

# Techknow's Notion Main Menu
def main():
    clear()
    print("\tTECHKNOW'S NOTION\n")
    print('1. Input Module Details\n2. View Modules\n3. Schedule Modules\n4. Get a Module\n5. Exit\n')
    while True:
        try:
            choice = int(input("Please enter a number: "))
            if choice not in range(1, 6): raise ValueError
        except ValueError:
            print('Invalid input.', '\n')
        else:
            break
    if (choice == 1):
        input_module_details()
    elif (choice == 2):
        view_module()
    elif (choice == 3):
        schedule_module()
    elif (choice == 4):
        get_a_module()
    elif (choice == 5):
        quit()


# Menu 1 - input module details
def input_module_details():
    """ Goes to menu 1 """
    marker = 0  # marker
    clear()
    print('\tINPUT MODULE DETAILS\n')
    while True:
        p = OtherFunctions()
        module_name = p.input_validation('Modules: ',2)
        type = p.input_validation('Type: ',2)
        tasks = p.input_validation('No. of Tasks: ',1)
        priority = p.input_validation('Priority: ',1)
        with open("all_modules.csv", "r") as f:
            csvreader = csv.reader(f, delimiter=",")
            for row in csvreader:
                list1.append(row[0])                                        # insert all_project data column to list
            for i in list1:                                                 # iterate data
                if i == module_name:                                        # check if module is in data
                    marker = 1
                else:
                    pass
            if marker == 1:                                                 # if module name exist
                print("\nModules Exist")
                p.try_again('Make new module details?', 'Invalid input.', 1)
            else:                                                           # data is not located : add new data to file
                with open("all_modules.csv", 'a', newline='\n') as f1, open("queue.csv", 'a', newline='\n') as f2:
                    f1writer = csv.writer(f1)
                    f1writer.writerow([module_name, type, tasks, priority])
                    f2writer = csv.writer(f2)
                    f2writer.writerow([module_name, type, tasks, priority])
                print("---Module Details Saved---")
                p.try_again('Make new module details?', 'Invalid input.', 1)


# Menu 2 - view
def view_module():
    """ Goes to menu 2 """
    clear()
    print('\tVIEW MODULES\n')
    print('1. Completed Modules\n2. All Modules\n3. Go Back\n')
    while True:
        try:
            choice = int(input("Please enter a number: "))
            if choice not in range(1, 4): raise ValueError
        except ValueError:
            print('Invalid input.', '\n')
        else:
            break
    if choice == 1:                                                         # all completed modules
        clear()
        print('\t     VIEW MODULES')
        print('    LIST OF ALL COMPLETED MODULES\n')
        p = OtherFunctions()
        if p.is_empty('completed_modules.csv') == True:
            p.iteration('completed_modules.csv')                            # display the data
            p.try_again('View module again?', 'Invalid input.', 2)
        else:
            print("\tNo completed module yet")
            p.try_again('View module again?', 'Invalid input.', 2)
    elif choice == 2:                                                       # all module
        clear()
        print('\t     VIEW MODULES')
        print('\t     ALL MODULES\n')
        p = OtherFunctions()
        if p.is_empty('all_modules.csv') == True:
            p.iteration('all_modules.csv')
            p.try_again('View module again?', 'Invalid input.', 2)
        else:
            print("\tNo module yet")
            p.try_again('View module again?', 'Invalid input.', 2)
    elif choice == 3:
        main()


# menu 3 - schedule_project
def schedule_module():
    """ Goes to menu 3 """
    clear()
    print('\tSCHEDULE MODULES\n')
    print('1. View Updated Schedule\n2. Go Back\n')
    while True:
        try:
            choice = int(input("Please enter a number: "))
            if choice not in range(1, 3): raise ValueError
        except ValueError:
            print('Invalid input.', '\n')
        else:
            break
    p = OtherFunctions()
    if choice == 1:
        clear()
        print('\t     VIEW MODULES')
        print('    VIEW SCHEDULE UPDATED SCHEDULE\n')
        if p.is_empty('queue.csv') == True:
            queue_projects = open('queue.csv', 'r')
            data = csv.DictReader(queue_projects)                           # read the file and separated the value
            mylist = []                                                     # as dictionary key
            for row in data:
                single_list = []
                single_list.append(row['Modules'])                          # appends the column under the header
                single_list.append(row['Type'])
                single_list.append(int(row['No. of Tasks']))                # typecast the value into integer
                single_list.append(int(row['Priority']))
                mylist.append(single_list)                                  # store the data into the list

            sorted_queue1 = (sorted(mylist, key=lambda v: (v[2], v[2])))         # sort the data by the sizes
            sorted_queue2 = (sorted(sorted_queue1, key=lambda v: (v[3], v[2])))  # sort the data by the priority

            with open('queue.csv', 'w', newline='') as queue_new:                # displaying the header
                queue_writer = csv.DictWriter(queue_new, delimiter=',', fieldnames=['Modules', 'Type', 'No. of Tasks',
                                                                                    'Priority'])
                queue_writer.writeheader()
                queue_writer = csv.writer(queue_new)
                queue_writer.writerows(sorted_queue2)                       # writes the sorted items in the csv
            queue_new.close()

            file3 = open('queue.csv', 'r')
            lines = file3.readlines()
            file3.close()
            p.iteration('queue.csv')

            p.try_again('Go back to schedule module?', 'Invalid input.', 3)
        else:
            print("\t Queue is empty")
            p.restart()
    elif choice == 2:
        main()


# menu 4 - get a project
def get_a_module():
    """ Goes to menu 4 """
    p = OtherFunctions()
    clear()
    a = False
    print('\t      GET A MODULE\n')
    if p.is_empty('queue.csv') == True:
        a = True
        p.iteration('queue.csv')                                            # display the data
        while True:
            try:
                choice = int(input('\nMark as complete the topmost module? YES(1) or NO(0): '))
                if choice not in range(0, 2): raise ValueError
            except ValueError:
                print('Invalid input.', '\n')
            else:
                break
        if choice == 1:
            if a == True:
                list5 = []
                lines = []
                with open('queue.csv', newline='') as f:
                    reader = csv.reader(f)
                    row1 = next(reader)                                     # header
                    row2 = next(f)                                          # get the first row
                list5 = row2.split(",")                                     # put the first row in list
                list6 = [i.strip() for i in list5]                          # removing \n \t
                with open('queue.csv', 'r') as readFile:
                    reader = csv.reader(readFile)
                    for row in reader:
                        lines.append(row)                                   # add data row in list - lines
                        for field in row:                                   # iterate the row
                            if field == list6[0]:                           # check if module of first row(list6) if same
                                lines.pop()                                 # remove line
                                break
                with open('queue.csv', 'w', newline='') as writeFile:
                    writer = csv.writer(writeFile)
                    writer.writerows(lines)                                 # rewrite csv file with the list - lines
                file2 = open("completed_modules.csv", 'a', newline='')
                awriter = csv.writer(file2)
                awriter.writerow(list6)                                     # add first row(list5) to completed projects
                file2.close()
                print("---Module complete---")
                file1 = open('queue.csv', 'r')
                lines = file1.readlines()
                file1.close()
                print()
                p.iteration('queue.csv')                                    # display updated queue"""
            else:
                print("Queue is empty")
        elif choice == 0:
            p.restart()
        p.try_again('Get a module again?', 'Invalid input.', 4)
    else:
        print("\t\tQueue is empty")
        p.restart()



def make_csv_files():
    if path.isfile('all_modules.csv'):
        pass
    else:
        with open('all_modules.csv', 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['Modules', 'Type', 'No. of Tasks', 'Priority'])

    if path.isfile('completed_modules.csv'):
        pass
    else:
        with open('completed_modules.csv', 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['Modules', 'Type', 'No. of Tasks', 'Priority'])

    if path.isfile('queue.csv'):
        pass
    else:
        with open('queue.csv', 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['Modules', 'Type', 'No. of Tasks', 'Priority'])


# ----------------- start --------------------
make_csv_files()
main()