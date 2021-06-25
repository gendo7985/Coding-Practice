# 파일명 정렬


def rename(file, pos):
    numpart = ""
    ind = 0
    for i in range(1, len(file)):
        if file[i].isdigit():
            if numpart == "":
                ind = i
                numpart += file[i]
            elif file[i - 1].isdigit():
                numpart += file[i]
    return (file[:ind].lower(), int(numpart), pos)


def solution(files):
    answer = sorted(files, key=lambda x: rename(x, files.index(x)))
    return answer