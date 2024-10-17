def encrypt(x):
    return(x[::-1])

def decrypt(x):
    encrypt(x)

def main():
    input("1. Encrypt\n2. Decrypt?\n --> ")
    r = encrypt(input("Whats your message? \n --> "))
    print(r)


if __name__ == "__main__":
    main()


