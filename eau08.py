#!/usr/bin/python3
import sys

# Gestion d'Erreur
def error_arguments(arguments):
    if len(arguments) != 2:
        print("error")
        sys.exit()

# Résolution
def capitalize_words(input_str):
    words = input_str.split()
    return ' '.join(word.capitalize() for word in words)

def contains_only_number(input):
    for char in input:
        if char.isalpha():
            return False
    return True

# Affichage / Main
def main():
    error_arguments(sys.argv)
    
    print(contains_only_number(sys.argv[1]))

main()
