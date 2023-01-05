###
### 아이템 9
###

for i in range(3):
    print('Loop', i)
else:
    print('Else block!')    # for문 루프까 끝나자마자 실행이 된다.
                            # try/except에서 except은 앞 블록을 시도하다가 예외가 발생하면 실행되는 것과는 다르다.
                            # try/except/else/finally에서의 else와는 다르게 for문에서의 else는 직관적이지 못하다.
for i in range(3):
    print('Loop', i)
    if i == 1:
        break               # break문을 사용하면 else문이 사용되지 않는다. 
else:
    print('Else block!')


for x in []:                # 빈 시퀀스에 대한 루프를 실행하면 else 블록이 바로 실행된다. 놀라우면서도 헷갈리기 쉽다. 
    print('이 줄은 실행되지 않음')
else:                       # 하지만 그렇게 작동되어야 유용하다.
    print('For Else block!')

while False:                # 처음부터 False로 루프가 실행되지 못할 때도 else 블록이 바로 실행된다.
    print('이 줄은 실행되지 않음')
else:
    print('While Else block!')

a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print('검사 중', i)
    if a % i == 0 and b % i == 0:
        print('서로소 아님')
        break
else:
    print('서로소')


def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False    # 원하는 조건을 찾자마자 빠르게 함수를 반환하는 방식
    return True

assert coprime(4, 9)
assert not coprime(3, 6)

def coprime_alternate(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break          # 원하는 대상을 찾자마자 break로 루프를 빠져나오는 방식
    return is_coprime

assert coprime_alternate(4, 9)
assert not coprime_alternate(3, 6)

# else 블록을 사용함으로써 얻을 수 있는 표현력보다는 미래에 이 코드를 이해하려는 사람들이 느끼게 될 부담감이 더 크다.
# 루프와 같은 구성 요소는 그 자체로 의미가 명확해야 한다. 따라서 절대로 루프 뒤에 else 블록을 사용하지 말아야 한다. 
