LBPN_VENTE_fonctions.py : 


#LA BOUTIQUE DU PERE NOEL VENTE
#le client peut commander plusieurs jouets ,
# et choisir la quantité de chaque jouet .
#une facture est éditée
#LES FONCTIONS
###################################

def affiche_message(texte):
    print("********************************")
    print("*   ",texte,"   *")
    print("********************************")
    print("")



def affiche_standard(lj,lp,lq):
    print("|━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|")
    print("| Nom | |Prix| |Quantité|          |")
    print("|━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|")
    for i in range (len(lj)):
        print("|----------------------------------|")
        print(" | ",lj[i]," | ",lp[i]," | ",lq[i], " | ")
        print("|----------------------------------|")
    print("")

def calcul_val(lp,lq):
    val_stock=0
    val_stock_initial=0
    for i in range (len(lp)):
        val_stock=val_stock+lq[i]*lp[i]
    if val_stock>=1000000:
        val_stock=val_stock-val_stock*0.1
        print("Suite à votre achat supérieur ou égal à 1000000 d'euros, vous recevez : -10%")
    else:
        val_stock=val_stock
    return val_stock

def calcul_vali(lp,lq):
    val_stock=0
    val_stock_initial=0
    for i in range (len(lp)):
        val_stock=val_stock+lq[i]*lp[i]
    if val_stock>=1000000:
        val_stock=val_stock-val_stock*0.1
        val_stock_initial=val_stock+val_stock*0.1
    else:
        val_stock=val_stock
    return val_stock_initial

def facture(lj,lp,lq):
    affiche_message("La Facture ")
    affiche_standard(lj,lp,lq)
    print("Vous avez un prix initial de : ",calcul_vali(lp,lq), "euros")
    print("Vous avez un prix final de : ",calcul_val(lp,lq), "euros")
    print("")



def vente (lj,lp,lq):
    ljc=[]
    lqc=[]
    lpc=[]

    affiche_message("La Vente ")

    réponse=1
    while réponse==1:

        affiche_message("La liste des véhicules disponibles")
        affiche_standard(lj,lp,lq)

        ind_jouet=int(input("Quel voiture souhaitez-vous, choix allant de 0 à 9 :"))
        qte=int(input("Quelle quantité ? (Attention à votre porte-monnaie :"))
        print("")
        lqb=[5,3,2,4,2,1,9,6,3,1]
        if qte>(lqb[ind_jouet]):
            while qte>(lqb[ind_jouet]):
                print("Quantité élevée à notre stock, resaisir la quantité :")
                qte=int(input("Quelle quantité ? (Attention à votre porte-monnaie :"))
        ljc.append(lj[ind_jouet])
        lqc.append(qte)
        lpc.append(lp[ind_jouet])

        réponse=int(input("Cher client, souhaitez-vous un autre véhicule ? Réponse :  0 : Non, 1 : Oui"))
        print("")

    facture(ljc,lpc,lqc)
    
    
    LBPN_VENTE_pgm_principal.py :
     
     
     #PROGRAMME PRINCIPAL
###############################################

from LBPN_VENTE_fonctions import *

print("                              _.-=_-         _")
print("                         _.-=°   _-          | ||------._________..")
print("             ___.=======-.______-,,,,,,,,,,,,`-''----| --------------__")
print("      __.---|     __        ,                   o \           __        [__|")
print(" __---=======.--||  ||--.=================================.---  ---.=======:")
print("]       [w] : /        \ : |========================|    : /        \ :  [w] :")
print("V___________:|          |: |========================|    :|          |:   _-")
print(" V__________: \        / :_|=======================/_____: \        / :__-")
print(" -----------'  |-____-|  `-------------------------------'  |-____-|")



ljb=["0-BMW","1-Mercedes","2-Lamborghini", "3-Ferrari", "4-Maserati", "5-McLaren", "6-Jaguar","7-Land Rover", "8-Audi", "9-Bugatti"]
lqb=[5,3,2,4,2,1,9,6,3,1]
lpb=[90000,110000,150000,160000,97000,210000,45000,75000,82000,1300000]


affiche_message("Concessionnaire de la NSI")

vente(ljb,lpb,lqb)

affiche_message("Concessionaire de la NSI")

affiche_message("Au revoir, à bientot !")
