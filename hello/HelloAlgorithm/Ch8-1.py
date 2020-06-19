# Ch8 Greedy algorithm

# 방송하고자 하는 주의 목록을 만들기
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])  # 배열을 넣으면 집합이 됩니다.

arr = [1, 2, 2, 3, 3, 3]
print(set(arr))  # {1,2,3}

# 선택된 방송국 목록 해시 테이블로 만들기
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# 방송국 목록을 저장할 집합
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()                                  # 아직 방송되지 않은 주 중에서 해당 방송국이 커버하는 주의 집합
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station        # 교집합
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)
    print(final_stations)

