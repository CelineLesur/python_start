#chercher motif dans un texte

texte="AACTGGCTGCTATTGACGCTA" #texte dans lequel chercher le motif
motif="GCT"                   # motif à trouver

n=len(texte)-len(motif)+1
liste=[]
ind_t=0

while ind_t<n:
	ind_m=0
	while ind_m<len(motif) and motif[ind_m]==texte[ind_t+ind_m]:
		ind_m=ind_m+1
	if ind_m==len(motif):
		liste.append(ind_t)
	ind_t=ind_t+1



print(" le motif est trouvé aux positions :",liste)
