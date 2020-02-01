

# def is_leap(year):
#     leap = False
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 leap=True
#         else:
#             leap=True
#     return leap

# year = int(input(''))
# print(is_leap(year))


# a=int(raw_input(" "))
# for i in range(1,a+1):
# 	print i,

################################
# a=int(input(" "))
# for i in  range(1,a+1):
# 	print(i,end="")
	
###########################################
# a=[{'rank':1,'age':32,'height':190}
# {'rank':2,'age':35,'height':175},
# {'rank':3,'age':41,'height':188},
# {'rank':4,'age':26,'height':195},
# {'rank':5,'age':24,'height':176}]
# for i in range(len(a)-1):  
# 	for j in range(len(a)-1):
# 		if a[j]['age'] > a[(j+1)]['age']:
# 			a[j],a[j+1]=a[j+1],a[j]
# # print(a)



# ###############################################
# a=input("enter ")
# b="1234567890"
# r=0
# for i in a:
# 	if i in b:
# 		r=r+1
# if len(a)==r:
# 	print("int")
# elif len(a)-1==r and "."in a:
# 	print("float") 
# else:
# 	print("str")

# # ############################				
# a=int(input("enter "))
# for i in range(a):
# 	print(" "*(a-i-1)+"$ "*(i+1))
# for i in range(a-1):
# 	print(" "*(i+1)+"$ "*(a-i-1))

# #########################################		

# a=int(input("enter "))
# for i in range(1,a):
# 	print("$ "*i)
# for i in range( a-1,0,-1):
# 	print("$ "*i)	


	##########################################
# a=int(input("enter "))
# num=1
# for i in range(1,a+1,1):
# 	for j in range(1,i+1,1):
# 		print(num," ",end="")
# 		num=num+1
# 	print()	
# # #########################################
# b=0
# while True:
# 	a=input("if u want to deposit press  D, if u want to withdral press  R ")

# 	if a=="D":
# 		c=int(input("enter the money"))
# 		b=b+c
# 		print(" now ur bank blance",b)
# 	elif a=="R":
# 		d=int(input("enter the money"))
# 		b=b-d
# 		print(" now ur bank blance",b)
# 	elif a=="done":
# 		break
# print(" now ur bank blance",b)
# ##############################################################################
# a=int(input("enter the no of  head s"))
# b=int(input("enter the no of legs"))
# c=0
# d=0
# for i in range(a):
# 	for j in range(b):
# 		if i+j==a:
# 			if (2*i)+(4*j)==b:
# 				print(i,"hens",j,"rabbit")


##################################################
# a=int(input("enter "))
# for i in range(2,a):
# 	if a%i==0:
# 		print("not")
# 		break
# else:
# 	print("prime") 


#################################################################
# a=input("enter  ")
# b=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# if a=="a" or a=="A":
# 	print("A")
# elif a=="e" or a=="E":
# 	print("E")
# elif a=="i" or a=="I":
# 	print("I")
# elif a=="o" or a=="O":
# 	print("O")
# elif a=="u" or a=="U":
# 	print("U")
# elif a=="z" or a=="Z":
# 	print("a")	
# # elif a=="Z":
# # 	print("a")	

# else:	
# 	for i in range(len(b)):
# 		# print(b[i])
#                 print(num1-num," ",end="")
#                 num=num+1
                
#     else:
#         print(num," ",end="")
#         num=num+1
            
#     print()


############################################################

# import requests,json
# from os import p
# 		if b[i]==a:
# 			print(c[i+1])
# 		elif c[i]==a:
# 			print(c[i+1])	
# 5
# 1
# 23
# 654
# 78910
##############################################################
# a=int(input("enter "))
# num=1
# num1=0
# for j in range(1,a+1):
# 	num1=num1+j
# print(num1)	
# for i in range(1,a+1,1):
#     if i>1:
#         if i%2==0:
#             for j in range(1,i+1,1):
#                 print(num," ",end="")
#                 num=num+1
#         else:        
#             for j in range(1,i+1,1):
#                 print(num1-num," ",end="")
#                 num=num+1
                
#     else:
#         print(num," ",end="")
#         num=num+1
            
#     print()


############################################################

# import requests,json
# from os import path
# if path.exists("cours.json"):
# 	with open("cours.json","r") as file:
# 		data=json.load(file)
# 	print("yes")
# else:
# 	b=requests.get("http://saral.navgurukul.org/api/courses")
# 	with open("cours.json","w") as file:
# 		data=json.loads(b.text)
# 		json.dump(data,file)
# 		file.close()
# 	print("no")
# 	with open("courses.json","r") as file:
# 	data=json.load(file)--+++++++++++++++++
# # print(data)
# counter=1
# for i in data['availableCourses']:
# 	print(counter,"" ,i["name"]) 
# 	print(counter,"",i["id"])
# 	counter+=1


# #####################################################
# a=int(input("enter "))
# c=0
# for i in range(a):
# 	b=int(input())
# 	c=c+b
# print(c)	



###################################
# def getFibList(number):
#     fib_list = []
#     key = 1
#     while (key < number + 1):
#         fib_list.append(fib(key))
#         key += 1
#     return fib_list

# print(getFibList(10))


##############################################
# import requests,json
# from os import path
# if path.exists("cours.json"):
# 	with open ("cours .json") as b:
# 		c=json.loads(b)
# 		# c=json.dump(b)
# else:
# 	a=requests.get("http://saral.navgurukul.org/api/courses")
# 	b=a.text
# 	print(b)
# 	with open ("course.json") as b:
# 		c=json.loads(b)
# 		c=json.dump(text,b)
# d=c["availableCourse"]
# for i in range(len(d)):
# 	print(d[i]["id"])



