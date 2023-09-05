n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

list_sum = 0
for i in student_marks[query_name]:
    list_sum += i

avg = list_sum / len(student_marks[query_name])
print(f"{avg:.2f}")
        