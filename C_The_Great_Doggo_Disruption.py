n = int(input())
s = input().strip()

if n == 1:
    print("Yes")
else:
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1
    
    has_at_least_two = False
    for cnt in freq:
        if cnt >= 2:
            has_at_least_two = True
            break
    
    if has_at_least_two:
        print("Yes")
    else:
        print("No")