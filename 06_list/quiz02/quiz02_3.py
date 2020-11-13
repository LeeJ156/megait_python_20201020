def get_score(scores):
    answer_cnt = scores.count('O')
    score = (100 / len(scores)) * answer_cnt  # 한 문제당 점수  * 맞은 개수
    return score

scores = ['X','O', 'O', 'X', 'X', 'O', 'O', 'O', 'O', 'X']

print("%g점 입니다." % get_score(scores))
