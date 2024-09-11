
#Task #11 -
#Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
# for f in fibonacci_generator():
#     if f > 100 :
#         break
#     print(f, end=" ")

def fib():
    a, b = 0,1
    while True:
        yield a
        a,b = b, a+b
for f in fib():
    if f > 50:
        break
    print(f)

