# programme de calcul du factorielle d'un nombre
# version séquentielle
def fact_seq(n):
	j=1
	tmp=1
	while j<=n:              #boucle qui permet de partir de 1 et de multiplier les chiffres croissants jusqu'à n
		tmp=tmp*j
		j=j+1
	return(tmp)

#version récursive
def fact_rec(n):
	if n<2:                   # test pour arrêter la fonction quand à partir de n, de façon décroissante, on arrive à 1
		return(n)
	else:
		return(n*fact_rec(n-1))   #nouvel appel de la fonction avec n-1


#interface
n=int(input("Entrez la factorielle à calculer:"))
v=input("Tapez seq pour la version séquentielle ou rec pour la version récursive:")
if v=="rec":
	print(fact_rec(n))
elif v=="seq":
	print(fact_seq(n))
else:
	print("Votre entrée n'est pas conforme, veuillez recommencer depuis le début")
