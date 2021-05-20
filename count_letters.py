# Author: Samuel Bennett
# Date: 5/19/2021
# Description: Function counts the how many letters of a specific kind are in a string
def count_letters(str):
    letters_dict = {}
    for letter in str:
        letters_numbered = ord(letter)
        if 97 <= letters_numbered <= 122:
            upper_case_letter = chr(letters_numbered - 32)
            letters_dict[upper_case_letter] = letters_dict.get(upper_case_letter, 0) + 1
        elif 65 <= letters_numbered <= 90:
            letters_dict[letter] = letters_dict.get(letter, 0) + 1
    return letters_dict

def main():
    print(count_letters("AaBb"))
    print(count_letters("Abazaba Bar"))

main()