"""created by Hadise Mirzaei"""


def fibonacci(n):
    if n <= 0:
        return "!!!!!!!! ENTER A normal NUMBER"
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


user_int = int(input("Enter"))
print(fibonacci(user_int))
