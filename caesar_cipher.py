def cipher(message, shift, mode):
    # if mode is "decrypt", make shift negative
    if mode == "decrypt":
        shift = -shift
    # then rest of your code using shift normally
    result = ""
    for i in range(len(message)):
        if message[i] in "abcdefghijklmnopqrstuvwxyz":
            char = (ord(message[i]) - 97 + shift) % 26 + 97
            char = chr(char)
            result += char
        else:
            result += message[i]
    print(f"result: {result}")
def brute_force(message):
    for shift in range(1, 27):
        print(f"Shift {shift}: ", end="")
        cipher(message, shift, "decrypt")
while True:
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. quit")
    print("4. Brute force!!")
    try:
        x = int(input("Choose: "))
        if x == 1:
            mode = "encrypt"
            message = input("Enter your message: ")
            shift = int(input("Shift by: "))
            cipher(message, shift, mode)
        elif x == 2:
            mode = "decrypt"
            message = input("Enter your message: ")
            shift = int(input("Was shifted by: "))
            cipher(message, shift, mode)
        elif x == 3:
            print("bye")
            break
        elif x == 4:
            message = input("Enter encrypted message: ")
            brute_force(message)
        else:
            print("Invalid input")
    except ValueError:
        print("Enter a number")
