import random
from time import perf_counter


def miller_rabin_test(number, iterations):
    start_time = perf_counter()
    if number <= 1:
        return False
    if number <= 3:
        return True

    # Write number as (2^s) * r + 1
    s = 0
    r = number - 1
    while r % 2 == 0:
        s += 1
        r = r // 2

    # Witness loop
    for _ in range(iterations):
        a = random.randint(2, number - 2)  # choosing random base a
        x = pow(a, r, number)
        if x == 1 or x == number - 1:
            continue  # number is probably prime, moving on to next iteration

        for _ in range(s - 1):
            x = pow(x, 2, number)
            if x == number - 1:
                break  # number is probably prime
        else:
            elapsed_time = perf_counter() - start_time
            print("Miller-Rabin test with %d iterations for the number %d took %.4f seconds" % (iterations, number, elapsed_time))
            return False  # number is definitely composite

    elapsed_time = perf_counter() - start_time
    print("Miller-Rabin test with %d iterations for the number %d took %.4f seconds" % (iterations, number, elapsed_time))
    return True  # number is probably prime


def lucas_lehmer_test(number):
    if number <= 2:
        return False

    u = 4
    m = 2 ** number - 1
    start_time = perf_counter()
    # Perform the iteration p-2 times
    for _ in range(number - 2):
        u = (u * u - 2) % m

    elapsed_time = perf_counter() - start_time
    print("Lucas-Lehmer test for the number %d took %.4f seconds" % (m, elapsed_time))

    # If the final value of u is 0, then 2^p - 1 is prime
    return u == 0


def fermat_test(number, iterations):
    if number <= 1:
        return False
    if number <= 3:
        return True
    start_time = perf_counter()
    for _ in range(iterations):
        a = random.randint(2, number - 2)
        if pow(a, number - 1, number) != 1:
            elapsed_time = perf_counter() - start_time
            print("Fermat test with %d iterations for the number %d took %.4f seconds" % (iterations, number, elapsed_time))
            return False
    elapsed_time = perf_counter() - start_time
    print("Fermat test with %d iterations for the number %d took %.4f seconds" % (iterations, number, elapsed_time))

    return True
