###
### 아이템 10
###

fresh_fruit = {
    '사과': 10,
    '바나나': 8,
    '레몬': 5,
}

def make_lemonade(count):
    n = 1
    print(f'레몬 {count*n} 개로 레모네이드 {count//n} 개를 만듭니다.')
    fresh_fruit['레몬'] -= (count * n)   
    print(f'레몬이 {fresh_fruit["레몬"]} 개 남았습니다.')

def out_of_stock():
    print(f'제료가 부족합니다. 재료를 보충해 주세요.')

count = fresh_fruit.get('레몬', 0)    # 보통은 if문 앞에 변수를 정의하면 그 이후 코드에서 변수에 접근해야 할 필요성이 있는 것처럼 보인다. 
if count:                             # 여기에서는 if 조건문 말고는 들어가지 않는다. 좋은 코드 방식이 아니다. 
    make_lemonade(count)
else:
    out_of_stock()

fresh_fruit['레몬'] = 5  # 테스트를 위해 갯수 리셋
if count := fresh_fruit.get('lemon', 0):   # := 왈러스 연산자. 대입식은 대입문이 쓰일 수 없는 위치에서 변수에 값을 대입할 수 있다. 
    make_lemonade(count)                   # 대입식의 값은 왈러스 연산자 왼쪽에 있는 식별자에 대입된 값으로 평가된다. 
else:                                      # 이 경우, count 변수가 if 조건문에서만 의미가 있다는 것이 명확히 보이기 때문에 코드 읽기가 더 쉽다.
    out_of_stock()                         # 대입 연산자는 count 변수에 값을 대입하고, if 문의 맥락에서 대입된 값을 평가하게 된다. (대입 후 평가)

def make_cider(count):
    n = 4

    print(f'사과 {count} 개로 사과주스 {count//n} 개를 만듭니다.')
    fresh_fruit['사과'] -= (n *(count//n))
    print(f'사과가 {fresh_fruit["사과"]} 개 남았습니다.')

fresh_fruit['사과'] = 10  # 테스트를 위해 갯수 리셋

count = fresh_fruit.get('사과', 0)
if count >= 4:
    make_cider(count)
else:
    out_of_stock()


fresh_fruit['사과'] = 10  # 테스트를 위해 갯수 리셋

if (count := fresh_fruit.get('사과', 0)) >= 4:    # 대입식을 괄호로 둘러싸서 대입 결과와 숫자 4와 비교를 하게 된다. 
    make_cider(count)
else:
    out_of_stock()

def slice_bananas(count):
    print(f'바나나 {count} 개를 슬라이스합니다.')
    fresh_fruit['바나나'] -=  count
    return count

class OutOfBananas(Exception):
    pass

def make_smoothies(count):
    n=2
    if count > n:
        print(f'바나나 슬라이스 {count} 개로 스무디 {count//n} 개를 만듭니다.')
        print(f'바나나가 {fresh_fruit["바나나"]} 개 남았습니다.')
    else:
        raise OutOfBananas

pieces = 0
count = fresh_fruit.get('바나나', 0) # count 변수가 불필요하게 강조된다. 중요한 것은 pieces인데 말이다. 
if count >= 2:
    pieces = slice_bananas(count)

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

fresh_fruit['바나나'] = 8  # 테스트를 위해 갯수 리셋

count = fresh_fruit.get('바나나', 0)
if count >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

fresh_fruit['바나나'] = 8  # 테스트를 위해 갯수 리셋

pieces = 0
if (count := fresh_fruit.get('바나나', 0)) >= 2:
    pieces = slice_bananas(count)

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

fresh_fruit['바나나'] = 8  # 테스트를 위해 갯수 리셋

if (count := fresh_fruit.get('바나나', 0)) >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

count = fresh_fruit.get('banana', 0)

fresh_fruit['바나나'] = 8  # 테스트를 위해 갯수 리셋

if count >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
else:
    count = fresh_fruit.get('사과', 0)
    if count >= 4:
        to_enjoy = make_cider(count)
    else:
        count = fresh_fruit.get('레몬', 0)
        if count:
            to_enjoy = make_lemonade(count)
        else:
            to_enjoy = '아무것도 없음'

if (count := fresh_fruit.get('바나나', 0)) >= 2:  # 왈러스 연산자를 사용하면 if/elif/else문을 보다 깔끔하게 작성할 수 있다. 
    pieces = slice_bananas(count)                # 마치 switch/case 문 같은 다중 선택 전용 구문과 거의 비슷하게 말이다. 훨씬 가독성이 좋아졌다.
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get('사과', 0)) >= 4:
    to_enjoy = make_cider(count)
elif count := fresh_fruit.get('레몬', 0):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = '아무것도 없음'

import random

def pick_fruit():
    if random.randint(1,10) > 2:   # 80% 확률로 새 과일 보충
        return {
            '사과': random.randint(0,10),
            '바나나': random.randint(0,10),
            '레몬': random.randint(0,10),
        }
    else:
        return None

def make_juice(fruit, count):
    if fruit == '사과':
        return [('사과주스', count/4)]
    elif fruit == '바나나':
        return [('바나나스무디',count/2)]
    elif fruit == '레몬':
        return [('레모네이드',count/1)]
    else:
        return []


bottles = []
fresh_fruit = pick_fruit() # 해당 코드를 두 번 반복하게 되는데 별로 좋지 못하다. 
while fresh_fruit:
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
    fresh_fruit = pick_fruit() # 반복 사용

print(bottles)

bottles = []
while True: # 무한루프
    fresh_fruit = pick_fruit()  # 코드 재사용성을 높이기 위해 무한 루프-중간에서 끝내기 관용어를 사용하지만
    if not fresh_fruit: # 중간에서 끝내기
        break                   # while 루프 흐름 제어가 모두 break 문에 달려있다. while 루프를 맹목적으로 무한 루프로 만들기에 유용성이 떨어진다.

    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)

print(bottles)

bottles = []
while fresh_fruit := pick_fruit():  # 왈러스 연산자를 사용하면 무한 루프-중간에서 끝내기 관용어의 필요성이 줄어든다. 
    for fruit, count in fresh_fruit.items(): # 더 짧고 코드를 이해하기 쉽다. 가독성을 향상시키기 위해서라도 대입식을 도입하는 것을 고려해봐야 한다.
        batch = make_juice(fruit, count)
        bottles.extend(batch)

print(bottles)
