n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

def region(x, y):
    return (x > ax, y > ay)

if region(bx, by) == region(cx, cy):
    print("YES")
else:
    print("NO")