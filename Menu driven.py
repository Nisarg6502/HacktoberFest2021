#Write a python program that accepts a string from the user and perform following\n
#string operations -i. Calculate the length of the string
                   #ii. String reversal
                   #iii. Equality check of two strings
                   #iv. Check Palindrome
                   #v. Check substring 

#i. Function to calculate the length of the string
def str_len(str):
    len=0
    for i in str:
        len=len+1
    return len

#ii. Function to find the reverse of the String 
def str_rev(str):
    return str[::-1]

#iii.Function to compare two strings
def str_cmp(str1,str2):
    if(str1==str2):
        return True
    else:
        return False

#iv. Function to Check Palindrome eg, level
def is_palindrome(str):
    rev=str_rev(str)
    if(rev==str):
        return True
    else:
        return False
    
#v. Function to check substring
def is_substr(str1,str2):
    if(str1.find(str2)==-1):
        return -1
    else:
        position=str1.find(str2)
        return position

while(True):
    print("Main menu")
    print("1. Calculate length of string")
    print("2. String reversal")
    print("3. Equality check of two strings")
    print("4. Check for palindrome")
    print("5. Check substring")
    print("6. Exit")
    print("Enter choice")
    choice=int(input())
    if choice==1:
        name=input("Enter your name:")
        print(name)
        print("Length of string:",str_len(name))
        
    elif choice==2:
        str = input("\nEnter the string you wanna reverse: ")
        print("\nThe reversed string is : ", str_rev(str))
        
    elif choice==3:
        str1=input("\nEnter the first string you wanna compare:")
        str2=input("\nEnter the second string you wanna compare:")
        compare= str_cmp(str1,str2)
        print (compare)
        
    elif choice==4:
        str = input("\nEnter a string")
        reverse= is_palindrome(str)
        print (reverse)
        
    elif choice==5:
        str1=input("\nEnter a string:")
        str2=input("\nEnter another string:")
        if(is_substr(str1,str2)<0):
            print("string",str2,"is not a substring of",str1)
        else:
            print("string",str2,"is a substring of",str1)
    else:
        print("exiting")
        break
    
        
        
        
 
