d=int(input("enter d"))
n=''
max=''
for i in range(d):
	if i==0:
		n=n+str(1)
	else   :
		n=n+str(0)
	max=max+str(9)
n=int(n)+1 #smallest odd no. with d digits if d>1 or 2 if d==1
max=int(max) #largest no. with d digits
def check_prime(m_odd): #returns truth value of an odd no. or of 2 being prime
	if m_odd==2:return True
	i=3
	while m_odd%i!=0 and i<m_odd:
		i=i+2
	return i==m_odd

l=[] #list of prime no.s of d digits
while n<=max:
	if check_prime(n):
		l.append(n)
		if n==2:
			n=n+1
			continue
	if n>2:
		n=n+2
print(l)
d=[] #list of tuples with consecutive difference 2
for i in range(len(l)-1):
	if (l[i+1]-l[i]==2):
		d.append((l[i],l[i+1]))
f=open('myFirstFile.txt','w')
for i in range(len(d)):
	f.write(str(d[i][0])+' '+str(d[i][1])+"\n")
f.close()
