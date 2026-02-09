n = int(input())
for i in range(n):
  size = int(input())
  year = input()
  if "2025" in year and "2026" not in year:
    print(1)
  else:
    print(0)