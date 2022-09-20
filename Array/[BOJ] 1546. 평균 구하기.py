n = input()
grade = list(map(int, input().split()))

maxGrade = max(grade)

print(100*(sum(grade)) / len(grade) / maxGrade) 


# 풀이 : 계산 식을 세움 => 100(A+B+C+ ... +Y) / len(grade) / M 