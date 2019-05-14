from tkinter import *
from turtle import *
from tkinter.messagebox import *


def krugovi(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.kruznica = krugovi

def krajIgreFun():
    prozor.destroy()

def opisIgreFun():
     showinfo("4 u nize - Upute", """                 4 u nizu drustevna je igra koju igraju dva igrača.
     Ploča za igru sastavljena je od 7x5 krugova. Igrači naizmjence                                   odabiru u koji stupac žele staviti svoju boju.

   Prisitkom na gumb ⇑ ispod stupca, program postavlja igračevu boju                               na zadnji prazni krug u tom stupcu.

        Cilj igre je skupiti četiri iste boje u bilokojem od osam smjerova.                                    Pobjednik je onaj koji to učini prvi!

                                   Želim vam sreću i zabavu!""")
     return
def uputaPrije():
     global uputa
     uputa=Tk()
     uputa.title("4 u nizu")
     uputa.config(bg="white")
     uputa.resizable(False,False)
     uputa.geometry("700x650+300+100")

     canvas = Canvas(uputa,width=700, height=650, borderwidth=0, bg="white")
     canvas.grid()
     canvas.kruznica(360,210,40,fill="red")
     canvas.kruznica(360,395,40,fill="blue")
     
     naslovUputa=Label(uputa, text="4    U    N  I  Z  U",bg="White",font=("Arial",12,"bold"))
     naslovUputa.place(x = 300, y = 25)
     potpisNovi=Label(uputa,text="Rudelic 2017.",bg="White",font=("Arial",11))
     potpisNovi.place(x=600,y=620)
     
     uputaCrveni=Label(uputa, text="Boja kruga 1. igrača je CRVENA",bg="White",font=("Arial",20,"bold"))
     uputaCrveni.place(x = 150, y = 100)
     uputaPlavi=Label(uputa, text="Boja kruga 2. igrača je PLAVA",bg="White",font=("Arial",20,"bold"))
     uputaPlavi.place(x = 150, y = 285)

     zapocni=Button(uputa, text="Započni igru!",bg="white", fg="Black", font=("Arial",50,"bold"),borderwidth=0,command=pocetakIgreFun)
     zapocni.place(x=110,y=450)   
     
     uputa.mainloop()
    
def pocetakIgreFun():
    
    global uputa
    uputa.destroy()
    
    global prozor
    prozor.destroy()
    
    global nova
    
    nova=Tk()
    #global nova
    nova.title("4 u nizu")
    nova.config(bg="white")
    nova.resizable(False,False)
    nova.geometry("700x650+300+100")
    global canvas
    canvas = Canvas(nova,width=700, height=650, borderwidth=0, bg="white")
    canvas.grid()
   # global canvas
    
    naslovNovi=Label(nova, text="4    U    N  I  Z  U",bg="White",font=("Arial",12,"bold"))
    naslovNovi.place(x = 300, y = 25)

###Razna sranja###
    
    global redA
    global redB
    global redC
    global redD
    global redE
    global redF
    global redG
    global dobarUnosA
    global dobarUnosB
    global dobarUnosC
    global dobarUnosD
    global dobarUnosE
    global dobarUnosF
    global dobarUnosG
    global matrica
    global naRedu
    
    redA=4
    redB=4
    redC=4
    redD=4
    redE=4
    redF=4
    redG=4
    dobarUnosA=0
    dobarUnosB=0
    dobarUnosC=0
    dobarUnosD=0
    dobarUnosE=0
    dobarUnosF=0
    dobarUnosG=0
    matrica=[]
    for i in range(7):
        l=[]
        for j in range(5):
            l = l + ["0"]
        matrica = matrica + [l]

    naRedu=1


### Kružnice ###
    
    canvas.kruznica(75,469,40,fill="white")
    canvas.kruznica(75+80+10,469,40,fill="white")
    canvas.kruznica(75+80*2+20,469,40,fill="white")
    canvas.kruznica(75+80*3+30,469,40,fill="white")
    canvas.kruznica(75+80*4+40,469,40,fill="white")
    canvas.kruznica(75+80*5+50,469,40,fill="white")
    canvas.kruznica(75+80*6+60,469,40,fill="white")

    canvas.kruznica(75,379,40,fill="white")
    canvas.kruznica(75+80+10,379,40,fill="white")
    canvas.kruznica(75+80*2+20,379,40,fill="white")
    canvas.kruznica(75+80*3+30,379,40,fill="white")
    canvas.kruznica(75+80*4+40,379,40,fill="white")
    canvas.kruznica(75+80*5+50,379,40,fill="white")
    canvas.kruznica(75+80*6+60,379,40,fill="white")

    canvas.kruznica(75,289,40,fill="white")
    canvas.kruznica(75+80+10,289,40,fill="white")
    canvas.kruznica(75+80*2+20,289,40,fill="white")
    canvas.kruznica(75+80*3+30,289,40,fill="white")
    canvas.kruznica(75+80*4+40,289,40,fill="white")
    canvas.kruznica(75+80*5+50,289,40,fill="white")
    canvas.kruznica(75+80*6+60,289,40,fill="white")

    canvas.kruznica(75,199,40,fill="white")
    canvas.kruznica(75+80+10,199,40,fill="white")
    canvas.kruznica(75+80*2+20,199,40,fill="white")
    canvas.kruznica(75+80*3+30,199,40,fill="white")
    canvas.kruznica(75+80*4+40,199,40,fill="white")
    canvas.kruznica(75+80*5+50,199,40,fill="white")
    canvas.kruznica(75+80*6+60,199,40,fill="white")

    canvas.kruznica(75,109,40,fill="white")
    canvas.kruznica(75+80+10,109,40,fill="white")
    canvas.kruznica(75+80*2+20,109,40,fill="white")
    canvas.kruznica(75+80*3+30,109,40,fill="white")
    canvas.kruznica(75+80*4+40,109,40,fill="white")
    canvas.kruznica(75+80*5+50,109,40,fill="white")
    canvas.kruznica(75+80*6+60,109,40,fill="white")

    
    
###    SIMBOLI ZA STUPCE  ###
    stupac1=Button(nova, text="⇑",bg="white", fg="Black", font=("Arial",50,"bold"),borderwidth=0,command=igraA)
    stupac1.place(x=28,y=510)
    
    stupac2=Button(nova, text="⇑",bg="white", fg="Black", font=("Arial",50,"bold"),borderwidth=0,command=igraB)
    stupac2.place(x=118,y=510)
    
    stupac3=Button(nova, text="⇑",bg="white", fg="Black", font=("Arial",50,"bold"),borderwidth=0,command=igraC)
    stupac3.place(x=208,y=510)
    
    stupac4=Button(nova, text="⇑",bg="white", fg="Black", font=("Arial",50,"bold"),borderwidth=0,command=igraD)
    stupac4.place(x=298,y=510)
    
    stupac5=Button(nova, text="⇑",bg="white", fg="Black", font=("Arial",50,"bold"),borderwidth=0,command=igraE)
    stupac5.place(x=388,y=510)
    
    stupac6=Button(nova, text="⇑",bg="white", fg="Black", font=("Arial",50,"bold"),borderwidth=0,command=igraF)
    stupac6.place(x=478,y=510)
    
    stupac7=Button(nova, text="⇑",bg="white", fg="Black", font=("Arial",50,"bold"),borderwidth=0,command=igraG)
    stupac7.place(x=568,y=510)
    
    nova.mainloop()
    return

def igraA():
    global redA
    global matrica
    global naRedu
    global dobarUnosA
    if dobarUnosA<5:
        redA=redA-1
        if naRedu%2==1:
            if redA==3:
                canvas.kruznica(75,469,40,fill="red")
                dobarUnosA+=1
                naRedu+=1
            if redA==2:
                canvas.kruznica(75,379,40,fill="red")
                dobarUnosA+=1
                naRedu+=1
            if redA==1:
                canvas.kruznica(75,289,40,fill="red")
                dobarUnosA+=1
                naRedu+=1
            if redA==0:
                canvas.kruznica(75,199,40,fill="red")
                dobarUnosA+=1
                naRedu+=1
            if redA==-1:
                canvas.kruznica(75,109,40,fill="red")
                dobarUnosA+=1
                naRedu+=1
            matrica[0][redA+1]="1"
        elif naRedu%2==0:
            if redA==3:
                canvas.kruznica(75,469,40,fill="blue")
                dobarUnosA+=1
                naRedu+=1
            if redA==2:
                canvas.kruznica(75,379,40,fill="blue")
                dobarUnosA+=1
                naRedu+=1
            if redA==1:
                canvas.kruznica(75,289,40,fill="blue")
                dobarUnosA+=1
                naRedu+=1
            if redA==0:
                canvas.kruznica(75,199,40,fill="blue")
                dobarUnosA+=1
                naRedu+=1
            if redA==-1:
                canvas.kruznica(75,109,40,fill="blue")
                dobarUnosA+=1
                naRedu+=1
            matrica[0][redA+1]="2"
    elif dobarUnosA==5:
        showinfo("Upozorenje!","Odabrani stupac je pun, odaberite drugi stupac!")
    pobjeda()
    return

def igraB():
    global redB
    global matrica
    global naRedu
    global dobarUnosB
    if dobarUnosB<5:
        redB=redB-1
        if naRedu%2==1:
            if redB==3:
                canvas.kruznica(75+90,469,40,fill="red")
            if redB==2:
                 canvas.kruznica(75+90,379,40,fill="red")
            if redB==1:
                canvas.kruznica(75+90,289,40,fill="red")
            if redB==0:
                canvas.kruznica(75+90,199,40,fill="red")
            if redB==-1:
                canvas.kruznica(75+90,109,40,fill="red")
            dobarUnosB+=1
            naRedu+=1
            matrica[1][redB+1]="1"
        elif naRedu%2==0:
            if redB==3:
                canvas.kruznica(75+90,469,40,fill="blue")
            if redB==2:
                 canvas.kruznica(75+90,379,40,fill="blue")
            if redB==1:
                canvas.kruznica(75+90,289,40,fill="blue")
            if redB==0:
                canvas.kruznica(75+90,199,40,fill="blue")
            if redB==-1:
                canvas.kruznica(75+90,109,40,fill="blue")
            dobarUnosB+=1
            naRedu+=1
            matrica[1][redB+1]="2"
    elif dobarUnosB==5:
        showinfo("Upozorenje!","Odabrani stupac je pun, odaberite drugi stupac!")
    pobjeda()
    return

def igraC():
    global redC
    global matrica
    global naRedu
    global dobarUnosC
    
    if dobarUnosC<5:
        redC=redC-1
        if naRedu%2==1:
            if redC==3:
                canvas.kruznica(75+80*2+20,469,40,fill="red")
            if redC==2:
                 canvas.kruznica(75+80*2+20,379,40,fill="red")
            if redC==1:
                canvas.kruznica(75+80*2+20,289,40,fill="red")
            if redC==0:
                canvas.kruznica(75+80*2+20,199,40,fill="red")
            if redC==-1:
                canvas.kruznica(75+80*2+20,109,40,fill="red")
            dobarUnosC+=1
            naRedu+=1
            matrica[2][redC+1]="1"
        elif naRedu%2==0:
            if redC==3:
                canvas.kruznica(75+80*2+20,469,40,fill="blue")
            if redC==2:
                 canvas.kruznica(75+80*2+20,379,40,fill="blue")
            if redC==1:
                canvas.kruznica(75+80*2+20,289,40,fill="blue")
            if redC==0:
                canvas.kruznica(75+80*2+20,199,40,fill="blue")
            if redC==-1:
                canvas.kruznica(75+80*2+20,109,40,fill="blue")
            dobarUnosC+=1
            naRedu+=1
            matrica[2][redC+1]="2"
    elif dobarUnosC==5:
        showinfo("Upozorenje!","Odabrani stupac je pun, odaberite drugi stupac!")
    pobjeda()
    return

def igraD():
    global redD
    global matrica
    global naRedu
    global dobarUnosD
    
    if dobarUnosD<5:
        redD=redD-1
        if naRedu%2==1:
            if redD==3:
                canvas.kruznica(75+80*3+30,469,40,fill="red")
            if redD==2:
                 canvas.kruznica(75+80*3+30,379,40,fill="red")
            if redD==1:
                canvas.kruznica(75+80*3+30,289,40,fill="red")
            if redD==0:
                canvas.kruznica(75+80*3+30,199,40,fill="red")
            if redD==-1:
                canvas.kruznica(75+80*3+30,109,40,fill="red")
            dobarUnosD+=1
            naRedu+=1
            matrica[3][redD+1]="1"
        elif naRedu%2==0:
            if redD==3:
                canvas.kruznica(75+80*3+30,469,40,fill="blue")
            if redD==2:
                 canvas.kruznica(75+80*3+30,379,40,fill="blue")
            if redD==1:
                canvas.kruznica(75+80*3+30,289,40,fill="blue")
            if redD==0:
                canvas.kruznica(75+80*3+30,199,40,fill="blue")
            if redD==-1:
                canvas.kruznica(75+80*3+30,109,40,fill="blue")
            dobarUnosD+=1
            naRedu+=1
            matrica[3][redD+1]="2"
    elif dobarUnosD==5:
        showinfo("Upozorenje!","Odabrani stupac je pun, odaberite drugi stupac!")
    pobjeda()
    return

def igraE():
    global redE
    global matrica
    global naRedu
    global dobarUnosE
    
    if dobarUnosE<5:
        redE=redE-1
        if naRedu%2==1:
            if redE==3:
                canvas.kruznica(75+80*4+40,469,40,fill="red")
            if redE==2:
                 canvas.kruznica(75+80*4+40,379,40,fill="red")
            if redE==1:
                canvas.kruznica(75+80*4+40,289,40,fill="red")
            if redE==0:
                canvas.kruznica(75+80*4+40,199,40,fill="red")
            if redE==-1:
                canvas.kruznica(75+80*4+40,109,40,fill="red")
            dobarUnosE+=1
            naRedu+=1
            matrica[4][redE+1]="1"
        elif naRedu%2==0:
            if redE==3:
                canvas.kruznica(75+80*4+40,469,40,fill="blue")
            if redE==2:
                 canvas.kruznica(75+80*4+40,379,40,fill="blue")
            if redE==1:
                canvas.kruznica(75+80*4+40,289,40,fill="blue")
            if redE==0:
                canvas.kruznica(75+80*4+40,199,40,fill="blue")
            if redE==-1:
                canvas.kruznica(75+80*4+40,109,40,fill="blue")
            dobarUnosE+=1
            naRedu+=1
            matrica[4][redE+1]="2"
    elif dobarUnosE==5:
        showinfo("Upozorenje!","Odabrani stupac je pun, odaberite drugi stupac!")
    pobjeda()
    return

def igraF():
    global redF
    global matrica
    global naRedu
    global dobarUnosF
    
    if dobarUnosF<5:
        redF=redF-1
        if naRedu%2==1:
            if redF==3:
                canvas.kruznica(75+80*5+50,469,40,fill="red")
            if redF==2:
                 canvas.kruznica(75+80*5+50,379,40,fill="red")
            if redF==1:
                canvas.kruznica(75+80*5+50,289,40,fill="red")
            if redF==0:
                canvas.kruznica(75+80*5+50,199,40,fill="red")
            if redF==-1:
                canvas.kruznica(75+80*5+50,109,40,fill="red")
            dobarUnosF+=1
            naRedu+=1
            matrica[5][redF+1]="1"
        elif naRedu%2==0:
            if redF==3:
                canvas.kruznica(75+80*5+50,469,40,fill="blue")
            if redF==2:
                 canvas.kruznica(75+80*5+50,379,40,fill="blue")
            if redF==1:
                canvas.kruznica(75+80*5+50,289,40,fill="blue")
            if redF==0:
                canvas.kruznica(75+80*5+50,199,40,fill="blue")
            if redF==-1:
                canvas.kruznica(75+80*5+50,109,40,fill="blue")
            dobarUnosF+=1
            naRedu+=1
            matrica[5][redF+1]="2"
    elif dobarUnosF==5:
        showinfo("Upozorenje!","Odabrani stupac je pun, odaberite drugi stupac!")
    pobjeda()
    return

def igraG():
    global redG
    global matrica
    global naRedu
    global dobarUnosG
    
    if dobarUnosG<5:
        redG=redG-1
        if naRedu%2==1:
            if redG==3:
                canvas.kruznica(75+80*6+60,469,40,fill="red")
            if redG==2:
                 canvas.kruznica(75+80*6+60,379,40,fill="red")
            if redG==1:
                canvas.kruznica(75+80*6+60,289,40,fill="red")
            if redG==0:
                canvas.kruznica(75+80*6+60,199,40,fill="red")
            if redG==-1:
                canvas.kruznica(75+80*6+60,109,40,fill="red")
            dobarUnosG+=1
            naRedu+=1
            matrica[6][redG+1]="1"
        elif naRedu%2==0:
            if redG==3:
                canvas.kruznica(75+80*6+60,469,40,fill="blue")
            if redG==2:
                 canvas.kruznica(75+80*6+60,379,40,fill="blue")
            if redG==1:
                canvas.kruznica(75+80*6+60,289,40,fill="blue")
            if redG==0:
                canvas.kruznica(75+80*6+60,199,40,fill="blue")
            if redG==-1:
                canvas.kruznica(75+80*6+60,109,40,fill="blue")
            dobarUnosG+=1
            naRedu+=1
            matrica[6][redG+1]="2"
    elif dobarUnosG==5:
        showinfo("Upozorenje!","Odabrani stupac je pun, odaberite drugi stupac!")
    pobjeda()
    return

def pobjeda():
    global matrica
    global nova
    global kraj
    global brojac
    brojac+=1
    
    for i in range(5):
        if matrica[0][i]==matrica[1][i]==matrica[2][i]==matrica[3][i]=="1":
            pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
            if pitanje == True:
                nova.destroy()
                main()    
            else:
                nova.destroy()
            kraj=kraj+1
        elif matrica[1][i]==matrica[2][i]==matrica[3][i]==matrica[4][i]=="1":
            pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
            if pitanje == True:
                nova.destroy()
                main()    
            else:
                nova.destroy()
            kraj += 1
        elif matrica[2][i]==matrica[3][i]==matrica[4][i]==matrica[5][i]=="1":
            pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
            if pitanje == True:
                nova.destroy()
                main()    
            else:
                nova.destroy()
            kraj += 1
        elif matrica[3][i]==matrica[4][i]==matrica[5][i]==matrica[6][i]=="1":
            pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
            if pitanje == True:
                nova.destroy()
                main()    
            else:
                nova.destroy()
            kraj += 1

        elif matrica[0][i]==matrica[1][i]==matrica[2][i]==matrica[3][i]=="2":
            pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
            if pitanje == True:
                nova.destroy()
                main()    
            else:
                nova.destroy()
            kraj += 1
        elif matrica[1][i]==matrica[2][i]==matrica[3][i]==matrica[4][i]=="2":
            pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
            if pitanje == True:
                nova.destroy()
                main()    
            else:
                nova.destroy()
            kraj += 1
        elif matrica[2][i]==matrica[3][i]==matrica[4][i]==matrica[5][i]=="2":
            pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
            if pitanje == True:
                nova.destroy()
                main()    
            else:
                nova.destroy()
            kraj += 1
        elif matrica[3][i]==matrica[4][i]==matrica[5][i]==matrica[6][i]=="2":
            pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
            if pitanje == True:
                nova.destroy()
                main()    
            else:
                nova.destroy()
            kraj += 1
    for i in range(7):
        if matrica[i][0]==matrica[i][1]==matrica[i][2]==matrica[i][3]=="1":
            pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
            if pitanje == True:
                nova.destroy()
                main()    
            else:
                nova.destroy()
            kraj += 1
        elif matrica[i][1]==matrica[i][2]==matrica[i][3]==matrica[i][4]=="1":
            pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
            if pitanje == True:
                nova.destroy()
                main()    
            else:
                nova.destroy()
            kraj += 1
        elif matrica[i][0]==matrica[i][1]==matrica[i][2]==matrica[i][3]=="2":
            pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
            if pitanje == True:
                nova.destroy()
                main()    
            else:
                nova.destroy()
        elif matrica[i][1]==matrica[i][2]==matrica[i][3]==matrica[i][4]=="2":
            pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
            if pitanje == True:
                nova.destroy()
                main()    
            else:
                nova.destroy()
            
    if matrica[0][3]==matrica[1][2]==matrica[2][1]==matrica[3][0]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[0][4]==matrica[1][3]==matrica[2][2]==matrica[3][1]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[1][3]==matrica[2][2]==matrica[3][1]==matrica[4][0]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[3][4]==matrica[4][3]==matrica[5][2]==matrica[6][1]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[1][4]==matrica[2][3]==matrica[3][2]==matrica[4][1]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[2][3]==matrica[3][2]==matrica[4][1]==matrica[5][0]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[2][4]==matrica[3][3]==matrica[4][2]==matrica[5][1]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[3][3]==matrica[4][2]==matrica[5][1]==matrica[6][0]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
        
    if matrica[0][3]==matrica[1][2]==matrica[2][1]==matrica[3][0]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[0][4]==matrica[1][3]==matrica[2][2]==matrica[3][1]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[1][3]==matrica[2][2]==matrica[3][1]==matrica[4][0]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[3][4]==matrica[4][3]==matrica[5][2]==matrica[6][1]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[1][4]==matrica[2][3]==matrica[3][2]==matrica[4][1]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[2][3]==matrica[3][2]==matrica[4][1]==matrica[5][0]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[2][4]==matrica[3][3]==matrica[4][2]==matrica[5][1]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[3][3]==matrica[4][2]==matrica[5][1]==matrica[6][0]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1

    if matrica[0][1]==matrica[1][2]==matrica[2][3]==matrica[3][4]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[0][0]==matrica[1][1]==matrica[2][2]==matrica[3][3]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[1][1]==matrica[2][2]==matrica[3][3]==matrica[4][4]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[1][0]==matrica[2][1]==matrica[3][2]==matrica[4][3]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[2][1]==matrica[3][2]==matrica[4][3]==matrica[5][4]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[2][0]==matrica[3][1]==matrica[4][2]==matrica[5][3]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[3][1]==matrica[4][2]==matrica[5][3]==matrica[6][4]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[3][0]==matrica[4][1]==matrica[5][2]==matrica[6][3]=="1":
        pitanje = askyesno("Pobjeda!","Igrač 1. pobjeđuje sa svojim crvenim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1

    if matrica[0][1]==matrica[1][2]==matrica[2][3]==matrica[3][4]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[0][0]==matrica[1][1]==matrica[2][2]==matrica[3][3]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[1][1]==matrica[2][2]==matrica[3][3]==matrica[4][4]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[1][0]==matrica[2][1]==matrica[3][2]==matrica[4][3]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[2][1]==matrica[3][2]==matrica[4][3]==matrica[5][4]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[2][0]==matrica[3][1]==matrica[4][2]==matrica[5][3]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[3][1]==matrica[4][2]==matrica[5][3]==matrica[6][4]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1
    if matrica[3][0]==matrica[4][1]==matrica[5][2]==matrica[6][3]=="2":
        pitanje = askyesno("Pobjeda!","Igrač 2. pobjeđuje sa svojim plavim krugovima! Želite li igrati ponovo?")
        if pitanje == True:
                nova.destroy()
                main()    
        else:
                nova.destroy()
        kraj += 1

    if brojac==35 and kraj==0:
        askyesno("Neriješeno!","Rezultat je neriješen! Želite li igrati ponovo?")
        if askyesno == True:
            poc()
        else:
            nova.destroy()
    return
    
def poc():
    global prozor
    prozor=Tk()
    prozor.title("4 u nizu")
    prozor.config(bg="white")
    prozor.resizable(False,False)
    prozor.geometry("700x650+300+100")
    
    global kraj
    kraj=0
    global brojac
    brojac=0
    
    naslov=Label(prozor, text="4 U NIZU",bg="White",font=("Arial",60,"bold"))
    naslov.place(x = 195, y = 100)
    potpis=Label(prozor,text="Rudelic 2017.",bg="White",font=("Arial",11))
    potpis.place(x=600,y=620)

    pocetakIgre=Button(prozor, text="Nova igra",bg="white", fg="Black", font=("Arial",32,"bold"),borderwidth=0,command=uputaPrije)
    pocetakIgre.place(x=245,y=240)

    opisIgre=Button(prozor, text="Uputstva",bg="white", fg="Black", font=("Arial",32,"bold"),borderwidth=0,command=opisIgreFun)
    opisIgre.place(x=255,y=325)

    krajIgre=Button(prozor, text="Izlaz",bg="white", fg="Black", font=("Arial",32,"bold"),borderwidth=0, command=krajIgreFun)
    krajIgre.place(x=303,y=410)
    prozor.mainloop()
    
def main():
    poc()
    
main()
