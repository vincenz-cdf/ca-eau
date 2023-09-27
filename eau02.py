import sys

def error_arguments_length(arguments):
    if len(sys.argv) < 2:
        print("Veuillez fournir au moins un arguments.")
        sys.exit()

def reverse_array():
    reversed_arguments = []
    for i in range(len(sys.argv)-1, 0, -1):
        reversed_arguments.append(sys.argv[i])     
    return reversed_arguments

def affichage(arguments):
    print("\n".join(arguments))

def main():
    affichage(reverse_array())

main()