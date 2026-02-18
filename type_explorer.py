# 1: Tipu pētnieks
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
# No piemēriem: Demonstrējam dažādas vērtības un to truthy/falsy uzvedību
print(bool(""))             # False (tukša virkne ir falsy)
print(bool(" "))            # True (atstarpe ir simbols, tāpēc truthy)
print(bool("0"))            # True (jebkura netukša virkne ir truthy, pat "0")
print(bool(0))              # False (0 ir falsy)
print(bool([]))             # False (tukšs saraksts ir falsy)
print(bool(None))           # False (None ir falsy)
print(bool(None))           # False (None ir falsy)
# Papildu no piemēriem: Jauktā aritmētika ar bool
print(True + True)          # 2 (bool ir int apakšklase, True=1, tāpēc 1+1=2)
print(True * 10)            # 10 (True=1, tāpēc 1*10=10)
print(False + 5)            # 5 (False=0, tāpēc 0+5=5)
print(10 / True)            # 10.0 (True=1, tāpēc 10/1=10.0)

# 1.4: Vismaz 3 tiešās datu tipu pārveides (explicit conversion) ar robežgadījumiem
print("\n=== Explicit conversion piemēri ===")
# No piemēriem: Virkņu savienošana un konversija
print("5" + "3")            # "53" (virkņu savienošana, Python neveic automātisku konversiju)
# print("5" + 3)            # TypeError! Atšķirībā no JS, Python to neatļauj (komentēts, lai neizraisītu kļūdu)
print(int("5") + 3)         # 8 (explicit konversija no str uz int)

# Robežgadījumi no piemēriem
print(int("abc"))       # ValueError — neizdodas, jo "abc" nav skaitlis
print(f"Kļūda: {e}")    # Izdrukās kļūdu ziņojumu
print(float("3.14"))        # 3.14 (veiksmīga konversija)

# Skaitļu pārveidošana no jūsu piemēriem
print(int(3.86))            # 3 ('norauj' beigas, nenotiek apaļošana)
print(int("3.14"))      # ValueError! Kāpēc? Jo "3.14" nav vesels skaitlis bez punkta
print(int(float("3.14")))   # 3 (pirms konversijas uz int, pārvērš uz float)
print(float("1e3"))         # 1000.0 (zinātniskā notācija)

# Citi interesanti gadījumi no piemēriem
print(0.1 + 0.2 == 0.3)     # False, kāpēc? Float precizitātes problēma (0.1+0.2=0.30000000000000004, kas nav tieši 0.3)
print(round(2.5))           # 2 (apaļošana uz leju pie .5, jo pirms ir pāra skaitlis)
print(round(3.5))           # 4 (apaļošana uz augšu pie .5, jo pirms ir nepāra skaitlis)
