#Day - 4 , Assignment - 1

#Print the first Armstrong number in the range of 1042000 to 702648265 and exit the loop as soon you encounter the first amstrong number using while loop



for num in range(1042000,702648266):

    count=len(str(num))
    sum=0
    temp=num
        
    
    while temp>0:
        d=temp%10
        sum=sum+d**count
        temp=temp//10

    if num==sum:
        print(num,"is a Amstrong Number")
        break
