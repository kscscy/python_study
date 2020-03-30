"""
print('hello world')

print('"isn\'t"')

print('test \ntest')

# r 은 raw string
print(r'C:\test\test')

# 삼중 싱글/더블 쿼트는 줄넘김 문자열
print('''
      a
      b
      c
      ''')

#곱하기 만큼 반복, 더하기는 연결
print(3 * 'a' + 'b')

# 쿼트 연속 사용시 문자열 연결
print('te''st')

ㅁ = 'test'
ㅁ += '1'
ㅁ += 'ㅅㄷㄴㅅ'
print(ㅁ)
print(ㅁ[1], ㅁ[3])
# 음수 index 는 문자열 뒤에서부터 센다
print(ㅁ[-1], ㅁ[-3])

# 문자열 substring 
print(ㅁ[2:5])
# 음수 index 가 시작점 보다 크면 공백 리턴
print(ㅁ[2:-1])

# substring 의 시작과 종료만 표기하는 경우
print(ㅁ[:2])
print(ㅁ[2:])

#print[999]
print(len(ㅁ))
"""

"""
arr = [1,4,9,16,25]
print(arr)
print(arr[1], arr[-1], arr[-3:])

# shallow copy
print(arr[:])

print(arr + [36,49,64,81,100])

arr2 = [1,8,27,65,125]
print(4**3)

arr2[3] = 64

arr2.append(216)
# **3제곱
arr2.append(7**3)

print(arr2)
"""

"""
let = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(let)

let[2:5] = ['C','D','E']
print(let)

let[2:5] = []
print(let)

print(len(let))
"""

"""
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print(x)
print(x[0])
print(x[0][1])
"""

"""
# 다중 대입
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

a, b = 0, 1
while a < 1000:
    print(a, end=',')  # 출력 끝에 포함되는 개행문자를 제거하거나 출력을 다른 문자열로 끝나게 하고 싶을 때
    a, b = b, a + b
"""

"""
x = int(input("please enter an integer: "))
if x < 0:
    x = 0
    print(x, ':Negative changed to zero')
elif x == 0: #else if
    print(x, ':Zero')
elif x == 1:
    print(x, ':Single')
else:
    print('More')
"""

"""
words =['cat','window','defenestrate']
for w in words:
    print(w, len(w))
"""

"""
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        
active_users = {}
for user,status in users.items():
    if status == 'active':
        active_users[user] = status
"""

"""
for i in range(5):
    print(i)

for i in range(5,10):
    print(i)    
for i in range(0,10,3):
    print(i)
    
for i in range (-10, -100, -30):
    print(i)
#많은 경우에 range()가 돌려준 객체는 리스트인 것처럼 동작하지만, 사실 리스트가 아닙니다. 이터레이트할 때 원하는 시퀀스 항목들을 순서대로 돌려주는 객체이지만, 실제로 리스트를 만들지 않아서 공간을 절약합니다.

print(sum(range(4))) # 0+1+2+3

print(list(range(4))) 
# range 에서 list 얻기
"""

"""
for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
        

for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
"""

"""
def funcname(self, parameter_list):
    pass 
    #pass문은 아무것도 하지 않습니다. 문법적으로 문장이 필요하지만, 특별히 할 일이 없을 때 사용할 수 있다.
    #최소한의 클래스를 만들 때, 새 코드를 작업할 때 함수나 조건부 바디의 자리를 채우기
"""

"""
def fib(n):
    a,b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a+b
    print()
    
fib(10000)
f = fib
f(10)
f(0)
print(fib(0)) #None이 출력할 유일한 값이라면, 인터프리터는 None값 출력을 억제
"""

"""
def fib2(n):
    result = []
    a,b = 0,1
    while a < n:
        # 메서드 append()는 리스트 객체들에 정의되어 있습니다; 요소를 리스트의 끝에 덧붙입니다. 이 예에서는 result = result + [a] 와 동등하지만, 더 효율적입니다.
        result.append(a)
        a,b = b, a+b
    return result
f100 = fib2(100)
print(f100)
"""

"""
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
"""

"""
i = 5

def f(arg=i):
    print(arg)
    
i = 6
f() # 출력 5
"""

"""
def f(a, L=[]):
    L.append(a)
    return L

print(f(0))
print(f(1))
print(f(2))
print(f(3))
"""

"""
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(0))
print(f(1))
print(f(2))
print(f(3))
# 선언부 차이로 인함 > 연속된 호출 간에 기본값이 공유되지 않음
"""

"""
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
# 하나의 필수인자 (voltage) 와 세개의 선택적 인자 = 를 받음
#parrot(100)
#parrot(voltage=1000)
#parrot(voltage=1000, action='VOOOOOOOOOOOOOOOOM')
#parrot(action='VOOOOOOOOOOOOOOOOOOm', voltage=100)
#parrot('a million', 'bereft of life', 'jump','mewwwwwww')
#parrot('a thousand', state='pushing up the daisies')


#invalid parameteres
#parrot()
#parrot(voltage=5.0, 'dead')  # positional argument follows keyword argument
#parrot(110, voltage=220)  # multiple values for argument 'voltage'
#parrot(test='123')  # an unexpected keyword argument 'test'
"""
"""
def function(a):
    pass

#function(0, a=0) #어떤 인자도 두 개 이상의 값을 받을 수 없다.
"""

"""
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
# 인쇄되는 키워드 인자들의 순서 함수 호출로 전달된 순서와 일치함이 보장됨에 주목하세요.


# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

#dictionary, tuple 차이
cheeseshop("test burger", "go home")
cheeseshop("test burger", test="go home")
"""

"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass

#pos1, pos2, 함수 정의에 /나 *가 없으면, 인자를 "위치" 나 "키워드" 로 함수에 전달할 수 있다.
#위치 전용 매개변수는 / 앞에 놓인다. 함수 정의에 / 가 없으면 위치 전용 매개변수는 없다.
# / 다음의 매개변수는 위치-키워드나 (pos_or_kwd) 키워드 전용일 수 있다. (kwd1, kwd2)
# * 매개변수를 키워드 전용으로 표시하려면, 첫 번째 키워드 전용 매개변수 앞 인자에 *를 넣는다.
def standard_arg(arg):
    print(arg)
    
def pos_only_arg(arg, /):
    print(arg)
    
def kwd_only_arg(*, arg):
    print(arg)
    
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
    
standard_arg(2)
standard_arg(arg=2)

pos_only_arg(1)
#pos_only_arg(arg=1) #some positional-only arguments passed as keyword arguments: 'arg'

#kwd_only_arg(3)  # takes 0 positional arguments but 1 was given
kwd_only_arg(arg=3)

combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)

"""

"""
def foo(name, **kwds):
    return 'name' in kwds
foo(1, **{'name':2})
#'name' 키워드는 항상 첫 번째 매개변수에 결합하므로 True 를 반환할 수 있느 호출은 불가능
def bar(name, /, **kwds):
    return 'name' in kwds
print(bar(1, **{'name':2}))

#그러나 /(위치 전용 인자)를 사용하면, name을 위치 인자로, 동시에 'name'을 키워드 인자의 키로 사용할 수 있으므로 가능합니다:

# *args 는 함수의 파라미터를 tuple로 저장하고 있습니다.
# **kwargs는 keyword argument를 dictionary로 저장하고 있습니다(단,formal parameter를 제외)


def foo(keyword=3, **kwargs):
    for key in kwargs:
        print (key, kwargs[key])


print ("---foo()---")
foo()

print ("\n---foo(number = 'one')---")
foo(number='one')

print ("\n---foo(keyword='1', temp1='hello', temp2='world!')---")
foo(keyword=1, temp1='hello', temp2='world!')

def foo(num1, num2):
    print (num1, num2)


l = [1, 2]
foo(*l)  # ([1,2])가 아닌 (1,2)로 전달
"""

"""
#보통 가변 길이 인자들은 형식 매개변수 목록의 마지막에 온다.
def concat(*args, sep="/"):
    return sep.join(args)

test = concat("earth", "mars", "venus")
print(test)

test2 = concat("earth", "mars", "venus", sep="+")
print(test2)
"""

"""
a = list(range(3,6))
print(a)
print("--"*20)
args = [3,6]
print(list(args))
print(list(range(*args))) # 튜플로부터 인자 언패킹
"""

"""
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM!"}
parrot(d)
print("--*"*20)
parrot(*d)
print("--*"*20)
parrot(**d)
"""

"""
# lambda 키워드를 사용해서 작고 이름 없는 함수를 만들 수 있다.
# 문법적으로는 하나의 표현식으로 제한된다. 의미적으로는 일반적인 함수 정의 편의 문법
# 람다 함수는 둘러싸는 스코프에 있는 변수들을 참조할 수 있다.
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
print(f(1))
"""

"""
# lambda 인자 : 표현식
# 작은 함수를 인자로 전달하는것?
pairs = [(1,'one'), (2,'two'), (3,'three'), (4,'four')]
print(pairs)
pairs.sort(key=lambda pair: pair[1]) # 2번째 인자 정렬
print(pairs)
"""

# 함수 어노테이션은 사용자 정의 함수가 사용하는 형들에 대한 선택적인 메타데이터 정보
# 어노테이션은 함수의 __annotations__ 어트리뷰트에 Dictionary 형태로 저장
# 매개변수 어노테이션은 매개변수 이름 뒤에 오는 콜론으로 정의, 값을 구할 때 어노테이션의 값을 주는 표현식이 뒤따름
# 반환 값 어노테이션은 리터럴 -> 와 그 뒤를 따르는 표현식으로 정의. 매개변수 목록과 def 문의 끝을 나타내는 콜론 사이에 놓임
def f(ham: str, eggs: str = 'eggs') -> str: # -> str: 반환값 어노테이션
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + 'and ' + eggs
f('spam')