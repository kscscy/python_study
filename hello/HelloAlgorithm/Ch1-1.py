#Ch1 Binary Search
def binary_search(list, item):
    low = 0                     # 탐색의 시작
    high = len(list) - 1        # 탐색의 끝

    while low <= high:
        mid = (low + high) // 2  # 가운데의 값

        guess = list[mid]

        if guess == item:       # 아이템을 찾음
            return mid

        if guess > item:        # 추측한 숫자가 큼
            high = mid - 1
        else:                   # 추측한 숫자가 작음
            low = mid + 1
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))