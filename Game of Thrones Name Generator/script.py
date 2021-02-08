import random
import pandas as pd

print('Welcome to the Game of Thrones Name Generator.\n')


names = pd.read_csv('got_names.csv')

gender = input('Male (m) or Female (f)?')

while True:
    if gender.lower() == 'm' or gender.lower() == 'f':
        break
    else:
        print('Sorry. Please enter your gender as either "m" or "f".')
        gender = input('Male (m) or Female (f)?')
print('\n')

male_first = []
female_first = []
house_list = []
for name in names['Male Names']:
    male_first.append(name)
for name in names['Female Names']:
    female_first.append(name)
for house in names['House']:
    house_list.append(house)

while True:
    if gender == 'm':
        first = random.choice(male_first)
    elif gender == 'f':
        first = random.choice(female_first)
    house = random.choice(house_list)
    print('Your given name in Westeros will be: {} of the House {}\n'.format(first,house))
    try_again = input("\n\nTry again? (Press Enter else 'n' to quit.)\n")
    if try_again.lower() == 'n':
        break

input('Press Enter to Exit.')