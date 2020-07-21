def next_palindrome(p):
	if len(str(p))==1:
		if p<9:
			return p+1
		else:
			return p+2
	elif len(str(p))==2:
		if p<99:
			return p+11
		else:
			return p+2
	elif len(str(p))>2:
		ps=int(str(p)[1:-1])
		if len(str(next_palindrome(ps)))==len(str(ps)):
			return int(str(p)[0]+str(next_palindrome(ps))+str(p)[-1])
		elif len(str(next_palindrome(ps)))>len(str(ps)):
			if int(str(p)[0])<9:
				pp=''
				for i in range(len(str(ps))):
					pp=pp+str(0)
				return int(str(p)[0]+pp+str(p)[-1])+int(str(1)+pp+str(1))
			elif int(str(p)[0])==9:
				return p+2

n=int(input("enter palindrome: "))
print(next_palindrome(n))