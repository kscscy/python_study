#Ch7 Dijkstra's algorithm
# 전체 그래프를 해시테이블로 만들기
graph = {}

# 간선들의 가중치
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

print(graph["start"].keys())
print(graph["start"]["a"])      # 6
print(graph["start"]["b"])      # 2

# 그래프의 나머지 정점과 그 이웃
graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}               # 도착점에는 이웃이 없습니다.

infinity = float("inf")         # 무한대
print(infinity)

# 가격표
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 부모를 위한 해시 테이블
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 이미 처리한 정점을 추적하기 위한 배열
processed = []

"""
모든 정점을 처리할 때까지 반복한다.
출발점에서 가장 가까운 정점을 찾는다.
이웃 정점의 가격을 갱신한다.
만약 이웃 정점의 가격을 갱신하면 부모도 갱신한다.
해당 정점을 처리했다는 사실을 기록한다.
"""

# 가장 싼 정점을 찾는 함수 (python 은 hoisting 안되는 것인가)
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:                      # 모든 정점을 확인합니다.
        cost = costs[node]                  # 아직 처리하지 않은 정점 중 더 싼 것이 있으면
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost              # 새로운 최저 정점으로 설정합니다.
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)         # 아직 처리하지 않은 가장 싼 정점을 찾습니다.
while node is not None:                     # 모든 정점을 처리하면 반복문이 종료됩니다.
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():              # 모든 이웃에 대해 반복합니다.
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:             # 만약 이 정점을 지나는 것이 가격이 더 싸다면
            costs[n] = new_cost             # 정점의 가격을 갱신하고
            parents[n] = node               # 부모를 이 정점으로 새로 설정합니다.
    processed.append(node)                  # 정점을 처리한 사실을 기록합니다.
    node = find_lowest_cost_node(costs)     # 다음으로 처리할 정점을 찾아 반복합니다.


