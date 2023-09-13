def finding_the_percentage(students, selected_name):
    list_sum = 0
    if students.get(selected_name) is not None:
        for i in students[selected_name]:
            list_sum += i
        avg = list_sum / len(students[selected_name])
        return f"{avg:.2f}"
    else:
        return "0"


if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print(finding_the_percentage(student_marks, query_name))
