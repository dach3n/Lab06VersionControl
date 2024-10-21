# COP3502C Lab 6
# By David Chen

def encode(password):
    pass

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
            encode(myPassword)
            print("Your password has been encoded and stored!\n")
        elif choice == "2":
            pass
        elif choice == "3":
            break