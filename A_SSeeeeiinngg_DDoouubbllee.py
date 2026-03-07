from collections import Counter
n = int(input())
for _ in range(n):
  word = input()
  freq = Counter(word)
  store = ""
  chars = []
  seen = set()
  for char in word:
    if char not in seen:
      chars.append(char)
      seen.add(char)
  po = dict(freq)

  for char in chars:
    if po[char] >= 2:
      if char == chars[0] and po[char] % 2 != 0:
        store += char
        po[char] -= 1
      take = 2
      store += char * take
      po[char] -=  take
    elif po[char] == 1:
      store += char
      po[char] -= 1
    
  for char in chars:
    if po[char] > 0:
      store += char * po[char]
      po[char] = 0
  res = store + store[::-1]

  print(res)