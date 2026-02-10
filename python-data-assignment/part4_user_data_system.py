def calculate_average(scores):
    return sum(scores) / len(scores)

def has_admin_access(roles):
    return "admin" in roles

def main():
    users = [
        {
            "name": "Alice",
            "scores": [80, 85, 90],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Bob",
            "scores": [70, 75, 80],
            "roles": {"viewer"}
        }
    ]

    for user in users:
        print("Name:", user["name"])
        avg = calculate_average(user["scores"])
        print("Average Score:", avg)
        print("Admin Access:", has_admin_access(user["roles"]))
        print("-" * 20)

main()
