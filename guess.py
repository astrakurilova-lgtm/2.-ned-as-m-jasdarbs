# guess.py

import random

def print_block(level, message):
    """Vizuāli sakārtots izvades bloks"""
    border = "*" * (len(message) + len(level) + 7)
    print(f"\n{border}")
    print(f"* {level}: {message} *")
    print(f"{border}\n")

def play_game(max_attempts=10):
    """Spēlē vienu raundu"""
    secret = random.randint(1, 100)
    attempts = 0
    
    print(f"\nEsmu izdomājis skaitli no 1 līdz 100.")
    print(f"Tev ir {max_attempts} mēģinājumi.\n")
    
    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"Mēģinājums {attempts + 1}/{max_attempts} (atlikuši: {remaining})")
        
        guess = input("Tavs minējums: ").strip()
        
        # Validācija
        if not guess.lstrip('-').isdigit():
            print("Kļūda: ievadi skaitli!\n")
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess == secret:
            print(f"\nPAREIZI! Tu uzminēji {secret} ar {attempts} mēģinājumiem!")
            return True, attempts
        
        if guess > secret:
            print("Par lielu! Mēģini mazāku.")
        else:
            print("Par mazu! Mēģini lielāku.")
        print()
    
    print(f"\nBeidzies laiks! Pareizais skaitlis bija {secret}")
    return False, attempts

def demo():
    """Demo piemērs"""
    print("=== DEMO ===")
    print("Piemērs: dators izdomāja 42")
    print("Lietotājs min: 50 -> Par lielu")
    print("Lietotājs min: 25 -> Par mazu")
    print("Lietotājs min: 37 -> Pareizi!")

def main():
    print_block("UZD5", "Minēšanas spēle")
    demo()
    
    print("\n" + "="*50)
    
    while True:
        input("\nNospied Enter, lai sāktu...")
        
        won, attempts = play_game()
        
        while True:
            play_again = input("\nSpēlēt vēlreiz? (j/n): ").strip().lower()
            if play_again in ['j', 'y', 'yes']:
                break
            elif play_again in ['n', 'no']:
                print("\nPaldies! Uz redzēšanos!")
                print_block("PABEIGTS", "Spēle beigusies")
                return
            else:
                print("Ievadi 'j' vai 'n'")

if __name__ == "__main__":
    main()