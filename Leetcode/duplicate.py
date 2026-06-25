s="priya"
t="Meghana"
if len(s)==len(t):
    print(False)

count={}
for char in s:
    count[char]=count.get(char,0)+1
print(count)    