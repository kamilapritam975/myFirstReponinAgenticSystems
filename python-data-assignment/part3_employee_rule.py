employee = (101, "Amit", "IT")
roles = {"admin", "editor", "viewer"}

print("Employee ID:", employee[0])
print("Employee Name:", employee[1])
print("Department:", employee[2])

if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")
