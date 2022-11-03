# A boolean is a type of variable that contains the value of True or False.

quote = (input('insert your favourite quote')).lower()
if (quote.find('life')) >= 0:
    quotevalue = True
else:
    quotevalue = False

if quotevalue:
    print('This text is about life 100%')
elif not quotevalue:
    print('This text is about something else probably')
