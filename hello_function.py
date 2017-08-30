# hello_function.py

def hello_world(n):
    count = 0
    while count < n:
        count += 1
        print("Hello")
    return


number = int(input(" Give me a number: "))
hello_world(number)
