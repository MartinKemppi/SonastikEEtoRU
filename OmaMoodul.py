from gtts import *
from random import *
import os

def Loe_failist(fail:str)->str:
    """
    lugemine failist
    """
    f=open(fail,"r",encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip()) 
    f.close()
    return jarjend 

def Kirjuta_failisse(fail1:str,fail2:str):
    """
    sisetab failise
    """
    rus=[]
    est=[]
    f=open(fail1,'r',encoding="utf-8-sig")
    for rida in f:
        rus.append(rida.strip())
    f.close()
    f=open(fail2,'r',encoding="utf-8-sig")
    for rida in f:
        est.append(rida.strip()) 
    f.close()
    indK=input("Milles keeles tahad sõna lisada? eesti keel või vene keel: ")
    while indK == "eesti keel" or "vene keel":
        sõna=input("Lisa sõna: ")
        sõna1=input("Mida see tähendab? ")
        if indK=="eesti keel":
            f=open(fail2,'a',encoding="utf-8-sig")
            f.write("\n"+sõna) 
            f.close()
            f=open(fail1,'a',encoding="utf-8-sig") 
            f.write("\n"+sõna1) 
            f.close()
        elif indK=="vene keel":
            f=open(fail1,'a',encoding="utf-8-sig")
            f.write("\n"+sõna) 
            f.close()
            f=open(fail2,'a',encoding="utf-8-sig") 
            f.write("\n"+sõna1) 
            f.close()
        else:
            indK=input("vali keel: eesti keel või vene keel: ")       
        return rus and est

def heli(text:str,keel:str):
    """
    annab heli et kuulata seda sõna/lause
    """   
    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
    os.system("heli.mp3")
    
def tõlk(fail1:str,fail2:str):
    """
    tõlk failist faili
    """
    rus=[] 
    est=[]
    f=open(fail1,'r',encoding="utf-8-sig")
    for rida in f:
        rus.append(rida.strip())
    f.close()
    f=open(fail2,'r',encoding="utf-8-sig")
    for rida in f:
        est.append(rida.strip()) 
    f.close()
    sõna=input("Kirjutage sõna, mida soovite tõlkida ")
    while sõna.isdigit():
        sõna=input("Kirjuta õige sõna")
    if sõna not in rus and sõna not in est:
        print("Seda sõna pole sõnastikus ")
        vastus_lisa=input("Kas soovite selle sõna sõnaraamatusse lisada? (jah või ei) ").lower() 
        while vastus_lisa == "jah" or "ei": 
            if vastus_lisa=="jah":
                keel=input("Kas see on vene keel või eesti keel? ").lower()
                while keel == "vene keel" or "eesti keel":
                    if keel=="vene keel":
                        f=open(fail1,'a',encoding="utf-8-sig") 
                        f.write("\n"+sõna) 
                        f.close()
                        tolke=input("Kirjutage sõna tõlge ") 
                        while tolke.isdigit():
                            tolke=input("Kirjuta õige sõna ")
                        f=open(fail2,"a",encoding="utf-8-sig")
                        f.write("\n"+tolke) 
                        f.close()
                    else: 
                        f=open(fail2,'a',encoding="utf-8-sig") 
                        f.write("\n"+sõna) 
                        f.close()
                        tolke=input("Kirjutage sõna tõlge ") 
                        while tolke.isdigit():
                            tolke=input("Kirjuta õige sõna ")
                        f=open(fail1,"a",encoding="utf-8-sig")
                        f.write("\n"+tolke) 
                        f.close()
        else:
            print("Las jääb siis")
    for i in range(len(rus)):
        if sõna==rus[i]:
            print(f"{rus[i]} - {est[i]}")
            heli(est[i],"et")
        elif sõna==est[i]:
            print(f"{est[i]} - {rus[i]}")
            heli(rus[i],"ru") 

def paranda(fail1:str,fail2:str):
    """
    sõna parandamine failis1 ja failis2
    """
    rus=[] 
    est=[]
    f=open(fail1,'r',encoding="utf-8-sig")
    for line in f:
        rus.append(line.strip())
    f.close()
    f=open(fail2,'r',encoding="utf-8-sig")
    for line in f:
        est.append(line.strip()) 
    f.close()
    keel=input("Parandame sõna vene või eesti sõnaraamatus? ").lower()
    while keel not in ["vene","eesti"]:
        keel=input("Kirjuta vene või eesti ")
    if keel=="vene":
        indv=input("Millist sõna soovite parandada? ")
        while indv not in rus:
            indv=input("Kirjutage õige sõna ")
        for i in range(len(rus)):
            if indv==rus[i]:
                ind=rus.index(indv) 
        parasona=input("Kirjutage parandatud sõna ")
        while parasona.isdigit():
            parasona=input("Kirjutage õige sõna ")
        rus[ind]=parasona
        for i in range(len(rus)):
            rus[i]=rus[i]+"\n"
        f=open(fail1,"w",encoding="utf-8-sig")
        f.writelines(rus)
        f.close()
    else:
        indv=input("Millist sõna soovite parandada? ")
        while indv not in est:
            indv=input("Kirjutage õige sõna ")
        for i in range(len(rus)):
            if indv==est[i]:
                ind=est.index(indv) 
        parasona=input("Kirjutage parandatud sõna ")
        while parasona.isdigit():
            parasona=input("Kirjutage õige sõna ")
        est[ind]=parasona
        for i in range(len(rus)):
            est[i]=est[i]+"\n"
        f=open(fail2,"w",encoding="utf-8-sig")
        f.writelines(est)
        f.close()

def test(fail1:str,fail2:str):
    """
    õigekiri test
    """
    rus=[] 
    est=[]
    game=[] 
    a=[]
    v=k=0
    f=open(fail1,'r',encoding="utf-8-sig")
    for line in f:
        rus.append(line.strip())
    f.close()
    f=open(fail2,'r',encoding="utf-8-sig")
    for line in f:
        est.append(line.strip()) 
    f.close()
    x=int(input("palju korda mängime: "))
    for i in range (x):
        num=randint(0,(len(rus)-1))
        while num in a:
            num=randint(0,(len(rus)-1))
        keel=input("Mis keelest sõna test on? (vene või eesti) ").lower()
        while keel not in ["vene","eesti"]:
            keel=input("Kirjutage ainult vene või eesti ").lower() 
        if keel=="vene":
            rana=rus[num] 
            tõlk=input(f"Mis on sõna {rana} tõlge? ") 
            if tõlk==est[num]:
                game.append(f"{i+1} {keel} mäng - võit")
                print("Võit") 
                v+=1
            else:
                game.append(f"{i+1}, {keel} mäng - kaotus") 
                print("Kaotus")
                k+=1
        else:
            rana=est[num] 
            tõlk=input(f"Mis on sõna {rana} tõlge? ") 
            if tõlk==rus[num]:
                game.append(f"{i+1} {keel} mäng - võit")
                print("Võit")
                v+=1
            else:
                game.append(f"{i+1}, {keel} mäng - kaotus") 
                print("Kaotus")
                k+=1       
        a.append(num)
    print()
    print(game)
    if k==0:
        resÕ=100
        resV=0
    elif v==0:
        resÕ=0
        resV=100
    else:
        resÕ=round((v/i)*100),1
        resV=round((k/i)*100),1
    print(f"Võiduprotsent - {resÕ}%")
    print(f"Kaotusprotsent - {resV}%")

