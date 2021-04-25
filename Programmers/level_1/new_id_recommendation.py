# 신규 아이디 추천


def solution(new_id):
    answer = new_id.lower()
    for char in "~!@#$%^&*()=+[{]}:?,<>/":
        answer = answer.replace(char, "")
    while answer.find("..") != -1:
        answer = answer.replace("..", ".")
    answer = answer.strip(".")
    if answer == "":
        answer = "a"
    if len(answer) > 15:
        answer = answer[:15].strip(".")
    while len(answer) < 3:
        answer = answer + answer[-1]
    return answer


if __name__ == "__main__":
    testcases = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p"]
    results = ["bat.y.abcdefghi", "z--", "aaa", "123_.def", "abcdefghijklmn"]
    for i in range(5):
        print(solution(testcases[i]) == results[i])
