# fizzbuzz.py
# FizzBuzz spēle ar bonusa variācijām

import sys

def print_block(level, message):
    """Vizuāli sakārtots izvades bloks"""
    border = "*" * (len(message) + len(level) + 7)
    print(f"\n{border}")
    print(f"* {level}: {message} *")
    print(f"{border}\n")

def fizzbuzz(n, custom_rules=None):
    """
    FizzBuzz funkcija
    n: skaitlis līdz kuram izvadīt
    custom_rules: papildus kārtulas (saraksts ar tuple: (skaitlis, vārds))
    """
    if custom_rules is None:
        custom_rules = []
    
    results = []
    
    for i in range(1, n + 1):
        output = ""
        
        # Vispirms pārbauda dalāmību ar abiem (3 un 5) - FizzBuzz
        if i % 3 == 0 and i % 5 == 0:
            output = "FizzBuzz"
        else:
            # Pārbauda katru atsevišķi
            if i % 3 == 0:
                output = "Fizz"
            elif i % 5 == 0:
                output = "Buzz"
            else:
                # Pārbauda papildus kārtulas
                for divisor, word in custom_rules:
                    if i % divisor == 0:
                        output = word
                        break
        
        # Ja nav atrasts neviens, izvada skaitli
        if output == "":
            output = str(i)
        
        results.append(output)
    
    return results

def main():
    print_block("UZD4", "FizzBuzz")
    
    # Noklusētās kārtulas
    custom_rules = []
    
    # Pārbauda vai ir papildus argumenti
    if len(sys.argv) > 1:
        # Pārbauda vai ir papildus kārtulas (--rules 7:Jazz)
        args = sys.argv[1:]
        
        # Parsējam argumentus
        n = None
        for arg in args:
            if arg.startswith("--rules="):
                # Izgūstam papildus kārtulas
                rules_str = arg.replace("--rules=", "")
                rule_parts = rules_str.split(",")
                for rule in rule_parts:
                    if ":" in rule:
                        divisor, word = rule.split(":")
                        custom_rules.append((int(divisor), word))
            elif arg.isdigit():
                n = int(arg)
            else:
                # Mēģinam pārveidot
                try:
                    n = float(arg)
                    if n != int(n):
                        print(f"Kļūda: {arg} nav vesels skaitlis")
                        return
                    n = int(n)
                except ValueError:
                    print(f"Kļūda: {arg} nav derīgs skaitlis")
                    return
        
        if n is None:
            print("Kļūda: Nav norādīts skaitlis N")
            print("Lietojums: python fizzbuzz.py N [--rules=7:Jazz,11:Jazz2]")
            return
    else:
        # Demo režīms ar vairākiem piemēriem
        print("=== Demo režīms ===\n")
        
        print("--- N = 15 (standarta) ---")
        result = fizzbuzz(15)
        print(", ".join(result))
        
        print("\n--- N = 20 ar papildus kārtulu (7:Jazz) ---")
        result = fizzbuzz(20, [(7, "Jazz")])
        print(", ".join(result))
        
        print("\n--- N = 30 ar vairākām kārtulām (7:Jazz, 11:Boom) ---")
        result = fizzbuzz(30, [(7, "Jazz"), (11, "Boom")])
        print(", ".join(result))
        
        print("\n=== Interaktīvais režīms ===")
        try:
            n = int(input("Ievadi N: "))
            if n < 1:
                print("Kļūda: N jābūt pozitīvam")
                return
        except ValueError:
            print("Kļūda: ievadi skaitli")
            return
        
        custom_rules = []
        use_custom = input("Vai izmantot papildus kārtulas? (j/n): ").strip().lower()
        if use_custom == "j":
            rules_input = input("Ievadi kārtulas (formāts: skaitlis:vārds, atdalītas ar komatu): ")
            try:
                rule_parts = rules_input.split(",")
                for rule in rule_parts:
                    if ":" in rule:
                        divisor, word = rule.split(":")
                        custom_rules.append((int(divisor.strip()), word.strip()))
            except:
                print("Kļūda: nepareizs formāts, izmanto standarta kārtulas")
                custom_rules = []
    
    # Galvenā FizzBuzz izvade
    print(f"\n--- FizzBuzz (N = {n}) ---")
    result = fizzbuzz(n, custom_rules)
    print(", ".join(result))

if __name__ == "__main__":
    main()