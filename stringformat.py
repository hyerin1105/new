# 방법1
print("나는 %d살입니다." % 23) # %d 정수형
print("나는 %s색을 좋아해요." % "초록") # %s 문자형
print("Apple은 %c로 시작해요." % "A") # %c 단어형

# 정수형과 단어 둘 다 %s로 해도 정상적으로 출력 가능
print("나는 %s살입니다." % 23) # %d 정수형
print("Apple은 %s로 시작해요." % "A") # %c 단어형

# 방법2
print("나는 {}살입니다.".format(23))
# print("나는 {}색을 좋아해요.".format("초록"))
print("나는 {1}색과 {0}색을 좋아해요.".format("초록", "검정")) # {} 안에 숫자를 통해 출력 변수의 순서를 바꿀 수 있음.
# {}과 .format()을 이용하면 %s처럼 정수형, 문자형, 단어 출력 다 가능

# 방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 23, color = "초록"))

# 방법4
age = 23
color = "초록"
print(f"나는 {age}살이며, {color}색을 좋아해요.") #f = .format()으로 f 뒤에 {변수}를 넣으면 괄호 안에 해당 변수가 지정되어 출력됨.