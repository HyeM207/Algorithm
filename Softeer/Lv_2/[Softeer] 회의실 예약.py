# lv2
import sys
r, n = map(int, input().split())
rooms = {}
for _ in range(r):
    rooms[input()] = []

for _ in range(n):
    name, start, end = input().split()
    start = int(start)
    end = int(end)
    rooms[name].append([start, end])

# 정렬
for name in rooms.keys():
    rooms[name] = sorted(rooms[name], key=lambda x : x[0] )
rooms = dict(sorted(rooms.items()))

for room, reserv in rooms.items():
    print(f"Room {room}:")
    if not reserv:
        print("1 available:")
        print("09-18")
    else:
        # 계산
        result = []
        prev = 9
        for start, end in reserv:
            if start > prev:
                result.append([prev, start])
            prev = end
        if end < 18:
            result.append([end, 18])
        if len(result) == 0 :
            print("Not available")
        else:
            print(len(result), "available:")
            for start, end in result:
                print("%02d-%02d"%(start, end))
    if room != list(rooms.keys())[-1]:
        print("-----")