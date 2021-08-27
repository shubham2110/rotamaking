import copy

shiftslist=["O","E","N", "M"]
days=7
people=6
exception=4

sundaynight=True
# fillplan
#input previous

def filter1(new1, i, j):
        if i > 2 : # Eliminate items which are having more than 3 shifts of same kind 
                for o in range(i):
                        ENM={"E":0, "N":0, "M":0, "O":0}
                        for p in range(j):
                                ENM[new1[o][p]]+=1
                        if 4 in sorted(ENM.values()): 
                                return False
        

        if new1[i].count("O") > 1:
                return False

        if new1[i].count("E") > 4 :
                if i == exception:
                        pass
                else:
                        return False

        if new1[i].count("N") > 2:
                return False
        if  new1[i].count("M") > 2:
                if i == exception:
                        pass
                else:
                        return False
        #print(new1)

        if new1[i][j] == "O" and j > 0 and (new1[i][j-1]  == "N"):
                return False
        if new1[i][j] == "N" and j > 0 and (new1[i][j-1]  == "N"):
                return False
        if new1[i][j] == "E" and j > 0 and (new1[i][j-1]  == "N"):
                return False
        if new1[i][j] == "M" and j > 0 and (not new1[i][j-1]  == "N"):
                if i == exception:
                        pass
                else:
                        return False        

        li=[]
        for p in range(days):
                li.append(0)

        for k in range(i+1):
                if new1[k].count("O"):
                        li[new1[k].index("O")]+=1
                elif j== people-1: # Making sure atleast one off
                        return False

                if new1[k].count("O") and not new1[k].index("O") == k:
                        return False

                        #print(k, new1, li)
        if li.count(2): # atmost 1 off
                return False

        if j == days-1 and new1[i][0] == "M" and not new1[i][j] == "N":
                if i == exception:
                        pass
                else:
                        return False
        if j == days-1 and new1[i][0] == "N" and  new1[i][j] == "N":
                return False
        if j == days-1 and new1[i][0] == "O" and  new1[i][j] == "N":
                return False
        if j == days-1 and new1[i][0] == "E" and  new1[i][j] == "N":
                return False

        return True


previous=[]
for each in range(people):
        pre=""
        #for eac in range(days):
        #       pre.append("")
        previous.append(pre)
#previous=[[""  ] * days ] * people
p=[previous, ]
newp=p
for i in range(people):
        for j in range(days):
                p=newp
                newp=[]
                for e in p:
                        for shift in shiftslist:
                                if sundaynight and i==exception and j==5 and not shift == "N": continue # optimization for night shift on sunday
                                new1=copy.deepcopy(e)
                                new1[i]+=shift
                                if filter1(new1, i, j):
                                        newp.append(new1)


#for e in newp : print(e)

import sys
#sys.exit()
import pickle
a=pickle.dumps(newp)

f=open("sundaynight.txt","wb")
f.write(a)
f.close()
