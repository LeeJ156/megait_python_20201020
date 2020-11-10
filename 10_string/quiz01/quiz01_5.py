# 주어진 문자열의 단어 개수
def word_count(t):
    words = t.split()
    return len(words)

text = "To be, or Not to Be. That Is The Question"
print("문자열의 단어 개수는 %d개 입니다." % word_count(text))
