# 영어 끝말잇기


def test(done, word):
    if len(word) == 1:
        return False
    if done[-1][-1] != word[0]:
        return False
    if word in done:
        return False
    return True


def solution(n, words):
    done = [words[0]]
    for i in range(1, len(words)):
        if not test(done, words[i]):
            return [i % n + 1, i // n + 1]
        else:
            done.append(words[i])
    return [0, 0]