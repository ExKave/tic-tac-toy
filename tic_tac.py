
l=[1,2,3,4,5,6,7,8,9]
def dis(a):
    j=0
    for i in a:
        print(" ",i," ",end="")
        j+=1
        if j%3==0:
            print()
            
    print()
def check(b):
    cond1=(l[0]==l[1] and l[1]==l[2]) or (l[3]==l[4] and l[3]==l[5]) or (l[6]==l[7] and l[7]==l[8])
    cond2=(l[0]==l[3] and l[3]==l[6]) or (l[1]==l[4] and l[4]==l[7]) or (l[2]==l[5] and l[5]==l[8])
    cond3=(l[0]==l[4] and l[4]==l[8]) or (l[2]==l[4] and l[2]==l[6])
    
    if ((cond1) or (cond2) or (cond3)):
        return True
        
    s=""
    for i in l:
    	h=str(i)
    	s+=h
    if s.isalpha():
    	global m
    	m=5
    	return True
	
sym=["X","O"]
m=0
dis(l)
player1=input("Enter the name of player 1(X):  ")
player2=input("Enter the name of player 2(O):  ")
player=[player1,player2]

while True:
    print("time for ",player[m])
    ps=int(input("enter the position:"))
    if ps not in l:
        continue
    l[ps-1]=sym[m]
    dis(l)
    r=check(sym[m])
    if r:
       break
    m=(m+1)%2

print("Game Over")
if m==5:
	print("game draw")	 
else:
	print("the winner is......")
	print(player[m])
'''	import time
	time.sleep(4)
	print("bhakti because he is game creator and you are not enough good to play with him !!!")'''
