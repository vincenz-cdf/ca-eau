#!/usr/bin/python3
import sys

# Gestion d'Erreur
def error_arguments(arguments):
    if len(sys.argv) != 3 or not all(arg.isnumeric() for arg in sys.argv[1:]):
        print("error")
        sys.exit()

# Parse
def parse_args(args):
    return int(args[1]), int(args[2])

# Résolution
def get_values_in_range(min_val, max_val):
    start, end = sorted([min_val, max_val])
    return list(range(start, end))

# Affichage / Main
def main():
    error_arguments(sys.argv)
    
    min_val, max_val = parse_args(sys.argv)
    values = get_values_in_range(min_val, max_val)
    
    print(' '.join(map(str, values)))

main()
