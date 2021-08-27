import copy

shiftslist=["E","N", "M", "O"]
days=7
people=4


# fillplan
#input previous

def filter1(new1, i, j):



        if new1[i].count("O") > 1:
                return False
        if new1[i].count("E") > 3:
                return False
        if new1[i].count("N") > 3:
                return False
        if new1[i].count("M") > 3:
                return False
        #print(new1)
        if new1[i][j] == "O" and j > 0 and (new1[i][j-1]  == "N"):
                return False
        if new1[i][j] == "N" and j > 0 and (new1[i][j-1]  == "N"):
                return False
        if new1[i][j] == "E" and j > 0 and (new1[i][j-1]  == "N"):
                return False
        if new1[i][j] == "M" and j > 0 and (not new1[i][j-1]  == "N"):
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
        if li.count(2):
                return False

        if j == people-1 and new1[i][0] == "M" and not new1[i][j] == "N":
                return False
        if j == people-1 and new1[i][0] == "N" and  new1[i][j] == "N":
                return False
        if j == people-1 and new1[i][0] == "O" and  new1[i][j] == "N":
                return False
        if j == people-1 and new1[i][0] == "E" and  new1[i][j] == "N":
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
                p=copy.deepcopy(newp)
                newp=[]
                for e in p:
                        for shift in shiftslist:
                                new1=copy.deepcopy(e)
                                new1[i]+=shift
                                if filter1(new1, i, j):
                                        newp.append(new1)

for e in newp:  print(e)
