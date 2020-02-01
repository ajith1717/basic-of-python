
# students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
# # for i in students_list:
# # 	print (i)



# marks = [23, 45, 89, 90, 56, 80]
# total=0
# for a in marks:
# 	total+=a
# print(total)


# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# # less_marks=0
# # more_marks=0
# for a in student_marks:
# 	if a<50:
# 		print("50 se bada hai",a)
# 		# less_marks+=1
# 	else:
# 		print("50 se chhota hai",a)
# 		# more_marks+=1
# # print(less_marks)
# # print(more_marks)		


# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# a=0
# for i in numbers:
# 	a=a+1
# # print(a)

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# for i in numbers:
# 	if 20 < i < 40:
# 		print(i)


# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# a=numbers[0]
# for i in numbers:
# 	if a<i:
# 		a=i
# print(a) 


# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# numbers.remove(max(numbers))
# print(max(numbers))


# numbers = [50, 40, 23, 70,88, 56, 12, 5, 10, 7]
# a=max(numbers[0],numbers[1])
# b=min(numbers[0],numbers[1])
# for i in range(len(numbers)):
# 	if numbers[i]>a:
# 		b=a
# 		a=numbers[i]
# 	elif numbers[i]>b:
# 		b=numbers[i]
# print(b)

# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# print(places[:: -1])



# a=0
# b=0
# binary= [1, 0, 0, 1, 1, 0, 1, 1]
# for i in  binary[:: -1]:
# 	a+=(i)*(2**b)
# 	b=b+1
# 	print(a)]



# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# p=len (n)
# l=[]
# for i in range(0, p):
# 	for j in range (i+1,p):
# 		if n[i]+n[j]==number:
# 			l.append([n[i],n[j]])
# print (l)	


# number=50
# n=[10,45,34,16,40,5,30,20,33]
# p=len(n)
# l=[]
# for i in range (0,p):
# 	for j in range (i+1,p):
# 		if n[i]+n[j]==number:
# 			l.append([n[i],n[j]])
# print(l)			



# i = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]
# a=i[0]
# b=i[1]
# c=i[2]
# d=0
# s=0
# for j in range(len(i)): 
# 	s=a[d]+b[d]+c[d]
# 	print (s)
# 	d+=1
# print (sum(i[0]))
# print (sum(i[1]))
# print (sum(i[2]))
# f=a[0]+b[1]+c[2]
# e=a[2]+b[1]+c[0]
# print (f,"\n",e)
################################################################

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36,84]
# # print (len(students))
# # print (len(marks))
# a = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho
# b= 0
# while b < a:
# 	print (students[b] + str(marks[b]))
# 	b=b+1
# print(a)	
########################################################

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# b=0
# c=0
# for a in elements:
# 	if a%2==0:
# 		b=b+1
# 	else:
# 		c+=1
# print(b)
# print(c)
###########################################################
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# b=0
# c=0
# for a in elements:
# 	if a%2==0:
# 		b=b+a
# 	else:
# 		c=c+a
# print(b)
# print(c)		

###################################################
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# b=0
# c=0
# d=0
# e=0
# for a in elements:
# 	if a%2==0:
# 		b=b+a
# 		d=d+1
	# else:
# 		c=c+a
# 		e=e+1	
# print(b//d)
# print(c//e)		
# ###########################################

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# b=0
# c=0
# d=0
# e=0
# for a in elements:
# 	if a%2==0:
# 		b=b+a
# 		d=d+1
# 	else:
# 		c=c+a
# 		e=e+1	
# print(b)
# print(c)
# print(d)
# print(e)
# print(b//d)
# print(c//e)
# print(len(elements))
# print(sum(elements))
# print(sum(elements)//len(elements))		
#######################################################################

# a= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# p=0
# d=0
# e=0
# for i in a:
# 	if i>=10000000:
# 		p+=1
# 	elif i>=100000:
# 		d+=1
# # else:
# # 	e+=1
# # 
# print(" ".join(p))crorepati hai")
# # print(d,"lackpati hai")
# # print(e,"diwaliya")

# # # ##############################################################################################3
# list1 = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# p=[]
# l=[]
# for i in list1:
# 	if i not in p:
# 		p.append(i)
# # print(p)
# for j in p:
# 	r=0
# 	for b in list1:
# 		if j==b:
# 			r+=1
# 	# print(j,r)
# 	l.append([(j,r)])
# print(l)	




# list1 = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# p=[]
# for i in list1:
# 	a=0
# 	for j in list1:
# 		if i==j:
# 			a+=1
# 	if (a>1) and [i,a] not in p:
# 		p.append([i,a])
# print(p)	

# # # # ##############################################################################################33

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# p=len(n)
# l=[]
# q=[]
# for i in n:
# 	if i not in l:
# 		l.append(i)
# l.sort()		
# print(l)
# for j in l:
# 	r=0
# 	for a in n:
# 		if j==a:
# 			r=r+1
# 	q.append([j,r])
# print(q)			
	

# ##########################################################
# # m = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# # s = "over"
# # a=m.replace(s,"")
# # print(a)

###################################################################
# m = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# s="over"
# p=m.split()
# for i in range (len(p)):
# 	if i==s:
# 		p.remove(s)
# print(" ".join(p))
########################################################################
# import pyttsx3
# engine = pyttsx3.init( )
# engine.setProperty("volume",1.0)
# engigne.setProperty("rate",100)
# user=input(" ")
# engine.say (user)
# engine.runAndWait


# # ############################################################################
# c=input("enter the name  ")
# print("hi "+c)
# print("welcome to KBC game   ")

# list1 = [
# 	"How many continents are there?",  			
# 	"What is the capital of India?",		
# 	"NG mei kaun se course padhaya jaata hai?"	
# ]
# print(" ")

# list2 = [
# 	["1.Four", "2.Nine", "3.Seven", "4.Eight"],
# 	["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
# 	["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]
# ]
# print(" ")
# sol= [3, 4, 1]
# help=[(3,1),(1,4),(1,3)]

# k=0
# n=0
# for i in list1:
# 	print(i)
# 	for j in list2[k]:
# 		print(j)
# 	if n==0:	
# 		s=input("if u need help line,yes or no")
# 		if s=="yes":
# 			n=n+1
# 			z=help[k] 
# 			print(z)
# 	b=int(input("enter the num"))
# 	if b<=4:
# 		if b==sol[k]:
# 			print("correct")
# 		else:
# 			print("wrong")
# 			break
# 		k=k+1
# 	else:
# 		print("option is wrong")	
# 		break

# ####################################################################
# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
# total_marks = 0
# counter = 0
# while counter < len(marks):
# 	total_marks = total_marks + marks[counter]
# 	counter = counter + 1

############
# thisset = {"apple", "banana", "cherry"}

# print("banana" not in thisset)
 

# thisset = {"apple", "banana", "cherry"}
# thisset.update(("1", "mango", "grapes"))

# print(thisset)



# thisset = {"bana", "banana", "cherry"}
# thisset.add(["orange", "go", "grapes"])

# print(thisset)



# thisset = {"1", "2", "3"}

# thisset.clear()

# print(thisset)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z=x.difference(y) 

# print(z)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.difference_update(y) 

# print(x)



# thisset = {"apple", "banana", "cherry"}

# x = thisset.pop()

# print(x)

# print(thisset)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "facebook"}

# z = x.isjoint(y) 

# print(z)


#  a = [2,312,123,3,12,23,12,12]
# # largest = a[0]
# i = 0
# for i in range(len(a)):
#   if a[i]>largest:
#     largest = a[i]
#   i = i+1
# print (largest)
# #similarly find smallest									

# #################################################################
# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)



# x = {"apple", "banana", "cherry"}
# y = {"go", "micrft", "apple"}

# z = x.symmetric_difference(y) 

# print(z)
#########################################################################
# 