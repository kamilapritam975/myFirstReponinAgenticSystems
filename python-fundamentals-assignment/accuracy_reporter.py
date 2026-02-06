accuracy_input = input("Enter model accuracy: ")

try:
    # % hata do agar diya ho
    accuracy_input = accuracy_input.replace("%", "")

    accuracy = float(accuracy_input)

    # agar 90 jaisa diya, to percent samjho
    if accuracy > 1:
        accuracy = accuracy / 100

    print(f"Model accuracy is {accuracy:.2f}")

except ValueError:
    print("Please enter a valid numeric value.")
