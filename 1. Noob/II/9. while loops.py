# while loops
i = 0

while i < 3:
    print('I already told ya so')
    i = i + 1  # This is a classic while loop which closes when i increments to 3

while True:
    response = input("John, tell me 'bye bye', or you will be trapped here FOR EVA' mwahahaha")
    if response == 'bye bye':
        break
