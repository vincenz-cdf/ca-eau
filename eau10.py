#!/usr/bin/python3
import sys

# Gestion d'Erreur
def error_arguments(arguments):
    if len(sys.argv) < 3:
        print("error")
        sys.exit()

# Parse
def split_array(args):
    return args[1:-1], args[-1]

# Résolution
def find_index(elements, target):
    try:
        return elements.index(target)
    except ValueError:
        return -1

# Affichage / Main
def main():
    error_arguments(sys.argv)
    
    elements, target = split_array(sys.argv)
    print(find_index(elements, target))

main()
