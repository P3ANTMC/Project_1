"""
text_analyzer.py: First Engeto Online Academy project

author: Petr Hrankay
email: pean.tmc@seznam.cz    (main email)
       pean.tmc@gmail.com
discord: PETR H.
"""


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }

# initial variables
number_of_texts = (len(TEXTS))
line = "-" * 40

# user inputs
username = input("username: ".capitalize())
password = input("password: ")
print(line)

# members verification
if users.get(username) == (password):
    print(f"Welcome to the app, {username.capitalize()}\n"
          f"We have {number_of_texts} texts to be analyzed.", line, sep="\n"
    )
else:
    print(f"Unregistered user, terminating the program..")
    quit()
      
# user selects the desired text
user_choice = input(f"Enter a number btw. 1 and {number_of_texts} to select: ")
print(line)

if not user_choice.isnumeric():
    print(f"Your input '{user_choice}' isn't a numeric value,\n"
          f"terminating the program.."""
    )
    quit()
elif int(user_choice) not in range(1, (number_of_texts + 1)):
    print(
        f"Text number {int(user_choice)} wasn't found,"
        f"terminating the program.."
    )
    quit()

selected_text = TEXTS[int(user_choice) - 1].split()
cleaned_text = []

for word in selected_text:
    clean_word = word.strip(",./;'<>?:!@#$%&*")
    cleaned_text.append(clean_word)




# the word counts variables
titlecases_words = 0
uppercases_words = 0
lowercase_words = 0
numeric_strings = 0
sum_numbers = []


for word in cleaned_text:
    if word.istitle():
        titlecases_words += 1
    elif word.isupper():
        uppercases_words += 1
    elif word.islower():
        lowercase_words += 1
    elif word.isnumeric():
        numeric_strings += 1
        sum_numbers.append(int(word))

# print results

    
print(
    f"There are {len(cleaned_text)} words in the selected text.",
    f"There are {titlecases_words} titlecase words.", 
    f"There are {uppercases_words} uppercase words.",       
    f"There are {lowercase_words} lowercase words.",
    f"There are {numeric_strings} numeric strings.",
    f"The sum of all the numbers is {sum(sum_numbers)}",
    line, sep="\n"
) 

# taking word lengths
word_lengths = {}

for word in cleaned_text:
    length = len(word)
    
    if length in word_lengths:
        word_lengths[length] += 1

    else:
        word_lengths[length] = 1

# bar graph
print(f"LEN|{'OCCURENCES'.center(17)}{'|NR.'.rjust(5)}")
print(line)

for length, quantity in sorted(word_lengths.items()):
    
    length_str = str(length)
    quantity_str = str(quantity)
    occurence = "*" * quantity
    print(f"{length_str.rjust(3)}|{occurence.ljust(18)}|{quantity}")
    


