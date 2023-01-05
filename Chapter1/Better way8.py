
###
### 아이템 8
###


names = ['Cecilia', '남궁민수', '毛泽东']
counts = [len(n) for n in names]
print(counts)

longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)

longest_name = None
max_count = 0

for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)

longest_name = None
max_count = 0

for name, count in zip(names, counts): # zip은 둘 이상의 이터레이터를 지연 계산 제너레이터를 사용해 묶어준다. 
    if count > max_count:              # zip은 자신이 감싼 이터레이터 원소를 하나씩 소비하기에 메모리가 절약된다. 무한히 긴 입력에도 사용할 수 있다.
        longest_name = name
        max_count = count

print(longest_name)

names.append('Rosalind')
for name, count in zip(names, counts): # zip은 자신이 감싼 이터레이터 중 어느 하나가 끝날 때까지 튜플을 내놓는다. 
    print(name)

import itertools
for name, count in itertools.zip_longest(names, counts): # 리스트의 길이가 같지 않을 것으로 예상한다면 뒷부분을 버리지 않는 zip_longest를 쓰자
    print(f'{name}: {count}')                            # zip_longest의 fillvalue 파라미터 값을 전달하면 해당 값이 반환된다. 디폴트 값은 None이다. 

