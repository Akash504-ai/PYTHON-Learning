s = "hello world python"
word = s.split()
for i in range(len(word)-1,-1,-1):
    print(word[i], end = " ")