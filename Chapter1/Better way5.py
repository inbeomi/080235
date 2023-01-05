###
### 아이템 5
###

from urllib.parse import parse_qs

my_values = parse_qs('빨강=5&파랑=0&초록=', # URL의 query string을 parsing하는.
                     keep_blank_values=True)
print(repr(my_values))

print('빨강: ', my_values.get('빨강')) # 딕셔너리의 get 메서드. key값을 넣으면 value값을 반환한다. 
print('초록: ', my_values.get('초록'))
print('투명도: ', my_values.get('투명도'))


# 질의 문자열이 `빨강=5&파랑=0&초록='인 경우
red = my_values.get('빨강', [''])[0] or 0 # 빈 문자열, 빈 리스트, 0 모두 암시적으로 False로 평가된다는 사실을 이용한다.
green = my_values.get('파랑', [''])[0] or 0  # or의 왼쪽이 False라면 or의 오른쪽 값을 사용하게 된다. 
opacity = my_values.get('투명도', [''])[0] or 0 # key값이 아예 없을 경우, [''] 값을 반환한다. 
print(f'빨강: {red!r}')
print(f'초록: {green!r}')
print(f'투명도: {opacity!r}')

red = int(my_values.get('빨강', [''])[0] or 0) # 코드 읽기가 어렵다. 시각적 잡음이 많다. 

red_str = my_values.get('빨강', ['']) # 코드를 간결하게 유지하면서 명확하게 표현하기 위해 if/else문을 사용하기도 한다. 
red = int(red_str[0]) if red_str[0] else 0 # boolean, or, and 연산자보다 if/else 식이 더 가독성이 좋다.

green_str = my_values.get('초록', ['']) # 완전한 if/else문을 사용함으로써 훨씬 더 명확하게 표현한다. 
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0
    
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default

green = get_first_int(my_values, '초록')

# 코드를 줄여 쓰는 것보다 가독성을 좋게 하는 것이 더 가치가 있다. 
# 복잡한 식을 표현할 수 있는 파이썬의 함축적인 문법이 지저분한 코드를 만들어내지 않도록 하자.
# 반복하지 말라. 
