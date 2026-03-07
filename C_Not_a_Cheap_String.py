t = int(input())
for _ in range(t):
    w = input()
    p = int(input())
    
    current_price = sum(ord(c) - 96 for c in w)
    
    if current_price <= p:
        print(w)
        continue

    sorted_chars = sorted(w, reverse=True)
    
    to_remove = {}
    for char in sorted_chars:
        if current_price <= p:
            break
        
        to_remove[char] = to_remove.get(char, 0) + 1
        current_price -= (ord(char) - 96)
            
    result = []
    for char in w:
        if char in to_remove and to_remove[char] > 0:
            to_remove[char] -= 1
        else:
            result.append(char)
            
    print("".join(result))