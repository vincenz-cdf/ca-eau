#!/usr/bin/python3
def process_combinaisons():
    combinations = []
    for i in range(100): 
        for j in range(i+1, 100): 
            combo = [
                f"0{i}" if i < 10 else f"{i}",
                f"0{j}" if j < 10 else f"{j}"
            ]
            combo.sort() 
            combinations.append(combo)
    return combinations


def affichage(combinations):
    formatted_combinations = []
    for i in combinations:
        formatted_combinations.append(f"{i[0]} {i[1]}") 
    print(", ".join(formatted_combinations))


def main():
    affichage(process_combinaisons())

main()