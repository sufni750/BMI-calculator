#vizsgálat, hogy a BMI érték hol helyezkedik el a WHO ajánlás szerint
def vizsgalat():
    if bmi < 18.5:
      return("sovány")
    elif 18.5 <= bmi < 25:
        return("normál")
    elif 25 <= bmi < 30:
        return("túlsúlyos")
    elif bmi > 30:
        return("elhízott")


testtomeg = int(input("Add meg a testtömeget (kg): "))
magassag = int(input("Add meg a testmagasságot (cm): "))

#magasság átalakítása m-re
magassag = magassag/100

#BMI kiszámítása
bmi = testtomeg/(magassag**2)
print("BMI: ", bmi, "\nA WHO ajánlott testsúlyosztályozás szerint", vizsgalat(), "vagy")

