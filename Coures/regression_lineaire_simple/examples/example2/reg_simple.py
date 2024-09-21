#!/usr/bin/env python3

"""
on donne : 
    x = 2 ,4 , 3 , 5 , 6 , 10
    y = 5 , 9 , 7 , 11 , 13 , 21

l'objectif d'écrire un ML simple qui donne la prédiction de la valeur de y en fonction de x 
on va uitliser le modéle régression linéaire  simple 

"""

def modele( a , b, x):
    "fonction du modéle de regression lineaire "
    return a*x + b 


def cout(X , Y ):
    " fonction, de cout du modéle de regression linéaire "
    m = len(Y) # le nombres d'exemples 
    predictions = [modele(x) for x in X] # [f(x_i) avec  x_i : fearture]

    cout = (1/(2*m))*sum([(predictions[i]-Y[i])**2 for i in range(m)])

    return cout 

def derive_cout_a(X , Y , a , b) :
    return (1/len(Y))*sum([ ( modele(a , b, X[i]) - Y[i] ) * X[i] for i in range(len(Y))])


def derive_cout_b(X , Y , a ,b ):

    return (1/len(Y))*sum([ modele(a , b, X[i]) - Y[i]  for i in range(len(Y))])



def algo_gradient(X , Y , nb , alpha):

    "etape 4 : Algo d'apprentissage --> Algo de gradiente descendante "

    a = 0 
    b  = 0 

    for _ in range(nb):
        a-=alpha*derive_cout_a(X , Y , a ,b)
        b-=alpha*derive_cout_b(X , Y , a , b)

    return a , b





# dataset :
X = [2 , 4, 3, 5 , 6 , 10] # features 
Y = [5 , 9 , 7 , 11 , 13 , 21] # target 
nb =  100000  # le nombre de fois d'app 
alpha = 0.01 # le vitesse d'app 


# donc notre modele mnt est pres apres la pahase d'apprentissage :
a , b = algo_gradient(X , Y , nb , alpha)

print(f'aprés la pahase d\'apprentissage a = {a} et b = {b} ')

# Exemples :

x = 12
y = modele( a ,b , x)



while(True) :
    
    chaine = input("tapez votre x ou quit pour terminer : ")

    if(chaine=='quit'):
        print("Au revoir")
        break

    try:
        x = int(chaine)
        print(f'la valeur prédir par notre ML est : {modele(a ,b , x)}')
    except :
        print(f'{chaine} ne peut pas etre convertir en numero')
    

