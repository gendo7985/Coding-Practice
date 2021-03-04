# 완주하지 못한 선수


def solution(participant, completion):
    sortedParticipant = sorted(participant)
    sortedCompletion = sorted(completion)
    for i in range(len(sortedCompletion)):
        if sortedParticipant[i] != sortedCompletion[i]:
            return sortedParticipant[i]
    return sortedParticipant[-1]


if __name__ == "__main__":
    participants = [
        ["leo", "kiki", "eden"],
        ["marina", "josipa", "nikola", "vinko", "filipa"],
        ["mislav", "stanko", "mislav", "ana"],
    ]
    completions = [
        ["eden", "kiki"],
        ["josipa", "filipa", "marina", "nikola"],
        ["stanko", "ana", "mislav"],
    ]
    returns = ["leo", "vinko", "mislav"]

    for i in range(3):

        print(solution(participants[i], completions[i]) == returns[i])
