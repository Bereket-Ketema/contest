import sys

def solve():
    input = sys.stdin.readline
    n, capacity = map(int, input().split())

    small_boats = []
    big_boats = []

    for idx in range(1, n + 1):
        boat_type, boat_power = map(int, input().split())
        if boat_type == 1:
            small_boats.append((boat_power, idx))
        else:
            big_boats.append((boat_power, idx))

    small_boats.sort(reverse=True)
    big_boats.sort(reverse=True)

    pref_small = [0]
    for power, _ in small_boats:
        pref_small.append(pref_small[-1] + power)

    pref_big = [0]
    for power, _ in big_boats:
        pref_big.append(pref_big[-1] + power)

    best_score = 0
    best_big = 0
    best_small = 0

    max_big = min(len(big_boats), capacity // 2)

    for cnt_big in range(max_big + 1):
        used_space = 2 * cnt_big
        remaining = capacity - used_space
        cnt_small = min(len(small_boats), remaining)
        current_score = pref_big[cnt_big] + pref_small[cnt_small]

        if current_score > best_score:
            best_score = current_score
            best_big = cnt_big
            best_small = cnt_small

    chosen = []
    for i in range(best_big):
        chosen.append(big_boats[i][1])
    for i in range(best_small):
        chosen.append(small_boats[i][1])

    print(best_score)
    print(*chosen)

if __name__ == "__main__":
    solve()