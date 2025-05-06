#problem - findin the nth fibonocci number
def nth_fibonocci_number(n):
    fibonocci = []
    fibonocci.append(0) #initiatin the list's index 0 and 1 as 0 and 1 respectively
    fibonocci.append(1)
    
    for i in range(2,n):
       fibonocci.append(fibonocci[i-1] + fibonocci[i-2])
        
    return fibonocci[n-1]

def nth_fibonocci_number_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return nth_fibonocci_number_recursion(n-1) + nth_fibonocci_number_recursion(n-2)

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    print(nth_fibonocci_number(n))
    
    print("The entire series till n is:")
    for i in range(n):
        print(nth_fibonocci_number_recursion(i))