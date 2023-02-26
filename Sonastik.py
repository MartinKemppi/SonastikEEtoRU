from OmaMoodul import *

laused=[]

while True:
    menu=input("\n0-välju\n1-loeme failist \n2-Salvestame failisse \n3-Tekst helisse \n4-Sõnade tõlkimine \n5-Vaata sõnastiku\n6-Paranda viga sõnastikus\n7-Test\n")
    if menu=="0":
        break
    if menu=="1":
        keel=input("Milles keeles tahad sõnad näha? eesti keel või vene keel: ")
        while keel=="eesti keel" or "vene keel":
            if keel=="eesti keel":
                laused=Loe_failist("est.txt")
                for line in laused:
                    print(line)
                break
            elif keel=="vene keel":
                laused=Loe_failist("rus.txt")
                for line in laused:
                    print(line)
                break
            else:
                keel=input("eesti keel või vene keel: ")     
    elif menu=="2":        
        Kirjuta_failisse("rus.txt","est.txt")
    elif menu=="3":
        text=""
        keel=input("Milles keeles tahad kuulata sõnastiku? eesti keel või vene keel: ")
        while keel=="eesti keel" or "vene keel":
            if keel=="vene keel":
                laused=Loe_failist("rus.txt")
                for line in laused:
                    text=text+" "+line
                heli(text,"ru")
            if keel=="eesti keel":
                laused=Loe_failist("est.txt")
                for line in laused:
                    text=text+" "+line
                heli(text,"et")        
    elif menu=="4":
        tõlk("rus.txt","est.txt")
    elif menu=="5":
        laused=Loe_failist("rus.txt")
        for line in laused:
            print(line)
        laused=Loe_failist("est.txt")
        for line in laused:
            print(line)
    elif menu=="6":
        paranda("rus.txt","est.txt")
    elif menu=="7":
        test("rus.txt","est.txt")

