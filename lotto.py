import random
sorsoltszamok=[]
while len(sorsoltszamok)<5:
	kihuzott=random.randrange(1,91)
	if kihuzott not in sorsoltszamok:
		sorsoltszamok.append(kihuzott)
print(sorsoltszamok)
		

