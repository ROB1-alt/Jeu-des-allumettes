from tkinter import *

#Creation de la fenetre
fen = Tk()
fen.title("Jeu des allumettes")
fen.geometry("1080x680")
fen.configure(bg="mistyrose")

#Variables
a=25
nbmj=1

#Fonctions
def un():
    global a,nbmj
    if a>0:
        a=a-1
        allumette.configure(text=a)
    if nbmj==1:
        nbmj=2
        nbmjoueurs.configure(text="C'est au joueur " + str(nbmj) + " de jouer !")
    else:
        nbmj=1
        nbmjoueurs.configure(text="C'est au joueur " + str(nbmj) + " jouer !")
    if a<=0:
        nbmjoueurs.configure(text="Bien joué au joueur " +str(nbmj)+" qui a gagné !")

def deux():
    global a,nbmj
    if a>0:
        a=a-2
        allumette.configure(text=a)
    if nbmj==1:
        nbmj=2
        nbmjoueurs.configure(text="C'est au joueur " + str(nbmj) + " de jouer !")
    else:
        nbmj=1
        nbmjoueurs.configure(text="C'est au joueur " + str(nbmj) + " de jouer !")
    if a<=0:
        nbmjoueurs.configure(text="Bien joué au joueur " +str(nbmj)+" qui a gagné !")

def trois():
    global a,nbmj
    if a>0:
        a=a-3
        allumette.configure(text=a)
    if nbmj==1:
        nbmj=2
        nbmjoueurs.configure(text="C'est au joueur " + str(nbmj) + " de jouer !")
    else:
        nbmj=1
        nbmjoueurs.configure(text="C'est au joueur " + str(nbmj) + " de jouer !")
    if a<=0:
        nbmjoueurs.configure(text="Bien joué au joueur " +str(nbmj)+" qui a gagné !")

#Widgets
nbmjoueurs=Label(fen,text="C'est au joueur 1 de commencer !",width=35,height=3,bd=3,relief="ridge",bg="darkslateblue")
nbmjoueurs.place_configure(x=405,y=25)
nbmjoueurs.place

boutun=Button(fen,text="Enlever 1 allumette",width=20,height=3,command=un,bd=6,relief="ridge",bg="darkslateblue")
boutun.place_configure(x=100,y=125)
boutun.place()

boutdeux=Button(fen,text="Enlever 2 allumettes",width=20,height=3,command=deux,bd=6,relief="ridge",bg="darkslateblue")
boutdeux.place_configure(x=450,y=125)
boutdeux.place()

bouttrois=Button(fen,text="Enlever 3 allumettes",width=20,height=3,command=trois,bd=6,relief="ridge",bg="darkslateblue")
bouttrois.place_configure(x=800,y=125)
bouttrois.place()

allumette=Label(fen,text=a,width=75,height=20,bg="darkslateblue",bd=8,relief="ridge")
allumette.place_configure(x=270,y=250)
allumette.place()

fen.quit = quit
quit = Button(fen, text="Quitter",command=fen.destroy)
quit.place_configure(x=1000,y=630)
quit.place()

#Boucle de rafraichissement de la fenetre
fen.mainloop()