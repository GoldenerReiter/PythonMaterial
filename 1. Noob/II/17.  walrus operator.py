# walrus operator (:=)
# the walrus operator, a feature of python 3.8, allows us to declare a variable as a part of an if statement

stringVar = 'hellooooooooooooo'

if (n := len(stringVar)) > 10:  # as you can see, the variable n was declared as the length of stringVar in the if
    print(f"Your variable is too long for printing ({n} characters). Please make it shorter.")
