###
### 아이템 3
###
a = b'h\x65llo'
print(list(a))
print(a)

a = 'a\u0300 propos'
print(list(a))
print(a)

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8') # 이진 데이터 > 유니코드 데이터
    else:
        value = bytes_or_str
    return value # str 인스턴스

print(repr(to_str(b'foo')))
print(repr(to_str('bar')))
print(repr(to_str(b'\xed\x95\x9c'))) # UTF-8에서 한글은 3바이트임

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8') # 유니코드 데이터 > 이진 데이터
    else:
        value = bytes_or_str
    return value # bytes 인스턴스

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))
print(repr(to_bytes('한글')))

# repr() 은 __repr__ 메소드를 호출하고, str() 이나 print 는 __str__ 메소드를 호출하도록 되어있는데, 
# __str__ 은 객체의 비공식적인(informal) 문자열을 출력할 때 사용하고, 
# __repr__ 은 공식적인(official) 문자열을 출력할 때 사용한다.

# 쉽게 말하면 __str__ 은 사용자가 보기 쉬운 형태로 보여줄 때 사용하는 것이고, 
# __repr__ 은 시스템(python interpreter)이 해당 객체를 인식할 수 있는 공식적인 문자열로 나타내 줄 때 사용하는 것이다.
# 그래서 eval(repr(object)) 를 하게 되면 해당 object 를 얻어올 수 있다.

print(b'one' + b'two')
print('one' + 'two')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# b'one' + 'two'   # TypeError : str과 bytes 인스턴스는 서로 더할 수 없다. 

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# 'one' + b'two'   # TypeError : 반대로도 마찬가지이다. 


assert b'red' > b'blue'
assert 'red' > 'blue'

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# assert 'red' > b'blue'  # TypeError : 서로 다른 타입의 인스턴스는 더하는 거 뿐만이 아니라 비교도 불가하다. 

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#assert b'blue' < 'red'  # TypeError

print(b'foo' == 'foo')  # 항상 false

print(b'red %s' % b'blue')  # 타입이 같은 형식화문자열 사용
print('red %s' % 'blue')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#print(b'red %s' % 'blue')   # TypeError : str 인스턴스를 bytes 형식화 문자열에 넘길 수 없다. 

print('red %s' % b'blue')   # 생각과 다르게 작동 : bytes 인스턴스를 str 형식화 문자열에 넘길 수는 있지만, 예상한 것과 다르게 작동한다. (__repr 메서드 관련 이슈)

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#with open('data.bin', 'w') as f:  # TypeError : 기본적으로 이진 바이트 타입이 아닌 유니코드 타입을 디폴트 값으로 기록하게 되어 있다. ('w' : 텍스트 모드)
#    f.write(b'\xf1\xf2\xf3\xf4\xf5')

with open('data.bin', 'wb') as f:  # ('wb' : 이진 쓰기 모드)로 변경하여야 이진 데이터를 파일에 기록할 수 있다.
    f.write(b'\xf1\xf2\xf3\xf4\xf5')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#with open('data.bin', 'r') as f:   # UnicodeDecodeError : ('r' : 텍스트 모드)
#    data = f.read()

with open('data.bin', 'rb') as f:   # ('rb' : 이진 읽기 모드)로 변경하여야 이진 데이터를 파일로부터 읽어들일 수 있다. 
    data = f.read()

assert data == b'\xf1\xf2\xf3\xf4\xf5'

with open('data.bin', 'r', encoding='cp1252') as f: # cp1252(윈도우에서 사용하던 레거시 인코딩). (encoding: ) 파라미터로 인코딩 방식을 명시해준다. 
    data = f.read()                                 # 인코딩 방식이 달라졌을 뿐인데, 기존 이진 데이터를 읽었을 때와는 다른 형태의 값이 반환되었다.
                                                    # 따라서 시스템의 디폴트 인코딩이 우리의 예상과는 다를 때는 아래의 시스템 인코딩 검사를 실시한다. 
assert data == 'ñòóôõ'

# 시스템 인코딩 검사: python3 -c 'import locale; print(locale.getpreferredencoding())'
