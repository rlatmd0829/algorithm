n = int(input())

_ = '____'

cnt2 = n+1
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
def recursive(cnt,index):
    
    print(_*cnt+"\"재귀함수가 뭔가요?\"")
    if index == 0:
        print(_*cnt+"\"재귀함수는 자기 자신을 호출하는 함수라네\"")
    
    else:
        print(_*cnt+"\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        print(_*cnt+"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print(_*cnt+"그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
        recursive(cnt+1,index-1)
        
    print(_*cnt+"라고 답변하였지.")
    
recursive(0,n)
    



# n = int(input())

# _ = '____'
# cnt = -1
# cnt2 = n+1
# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# def recursive(index):
#     global cnt
#     global cnt2
#     cnt += 1
#     print(_*cnt+"\"재귀함수가 뭔가요?\"")
#     if index == 0:
#         print(_*cnt+"\"재귀함수는 자기 자신을 호출하는 함수라네\"")
    
#     else:
#         print(_*cnt+"\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
#         print(_*cnt+"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
#         print(_*cnt+"그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
#         recursive(index-1)
#     cnt2 -= 1
#     print(_*cnt2+"라고 답변하였지.")
    
# recursive(n)
    