photo = {'황예지', '임나연', '황광희', '장원영', '하성운', '권은비'}
dance = {'박명수', '하성운', '유재석', '박지민', '임나연'}
band = {'하성운', '민경훈', "권은비", '황광희'}

# 1. 3개의 동아리 중 하나 이상 가입된 사람들의 전체 명단을 중복 없이 출력하세요.
# {'박지민', '황광희', '임나연', '하성운', '황예지', '장원영', '유재석', '민경훈', '권은비', '박명수'}
print(photo | dance | band)
# 2. 댄스동아리에만 가입된 사람 {'박지민', '유재석', '박명수'}
print(dance - photo - band)

# 3. 3개의 동아리에 모두 가입된 사람
print(dance & photo & band)

# 4. 2개의 동아리에 가입된 사람
a = photo.intersection(dance)
b = photo.intersection(band)
c = dance.intersection(band)

# 연산자 우선순위 (뺄셈이 집합연산보다 우선순위가 더 높으므로 괄호를 해주어야 한다)
print((a | b | c) - (dance & photo & band))




