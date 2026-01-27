total_score = 0
student_count = 0
student_score = 0

while student_score != -1:
    student_score = float(input("Student Score: "))
    if student_score == -1:
        break
    total_score += student_score
    student_count += 1

if student_count == 0:
    print("No marking today")
    exit()  # This exits the program - The other lines do not run.

average_score = total_score / student_count

if average_score >= 70:
    print(f"Average Score: {average_score}%. Great Job, class")
else:
    print(f"Average Score: {average_score}%. The class needs more practice")
