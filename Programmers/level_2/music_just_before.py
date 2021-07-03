# 방금그곡


def solution(m, musicinfos):
    music = "(None)"
    maxtime = 0
    sharps = [chr(i) + "#" for i in range(65, 72)]
    for note in sharps:
        m = m.replace(note, note[0].lower())
    for musicinfo in musicinfos:
        info = musicinfo.split(",")
        time = (int(info[1][:2]) - int(info[0][:2])) * 60 + int(info[1][3:]) - int(info[0][3:])
        title = info[2]
        for note in sharps:
            info[3] = info[3].replace(note, note[0].lower())
        melody = (info[3] * (time // (len(info[3])) + 1))[:time]
        if m in melody:
            if time > maxtime:
                music = title
                maxtime = time
    return music