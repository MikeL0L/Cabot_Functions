def smallest_factor(num):
    for num2 in range(2, 10):
        if num % num2 == 0:
            return num2

def primes_in_range(num1, num2):
    primes = []
    for num in range(num1, num2 + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

while True:
    print('----------------------------------')
    print("Options:")
    print("[1] Find the smallest factor")
    print("[2] Find prime numbers in a range")
    print("[0] Exit the Program")

    option = input("Enter your choice: ")

    if option == '1':
        num = eval(input('Enter a Number >= 2: '))
        if num < 2:
            print("Invalid input, Enter a number greater than 2\n")
            continue

        smallest_factor = smallest_factor(num)
        if smallest_factor:
            print("Smallest factor other than 1 for" , num, 'is', smallest_factor); print()
        else:
            print('Error!\n')

    elif option == '2':
        start = int(input('Enter a Number [start range]: '))
        if start < 0:
            print("Enter a non-negative number.\n")
            continue

        end = int(input('Enter a Number [end range]: '))
        if end <= start:
            print("Invalid input. End range should be greater than start range.\n")
            continue

        prime = primes_in_range(start, end)
        print("Prime numbers between the range", start, 'and', end, 'are:', prime); print()

    elif option == '0':
        print("Program terminated.\n")
        break

    else:
        print("Invalid option. Please enter 1, 2, or 0.\n")