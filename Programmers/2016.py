# 2016년

import datetime


def solution(a, b):
    week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    answer = datetime.date(2016, a, b).weekday()
    return week[answer]
