#
# 아이템 15
#

baby_names = {
    'cat': 'kitten',
    'dog': 'puppy',
}
# 파이써 3.5에서는 {'dog': 'puppy', 'cat': 'kitten'}가 출력되지만 3.7 이후에서는 {'cat': 'kitten', 'dog': 'puppy'}
print(baby_names)

print(list(baby_names.keys()))
print(list(baby_names.values()))
print(list(baby_names.items()))
print(baby_names.popitem()) # 파이썬 3.5에서는 아무 원소나 하나를 선택해 출력되지만, 파이썬 3.7이후에서는 마지막에 삽입된 원소

def my_func(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

my_func(goose='gosling', kangaroo='joey') # 3.5와 3.7이후가 다름 : 3.7 이후에는 키워드 인자가 넣은 순서대로 나오게 된다.

class MyClass:
    def __init__(self):
        self.alligator = 'hatchling'
        self.elephant = 'calf'

a = MyClass()
for key, value in a.__dict__.items(): # 클래스도 인스턴스 딕셔너리에 dict 타입을 사용하는데 파이썬 3.7 이후로 삽입 순서를 유지하게 된다. 
    print(f'{key} = {value}')

# 이전에는 삽입 순서를 유지해주는 OrderDict 클래스를 활용하곤 했다. 지금은 표준 dict의 동작과 비슷하지만 성능 특성은 다르다.
# 만약, 키 삽입과 popitem 호출을 자주 처리한다면 표준 dict보다는 OrderDict가 더 낫다. 
    
votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863,
}

def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner(ranks):
    return next(iter(ranks))

ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)

from collections.abc import MutableMapping

class SortedDict(MutableMapping): # collections.abc 묘듈을 사용해 딕셔너리외 비슷하지만 내용을 알파벳 순서대로 이터레이션해주는 클래스를 새로 정의할 수 있다.
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)


sorted_ranks = SortedDict() # SortedDict는 표준 딕셔너리의 프로토콜을 지킨다. 그래서 오류는 나지 않지만 실행 결과는 요구 사항에 맞지 않는다. 
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)

def get_winner(ranks):
    for name, rank in ranks.items(): # 딕셔너리가 어떤 특정 순서로 이터레이션 된다고 생각하지 않고도 원하는 값을 반환하도록 하는 방식. 
        if rank == 1:
            return name

winner = get_winner(sorted_ranks)
print(winner)

def get_winner(ranks):
    if not isinstance(ranks, dict):  # 아니면 표준 딕셔너리 타입으로 들어올 수 있도록 예외를 던지는. 
        raise TypeError('dict 인스턴스가 필요합니다') # 앞의 것보다 실행 성능은 더 좋을 것이다. 
    return next(iter(ranks))


from typing import Dict, MutableMapping # 타입 어노테이션을 붙이고 mypy 도구를 엄격한 모드(strict)로 실행해서 버그를 최대한 없앤다. 
                                        # $ python3 -m mypy --strict example.py
                                        # 이 방식은 적절한 타입의 객체를 사용하지 않았을 대 오류를 발생시킨다. 

def populate_ranks(votes: Dict[str, int],
                   ranks: Dict[str, int]) -> None: # 아니면 Type Annotation을 사용해서 MutableMapping 인스턴스가 아닌 Dict 인스턴스가 강제되도록 한다.
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True) # dict.get을 쓰면 디폴트 값은 None 처리가 되니 dict를 key값으로만 다루기 좋은. 
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))

class SortedDict(MutableMapping[str, int]):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)
