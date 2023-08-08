# tri d'une liste de nombres aléatoires

#création de la liste aléatoire
from random import randrange
liste=[] #liste vide
taille=8 #définition de la taille de la liste
for i in range(0,taille):
	liste.append(randrange(0,50))

print(liste)

#tri de la liste aléatoire
for j in range(0,taille):   #parcours des éléments de la liste initial
	tmp=liste[j]        #variable temporaire qui sert de comparatif
	i=j-1
	while i>=0 and liste[i]>tmp:         #boucle pour tester la valeur précedente par rapport au comparatif
		liste [i+1]=liste[i]         #on décale le chiffre i vers la droite s'il est plus grand
		i=i-1
	liste[i+1]=tmp                       #valeur de la variable temporaire assigné quand la boucle est finie
	
print(liste)

#recherche d'un élément particulier en parcourant la liste
x=int(input("Taper le nombre recherché:"))
j=0
while j<taille:                                        #boucle de parcours de la liste
	if liste[j]==x:                                    # cas où une occurence est trouvée
		print("le nombre",x,"arrive à la position",j+1)
		j=taille
	elif j==taille-1:                                   # cas où aucune occurrence n'est trouvée à la fin de la liste
		print("aucune occurence de",x,"trouvée dans la liste")
		j=taille
	else:                                               # cas où l'occurrence n'est pas à cette position
		j=j+1

# recherche d'un élément par dichotomie
# définition de la fonction dichotomie
def dichotomie(x,liste):
	b=0                  #borne basse
	h=taille-1           #borne haute
	i=0
	while b<=h:                   #boucle tant que h>b
		m=(b+h)//2            # m est recalculée à chaque division
		if x==liste[m]:       # cas où x est trouvé
			return m
		elif x<liste[m]:      # cas où x est inférieur au chiffre du milieu, on conserve donc la division basse en diminuant la borne haute h
			h=m-1
		else:                 # cas où x est supérieur au chiffre du milieu, on conserve donc la division haute en augmentant la borne basse b
			b=m+1
	return -1                     # cas où x n'est pas présent dans la liste

#appel de la fonction
j=dichotomie(x,liste)
if j==-1:
	print("aucune occurence de",x,"trouvée dans la liste")
else:
	print("le nombre",x,"arrive à la position",j+1)









		
