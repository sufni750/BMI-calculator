import globals 
import bmi_calc
import tkinter as tk


def button_command():
    magassag = int(ent1.get())
    testtomeg = int(ent2.get())
    bmi_calc.szamitas(magassag, testtomeg)
    bmi_strvar.set(str(round(globals.bmi, 2)))
    vizsgalat_strvar.set(bmi_calc.vizsgalat())    
    

if __name__ == "__main__": 
    globals.initialize() 
    # root window
    root = tk.Tk()

    bmi_strvar = tk.StringVar()
    vizsgalat_strvar = tk.StringVar()
    
    
    # configure the root window
    root.geometry('300x200')
    root.resizable(False, False)
    root.title('BMI kalkulátor')

    lf_alap = tk.Frame(root)
    lf_alap.grid()
    lf1 = tk.LabelFrame(lf_alap, text='Adatok')
    lf1.grid(column=0, row=0, padx=20, pady=20)
    
    lab1 = tk.Label(lf1, text = "Magasság: ")
    lab1.grid(row = 0, column = 0)
    lab2 = tk.Label(lf1, text = "Testtömeg: ")
    lab2.grid(row = 1, column = 0)

    ent1 = tk.Entry(lf1, width = 5)
    ent1.grid(row = 0, column =1, padx = 5)
    ent2 =tk.Entry(lf1, width = 5)
    ent2.grid(row = 1, column =1, padx = 5, pady = 5)
    

    btn1 = tk.Button(lf_alap, text = "Kiszámol", command = button_command )
    btn1.grid(row = 0, column = 1) 
     
    bmi_felirat = tk.Label(lf_alap, text = "BMI: ")
    bmi_felirat.grid(row = 1, column = 0, sticky = "W", padx = 20)

    bmi_ertek = tk.Label(lf_alap, textvariable = bmi_strvar)
    bmi_ertek.grid(row = 1, column = 0)
    
    bmi_vizsgalat_szoveg = tk.Label(lf_alap, text ="WHO ajánlás alapján:")
    bmi_vizsgalat_szoveg.grid(row = 2, column = 0, sticky = "W", padx = 20)

    bmi_vizsgalat_eredmeny = tk.Label(lf_alap, textvariable = vizsgalat_strvar)
    bmi_vizsgalat_eredmeny.grid(row = 2, column = 1, sticky = "W")
    



    root.mainloop() 

   # testtomeg = int(input("Add meg a testtömeget (kg): "))
   # magassag = int(input("Add meg a testmagasságot (cm): "))
    
   # print("BMI index: ", bmi_calc.szamitas(magassag, testtomeg))
   # print("A WHO ajánlott testsúlyosztályozás szerint", bmi_calc.vizsgalat(), "vagy")
