graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque

# search_queue = deque()                          # 새 큐를 생성
# search_queue += graph["you"]                    # 모든 이웃을 탐색 큐에 추가
#
def person_is_seller(name):
    return name[-1] == 'm'                      # 사람 이름이 m자로 끝나는지 확인. m 자로 끝나는 사람이 망고 판매상!
#
# while search_queue:                             # 큐가 비어 있지 않는 한 계속 실행
#     person = search_queue.popleft()             # 큐의 첫 번째 사람을 꺼냄
#     if person_is_seller(person):                # 망고 판매상인지 확인
#         print(person + " is a mango seller!")   # 망고 판매상이 맞음
#         return True
#     else:
#         search_queue += graph[person]           # 망고 판매상이 아님. 모든 이웃을 탐색 목록에 추가
# return False                                    # 여기에 도달했다는 것은 망고 판매상이 아무도 없다는 의미

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []                                 # 이 배열은 이미 확인한 사람을 추적하기 위한 것
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:                # 이전에 확인하지 않은 사람만 확인
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)           # 이 사람을 확인한 것으로 표시
    return False

search("you")