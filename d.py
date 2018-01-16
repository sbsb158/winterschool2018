import random

ans1='네 마자요'
ans2='할 수 있을꺼에요'
ans3='파이팅'
ans4='열심히하세요'
ans5='언제든 기회가 있을거에요'
ans6='잘했어요'
ans7='다시생각해봐요'
ans8='일단 부딪혀보세요'


print('환영합니다')

Q=input('조언을 구하고 싶으면 질문을 입력하고 엔터 키를 누르세요.\n')

print('\n'+'고민중...\n'*4)

choice=random.randint(1,8)

if choice==1:
    answer=ans1

elif choice==2:
    answer=ans2

elif choice==3:
    answer=ans3

elif choice==4:
    answer=ans4

elif choice==5:
    answer=ans5

elif choice==6:
    answer=ans6

elif choice==7:
    answer=ans7

else:
    answer=ans8

print(answer)

input('\n\n마치려면 엔터 키를 누르세요')
