import globals 
import bmi_calc
 
if __name__ == "__main__": 
    globals.initialize() 

    testtomeg = int(input("Add meg a testtömeget (kg): "))
    magassag = int(input("Add meg a testmagasságot (cm): "))
    
    print("BMI index: ", bmi_calc.szamitas(magassag, testtomeg))
    print("A WHO ajánlott testsúlyosztályozás szerint", bmi_calc.vizsgalat(), "vagy")
