#creating function for sum of arthmetic progression
def sumOfAP( a, d,n) :
    sum1 = 0
    i = 0
    while i < n :  #Conditions and limits.
        sum1 = sum1 + a
        a = a + d
        i = i + 1
    return sum1

#User can try different inputs as long as he want.
run="yes"
while run == "yes":
    n = eval(input("Enter the no of terms in series :"))
    a = eval(input("Enter the first term of series :"))
    d = eval(input("Enter the common difference of series :"))
    print ("Sum of Arthmetic Progression is : ",sumOfAP(a, d, n))
    run = input("Do u wish to continue?")
else:
    print ('end')
