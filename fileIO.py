

def save_prime_to_file(prime):
    file_name = input("Enter a file name: ")
    file_name += ".txt"
    f = open(file_name, "w")
    f.write(str(prime))
    f.close()
    print("Your number %d was saved to a file named %s" % (prime, file_name))


def read_prime_from_file():
    file_name = input("Enter a file name: ")
    file_name += ".txt"
    f = None
    prime = None
    try:
        f = open(file_name, "r")
        prime = int(f.read())
    except FileNotFoundError:
        print("File with name '%s' does not exist\nTry a different name" % file_name)
    else:
        f.close()
    return prime
