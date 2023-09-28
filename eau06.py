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
def alternate_uppercase(input_str):
    result_str = []
    to_upper = True  

    for char in input_str:
        if char.isalpha():
            if to_upper:
                result_str.append(char.upper())
            else:
                result_str.append(char.lower())
            to_upper = not to_upper
        else:
            result_str.append(char)

    return ''.join(result_str)

# Affichage / Main
def main():
    error_arguments(sys.argv)
    
    print(alternate_uppercase(sys.argv[1]))

main()
