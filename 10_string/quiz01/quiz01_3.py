# 영어 단어를 입력 받고 'e' 가 몇개 들어 있는지 출력하세요.

def word_count(word, char):
    print("%s의 개수는 %d개 입니다." % (char, word.count(char)))

word = input("단어를 입력하세요: ")
word_count(word, 'e')
