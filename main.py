number = int(input("Think of a number b/w 1 and 25: "))
low = 1
high = 25
attempts = 0


while True:
    mid = (low + high)//2
    attempts =attempts + 1
    print(f"Is your number {mid}?")
    response = input("My guess is: Enter H for high, L for low and C for correct.").strip().upper()
    if response == "H":
        high = mid - 1
    elif response == "L":
        low = mid + 1
    elif response == "C":
        print(f"Computer have guessed yout nmber in {attempts} attempts")
        break

    else:
        print("Invalid command, please enter L, H or C")