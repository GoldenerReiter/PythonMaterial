import random
import time


class Activity:
    def __init__(self, name, value):
        self.name = name
        self.value = value


def activity_array_creator():
    act_array = []
    array_num = int(input("Insert the number of activities to create \n"))
    i = 0
    while i < array_num:
        act_array.append(Activity(input("Insert the name of your activity \n"), random.randint(0, 100)))
        i = i + 1
    return act_array


def array_printer():
    act_array = activity_array_creator()
    for i in act_array:
        print("Activity name: " + i.name)
        print("Activity value: " + str(i.value) + "\n" + "\n")
    time.sleep(10)


array_printer()
