#!/usr/bin/python3
import sys

# Gestion d'Erreur
def error_arguments(arguments):
    if len(arguments) != 2:
        print("error")
        sys.exit()

    contain_at_least_one_letter = False
    for char in arguments[1]:
        if char.isalpha():
            contain_at_least_one_letter = True
    
    if(not contain_at_least_one_letter):
        print("error")
        sys.exit()

# Résolution
def capitalize_words(input_str):
    words = input_str.split()
    return ' '.join(word.capitalize() for word in words)

# Affichage / Main
def main():
    error_arguments(sys.argv)
    
    print(capitalize_words(sys.argv[1]))

main()
