# 문자열 압축


def solution(s):
    if len(s) == 1:
        return 1
    answer = []
    for i in range(1, len(s) // 2 + 1):
        cut = [s[i * j : i * (j + 1)] for j in range(len(s) // i)]
        if len(s) % i != 0:
            cut.append(s[i * (len(s) // i) :])
        cnt = 1
        comp = cut[0]
        zipword = ""
        for i in range(1, len(cut)):
            if cut[i] == comp:
                cnt += 1
            else:
                if cnt == 1:
                    zipword += comp
                else:
                    zipword += str(cnt) + comp
                comp = cut[i]
                cnt = 1
        if cnt == 1:
            zipword += comp
        else:
            zipword += str(cnt) + comp
        answer.append(len(zipword))
    return min(answer)