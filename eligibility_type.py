# eligibility.py
# Atbilstības pārbaudītājs

def main():
    print("=== Atbilstības pārbaudītājs ===\n")
    
    # Vecums
    while True:
        try:
            age = int(input("Ievadi vecumu: ").strip())
            if age < 0:
                print("Kļūda: vecums nevar būt negatīvs")
                continue
            break
        except ValueError:
            print("Kļūda: ievadi skaitli")
    
    # Jautājumi ar j/n
    while True:
        license_input = input("Vai ir autovadītāja apliecība? (j/n): ").strip().lower()
        if license_input in ['j', 'n']:
            has_license = (license_input == 'j')
            break
        print("Kļūda: ievadi 'j' vai 'n'")
    
    while True:
        student_input = input("Vai ir students? (j/n): ").strip().lower()
        if student_input in ['j', 'n']:
            is_student = (student_input == 'j')
            break
        print("Kļūda: ievadi 'j' vai 'n'")
    
    while True:
        veteran_input = input("Vai ir veterāns? (j/n): ").strip().lower()
        if veteran_input in ['j', 'n']:
            is_veteran = (veteran_input == 'j')
            break
        print("Kļūda: ievadi 'j' vai 'n'")
    
    # Pārbaudes (if/elif/else, and, or, not)
    print("\n---")
    
    # Balsošana
    can_vote = age >= 18
    vote_str = "Jā ✓" if can_vote else "Nē ✗"
    print(f"Balsošana:        {vote_str}")
    
    # Auto īre
    can_rent = (age >= 21) and has_license
    if can_rent:
        print(f"Auto īre:         Jā ✓")
    else:
        reason = []
        if not (age >= 21):
            reason.append("nav vecuma")
        if not has_license:
            reason.append("nav apliecības")
        print(f"Auto īre:         Nē ✗ ({', '.join(reason)})")
    
    # Senioru atlaide
    senior = (age >= 65) or is_veteran
    senior_str = "Jā ✓" if senior else "Nē ✗"
    print(f"Senioru atlaide:   {senior_str}")
    
    # Studentu atlaide
    student = (16 <= age <= 26) and is_student
    student_str = "Jā ✓" if student else "Nē ✗"
    print(f"Studentu atlaide:  {student_str}")

if __name__ == "__main__":
    main()
    