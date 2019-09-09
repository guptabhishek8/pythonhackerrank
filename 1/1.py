if __name__ == '__main__':
    n = int(input())
    
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    b=0
    c=0
    for a in student_marks[query_name]:
        b=b+a
        c+=1
    print(format(b/c , '.2f'))
