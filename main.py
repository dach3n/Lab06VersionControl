# COP3502C Lab 6
# By David Chen

def encode(password):
    newPass = ""
    for i in password:
        newPass += str((int(i) + 3) % 10)
    return newPass


# decode function - Malia Arellano
def decode(password):
    decoded_password = ""
    for i in password:
        decoded_password += str((int(i) - 3) % 10)
    return decoded_password

if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")

        choice = input("\nPlease enter an option: ")

        if choice == "1":
            myPassword = input("Please enter your password to encode: ")
            myPassword = encode(myPassword)
            print("Your password has been encoded and stored!\n")
        elif choice == "2":
            print(f"The encoded password is {encode(myPassword)}, and the original password is {decode(myPassword)}.")
        elif choice == "3":
            break