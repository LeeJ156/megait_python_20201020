first_day = [96, 80, 79, 92]
second_day = [90, 88, 70, 87]
third_day = [72, 84, 100, 90]

scores = first_day + second_day + third_day

sum = 0
average = 0
for score in scores:
    sum += score

average = sum / len(scores)
print("바다의 평균 점수는 %g 입니다." % average)
