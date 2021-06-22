# 캐시


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    queue = []
    time = 0
    for city in cities:
        city = city.lower()
        if city in queue:
            time += 1
            queue.remove(city)
            queue.append(city)
        else:
            time += 5
            if len(queue) >= cacheSize:
                queue.pop(0)
            queue.append(city)

    return time