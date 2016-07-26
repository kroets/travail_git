'''
Opérations sur les fractions

'''

# -*- coding :utf-8 -*-

from fractions import Fraction

def print_choix() :
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

def addition_Fraction(a,b):
    print("Le résultat de l'addition de {0} et de {1} est {2}".format(a,b,a+b))

def soustraction_Fraction(a,b):
    print("Le résultat de la soustraction de {0} et de {1} est {2}".format(a,b,a-b))

def multiplication_Fraction(a,b):
    print("Le résultat de la multiplication de {0} et de {1} est {2}".format(a,b,a*b))

def division_Fraction(a,b):
    print("Le résultat de la division de {0} et de {1} est {2}".format(a,b,a/b))

if __name__=='__main__' :
    while True :
        try :
            a = Fraction(input("Entrez la première fraction : "))
            b = Fraction(input("Entrez la deuxième fraction : "))
            print_choix()
            choix = input("Quelle opération voulez-vous réaliser ? ")
            if choix =='1' :
                addition_Fraction(a,b)
            if choix =='2' :
                soustraction_Fraction(a,b)
            if choix =='3' :
                multiplication_Fraction(a,b)
            if choix =='4' :
                division_Fraction(a,b)
        except ValueError :
            print("Vous avez saisi une fraction invalide")
        answer = input("Voulez-vous quitter ? (o) pour oui ")
        if answer == 'o':
            break
            

 
