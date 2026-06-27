correct_pin = "1234"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("Access Granted!")
        break
    attempts += 1
    print(f"Wrong PIN! Attempts left: {max_attempts - attempts}")
else:
    print("Too many failed attempts. Account locked.")
