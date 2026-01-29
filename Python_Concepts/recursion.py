# Iterative


# def walk(steps):
#     for step in range(1,steps+1):
#         print(f"You take {step}")
        
# walk(99)


#Recursive

# def walk(steps):
#     if steps == 0:
#         return
#     walk(steps-1)
#     print(f"You have taken {steps}")
    
# walk(45)


# Finding the factorial

def factorial(n):
    result = 1
    for i in range(1,n + 1):
        result = result * i
    return result
print(factorial(5))


# recursive

def findfact(n):
    if n == 1:
        return 1
    return n * findfact(n-1)

print(findfact(5))



# 1 to 10 iteratively

# def get_n(n):
#     for i in range(n+1):
#         print(i)
        
# get_n(10)


# using recursion

def rec_get_n(n):
    #base condition
   if n >= 9:
       return n + 1
   
   total = n + 1
   print(total)
   
   return rec_get_n(total)

newTotal = rec_get_n(0)

