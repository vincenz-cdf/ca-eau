#!/usr/bin/python3
import sys

# Gestion d'erreur
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

# Parse
def parseint(string):
    return int(string)

# Resolution
def find_next_prime(number):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n / 2) + 1):
            if n % i == 0:
                return False
        return True
    
    candidate = number + 1
    while not is_prime(candidate):
        candidate += 1
    
    return candidate

# Affichage / Main
def main():
    error_arguments_length(sys.argv)
    error_arguments_type(sys.argv[1])

    number = parseint(sys.argv[1])
    
    next_prime = find_next_prime(number)
    print(next_prime)


main()
