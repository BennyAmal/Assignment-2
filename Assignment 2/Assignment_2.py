

def numberofdigits(nmbr):                #defining funtion

    digits = 0                             # setting a variable digits and assign the value to 0
    while nmbr > 0:    
         digits=digits+1
         nmbr=nmbr//10        

    print("Number of digits:", digits)

print("this is a program to count the number of digits in a given number")
a=int(input("enter your number"))              # recieving an input from user and assign the same to an integer variable named a
numberofdigits(a)                               # invoking the funtion and passing the input recieved to funtiom
