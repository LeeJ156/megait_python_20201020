books_dict = {'자기계발':{'말 그릇':'김윤나', '메모의 마법':'마에다 유지'}, '소설':{'아몬드':'손원평', '나미야 잡화점의 기적':'히가시노 게이고', '어린왕자':'생텍쥐페리'}, '과학':{'마음의 미래':'미치오 카쿠', '시간은 흐르지 않는다':'카를로 로벨리', '평행우주':'미치오 카쿠'}}

# 1. 장르가 소설인 책의 목록 출력하기
print(list(books_dict.get('소설').keys()))

# 2. 책이 존재하는지 여부
'''
* 과학 장르에 '코스모스' 책이 있는지 여부를 출력하세요. 
* 소설 장르에 '나미야 잡화점의 기적' 책이 있는지 여부를 출력하세요.
'''

science_books = books_dict.get('과학')
if '코스모스' in science_books:
    print("'코스모스' 책이 있습니다.")
else:
    print("'코스모스' 책이 없습니다.")

science_books = books_dict.get('소설')
if '나미야 잡화점의 기적' in science_books:
    print("'나미야 잡화점의 기적' 책이 있습니다.")
else:
    print("'나미야 잡화점의 기적' 책이 없습니다.")

# 3. '메모의 마법'의 저자가 누구인지 출력
# key로 value에 접근을 해야한다.
# 바깥쪽의 '장르' 키들을 얻어서 책 dict에 접근 해야한다.
for genre in books_dict:
    print(genre)
    books_of_genre = books_dict.get(genre)
    print(books_of_genre)
    writer = books_of_genre.get('메모의 마법')
    if writer:    # if writer != None 과 같다  즉, writer에 값이 들어있으면 빠져나온다.
        break

print(writer)
