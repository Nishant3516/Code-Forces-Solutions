def longWord(values):
    if len(word) <= 10:
        return word
    return word[0] + str(len(word[1:-1])) + word[-1]


N = int(input())
for _ in range(N):
    word = input()
    print(longWord(word))
