from random import randint
import os
n=int(input("N="))

###
e=[]
with open("test.py",'r') as f:
	s=f.readlines()
	for line in s:
		if("###" in line):
			break
		if 'n=int' in line:
			i=0
			e.append(f'n={n}\n')
			while(i<n):
				e.append(f'r{i}={randint(0,9)}\n')
				i+=1
		else:
			e.append(line)
for i in range(n):
	e.append(f"print(r{i})\n")
with open("test.py",'w') as f:
	f.writelines(e)
os.system("python C:\\Users\\Pink\\OneDrive\\Documents\\test\\test.py ")