#!/usr/bin/python3
import sys

# Gestion d'Erreur
def error_arguments(arguments):
    if len(sys.argv) < 2:
        print("error")
        sys.exit()
    for arg in arguments[1:]:
        try:
            float(arg)
        except ValueError:
            print("error")
            sys.exit()

# Parse
def parse_args(args):
    return [float(arg) for arg in args[1:]]

# Résolution
def my_select_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

# Affichage / Main
def main():
    error_arguments(sys.argv)
    
    elements = parse_args(sys.argv)
    sorted_elements = my_select_sort(elements)
    
    print(' '.join(map(str, sorted_elements)))

main()
