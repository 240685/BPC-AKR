import random
from time import perf_counter
from tests import miller_rabin_test, lucas_lehmer_test


def numbers_only():
    try:
        number = int(input("Your choice: "))
    except Exception as e:
        number = numbers_only()
    if number < 0:
        print("Please enter positive whole number")
        number = numbers_only()
    return number


def generate_n_bit_number(n):
    if n <= 0:
        print("Length of the number in bits must be positive")
        return 0  # Return 0 for non-positive n

    # Generate a random integer in the range [0, 2^n - 1]
    random_number = random.randint(0, 2 ** n - 1)

    return random_number


def prime_generator():
    print("Enter length of the desired number in bits")
    n = numbers_only()
    iterations = None
    prime = False
    count = 0
    start_time = perf_counter()
    while not prime:
        prime_candidate = generate_n_bit_number(n)
        count += 1
        if prime_candidate <= 2 ** 64:
            iterations = 10
        if 2 ** 64 < prime_candidate <= 2 ** 128:
            iterations = 25
        if prime_candidate > 2 ** 128:
            iterations = 50
        if miller_rabin_test(prime_candidate, iterations):
            elapsed_time = perf_counter() - start_time
            print("%d numbers were generated and tested\nThis process took %.4f seconds" % (count, elapsed_time))
            return prime_candidate


def eratosthenes_sieve(number):
    print("Generating primes leading to %d" % number)
    start_time = perf_counter()

    # Create a boolean list to mark numbers as prime or composite
    is_prime = [True] * (number + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    # Start with the first prime number (2)
    p = 2
    while p ** 2 <= number:
        if is_prime[p]:
            # Mark all multiples of p as non-prime
            for i in range(p ** 2, number + 1, p):
                is_prime[i] = False
        p += 1

    # Collect the prime numbers
    primes = []
    for i in range(2, number + 1):
        if is_prime[i]:
            primes.append(i)

    elapsed_time = perf_counter() - start_time
    print("Generating took %.4f seconds" % elapsed_time)
    return primes
