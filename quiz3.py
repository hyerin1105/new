# Quiz3) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙1: http:// 부분은 제외 => naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                      (nav)         (5)            (1)             (!)   ==> nav51!

site = "http://naver.com"

pw = site.replace("http://", "") # 변수.replace()를 통해 () 안에 전자를 후자로 대체
print(pw)

pw = pw[:pw.index(".")] # 변수.index()로 () 안 문자의 위치를 찾고 [:변수.index()]로 처음부터 그 문자가 나오기 직전까지 출력
print(pw)

password = pw[:3] + str(len(pw)) + str(pw.count("e")) + "!"
# len()와 변수.count()가 정수형으로 나오기 때문에 문자열로 출력하기 위해 str() 사용
# 변수.count()로 () 안 문자가 몇 번 나오는지를 출력
print(password)

print("{0}의 비밀번호는 {1}입니다.".format(site, password))