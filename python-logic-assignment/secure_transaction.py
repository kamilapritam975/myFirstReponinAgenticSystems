balance = int(input("Enter account balance: "))
withdrawal = int(input("Enter withdrawal amount: "))
verified_input = input("Verified (True/False): ").strip().lower()

if verified_input == "true":
    verified = True
elif verified_input == "false":
    verified = False
else:
    print("Invalid verification input")
    exit()

if verified and withdrawal <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")