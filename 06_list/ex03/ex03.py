# 2차원 리스트

# A의 시험점수 : [83, 93, 91]
# B의 시험점수 : [45, 50, 76]
scores = [[83, 93, 91], [45, 50, 76]]

print("B의 첫 번째 시험 점수는 %d입니다." % scores[1][0]) 
print("A의 두 번째 시험 점수는 %d입니다." % scores[0][1])
print("B의 세 번째 시험 점수는 %d입니다." % scores[1][2])

print("=" * 50)

# 각 학생의 평균 점수 구하기(1) - index 접근 기반
for i in range(len(scores)):  # 0 1
    print(scores[i])
    sum = 0
    for j in range(len(scores[i])):  # 0 1 2
        sum += scores[i][j]

    average = sum / len(scores[i])
    print("평균 점수는 %g입니다." % average)

print("=" * 50)

# 각 학생의 평균 점수 구하기(2) - 값 기반
for student in scores:
    sum = 0
    for score in student:
        sum += score
        
    average = sum / len(student)
    print("평균 점수는 %g입니다." % average)
