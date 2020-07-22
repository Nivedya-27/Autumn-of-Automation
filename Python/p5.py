def maximise(n,p):
	if max(p)==min(p):
		return 0,p.index(min(p))
	elif p.index(max(p))>p.index(min(p)):
		return max(p)-min(p),p.index(min(p))
	else:
		if p.index(min(p))==n-1:
			return maximise(n-1,p[:-1])
		else:
			if p.index(max(p))==0:
				return maximise(n-1,p[1:])
			else:
				q=p[:p.index(max(p))]
				pr1,jmin=max(p)-min(q),q.index(min(q))
				pr2,kmin=maximise(n-p.index(max(p))-1,p[p.index(max(p))+1:])
				if max(pr1,pr2)==pr1:
					return pr1,jmin
				else:
					return pr2,p.index((p[p.index(max(p))+1:])[kmin])


n=int(input("enter n "))
P=input("enter stocks ")
P=P.split(' ')
P=[int(p) for p in P]
profit,ind=maximise(n,P)
print("max profit:",profit)
print("day:",ind+1)