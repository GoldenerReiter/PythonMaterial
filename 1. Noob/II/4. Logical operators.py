# Logical Operators
# >
# <
# ==
# and
# or
# !=
# >=
# not (¬)

# Exercise
is_magician = False
is_expert = False

if is_magician and is_expert:
    print("You're a master magician, mate.")
elif is_magician and not is_expert:
    print("At least you're getting there, mate. Keep going.")
elif not is_magician:
    print("You need magic powers, mate.")

# is
print(True is True)  # True and True use the same space in memory, so it will be True.
print([] is [])  # [] is a data structure, so everytime you declare one, it will use a different space in memory.
print([] == [])  # But it has the same value, so == will say that [] is equal to [] in value, but not in identity.
