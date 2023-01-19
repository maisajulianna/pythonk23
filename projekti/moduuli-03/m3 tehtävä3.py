#3.3
print("tehtävä 3")
#kysy sukupuoli → print hemoglobiiniarvo

print()
sex = input("Kerro sukupuolesi: ")
print()

if sex == "nainen" or "Nainen":
    hg = float(input("Anna hemoglobiiniarvosi (g/l): "))
    if hg > 175:
               print("Hemoglobiiniarvosi on korkea.")
    elif hg < 117:
                print("Hemoglobiiniarvosi on alhainen.")
    else:
        print("Hemoglobiiniarvosi on normaali!")

if sex == "mies" or "Mies":
    hg = float(input("Anna hemoglobiiniarvosi (g/l): "))
    if hg > 195:
        print("Hemoglobiiniarvosi on korkea.")
    elif hg < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    else:
        print("Hemoglobiiniarvosi on normaali!")
