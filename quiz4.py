# Quiz4) 당신의 학교에서 파이썬 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하고, 댓글 작성자들 중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 당첨 불가
# 조건3: random 모듈의 shuffle과 sample을 활용

# 출력 예제
# -- 당첨자 발표 --
# 치킨 당첨자: 1
# 커피 당첨자: [2, 3, 4]
# -- 축하합니다 --

### 내 풀이 ###
from random import * # <from random import *>을 이용해 random 함수를 사용할 수 있게 함.
users = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(users) # range로 하려 했으나 range로 하면 shuffle이 실행되지 않아 하나씩 나열함

print("-- 당첨자 발표 --")
print("치킨 당첨자: " + str(sample(users, 1))) # str(sample(, 1))을 통해 무작위로 정수 하나를 출력함
print("커피 당첨자: " + str(sample(users, 3)))
print("-- 축하합니다 --") # 디버깅 결과; 치킨 당첨자가 리스트형처럼 []으로 나옴. (출력 예제와 다름)

### 답안 ###
from random import *
users = range(1, 21)
users = list(users) # range()를 쓰려면 list()를 통해 리스트형으로 형태를 변환해야 shuffle()이 출력된다는 것을 알게 됨.
shuffle(users)

winners = sample(users, 4) # user에서 무작위로 4명을 뽑은 변수 winners 생성

print("-- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winners[0])) # winners에 0번째 오는 사람 출력
print("커피 당첨자: {0}".format(winners[1:])) # 1번부터 끝까지 출력
print("-- 축하합니다 --") # 디버깅 결과; 변수를 리스트로 만들면 한 개를 출력할 때 []를 벗는 것을 알게 됨.