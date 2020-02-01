# a=1
# while a<=100:
# 	if a%5==0 and a%6==0:
# 		print ("ajith subramaniam")
# 	elif a%5==0:
# 		print ("ajith")
# 	elif a%6==0:
# 		print ("subramaniam")
# 	else:
# 		print(a)
# 	a=a+1		




# a=1
# while a<100:
# 	if a%5!=0:
# 		print("ajith")
# 	else:
# 		print(a)	
# 	a=a+1

# a=int (input("enter the num"))
# b=2
# while a>b:
# 	if a%b==0:
# 		print ("its not prime num")
# 	b=b+1
# else:
# 	print ("its prime num")	


# a=2
# while a<100:
# 	b=2
# 	while a>b:
# 		if a%b==0:
# 			break
# 		b=b+1
# 	else:
# 		print(a)
# 	a=a+1	
	
	

# a=int(input("how many num want to multiply?"))
# b=1
# c=1
# while b<=a:
# 	d=int(input("enter the num "))
# 	c=c*d
# 	b=b+1
# print (c)


# a=int(input("how many num want to subtract?"))
# b=1
# c=0
# while b<=a:
# 	d=int(input("enter the num "))
# 	c=d-c
# 	b=b+1
# 	print 



# a=100
# b=3
# while a>0:
# 	print (a)
# 	print(-b)
# 	a=a-3
# 	b=b+3


# a=0
# c=int(input("enter the num"))
# while a<c:
# 	b=int(raw_input("enter any integer"))
# 	if b==c:
# 		print("you entered correct value")
# 		break
# 	elif b>c:
# 		print("your value is grater than the expected value")
# 	else :
# 		print("you entered value is less than expected value")
# 	a+=1


# a=1
# while a>0:
# 	name=raw_input("Student name")
# 	e=int(raw_input("english marks>>"))
# 	t=int(raw_input("Tamil marks>>"))
# 	m=int(raw_input("maths marks>>"))
# 	s=int(raw_input("science marks>>"))
# 	ss=int(raw_input("social science marks>>"))
# 	total=e+t+m+s+ss
# 	print(name," is ",total," marks")
# 	a=a-1
# 	b=raw_input("do u want for another student yes or no")
# 	if b=="yes":
# 		a=1

# a=1
# while a>0:
# 	name =raw_input("student name ")
# 	total=int(raw_input("enter his total marks"))
# 	subjects=int(raw_input("enter his total subjects"))
# 	percentage=total/subjects
# 	print(" total percentage =",percentage,"%")
# 	a=a-1
# 	if 33 <percentage <= 60:
# 		print (" 2nd rank")
# 	elif percentage > 60:
# 	 	print ("1st rank")
# 	else:
# 		print("fail")
# 	b=raw_input("do u want for another student yes or no")
# 	if b=="yes":
# 		a=1



# b=input("enter any number")
# a=b[:: -1]
# if a == b:
# 	print ("palindrome")
# else:
# 	print("not")




# a=int(input("enter the marks"))
# b=int(input("enter the marks"))
# c=int(input("enter the marks"))
# d=int(input("enter the marks"))
# e=int(input("enter the marks"))
# marks=[a,b,c,d,e]
# a=0
# b=0
# while a<len(marks):
# 	b=b+marks[a]
# 	a=a+1
# print("total marks of the student is")
# print(b)
# s=input("do u want for another student yes or no")
# if s=="yes":
# 		a=1 





# import getpass
# a=getpass.getpass("enter your password")
# if a=="AJITH":
# 	print("congrats")
# else:
# 	print("invalid password")



# a=int(input("enter the num"))
# b=[]
# c=0
# d=0
# e=0
# total_input =a
# while a>0:
# 	s=int(input("enter the number"))
# 	if (s== 0 or s==1):
# 		b.append (s)
# 	a=a-1
# if (len(b)) == total_input:
# 	for i in b[:: -1]:
# 		c=(i)*(2**d)
# 		d=d+1
# 		e=c+e
# # 	print (e)
# else:
# 	print ("numbers are not binary")	


# # # number=50
# # # n=[10,45,34,16,40,5,30,20,33]
# # # p=len(n)
# # l=[]
# # for i in range (0,p):
# # 	for j in range (i+1,p):
# # 		if n[i]+n[j]==number:
# # 			l.append([n[i],n[j]])
# # print(l)	




# # i=[[12,12,1,2,12],[23,23,23,54],[23,45,67]]
# for a in i:
# 	c=0
# 	s=0
# 	d=len(a)
# 	for b in a:
# 		s+=b
# 		c=s/d
# 	print (c)
##############################################
# b=10
# for a in range(1,20,2):
# 	print (" "*b,"$"*a,end=" ")
# 	b=b-1
# 	print (" ")
# a=1
# for b in range (19,0,-2):
# 	print (" "*a,"$"*b,end=" ")
# 	a=a+1
# 	print(" ")	

# #########################################################################
# while True: 
# 	c=input("enter the name  ")
# 	print("hi "+c)
# 	print("welcome to KBC game   ")

# 	list1 = [
# 		"How many continents are there?",  			
# 		"What is the capital of India?",		
# 		"NG mei kaun se course padhaya jaata hai?"	
# 	]
# 	print(" ")

# 	list2 = [
# 		["1.Four", "2.Nine", "3.Seven", "4.Eight"],
# 		["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
# 		["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]
# 	]
# 	print(" ")
# 	sol= [3, 4, 1]
# 	help=[(3,1),(1,4),(1,3)]
# 	k=0
# 	n=0
# 	for i in list1:
# 		print(i)
# 		for j in list2[k]:
# 			print(j)
# 		if n==0:	
# 			s=input("if u need help line,yes or no")
# 			if s=="yes":
# 				n=n+1
# 				z=help[k] 
# 				print(z)
# 		b=int(input("enter the num"))
# 		if b<=4:
# 			if b==sol[k]:
# 				print("correct")
# 			else:
# 				print("wrong")
# 				break
# 			k=k+1
# 		else:
# 			print("option is wrong")	
# 			break
# 	h=input("do u need another chance,yes or no")
# 	if h=="no":
# 		break



# # # ############################################################
# list1 = ["a", "n", "t", "a", "a", "t", "n", "n","a","a","n" "a", "x", "u", "g", "a", "x", "a"]
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
# ###############################################
# for row in range(6):
# 	for col in range(7):
# 		if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row - col==2) or (row + col==8):
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()		

# ###########################################################
# # import calendar 

# # y=int(input("year"))
# # m=int(input("month"))
# print(calendar.month(y,m)) 

#############################################################
# a=[]
# b=[]
# c=[]
# d=[a,b,c]
# user=int(input("enter the number of element in  list"))
# for i in range(user):
# 	m=int(input("enter the element"))
# 	a.append(m)
# user1=int(input("enter the  number of element list"))
# for i in range(user1):
# 	m=int(input("enter the element"))
# 	b.append(m)
# user2=int(input("enter the  number of  element in the list"))
# for i in range(user2):
# 	m=int(input("enter the element"))
# 	c.append(m)
# print(d)
# if len(a)==len(b)==len(c):
# 	for j in range(len(a)):             
# 		s=a[j]+b[j]+c[j]
# 		print(s)
# 	print(sum(a))
# 	print(sum(b))
# 	print(sum(c))
# 	f=a[0]+b[1]+c[2]
# 	e=a[2]+b[1]+c[0]
# 	print (f,"\n",e)
# 	print( sum(a)==sum(b)==sum(c) and s==e==f)
# 	if sum(a)==sum(b)==sum(c) and s==f==e:
# 		print("magic square")
# 	else:
# 		print("not a magic square")
# else:
# 	print("not a square")	

# ############################################################

# def rec():
# 	length=int(input("enter the num"))
# 	breadth=int(input("enter the num"))
# 	area=length*breadth
# 	print("area=",area)
# 	perimeter=2*(length+breadth)
# 	print("perimeter=",perimeter)
# rec()	

# ############################################################
# for i in range(0,100,2):
# 	print(i)
# for j in range(1,101,2):
# 	print(j)
####################################################
# def factorial():
# 	b=1
# 	a=int(input("enter the num"))
# 	for i in range(1,a+1):
# 		b=b*i
# 		print(b)
# factorial()	
# ########################################################################
# a=input("enter the num")
# d=int(a)
# b=list(a)
# print(b)
# c=0
# for i in a:
# 	c+=int(i)
# print(c)
# if d%c==0:
# 	print("harashad no")
# else:
# 	print("not ")
# ############################################################################
# def facebook():
# 	print(".................CREATE FACEBOOK ACCOUNT.........")
# 	n=input("enter the name : ")
# 	a=int(input("enter the age: "))
# 	d=input("enter DOB:")
# 	j=int(input("enter the phone number:"))
# 	b=input("enter the E mail : ")
# 	print("welcome to FACEBOOK",n)
# 	c=["name","age","date of birth","phone no","e mail"]
# 	e=[n,a,d,j,b]
# 	for i in range(len(c)):
# 		print(c[i]," /",e[i])
# 	import getpass
# 	a=True
# 	while a:
# 		z=getpass.getpass("enter the pass_word and your passwordmust have 1,2,3,4,5,@,A,Z and ur wish")
# 		if (6<len(z)<20) and ("@" in z):
# 			if ("2" in z or "1" in z or "3" in z or "4" in z or "5" in z) and ("A" or "Z" in z):
# 				while True:
# 					w=getpass.getpass("enter the confirm password")
# 					if w==z:
# 						print("congrats",n,"welcome to FACEBOOK")
# 						print("..............FB................")
# 						for row in range(7):
# 							for col in range(9):
# 								if (row==0 and col!=4) or (row==3 and col%4!=0) or (col==0 or col==5 or col==8) or (row==6 and col==6) or (row==6 and col==7):
# 									print("@",end=" ")	

# 								else:
# 									print(" ",end=" ")
# 							print(" ")	

# 						a=False
# 						break
# 					else:
# 						print("your confirm password is wrong")
# 			else:
# 				print("add number and capital letter")
# 		else:
# 			print("make the password strong")	
# 			# if h=="ok":
# facebook()



###############################################################################
# for row in range(7):
# 	for col in range(9):
# 		if (row==0 and col!=4) or (row==3 and col%4!=0) or (col==0 or col==5 or col==8) or (row==6 and col==6) or (row==6 and col==7):
# 			print("@",end=" ")	

# 		else:
# 			print(" ",end=" ")
# 	print(" ")	

# for row in range(7):
# 	for col in range(4):
# 		if (row==0 or col==0) or (row==3) or (col==3) or (row==6):
# 			print("@",end=" ")	

# 		else:
# 			print(" ",end=" ")
# 	print(" ")	


# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#         return "Mutton Chaap"
#     else:
#         return "Chole Bhature"

#     # print ("Kya main print ho payungi? :-")

# mon_menu = menu("monday")
# print (mon_menu)
# tues_menu = menu("tuesday")
# print (tues_menu)
# fri_menu = menu("friday")
# print (fri_menu)



# b=input("enter ") 	
# a=b[:: -1]
# if a== b:
# 	print ("palindrome")
# else:
# 	print("not")

# b=input("enter ") 	
# a=b[:: -1]
# print ("palindrome") if a== b else print("not")
	


# num="htriuyxgdfiutiucfdshcnmvfyurthc"
# c=0
# d=0
# # for i in num:
# # 	if i=="u":
# # 		c=c+1
# # print(c)
# while c<len(num):
# 	if "u" in num:
# 		d+=1
# 	c=c+1
# print(d)

# def calculator():
# 	a=input("what u want to calculate?")
# 	num1=int(input(" "))
# 	num2=int(input(" "))

# 	if a=="add":
# 		return (num1+num2)
# 	if a=="sub":
# 		return (num1-num2)
# 	if a=="multiply":
# 		return (num1*num2)
# 	if a=="divide":
# 		return (num1/num2)


# print (calculator())

#################################################################
# from random import randint

# def win():
#     print 'You win!'

# def lose():
#     print 'You lose!'

# while True:
#     player_choice = raw_input('What do you pick? (rock, paper, scissors)')
#     random_move = randint(0, 2)
#     option = ['rock', 'paper', 'scissors']
#     computer_choice = option[random_move]

#     if player_choice == computer_choice:
#         print 'Draw!'
#     elif player_choice == 'rock' and computer_choice == 'scissors':
#         win()
#     elif  player_choice == 'paper' and computer_choice == 'scissors':
#         lose()
#     elif player_choice == 'scissors' and computer_choice == 'paper':
#         win()
#     elif player_choice == 'scissors' and computer_choice == 'rock':
#         lose()
#     elif player_choice == 'paper' and computer_choice == 'rock':
#         win()
#     elif player_choice =='rock'  and computer_choice =='paper':
#         lose()
#     again = raw_input('Do you want to play again? (y or n)')
#     if again == 'n':
#         break

##################################################################

# chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

# # encrypt_message function defined here but not called
# def encrypt_message(plain_msg):
# # this fucnction takes "plain_msg" as an argument and print/return the encrypted message. The "plain_msg" is tranfered into "encrypted_msg" using "shifted_chars" list. Example, if plain_msg = "ng" then n => p, g => i  and hence encrypted_msg = "pi"
#     encrypted_msg = ""
#     for character in plain_msg:
#       # for character in msg
#         if character in chars:
#             char_index = chars.index(character)
#             new_char = shifted_chars[char_index]
#             encrypted_msg = encrypted_msg + new_char

#         else:
#             encrypted_msg = encrypted_msg + character
#     print encrypted_msg

# def decrypt_message(encrypted_msg):
# # this fucnction takes "encrypted_msg" as an argument and print/return the encrypted message. The "encrypted_msg" is tranfered into "decrypted_msg" using "shifted_chars" list. Example, if encrypted_msg = "pi" then p => n, i => g  and hence decrypted_msg = "ng"
#     decrypted_msg = ""
#     for character in encrypted_msg:
#         if character in shifted_chars:
#             char_index = shifted_chars.index(character)
#             new_char = chars[char_index]
#             decrypted_msg = decrypted_msg + new_char
#         else:
#             decrypted_msg = decrypted_msg + character
#     print(decrypted_msg)

# # methods should return or print the new messages.
# ############################################### Code starts from here ##################################################
# flag = True
# while flag == True:
# 	choice = raw_input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
# 	if choice == 'e':
# 	    plain_message = raw_input("Enter message to encrypt??")
# 	    encrypt_message(plain_message)

# 	elif choice == 'd':
# 		encrypted_msg = raw_input("Enter message to decrypt?")
# 		decrypt_message(encrypted_msg)
# 	else:
# 	    play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N)")
# 	    if play_again == 'Y':
# 	        continue
# 	    elif play_again == 'N':
# 	        break


##########################################################