# if
temp = int(input("오늘 기온은? ")) # input()은 입력값 받는 함수
if 30 <= temp:
    print("열사병/일사병 주의요망")
elif 10 <= temp < 30:
    print("버틸 수 있는 더위")
elif -10 <= temp < 10:
    print("외투 필수")
else:
    print("한파 주의")

# for
for waiting_no in range(5): # 0~4까지
    print("대기번호: {0}".format(waiting_no))

# while
customer = "민형"
person = "Unknown"

while person != customer:
    print("\n잠시만 기다려주세요. {0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ") # 민형이 아닌 경우 이름을 되묻고, 민형일 경우 while문 종료