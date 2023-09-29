#!/usr/bin/python3
import sys

# Gestion d'Erreur
def error_arguments(arguments):
    if len(arguments) < 3:
        print("error")
        sys.exit()

    for char in arguments[1:]:
        if char.isalpha():
            print("error")
            sys.exit()

#Parse
def parse_args(args):
    return args[1:]

# Résolution
def find_abs_diff(array):
    lowest_diff = abs(int(array[0])-int(array[-1]))
    for i in array:
        for j in array:
            if j != i:
                current_diff = abs(int(j)-int(i))
                if lowest_diff > current_diff:
                    lowest_diff = current_diff
    
    return lowest_diff



# Affichage / Main
def main():
    error_arguments(sys.argv)
    print(find_abs_diff(parse_args(sys.argv)))

main()