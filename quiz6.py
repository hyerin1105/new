# Quiz6) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 페중: 각 개인의 키에 적당한 체중
# (성별에 따른 공식) 남자: 키(m) * 키(m) * 22
#                   여자: 키(m) * 키(m) * 21

# 조건1: 표준 체중은 별도의 함수 내에서 계산
#        * 함수명: std_weight
#        * 전달값: 키(height), 성별(gender)
# 조건2: 표준 체중은 소숫점 둘쨋자리까지 표시
# 출력 예제) 키 175cm 남자의 표준 체중은 67.38kg입니다.

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # 키와 성별은 input이 아니라 임의로 지정함
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
# m단위로 바꿔야 하기에 나누기 100
# round( , 2)를 이용해 소숫점 둘쨋짜리까지 출력

print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))