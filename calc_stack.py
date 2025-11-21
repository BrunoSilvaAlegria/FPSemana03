from collections import deque

stack = deque()
nums = input()
#nums.strip()
for num in nums.strip().split():
    stack.append(int(num)) #If it doesn't have the int(num), then numbers will appear with ' '. Ex:'2'; Also affects the multiplication, causing it to print a double string 22 instead of doubled int 4. It also doesn't print in the LIFO order.
print(stack)

while stack:    #True
    num = stack.pop() #This causes LIFO order
    print(num*2)