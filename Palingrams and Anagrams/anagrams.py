import load_dictionary
import sys

word_list = load_dictionary.load('2of4brif.txt')

anagram_list = []

def anagrams():
    var = input("What word would you like to find anagrams of?")
    print("Input = {}".format(var))
    var = var.lower()
    print("Using = {}".format(var))

    # sort name and find anagrams
    var_sorted = sorted(var)
    for word in word_list:
        word = word.lower()
        if word != var:
            if sorted(word) == var_sorted:
                anagram_list.append(word)

    # print out list of anagrams
    print()
    if len(anagram_list) == 0:
        print("You need a larger dictionary or try a new word.")
    else:
        print("Anagrams =", *anagram_list, sep="\n")
    
    while True:
        answer = input("Would you like to try again? Please enter yes (y) or no (n).")
        answer = answer.lower()
        if answer == 'n':
            input("\nPress Enter to exit")
            sys.exit()
        if answer == 'y':
            return True
        else:
            print("\nPlease enter either Y or N\n")
    
while anagrams():
    pass
