test_cases = int(input().strip())

for _ in range(test_cases):
    n = int(input().strip())
    array = list(map(int, input().split()))

    def is_sorted(arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True

    def mex_value(arr, n):
        present = set(arr)
        for x in range(n + 1):
            if x not in present:
                return x

    def first_wrong(arr):
        for i in range(n):
            if arr[i] != i:
                return i

    ops = []
    for _ in range(2 * n):
        if is_sorted(array):
            break

        mex = mex_value(array, n)

        if mex < n:
            array[mex] = mex
            ops.append(mex + 1)
        else:
            pos = first_wrong(array)
            array[pos] = mex
            ops.append(pos + 1)

    print(len(ops))
    print(*ops)