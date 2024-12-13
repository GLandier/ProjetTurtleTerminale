#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from turtle import *#on importe tutrle
from random import *#on import random
speed(0)#on augmente la vitesse
colormode(255)

def trapeze(l):#dessiner le trapeze
    """Cette fonction permet de tracer un trapèze de taille l et de couleur 
    aléatoire"""
    fillcolor(randint(0,255),randint(0,255),randint(0,255))# designe un couleur de remplissage aleatoire
    begin_fill()#on commence a colorié le trapèze
    forward(2*l)#la base du trapèze mesure 2 fois la longueur du petit triangle
    left(120)
    forward(l)
    left(60)
    forward(l)
    left(60)
    forward(l)
    left(120) # retourne la tortue a l'etat initial
    end_fill()#on a arrete de colorié 
    forward(l)#on se place a au milieu de la base du trapèze car cela est plus pratique pour la suite du code






def triangle(l,n):# permet de créer le triangle
    """Cette fonction permet de créer un triangle equilaterale de longueur 2**n fois plus grand que la longueur
    du petit triangle. l est la taille du petit triangle et n est le niveau du "puzzle" """
    forward(l*2**n)
    left(120)
    forward(l*2**n)
    left(120)
    forward(l*2**n)
    left(120)
    

def dessine_solution(l,n):
    """Cette fonction est récursive permettant de placer des trapèze de maniere optimisé 
    dans un triangle. l est la longueur des trapèze et n est le niveau du "puzzle" """
    triangle(l,n) #on dessine le triangle
    up() # on leve le stylo pour pas tracer de triangle a chaque étape
    if n==1: #cas de base
        #On se rend au milieu du coté opposé au petit triangle
        forward(l*2**n)#on parcours la base du triangle
        left(120)#on va sur le coté opposé au petit triangle
        trapeze(l)#on trace le trapèze
        forward(l*2**n/2)#on parcours la moitié du triangle car la turtle c'est arrété a la moitié de la base du trapèze  
        #on retourne a la position initiale
        left(120)
        forward(l*2**n)
        left(120)
    else:
        forward(l*2**(n))#on parcours la base du triangle
        left(120)#on va sur le coté opposé au petit triangle
        forward((l*2**n)/2)#on parcours la moitié du triangle car la turtle c'est arrété a la moitié de la base du trapèze
        backward(l)#on recule de la longueur du petit triangle afin que le trapèze soit au centre du coté opposé au peit triangle 
        trapeze(l)#on trace le trapèze
        forward((l*2**n)/2)#on parcours la moitié du triangle car la turtle c'est arrété a la moitié de la base du trapèze
        #on retourne au point de depart
        left(120)
        forward(l*2**n)
        left(120)
        dessine_solution(l,n-1) #permet de tracer des trapèze dans le meme sens mais dans un triangle n-1
        #permet de tracer les trapèze de facon recusive en prenant comme point de depart les triangle du haut(premier triangle)formé par le premier trapèze créé
        forward(l*2**n)
        left(120)
        forward(l*2**n/2)
        dessine_solution(l,n-1)#permet de tracer des trapèze dans le meme sens mais dans un triangle n-1
        #permet de tracer les trapèze de facon recusive en prenant comme point de depart les triangle du milieu(deuxième triangle)formé par le premier trapèze créé
        left(60)
        dessine_solution(l,n-1)#permet de tracer des trapèze dans le meme sens mais dans un triangle n-1 
        #permet de tracer les trapèze de facon recusive en prenant comme point de depart le triangle du bas(troisième triangle)formé par le premier trapèze créé
        left(60)
        dessine_solution(l,n-1)#permet de tracer des trapèze dans le meme sens mais dans un triangle n-1
        #permet de se replacer au premier point de départ (le petit triangle de base)
        right(120)
        forward(l*2**n/2)
        left(120)
        forward(l*2**n)
        left(120)
    
dessine_solution(20,3)#permet de lancer la fonction

exitonclick()#permet de fermer la fenetre 
