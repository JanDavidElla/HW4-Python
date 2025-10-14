def my_steps(n):
    if n > 25 or n < 1: #checks if input is within range
        raise ValueError("Input is not within range")
    if n == 1: #base cases when n is 1 or 2
        return 1
    if n == 2:
        return 2
    numWays = [0] * (n + 1) #creates a list of size n+1, where all values are 0
    numWays[1] = 1 #second num is 1
    numWays[2] = 2 #third num is 2
    print(numWays)
    for i in range(3, n + 1): #starts on the fourth num, uses Fibonacci sequence to calculate next num
        numWays[i] = numWays[i - 1] + numWays[i - 2]
    return numWays[n] #returns last num in list



