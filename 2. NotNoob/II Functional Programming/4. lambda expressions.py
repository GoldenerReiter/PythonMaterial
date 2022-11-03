# lambda expressions

my_list = [1, 2, 3]

print(list(map(lambda item: item*2, my_list)))

generic_dictionary = {
    "rut": 1234567,
    "address": "las hortencias 2719"
}
generic_dictionary2 = {
    "rut": 9876543,
    "address": "assland 2719"
}
list_dictionary = [generic_dictionary, generic_dictionary2]

input_instance1 = int(input('Insert the your rut number\n'))

print(list(filter(lambda i: i['rut'] == input_instance1, list_dictionary)))
