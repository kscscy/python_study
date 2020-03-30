"""
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))
print(fruits.count('cat'))

print(fruits.index('banana'))
print(fruits.index('banana',4)) # 배열의 4번 이후에 오는 banana 는 몇번째인가

fruits.reverse()
print('after reverse: ', fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop())
print(fruits)

print(fruits.pop())
print(fruits)
"""

"""
# 리스트 메서드들은 리스트를 스택으로 사용하기 쉽게 만드는데, 마지막에 넣은 요소가 처음으로 꺼내지는 요소입니다 (《last-in, first-out》). 
# 스택의 꼭대기에 항목을 넣으려면 append() 를 사용하세요. 스택의 꼭대기에서 값을 꺼내려면 명시적인 인덱스 없이 pop() 을 사용하세요.
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

print(stack.pop())
print(stack)
stack.pop()
stack.pop()
print(stack)
"""
"""
from collections import deque
queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")
queue.append("Graham")
print(queue)

print(queue.popleft())
print(queue)
queue.popleft()
print(queue)
"""

"""
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

"""

"""
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y)) # 표현식이 튜플이면 반드시 괄호로 둘러싸야 한다.
print(combs)
"""

vec = [-4, -2, 0, 2, 4]

print([x * 2 for x in vec])
# [-8, -4, 0, 4, 8]

print([x for x in vec if x >= 0])
# [0, 2, 4]

print([abs(x) for x in vec])
# [4, 2, 0, 2, 4]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

print([weapon.upper() for weapon in freshfruit])