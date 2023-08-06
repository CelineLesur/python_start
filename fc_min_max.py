# fonction minimum
def min(i,j):
	if i<j:                                      #test de comparaison entre les deux nombres en entrée
  		print("le minimum est",i) 
	else :
  		print("le minimum est",j)
  
# fonction maximum
def max(i,j):
	if i>j:                                     #test de comparaison entre les deux nombres en entrée
  		print("le maximum est",i)
	else :
  		print("le maximum est",j)
  
#interface  
i = int(input("Entrez le premier nombre: "))
j = int(input("Entrez le deuxième nombre: "))
#appel des fonctions min et max
min(i,j)
max(i,j)

