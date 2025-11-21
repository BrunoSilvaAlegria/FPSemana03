from collections import deque

queue = deque()
words = input()

for word in words.strip().split():
    queue.appendleft(word)
print(queue)

while queue:
    wrd = queue.pop()
    if "a" in wrd:
        print(wrd)