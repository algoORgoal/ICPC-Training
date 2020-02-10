count_rope = int(input())
w = list()


for i in range(count_rope):
    w.append(int(input()))

w.sort()
# print(w)

max_w = list()

count_used_rope = 0
while w:
    used_rope = w.pop()
    count_used_rope += 1
    max_w.append(used_rope * count_used_rope)

answer = max_w[0]
for i in max_w:
    if answer < i:
        answer = i
print(answer)
