#!/usr/bin/python3
import sys

# Gestion d'Erreur
def error_arguments(arguments):
    if len(sys.argv) != 3 or not all(arg.isnumeric() for arg in sys.argv[1:]):
        print("error")
        sys.exit()