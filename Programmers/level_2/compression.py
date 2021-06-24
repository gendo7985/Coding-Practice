# 압축


def solution(msg):
    ans = []
    dic = [chr(i) for i in range(64, 91)]
    while msg:
        pos, length = ord(msg[0]) - 64, 1
        for w in range(26, len(dic)):
            if len(dic[w]) > length and dic[w] == msg[: len(dic[w])]:
                pos, length = w, len(dic[w])
        ans.append(pos)
        dic.append(msg[: length + 1])
        msg = msg[length:]
    return ans