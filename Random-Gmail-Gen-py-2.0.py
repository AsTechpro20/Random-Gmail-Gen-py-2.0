import random

#main
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "Abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
gmailcom = "@gmail.com"

#adding

string = upper + lower +  number
length = 2

#inputing username
username = input ("Please Enter Your Username: ")

#printing
gmail = "".join(random.sample(string,length))
ready = input ("Are you ready to see your gmail: ")
if ready.lower() == 'no':
    print("Ok")
elif ready.lower() == 'yes':
 print ("Here is you Gmail: "+username+ gmail + gmailcom)
else:
    yesorno = input ("Yes or No: ")
    if yesorno.lower() == 'no':
        print ("ok")
    elif yesorno.lower() =='yes':
        print ("Here is you Gmail: "+ username+ gmail + gmailcom)
    
    