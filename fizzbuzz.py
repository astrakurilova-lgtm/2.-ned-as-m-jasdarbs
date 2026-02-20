# fizzbuzz.py

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
    custom_rules: papildus kārtulas [(skaitlis, vārds)]
    """
    if custom_rules is None:
        custom_rules = []
    
    results = []
    
    for i in range(1, n + 1):
        output = ""
        
        # Vispirms pārbauda dalāmību ar abiem (3 un 5)
        if i % 3 == 0 and i % 5 == 0:
            output = "FizzBuzz"
        else:
            # Pārbauda katru atsevišķi
            if i % 3 == 0:
                output = "Fizz"
            elif i % 5 == 0:
                output = "Buzz"
            else:
                # Papildus kārtulas
                for divisor, word in custom_rules:
                    if i % divisor == 0:
                        output = word
                        break
        
        if output == "":
            output = str(i)
        
        results.append(output)
    
    return results

def task_4():
    """FizzBuzz"""
    print_block("UZD4", "FizzBuzz")
    
    print("=== Demo ===\n")
    
    # Standarta FizzBuzz
    print("--- N = 15 (standarta) ---")
    result = fizzbuzz(15)
    print(", ".join(result))
    
    # Ar papildus kārtulu
    print("\n--- N = 20 ar 7:Jazz ---")
    result = fizzbuzz(20, [(7, "Jazz")])
    print(", ".join(result))
    
    # Ar vairākām kārtulām
    print("\n--- N = 30 ar 7:Jazz, 11:Boom ---")
    result = fizzbuzz(30, [(7, "Jazz"), (11, "Boom")])
    print(", ".join(result))

def main():
    task_4()
    print("\n" + "="*40)
    print("FizzBuzz demo izpildīts!")

if __name__ == "__main__":
    main()