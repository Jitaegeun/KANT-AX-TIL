import random # 난수 발생

game = {1:"가위",2:"바위",3:"보"} #딕셔너리에 값 넣기
computer = random.randint(1, 3)


try_count = 0 # 시도 횟수
win_count = 0 # 승리 횟수

#타이틀
print("=" * 30)
print("가위/바위/보 게임")
print("=" * 30)

#게임 실행
user_input = input("1.가위/2.바위/3.보 번호를 선택하시오.")

#승리 규칙
if user_input == computer:
    print ("비김")
elif user_input == 1 and computer == 3:
    print("승리")
elif user_input == 2 and computer == 1:
    print("승리")
elif user_input == 3 and computer == 2:
    print("승리")
else:
    print("패배")

        





