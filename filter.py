f=open("sundaynightfridayevening.txt","rb")
import pickle
l=pickle.loads(f.read())

def rotafilter(rota):
	# atmost 2 people with 2 night
	
	count=0
	for i in range(len(rota)):
		if rota[i].count("N") > 2 :
			return False
		elif rota[i].count("N")==2:
			count+=1
	if count > 2 : return False
			
	

	t=1
	for j in range(len(rota[0])):
		ENM={"E":0 , "N":0, "M":0, "O":0}
		for i in range(len(rota)):
			ENM[rota[i][j]]+=1
		if ENM["E"] > 0 and ENM["N"] > 0 and ENM["M"] > 0  :
			t*=1
		else:
		#	print(ENM, rota, i, j)
			t*=0
		
	return t
			


k=list(filter(rotafilter, l))

for i in k: print(i)
	
