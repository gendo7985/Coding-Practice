# 키패드 누르기


def solution(numbers, hand):
    left, right = 10, 12
    ans = ""
    for n in numbers:
        if n in [1, 4, 7]:
            left = n
            ans += "L"
        elif n in [3, 6, 9]:
            right = n
            ans += "R"
        else:
            if n == 0:
                n = 11
            pt_l = ((left + 2) // 3, (left + 2) % 3)
            pt_r = ((right + 2) // 3, (right + 2) % 3)
            pt_n = ((n + 2) // 3, (n + 2) % 3)
            if abs(pt_l[0] - pt_n[0]) + abs(pt_l[1] - pt_n[1]) < abs(pt_r[0] - pt_n[0]) + abs(
                pt_r[1] - pt_n[1]
            ):
                left = n
                ans += "L"
            elif abs(pt_l[0] - pt_n[0]) + abs(pt_l[1] - pt_n[1]) > abs(pt_r[0] - pt_n[0]) + abs(
                pt_r[1] - pt_n[1]
            ):
                right = n
                ans += "R"
            else:
                if hand == "left":
                    left = n
                    ans += "L"
                else:
                    right = n
                    ans += "R"
    return ans

