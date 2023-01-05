###
### 아이템 4
###

a = 0b10111011
b = 0xc5f
print('이진수: %d, 십육진수: %d' % (a, b)) # %d : 십진수로 표시할 때 사용

key = 'my_var'
value = 1.234
formatted = '%-10s = %.2f' % (key, value)
print(formatted)

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#reordered_tuple = '%-10s = %.2f' % (value, key)  # TypeError : % 타입 순서와 데이터 순서가 다르면 데이터의 타입 변환이 불가능하다. 

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#reordered_string = '%.2f = %-10s' % (key, value) # TypeError

pantry = [
    ('아보카도', 1.25),
    ('바나나', 2.5),
    ('체리', 15),
]
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (i, item, count))
    
    
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %d' % (
        i + 1,
        item.title(), # title : 단어의 앞만 대문자로 바꿔주는 함수
        round(count)))

template = '%s는 음식을 좋아해. %s가 요리하는 모습을 봐요.'
name = '철수'
formatted = template % (name, name)
print(formatted)

name = '영희'
formatted = template % (name.title(), name.title())
print(formatted)

key = 'my_var'
value = 1.234

old_way = '%-10s = %.2f' % (key, value)

new_way = '%(key)-10s = %(value).2f' % {
    'key': key, 'value': value} # 원래 방식
    
reordered = '%(key)-10s = %(value).2f' % {
    'value': value, 'key': key} # 바꾼 방식
    
assert old_way == new_way == reordered

name = '철수'
template = '%s는 음식을 좋아해. %s가 요리하는 모습을 봐요.'

before = template % (name, name)  # 튜플
template = '%(name)s는 음식을 좋아해. %(name)s가 요리하는 모습을 봐요.'
after = template % {'name': name} # 딕셔너리

assert before == after

for i, (item, count) in enumerate(pantry):
    before = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count))
    after = '#%(loop)d: %(item)-10s = %(count)d' % {
        'loop': i + 1,
        'item': item.title(),
        'count': round(count),
    } # 각 키를 최소 두 번 반복하게 된다. (한 번은 형식 지정자에, 다른 한 번은 딕셔너리 키에) 이는 가독성을 해친다. 
    
    assert before == after

soup = 'lentil'
formatted = 'Today\'s soup is %(soup)s.' % {'soup': soup}  # \'를 보여주기 위해 일부러 원서 코드를 그대로 남겨둠
print(formatted)

# 위 Today..를 영어로 남겨뒀기 때문에 나머지 예제에서도 스프 관련 부분은 영어로 남겨둠
menu = {
    'soup': 'lentil',
    'oyster': 'tongyoung',
    'special': 'schnitzel',
}
template = ('Today\'s soup is %(soup)s, '
            'buy one get two %(oyster)s oysters, '
            'and our special entrée is %(special)s.')
formatted = template % menu
print(formatted)

#
# 내장 함수 format과 str.format
#

a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)

b = 'my 문자열'
formatted = format(b, '^20s')
print('*', formatted, '*')

key = 'my_var'
value = 1.234

formatted = '{} = {}'.format(key, value) # 순서가 같은 위치에 있는 인자를 가리킨다. 
print(formatted)

formatted = '{:<10} = {:.2f}'.format(key, value) # 콜론(:) 뒤에 형식 지정자를 붙여준다. 모든 형식 지정자에 대한 정보를 보고 싶으면 help('FORMATTING') 를 참고하라.
print(formatted)                                 # {:.2f}는 format(value, '.2f')와도 같다. 

print('%.2f%%' % 12.5) # %를 나타내고 싶다면 %%로 이스케이프해야 한다.
print('{} replaces {{}}'.format(1.23)) # str.format을 사용할 때는 중괄호를 이스케이프해야 한다. 


formatted = '{1} = {0}'.format(key, value) # 중괄호 안에 위치 인덱스를 지정해줄 수도 있다. 
print(formatted)

name = '철수'
formatted = '{0}는 음식을 좋아해. {0}가 요리하는 모습을 봐요.'.format(name) # 동일한 위치 인덱스를 여러 번 사용할 수 있다. 
print(formatted)

for i, (item, count) in enumerate(pantry):
    old_style = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count))
        
    new_style = '#{}: {:<10s} = {}'.format(
        i + 1,
        item.title(),
        round(count))   # 이러한 방식도 마찬가지로 가독성은 좋지 못하다. 
        
    assert old_style == new_style

formatted = '첫번째 글자는 {menu[oyster][0]!r}'.format( 
    menu=menu) # 위와 같이 딕셔너리 키나 리스트 인덱스를 조합해 위치 지정자에 사용하거나 값을 유니코드나 repr 문자열로 변환하는 등의 고급 옵션이 있다. 
print(formatted)

old_template = (
    'Today\'s soup is %(soup)s, '
    'buy one get two %(oyster)s oysters, '
    'and our special entrée is %(special)s.')
old_formatted = template % {
    'soup': 'lentil',
    'oyster': 'tongyoung',
    'special': 'schnitzel',
}

new_template = (
    'Today\'s soup is {soup}, '
    'buy one get two {oyster} oysters, '
    'and our special entrée is {special}.')
new_formatted = new_template.format(
    soup='lentil',
    oyster='tongyoung',
    special='schnitzel',
)

assert old_formatted == new_formatted # 결국 str.format 메서드는 사용하지 말 것을 권한다. 그러나 여기의 아이디어가 일부 f-문자열의 동작과 유용성을 이해하는 데 도움을 준다. 

#
# 인터폴레이션 
#

# 바이트 문자열 앞에는 b문자를 붙이고, raw 문자열에는 r문자를 붙이는 것처럼 이러한 문자열에는 f문자를 붙인다.
formatted = f'{key!r:<10} = {value:.2f}'  # !r : 아마도 repr 문자열로 변환하는 것 같다. 
print(formatted)

f_string = f'{key:<10} = {value:.2f}'

c_tuple  = '%-10s = %.2f' % (key, value)

str_args = '{:<10} = {:.2f}'.format(key, value)

str_kw   = '{key:<10} = {value:.2f}'.format(key=key,
                                            value=value)

c_dict   = '%(key)-10s = %(value).2f' % {'key': key,
                                         'value': value}

assert c_tuple == c_dict == f_string
assert str_args == str_kw == f_string

for i, (item, count) in enumerate(pantry):
    old_style = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count))
        
    new_style = '#{}: {:<10s} = {}'.format(
        i + 1,
        item.title(),
        round(count))
        
    f_string = f'#{i+1}: {item.title():<10s} = {round(count)}'
        
    assert old_style == new_style == f_string

for i, (item, count) in enumerate(pantry):
    print(f'#{i+1}: '
    f'{item.title():<10s} = '
    f'{round(count)}')

places = 3
number = 1.23456
print(f'내가 고른 숫자는 {number:.{places}f}') # 형식 옵션값을 하드코딩하는 대신 변수를 사용해 형식 문자열 안에 파라미터화했다. 
