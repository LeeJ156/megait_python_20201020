text = "I love fried chiken"
input_text = input(text + "를 따라 치세요 \n")

correct_cnt = 0
for i in range(len(text)):
    if text[i] == input_text[i]:
        correct_cnt += 1

ratio = (correct_cnt / len(text)) * 100
print("정확도: %g%%" % ratio)
