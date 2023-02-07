import random
import time


class Activity:
    def __init__(self, name, value):
        self.actName = name
        self.rngValue = value


def activity_array_creator():
    act_array = []
    array_num = int(input("Insert the number of activities to create \n"))
    i = 0
    while i < array_num:
        act_array.append(Activity(input(f"Insert the name of your activity {i+1} \n"), random.randint(0, 100)))
        i = i + 1
    return act_array


def array_sorter(to_sort_array):
    to_sort_array.sort(key=lambda x: x.rngValue, reverse=True)
    return to_sort_array


def array_representation(sort_array):
    for i in sort_array:
        print("Activity name: " + i.actName)
        print("Activity value: " + str(i.rngValue) + "\n")
    print(sort_array[0].actName + " won! \n")


def array_printer():
    act_array = activity_array_creator()
    sort_array = array_sorter(act_array)
    array_representation(sort_array)
    time.sleep(10)


array_printer()
