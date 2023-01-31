# Quiz2) 당신은 최근에 코딩스터디를 새로 만들었습니다.
#        월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
#        아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1: 랜덤으로 날짜 뽑기
# 조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3: 매월 1~3일은 스터디 준비를 해야하므로 제외
# 출력문 예제) "오프라인 스터디 날짜는 매월 xx일로 선정되었습니다."

## 1차 풀이 ## (답안에는 오프라인만 출력하길래 조금 더 응용해 온라인까지 출력함.)
from random import *

# day = int(random() * 7) + 4 <- random() 함수 쓰면 0부터 출력되기에 4일부터 출력될 수 있도록 +4함.
# day = randint(4, 28) <- randint()로 4~28 이하의 정수 출력

on_day1 = randrange(4, 29) # randrange()로 4~28 이하의 정수 출력
on_day2 = randrange(4, 29)
on_day3 = randrange(4, 29)
off_day = randrange(4, 29)
print("온라인 스터디 날짜는 매월 ", str(on_day1), str(on_day2), str(on_day3), "일로,")
print("오프라인 스터디 날짜는 매월 ", str(off_day), "일로 선정되었습니다.")
# 디버깅 결과; 변수를 각각 지정해 출력했더니 온라인과 오프라인 일정이 겹치는 경우 발생

## 2차 풀이 ##
from random import *

day = range(4, 29) # range()로 4~28 이하의 정수 출력
day = sample(day, 4) # 무작위로 4일 뽑기
print("온라인 스터디 날짜는 매월 {}일로".format(day[0:3])) # 무작위로 뽑은 4일 중 1~3번 출력
print("오프라인 스터디 날짜는 매월 {}일로 선정되었습니다.".format(day[3])) # 남은 4번 출력
# 디버깅 결과; 온라인과 오프라인 날짜를 한번에 뽑아 중복의 경우를 없앰.