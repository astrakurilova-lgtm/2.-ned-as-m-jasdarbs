# converter.py
# Vienību konvertors: konvertē starp kilometriem/jūdzēm, kilogramiem/mārciņām, litriem/galoniem, dolāriem/eiro un temperatūrām.

# Konstantes konversijas koeficientiem (lielajiem burtiem)
KM_TO_MI = 0.621371
MI_TO_KM = 1 / KM_TO_MI
KG_TO_LB = 2.20462
LB_TO_KG = 1 / KG_TO_LB
L_TO_GAL = 0.264172
GAL_TO_L = 1 / L_TO_GAL
USD_TO_EUR = 0.84235020
EUR_TO_USD = 1 / USD_TO_EUR
C_TO_F_FACTOR = 9 / 5  # Koeficients °C -> °F
F_TO_C_FACTOR = 5 / 9  # Koeficients °F -> °C
F_OFFSET = 32  # Nobīde °F formulā

def demo():
    """
    Demonstrācijas funkcija: parāda dažus konversijas piemērus automātiski.
    """
    print("=== DEMO: Vienību konvertora piemēri ===")
    print("Šie ir automātiski aprēķināti piemēri, lai parādītu funkcionalitāti.\n")
    
    # Piemēri konversijām
    examples = [
        (1, 1, 42, "km -> mi"),  # Izvēle 1, virziens 1, vērtība 42
        (1, 2, 26.1, "mi -> km"),  # Izvēle 1, virziens 2, vērtība 26.1
        (2, 1, 10, "kg -> lb"),  # Izvēle 2, virziens 1, vērtība 10
        (3, 1, 5, "L -> gal"),  # Izvēle 3, virziens 1, vērtība 5
        (4, 1, 100, "$ -> €"),  # Izvēle 4, virziens 1, vērtība 100
        (5, 1, 0, "°C -> °F"),  # Izvēle 5, virziens 1, vērtība 0
        (5, 2, 32, "°F -> °C"),  # Izvēle 5, virziens 2, vērtība 32
    ]
    
    for choice, direction, value, desc in examples:
        if choice == 1:
            units = ("km", "mi", KM_TO_MI, MI_TO_KM)
        elif choice == 2:
            units = ("kg", "lb", KG_TO_LB, LB_TO_KG)
        elif choice == 3:
            units = ("L", "gal", L_TO_GAL, GAL_TO_L)
        elif choice == 4:
            units = ("$", "€", USD_TO_EUR, EUR_TO_USD)
        elif choice == 5:
            units = ("°C", "°F", None, None)
        
        if choice == 5:  # Temperatūra
            if direction == 1:
                result = value * C_TO_F_FACTOR + F_OFFSET
            else:
                result = (value - F_OFFSET) * F_TO_C_FACTOR
        else:  # Parastās
            if direction == 1:
                result = value * units[2]
            else:
                result = value * units[3]
        
        if direction == 1:
            print(f"{value:.2f} {units[0]} = {result:.2f} {units[1]} ({desc})")
        else:
            print(f"{value:.2f} {units[1]} = {result:.2f} {units[0]} ({desc})")
    
    print("\n=== Beigas demo. Tagad pāriet uz interaktīvo režīmu. ===")

def main():
    while True:  # Cikls konversijas tipa izvēlei
        print("Izvēlies konversiju: 1) km<->mi  2) kg<->lb  3) L<->gal  4) $<->€  5) °C<->°F")
        user_input = input("> ").strip().lower()  # Noņem atstarpes un pārvērš mazajiem burtiem
        if user_input in ["exit", "q"]:
            print("Iziet no skripta. Uz redzēšanos!")
            return  # Beidz funkciju
        try:
            choice = int(user_input)
            if choice in [1, 2, 3, 4, 5]:
                break  # Pareiza izvēle, iziet no cikla
            else:
                print("Nepareiza izvēle. Izvēlies no 1 līdz 5.")
        except ValueError:
            print("Nepareiza ievade. Ievadi skaitli no 1 līdz 5 (vai 'exit'/'q' lai izietu).")

    # Virziena izvēlne atkarībā no tipa
    while True:  # Cikls virziena izvēlei
        if choice == 1:
            print("Virziens: 1) km -> mi  2) mi -> km")
            units = ("km", "mi", KM_TO_MI, MI_TO_KM)
        elif choice == 2:
            print("Virziens: 1) kg -> lb  2) lb -> kg")
            units = ("kg", "lb", KG_TO_LB, LB_TO_KG)
        elif choice == 3:
            print("Virziens: 1) L -> gal  2) gal -> L")
            units = ("L", "gal", L_TO_GAL, GAL_TO_L)
        elif choice == 4:
            print("Virziens: 1) $ -> €  2) € -> $")
            units = ("$", "€", USD_TO_EUR, EUR_TO_USD)
        elif choice == 5:
            print("Virziens: 1) °C -> °F  2) °F -> °C")
            units = ("°C", "°F", None, None)  # Īpašs gadījums temperatūrai

        user_input = input("> ").strip().lower()
        if user_input in ["exit", "q"]:
            print("Iziet no skripta. Uz redzēšanos!")
            return
        try:
            direction = int(user_input)
            if direction in [1, 2]:
                break  # Pareiza izvēle, iziet no cikla
            else:
                print("Nepareiza izvēle. Izvēlies 1 vai 2.")
        except ValueError:
            print("Nepareiza ievade. Ievadi 1 vai 2 (vai 'exit'/'q' lai izietu).")

    # Ievade vērtībai
    while True:  # Cikls vērtības ievadei
        user_input = input("Ievadi vērtību: ").strip().lower()
        if user_input in ["exit", "q"]:
            print("Iziet no skripta. Uz redzēšanos!")
            return
        try:
            value = float(user_input)
            break  # Pareiza vērtība, iziet no cikla
        except ValueError:
            print("Nepareiza ievade. Ievadi skaitlisku vērtību (vai 'exit'/'q' lai izietu).")

    # Konversija
    if choice == 5:  # Īpašs gadījums temperatūrai
        if direction == 1:
            result = value * C_TO_F_FACTOR + F_OFFSET  # °C -> °F
            print(f"{value:.2f} {units[0]} = {result:.2f} {units[1]}")
        else:
            result = (value - F_OFFSET) * F_TO_C_FACTOR  # °F -> °C
            print(f"{value:.2f} {units[1]} = {result:.2f} {units[0]}")
    else:  # Parastās konversijas
        if direction == 1:
            result = value * units[2]  # No pirmās vienības uz otro
            print(f"{value:.2f} {units[0]} = {result:.2f} {units[1]}")
        else:
            result = value * units[3]  # No otrās vienības uz pirmo
            print(f"{value:.2f} {units[1]} = {result:.2f} {units[0]}")

if __name__ == "__main__":
    demo()  # Izsauc demo pirmo reizi
    main()  # Tad pāriet uz interaktīvo režīmu