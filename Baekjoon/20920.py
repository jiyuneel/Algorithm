import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = set()
words_d = dict()

for _ in range(N):
    word = input().strip()
    if word in words:
        words_d[word] += 1
    elif len(word) >= M:
        words.add(word)
        words_d[word] = 1

words = sorted(words_d, key=lambda x:(-words_d[x], -len(x), x))

for w in words:
    print(w)
