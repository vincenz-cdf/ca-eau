#!/usr/bin/python3
import sys

# Gestion d'Erreur
def error_arguments(arguments):
    if len(sys.argv) < 2:
        print("error")
        sys.exit()
    for char in arguments[1:]:
        if char.isalpha():
            print("error")
            sys.exit()

# Résolution
def my_bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# Affichage / Main
def main():
    error_arguments(sys.argv)
    sorted_elements = my_bubble_sort(sys.argv[1:])
    
    print(' '.join(map(str, sorted_elements)))

main()