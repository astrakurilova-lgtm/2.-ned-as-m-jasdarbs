# eligibility.py

def print_block(level, message):
    """Vizuāli sakārtots izvades bloks"""
    border = "*" * (len(message) + len(level) + 7)
    print(f"\n{border}")
    print(f"* {level}: {message} *")
    print(f"{border}\n")

def convert_yes_no(answer):
    """Pārveido 'j'/'n' uz True/False"""
    answer = answer.strip().lower()
    if answer in ["j", "yes", "y"]:
        return True
    elif answer in ["n", "no"]:
        return False
    return None

def get_valid_age():
    """Prasa vecumu ar validāciju"""
    while True:
        try:
            age = int(input("Ievadi vecumu: ").strip())
            if age < 0:
                print("Kļūda: vecums nevar būt negatīvs")
                continue
            return age
        except ValueError:
            print("Kļūda: ievadi skaitli")

def get_yes_no(prompt):
    """Prasa j/n atbildi"""
    while True:
        result = convert_yes_no(input(prompt))
        if result is None:
            print("Kļūda: ievadi 'j' vai 'n'")
        else:
            return result

def check_eligibility(age, has_license, is_student, is_veteran):
    """Pārbauda visus atbilstības kritērijus"""
    can_vote = age >= 18
    can_rent = (age >= 21) and has_license
    senior = (age >= 65) or is_veteran
    student = (16 <= age <= 26) and is_student
    return can_vote, can_rent, senior, student

def print_result(age, has_license, is_student, is_veteran):
    """Izdrukā rezultātus"""
    can_vote, can_rent, senior, student = check_eligibility(age, has_license, is_student, is_veteran)
    
    print(f"\n--- (vecums: {age}) ---")
    print(f"Balsot:         {'Jā' if can_vote else 'Nē'}")
    
    if can_rent:
        print(f"Auto īre:       Jā")
    else:
        reasons = []
        if not (age >= 21):
            reasons.append("nav vecuma")
        if not has_license:
            reasons.append("nav apliecības")
        print(f"Auto īre:       Nē ({', '.join(reasons)})")
    
    print(f"Senioru atlaide: {'Jā' if senior else 'Nē'}")
    print(f"Studentu atlaide: {'Jā' if student else 'Nē'}")

def demo():
    """Demo versija - parāda piemērus"""
    test_cases = [
        (20, False, True, False),
        (70, True, False, False),
        (17, False, False, False),
        (25, True, True, False),
    ]
    
    for age, has_license, is_student, is_veteran in test_cases:
        print_result(age, has_license, is_student, is_veteran)

def main():
    # Demo
    input("\nNospied Enter, lai sāktu demo...")
    demo()
    
    # Interaktīvais režīms
    input("\nNospied Enter, lai sāktu interaktīvo režīmu...")
    
    age = get_valid_age()
    has_license = get_yes_no("Vai ir autovadītāja apliecība? (j/n): ")
    is_student = get_yes_no("Vai ir students? (j/n): ")
    is_veteran = get_yes_no("Vai ir veterāns? (j/n): ")
    
    print_result(age, has_license, is_student, is_veteran)

if __name__ == "__main__":
    print_block("UZD3", "Atbilstības pārbaudītājs")
    main()