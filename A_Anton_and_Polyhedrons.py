freq = {"Tetrahedron":4, "Cube" : 6, "Octahedron" : 8, "Dodecahedron": 12, "Icosahedron": 20}
num = int(input())
arr = []
for i in range(num):
  arr.append(input())

count = 0

for i in arr:
  count += freq[i]
print(count)

