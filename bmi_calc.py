import globals

def vizsgalat():
    if globals.bmi < 18.5:
      return("sovány")
    elif 18.5 <= globals.bmi < 25:
        return("normál")
    elif 25 <= globals.bmi < 30:
        return("túlsúlyos")
    elif globals.bmi > 30:
        return("elhízott")

def szamitas(magassag, testtomeg):
    #magasság átalakítása m-re
    magassag = magassag/100

    #BMI kiszámítása
    globals.bmi = testtomeg/(magassag**2)
    return(globals.bmi)