#!/usr/bin/python3

import sys

#Gestion d'erreur
def error_arguments_length(arguments):
    if len(sys.argv) < 2:
        print("Veuillez fournir au moins un argument.")
        sys.exit()

def error_arguments_type(argument):
    try:
        index = int(argument)
        if index < 0:
            print("-1")
            sys.exit()
    except ValueError:
        print("-1")
        sys.exit()

#Parse
def parseint(string):
    return int(string)

#Resolution
def initialize_fibonacci(index):
    premier = 0
    deuxieme = 1
    fibonacci = [0, 1]
    for i in range(2, index+1):
        resultat = premier + deuxieme
        fibonacci.append(resultat)
        premier = deuxieme
        deuxieme = resultat
    return fibonacci

#Affichage / Main
def main():
    error_arguments_length(sys.argv)
    error_arguments_type(sys.argv[1])

    index = parseint(sys.argv[1])

    final_array = initialize_fibonacci(index)
    print(final_array[index])

main()
    