from tests import *
from fileIO import *
from generators import *

run = True
prime = None
while run:
    print("Choose one of the options")
    print("1 : Generate prime number")
    print("2 : Enter own number")
    print("3 : Print all prime numbers")
    print("4 : Load number from a file")
    print("5 : Save number to a file")
    print("6 : Test a number")
    print("7 : Quit program")
    cmd = numbers_only()
    if cmd == 1:
        prime = prime_generator()
        print("You have generated number ", prime)
    elif cmd == 2:
        print("Enter your own number")
        prime = numbers_only()
    elif cmd == 3:
        print("Enter limit")
        limit = numbers_only()
        print(eratosthenes_sieve(limit))
    elif cmd == 4:
        prime = read_prime_from_file()
        print("Prime read from file is ", prime)
    elif cmd == 5:
        if prime is not None:
            save_prime_to_file(prime)
        else:
            print("Enter prime, you want to save to a file")
            prime = numbers_only()
            save_prime_to_file(prime)
    elif cmd == 6:
        if prime is None:
            print("Enter number you want to test")
            prime = numbers_only()
        print("Choose one of the test")
        print("1 : Miller-Rabin test")
        print("2 : Lucas-Lehmer test")
        print("3 : Fermat test")
        print("4 : Back to main menu")
        subcmd = numbers_only()
        if subcmd == 1:
            print("Enter the number of iterations for Miller-Rabin test")
            iterations = numbers_only()
            if miller_rabin_test(prime, iterations):
                print("%d is a prime" % prime)
            else:
                print("%d is a composite" % prime)
        elif subcmd == 2:
            print("Lucas-Lehmer test works on primes in the form (2^p) - 1")
            print("Enter p")
            prime = numbers_only()
            if lucas_lehmer_test(prime):
                print("%d is a prime" % prime)
            else:
                print("%d is a composite" % prime)
        elif subcmd == 3:
            print("Enter the number of iterations for Fermat test")
            iterations = numbers_only()
            if fermat_test(prime, iterations):
                print("%d is a prime" % prime)
            else:
                print("%d is a composite" % prime)
        elif subcmd == 4:
            continue
    elif cmd == 7:
        run = False
