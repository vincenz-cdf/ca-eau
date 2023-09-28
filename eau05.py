#!/usr/bin/python3
import sys

# Gestion d'Erreur
def error_arguments(arguments):
    if len(sys.argv) != 3:
        print("error")
        sys.exit()


# Résolution
def is_substring(str1, str2):
    return str2 in str1

# Affichage / Main
def main():
    error_arguments(sys.argv)
    
    result = is_substring(sys.argv[1], sys.argv[2])
    
    print(str(result))

main()
