N = int(input())
options = []
quick = set()
for i in range(N):
    words = input().split()
    for j in range(len(words)):
        if words[j][0].lower() not in quick:
            quick.add(words[j][0].lower())
            words[j] = "[" + words[j][0] + "]" + words[j][1:]
            options.append(" ".join(words))
            break
    else:
        words = " ".join(words)
        for c in range(len(words)):
            if words[c] == " ":
                continue
            if words[c].lower() not in quick:
                quick.add(words[c].lower())
                words = words[:c] + "[" + words[c] + "]" + words[c+1:]
                options.append(words)
                break
        else:
            options.append(words)
for option in options:
    print(option)


# 문제 : 백준 - 1283번 단축키 지정
# 유형 : 구현