#
# 아이템 13
#
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#oldest, second_oldest = car_ages_descending

oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldest, others)

oldest, second_oldest, *others = car_ages_descending # 별표 식(starred expression(을 사용해 모든 값을 담는 언패킹을 사용하자. 
print(oldest, second_oldest, others)                 # 이 구문을 사용하면 언패킹 패턴의 다른 부분에 들어가지 못하는 모든 값을 별이 붙은 부분에 다 담을 수 있다.

oldest, *others, youngest = car_ages_descending      # 다른 위치에도 쓸 수 있다. 
print(oldest, youngest, others)

*others, second_youngest, youngest = car_ages_descending
print(youngest, second_youngest, others)

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#*others = car_ages_descending : 별표 식이 포함된 언패킹 대입을 처리하려면 필수인 부분이 적어도 하나는 있어야 한다. 별표 식만 사용해 언패킹할 수는 없다. 

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#first, *middle, *second_middle, last = [1, 2, 3, 4] : 또한 한 수준의 언패킹 패턴에 별표 식을 두 개 이상 쓸 수도 없다. 

car_inventory = {
    '시내': ('그랜저', '아반테', '티코'),
    '공항': ('제네시스 쿠페', '소나타', 'K5', '악센트'),
}

((loc1, (best1, *rest1)), 
 (loc2, (best2, *rest2))) = car_inventory.items() # 여러 계층으로 이뤄진 구조를 언패킹할 때는 서로 다른 부분에 포함되는 한, 별표 식을 여럿 사용해도 된다. 
print(f'{loc1} 최고는 {best1}, 나머지는 {len(rest1)} 종') # 그러나, 그리 권장하지는 않는다. 
print(f'{loc2} 최고는 {best2}, 나머지는 {len(rest2)} 종')

short_list = [1, 2]
first, second, *rest = short_list # 별표 식은 항상 list 인스턴스가 된다. 여기에서는 빈 리스트가 별표 식에 담긴다. 
print(first, second, rest)

it = iter(range(1, 3))
first, second = it
print(f'{first} & {second}')

def generate_csv():
    yield ('날짜', '제조사' , '모델', '연식', '가격')
    for i in range(100):
        yield ('2019-03-25', '현대', '소나타', '2010', '2400만원')
        yield ('2019-03-26', '기아', '프라이드', '2008', '1400만원')

all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print('CSV 헤더:', header)
print('행 수: ', len(rows))

it = generate_csv()
header, *rows = it # 별표 식으로 언패킹하면 이터레이터가 내보내는 내용을 쉽게 나눠서 처리할 수 있다. 
print('CSV 헤더:', header)    # 이터레이터를 별표 식으로 언패킹하면 컴퓨터 메모리를 다 사용해서 프로그램이 멈출 수 있다. 
print('행 수: ', len(rows))   # 따라서 결과 데이터가 모두 메모리에 들어갈 수 있다고 확신할 때만 나머지를 모두 잡아내는 언패킹을 사용해야 한다. 
