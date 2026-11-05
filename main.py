import random # 난수 발생

game = {1:"가위",2:"바위",3:"보"} #딕셔너리에 값 넣기
game = random.randint[1, 3]
game 

try_count = 0 # 시도 횟수
win_count = 0 # 승리 횟수
score()

#승리 기준

#타이틀
print("=" * 30)
print("가위/바위/보 게임")
print("=" * 30)

# 메인 루프
while True:
    user_input = input("1 ~ 3 번호를 선택하시오.")
    
    if user_input = "q":
        print(f"게임을 종료합니다.")
        break
    
    if not user_input.isdecimal():
        print(f"숫자만 입력해주세요.")
        continue
    
    user_number = int(user_input)
    #시도 횟수 증기
    try_count +=1
    
    # 1번 키가 3번 키보다 크다 라는걸 어떻게 표시하지..
    1 > 3
    
    # 입력값과 정답을 비교
    if user_number < game:
        print("패배")
    elif user_number > game:
        print("승리")
    else:
        print("비김")
        return
        





