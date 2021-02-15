"""This script will find palindromes in a dictionary file"""
import load_dictionary
word_list = load_dictionary.load('2of4brif.txt')
pali_list = []

def num_palindromes():
    for word in word_list:
        if len(word) > 1 and word == word[::-1]:
            pali_list.append(word) 

    print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
    print(*pali_list, sep='\n')

def is_palindrome(word):
    if len(word) <2:
        return True
    if word[0] != word[-1]: 
        return False
    return is_palindrome(word[1:-1])
            