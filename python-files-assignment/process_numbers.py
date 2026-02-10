# File names
input_file = "numbers.txt"
log_file = "results.log"

numbers = []

# Step 1: Read data from file
with open(input_file, "r") as file:
    print("File opened successfully")

    for line in file:
        number = int(line.strip())
        numbers.append(number)

# Step 2: Calculations
total_numbers = len(numbers)
total_sum = sum(numbers)
average = total_sum / total_numbers

# Step 3: Write logs (append mode)
with open(log_file, "a") as log:
    log.write("File opened successfully\n")
    log.write(f"Read {total_numbers} numbers\n")
    log.write(f"Sum: {total_sum}\n")
    log.write(f"Average: {average}\n")
    log.write("Processing completed\n\n")

print("Processing completed")
