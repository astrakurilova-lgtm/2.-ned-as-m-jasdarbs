# type_explorer.py
# Demo skripts Python datu tipiem, truthy/falsy uzvedībai un explicit conversion.
# Šis skripts demonstrē pamata koncepcijas no Python pamatiem.

# 1.1: Piešķirt vismaz 2 pamata tipu vērtības mainīgajiem (str, int, float, bool, None)
# Izveidojam mainīgos ar dažādiem tipiem (vairāk nekā minimums, lai demonstrētu)
str_var1 = "Hello"  # String tips
str_var2 = "World"  # Vēl viens string
int_var1 = 42       # Integer tips
int_var2 = -10      # Vēl viens integer
float_var1 = 3.14   # Float tips
float_var2 = 0.0    # Vēl viens float
bool_var1 = True    # Boolean tips
bool_var2 = False   # Vēl viens boolean
none_var = None     # None tips

# 1.2: Konsoles izvade ar katras vērtības tipu, izmantojot type()
print("=== Datu tipi ===")
print(f"str_var1: {str_var1}, tips: {type(str_var1)}")
print(f"str_var2: {str_var2}, tips: {type(str_var2)}")
print(f"int_var1: {int_var1}, tips: {type(int_var1)}")
print(f"int_var2: {int_var2}, tips: {type(int_var2)}")
print(f"float_var1: {float_var1}, tips: {type(float_var1)}")
print(f"float_var2: {float_var2}, tips: {type(float_var2)}")
print(f"bool_var1: {bool_var1}, tips: {type(bool_var1)}")
print(f"bool_var2: {bool_var2}, tips: {type(bool_var2)}")
print(f"none_var: {none_var}, tips: {type(none_var)}")

# 1.3: Vismaz 3 Python truthy/falsy uzvedības piemērus ar komentāriem
print("\n=== Truthy/Falsy piemēri ===")
# Demonstrējam dažādas vērtības un to truthy/falsy uzvedību
print(f"bool(''): {bool('')}")             # False (tukša virkne ir falsy)
print(f"bool(' '): {bool(' ')}")           # True (atstarpe ir simbols, tāpēc truthy)
print(f"bool('0'): {bool('0')}")           # True (jebkura netukša virkne ir truthy, pat "0")
print(f"bool(0): {bool(0)}")               # False (0 ir falsy)
print(f"bool([]): {bool([])}")             # False (tukšs saraksts ir falsy)
print(f"bool(None): {bool(None)}")         # False (None ir falsy)
# Papildu piemēri: Jauktā aritmētika ar bool (bool ir int apakšklase)
print(f"True + True: {True + True}")       # 2 (True=1, tāpēc 1+1=2)
print(f"True * 10: {True * 10}")           # 10 (True=1, tāpēc 1*10=10)
print(f"False + 5: {False + 5}")           # 5 (False=0, tāpēc 0+5=5)
print(f"10 / True: {10 / True}")           # 10.0 (True=1, tāpēc 10/1=10.0)

# 1.4: Vismaz 3 tiešās datu tipu pārveides (explicit conversion) ar robežgadījumiem
print("\n=== Explicit conversion piemēri ===")
# Virkņu savienošana un konversija
print(f"'5' + '3': {'5' + '3'}")           # "53" (virkņu savienošana, Python neveic automātisku konversiju)
# print("'5' + 3")                         # TypeError! Atšķirībā no JS, Python to neatļauj (komentēts, lai neizraisītu kļūdu)
print(f"int('5') + 3: {int('5') + 3}")     # 8 (explicit konversija no str uz int)

# Robežgadījumi ar try-except, lai demonstrētu kļūdas
try:
    result = int("abc")
    print(f"int('abc'): {result}")
except ValueError as e:
    print(f"int('abc') izraisīja ValueError: {e}")  # ValueError — neizdodas, jo "abc" nav skaitlis

print(f"float('3.14'): {float('3.14')}")   # 3.14 (veiksmīga konversija)

# Skaitļu pārveidošana
print(f"int(3.86): {int(3.86)}")           # 3 ('norauj' beigas, nenotiek apaļošana)
# int("3.14") ir ValueError, tāpēc demonstrējam caur float
try:
    result = int(float("3.14"))
    print(f"int(float('3.14')): {result}")  # 3 (pirms konversijas uz int, pārvērš uz float)
except ValueError as e:
    print(f"int(float('3.14')) izraisīja ValueError: {e}")

print(f"float('1e3'): {float('1e3')}")     # 1000.0 (zinātniskā notācija)

# Citi interesanti gadījumi
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")  # False, float precizitātes problēma (0.1+0.2=0.30000000000000004)
print(f"round(2.5): {round(2.5)}")         # 2 (apaļošana uz leju pie .5, jo pirms ir pāra skaitlis)
print(f"round(3.5): {round(3.5)}")         # 4 (apaļošana uz augšu pie .5, jo pirms ir nepāra skaitlis)

# Funkcija vizuāli sakārtotai izvadei (piemēram, ar rāmīti)
def print_block(level, message):
    """
    Izdrukā ziņojumu vizuāli sakārtotā blokā.
    level: Ziņojuma līmenis (piem., "INFO", "ERROR").
    message: Ziņojuma teksts.
    """
    border = "*" * (len(message) + len(level) + 7)  # Rāmīte atbilstoši garumam
    print(f"\n{border}")
    print(f"* {level}: {message} *")
    print(f"{border}\n")

# Galvenais bloks (standarta Python prakse, lai skripts būtu izpildāms tieši)
if __name__ == "__main__":
    print_block("INFO", "Šis ir vizuāli sakārtots demo bloks.")
    print("Šis ir demo fails Python datu tipiem. Palaid to ar 'python type_explorer.py'.")