def greet_student(name):
    return f"Hello, {name}"

def calculate_scores(scores):
    total_subjects = len(scores)
    average = sum(scores) / total_subjects
    return total_subjects, average

def check_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    name = "Pritam"
    scores = [60, 70, 65]

    greeting = greet_student(name)
    subjects, avg_score = calculate_scores(scores)
    result = check_result(avg_score)

    print(greeting)
    print("Subjects:", subjects)
    print("Average Score:", avg_score)
    print("Result:", result)

main()