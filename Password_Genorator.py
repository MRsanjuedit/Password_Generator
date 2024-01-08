import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check(size):
    if(size>=15):
        print("Over Size Length Must be <=15 \n")
    else:
        return generate_password(size)
        
# Generate a password of length 10
def main():
    size=int(input("Enter the required Length of password :\t"))
    generated_password = check(size)
    print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()