# tri d'une liste de nombres aléatoires

#création de la liste aléatoire
from random import randrange
liste=[] #liste vide
taille=6 #définition de la taille de la liste
for i in range(0,taille):
	liste.append(randrange(0,100))

print(liste)

#tri de la liste aléatoire
for j in range(0,taille):   #parcours des éléments de la liste initial
	tmp=liste[j]        #variable temporaire qui sert de comparatif
	i=j-1
	while i>=0 and liste[i]>tmp:         #boucle pour tester la valeur précedente par rapport au comparatif
		liste [i+1]=liste[i]         #on décale le chiffre i vers la droite s'il est plus grand
		i=i-1
		print(liste)
	liste[i+1]=tmp                       #valeur de la variable temporaire assigné quand la boucle est finie
	
print(liste)
	
	
	
