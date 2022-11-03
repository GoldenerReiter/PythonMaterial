def input_check(iterable):
    return input_instance == iterable


generic_list = [1, 2, 3, 4, 5]
input_instance = int(input())

print(list(filter(input_check, generic_list)))

generic_dictionary = {
    "rut": 1234567,
    "address": "las hortencias 2719"
}
generic_dictionary2 = {
    "rut": 9876543,
    "address": "Johnland 2719"
}
list_dictionary = [generic_dictionary, generic_dictionary2]

input_instance1 = int(input())

print(list(filter(lambda i: i['rut'] == input_instance1, list_dictionary)))

