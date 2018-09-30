import pandas as pd

s1 = "_"+"sunday"
s2 = "_"+"saturday"

m = []

print len(s1),len(s2)

for i in range(len(s1)):
	row = []
	for j in range(len(s2)):
		if i == 0 and j == 0:
			row.append(0)
		elif j == 0:
			row.append(i)
		elif i == 0:
			row.append(j)
		else:
			row.append(-1)
	m.append(row)	

for i in range(1,len(s1)):
	row = []
	for j in range(1,len(s2)):

		if s1[i] == s2[j]:
			summ = 0
		else:
			summ = 1
		m[i][j] = min((m[i-1][j-1]+ summ),m[i-1][j]+1,m[i][j-1]+1)

print pd.DataFrame(m)