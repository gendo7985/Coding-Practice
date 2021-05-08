# 오픈채팅방


def solution(record):
    answer = []
    userdata = {}
    for i in record:
        data = i.split()
        if data[0] in ["Enter", "Change"]:
            userdata[data[1]] = data[2]
    for i in reversed(record):
        data = i.split()
        if data[0] == "Leave":
            answer.append(userdata[data[1]] + "님이 나갔습니다.")
        elif data[0] == "Enter":
            answer.append(userdata[data[1]] + "님이 들어왔습니다.")
    return answer[::-1]