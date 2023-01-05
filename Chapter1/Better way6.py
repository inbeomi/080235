###
### 아이템 6
###

snack_calories = {
    '감자칩': 140,
    '팝콘': 80,
    '땅콩': 190,
}
items = tuple(snack_calories.items())
print(items)

item = ('호박엿', '식혜')
first = item[0] # 숫자 인덱스로 접근 가능하다. 
second = item[1]
print(first, '&', second)

pair = ('약과', '호박엿')
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#pair[0] = '타래과'    # TypeError : 튜플은 값을 변경할 수 없다. 

item = ('호박엿', '식혜')
first, second = item # 언패킹. 이렇게 하면 한 문장 안에서 여러 값을 대입할 수 있다. 
print(first, '&', second)

favorite_snacks = {
    '짭조름한 과자': ('프레즐', 100),
    '달콤한 과자': ('쿠키', 180),
    '채소': ('당근', 20),
}

((type1, (name1, cals1)),
 (type2, (name2, cals2)),
 (type3, (name3, cals3))) = favorite_snacks.items()

print(f'제일 좋아하는 {type1} 는 {name1}, {cals1} 칼로리입니다.')
print(f'제일 좋아하는 {type2} 는 {name2},  {cals2} 칼로리입니다.')
print(f'제일 좋아하는 {type3} 는 {name3},  {cals3} 칼로리입니다.')

def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp

names = ['프레즐', '당근', '쑥갓', '베이컨']
bubble_sort(names)
print(names)

def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1] # 위와는 다르게 한 줄로도 두 원소를 서로 맞바꾸기


names = ['프레즐', '당근', '쑥갓', '베이컨']
bubble_sort(names)
print(names)

snacks = [('베이컨', 350), ('도넛', 240), ('머핀', 190)]
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f'#{i+1}: {name} 은 {calories} 칼로리입니다.')

for rank, (name, calories) in enumerate(snacks, 1):
    print(f'#{rank}: {name} 은 {calories} 칼로리입니다.') # 훨씬 파이썬다운 코드 방식이다. 명확하다.
 
# 파이썬 언패킹은 일반화돼 있으므로 모든 이터러블에 적용할 수 있다.
