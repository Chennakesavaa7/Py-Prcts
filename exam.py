salary = 8000
def printSalary():
	salary = 12000
	print("Salary:",salary)

printSalary()
print("Salary:", salary)

# var1 = 1
# var2 = 2
# var3 = "3"
# print(var1+var2+var3)

# l = ["jon","kie"]
# l.append(2,"scott")
# print(l)
#n=input(45)
#print(n)
# #print(type(n))
# n= int(input(33))
# print(n)
# print(type(n))

s = "james bond"

print(s[2::-1])

def calculate(num1, num2= 4):
	res = num1*num2
	print(res)

calculate(5,6)

# d = {"kir", "kkk", "jjj"}
# d.add(1,"kjhih")
# print(d)

p,q,r = 10,20,30
print(p,q,r)

# for x in range(0.5,5.5,0.5):
# 	print(x)

print("\n")

s = "pynative"
print(s[2::1])
print(s[4::1])
def char(word,n):
	x = word[n:]
	return x
print(char("pynative", 4))
print(char("pynative", 4))

l = [10,20.2,30,10]
def frst_last_same(numberslist):
	frst = l[0]
	last = l[-1]
	if frst == last:
		return True
	else:
		return False
print("result is", frst_last_same(l))

l = [10,20,33,46,55]
for i in l:
	if i%5 == 0:
		print(i)

s = "emma is a good developer. emma is a writer"

print(s.count("emma"))

def count_name(s):
	count= 0
	for i in range(len(s)-1):
		count += s[i:i + 4] == "emma"
	return count

count = count_name(s)
print(count)

rows = 5
for i in range(1, rows+1):
	for j in range(1, i+1):
		print(i, end = " ")
	print("\n")


for i in range(1, 6):
	for j in range(1, i+1):
		print(i, end = " ")
	print("\n")

a = 121
def palindrome(a):
	original_num = a
	reverse_num = 0
	while a >0:
		reminder = a% 10
		reverse_num = (reverse_num*10)+ reminder
		a = a//10
	if original_num == reverse_num:
		print("given no. is a palindrome")
	else:
		print("xxxx")
print(palindrome(a))

l1 = [10,20,25,30,35]
l2 = [40,45,60,75,90]
def merg_list(l1,l2):
	l3 = []
	for i in l1:
		if i%2 != 0:
			l3.append(i)
	for i in l2:
		if i%2 == 0:
			l3.append(i)
	return l3
print("l3 :", merg_list(l1,l2))

a = 1256
print("given no.", a)
while a >0:
	x = a % 10
	a = a // 10
	print(x ,end= " ")
print("\n")
a = 45000
tax = 0
print("given income", a)
if a <= 10000:
	tax = 0
elif a <= 20000:
	x = a -10000
	tax = x*10/100
else:
	tax = 0
	tax = 10000*10/100
	tax += (a -20000)*20/100
print(tax)

for i in range(1,11):
	for j in range(1,11):
		print(i*j, end =" ")
	print("\t\t")

for i in range(6,0,-1):
	for j in range(0,i-1):
		print("*", end = " ")
	print(" ")



