###
### 아이템 7
###

from random import randint

random_bits = 0
for i in range(32):
    if randint(0, 1):
        random_bits |= 1 << i # <<, >> 비트 연산자. 2진수 형태로 되어 있기에 비트 수만큼 밀어주는. 즉, 2배가 되거나 1/2배가 된다.

print(bin(random_bits))

flavor_list = ['바닐라', '초콜릿', '피칸', '딸기']
for flavor in flavor_list:
    print(f'{flavor} 맛있어요.')

for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i + 1}: {flavor}')

it = enumerate(flavor_list)
print(next(it))
print(next(it))

for i, flavor in enumerate(flavor_list): # range보다는 enumerate를 사용하자. 
    print(f'{i + 1}: {flavor}')          # 두 번째 파라미터로 어디부터 수를 셀 것인지 지정할 수 있다. 디폴트 값은 0이다.

for i, flavor in enumerate(flavor_list, 1): # enumerate는 이터레이터를 지연 계싼 제너레이터로 감싸게 된다. 
    print(f'{i}: {flavor}')                 # enumerate는 yield로 원소 쌍을 넘겨주며, next 내장 함수로 다음 원소 쌍을 가져온다. 
