#!/usr/bin/python3
def process_combinaisons():
    combinations = []
    for i in range(10): 
        for j in range(10): 
            for k in range(10):
                if i != j and j != k and i != k: 
                    combo = [i, j, k]
                    combo.sort() 
                    if combo not in combinations:
                        combinations.append(combo)
    return combinations


def affichage(combinations):
    formatted_combinations = []
    for i in combinations:
        formatted_combinations.append(f"{i[0]}{i[1]}{i[2]}") 
    print(", ".join(formatted_combinations))


def main():
    affichage(process_combinaisons())

main()