import sys
input = sys.stdin.readline

def solve_case():
    n = int(input())
    people = [tuple(map(int, input().split())) for _ in range(n)]

    people.sort()

    end_positions = [p[1] for p in people]
    temp_array = [0] * n

    def count_greetings(left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2

        total = count_greetings(left, mid)
        total += count_greetings(mid + 1, right)

        i = left
        j = mid + 1
        k = left

        while i <= mid and j <= right:
            if end_positions[i] <= end_positions[j]:
                temp_array[k] = end_positions[i]
                i += 1
            else:
                total += (mid - i + 1)
                temp_array[k] = end_positions[j]
                j += 1
            k += 1

        while i <= mid:
            temp_array[k] = end_positions[i]
            i += 1
            k += 1

        while j <= right:
            temp_array[k] = end_positions[j]
            j += 1
            k += 1

        for idx in range(left, right + 1):
            end_positions[idx] = temp_array[idx]

        return total
    return count_greetings(0, n - 1)


t = int(input())
for _ in range(t):
    print(solve_case())