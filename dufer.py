date = list(map(int, input().split()))
answ = []
for i in range(len(date) - 1):
    if abs(date[i]) % 4 == 0 and abs(date[i + 1]) % 4 == 0:
        answ.append(date[i] + date[i + 1])
print(len(answ), max(answ))