#!/usr/bin/python3
import sys

# Gestion d'Erreur
def error_arguments(arguments):
    if len(sys.argv) < 2:
        print("error")
        sys.exit()

# Résolution
def ascii_sort(array):
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

    sorted_elements = ascii_sort(sys.argv[1:])
    
    print(' '.join(sorted_elements))

main()