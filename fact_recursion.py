number = int(input('Enter a number: '))
def fact(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fact(num-1)

print(f'Factorial of {number} is {fact(number)}')