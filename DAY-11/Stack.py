# stack=[]
# stack.append(5)
# stack.append(6)
# print(stack)
# stack.pop()
# print(stack)

# stack.append(7)
# stack.append(4)
# print(stack,stack)
# print(stack[-1])
# print(len(stack)==0)

# stack=[5, 3, 8, 2, 9]
# l=len(stack)
# t=9
# for i in range(l):
#     if stack.pop() == t:
#         print("Found")
#         break

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets=={")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack:return False
                if stack.pop()==brackets[i]:
                    return False
        return len(stack)==0
                