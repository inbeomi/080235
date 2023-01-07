#
# 아이템 14
#
numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers)

class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'

tools = [
    Tool('수준계', 3.5),
    Tool('해머', 1.25),
    Tool('스크류드라이버', 0.5),
    Tool('끌', 0.25),
]

print('미정렬:', repr(tools))
tools.sort(key=lambda x: x.name)
print('\n정렬: ', tools)

tools.sort(key=lambda x: x.weight)
print('무게순 정렬:', tools)

places = ['home', 'work', 'New York', 'Paris']
places.sort()
print('대소문자 구분:', places)
places.sort(key=lambda x: x.lower())
print('대소문자 무시:', places)

power_tools = [
    Tool('드릴', 4),
    Tool('원형 톱', 5),
    Tool('착암기', 40),
    Tool('연마기', 4),
]

saw = (5, '원형 톱')
jackhammer = (40, '착암기')
assert not (jackhammer < saw) # 예상한 대로 결과가 나온다

drill = (4, '드릴')
sander = (4, '연마기')
assert drill[0] == sander[0] # 무게가 같다
assert drill[1] < sander[1]  # 알파벳순으로 볼 때 더 작다
assert drill < sander        # 그러므로 드릴이 더 먼저다 : 튜플의 원소를 첫 번째부터 차례로 비교하며 순위를 정한다. 

power_tools.sort(key=lambda x: (x.weight, x.name)) # default값은 오름차순이다.  
print(power_tools)

power_tools.sort(key=lambda x: (x.weight, x.name),
                 reverse=True) # 모든 비교 기준을 내림차순으로 만든다
print(power_tools)

power_tools.sort(key=lambda x: (-x.weight, x.name)) # 모든 비교 기준이 동일하게 반영이 되니, 이처럼 -를 붙여서 다르게 반영되도록 한다
print(power_tools)

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#power_tools.sort(key=lambda x: (x.weight, -x.name), # 숫자가 아닌 문자열은 - 처리가 되지 않는다.
#                 reverse=True)

power_tools.sort(key=lambda x: x.name)   # name 기준 오름차순 
power_tools.sort(key=lambda x: x.weight, # weight 기준 내림차순
                 reverse=True)
print(power_tools)

power_tools.sort(key=lambda x: x.name)   # 만약, key 함수가 반환하는 값이 서로 같은 경우 리스트에 들어 있던 원래 순서를 그대로 유지해준다. 
print(power_tools)                       # 이는, 같은 리스트에 대해 서로 다른 기준으로 sort를 여러 번 호출해도 된다는 뜻이다. (부호를 바꿀 수 없는 타입이라면 고려할 만하다.)
                                         # 여러 번 호출하는 방법은 필요할 때만 사용하는 것을 권장한다. 
power_tools.sort(key=lambda x: x.weight,
                 reverse=True)
print(power_tools)
