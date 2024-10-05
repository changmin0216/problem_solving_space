from collections import Counter
def solution(points, routes):

    def routing(route):
        path = []
        time = 0

        for i in range(len(route) - 1):
            sy, sx = points[route[i] - 1]
            ny, nx = points[route[i+1] - 1]

            while sy!=ny:
                path.append((sy, sx, time))
                if sy > ny:
                    sy -= 1
                else:
                    sy += 1
                time+=1
            while sx!=nx:
                path.append((sy, sx, time))
                if sx > nx:
                    sx -= 1
                else:
                    sx += 1
                time+=1
        path.append((sy, sx, time))
        return path

    robot_routes = []
    for route in routes:
        robot_routes.extend(routing(route))
    answer = 0
    counter = Counter(robot_routes)
    for v in counter.values():
        if v >= 2:
            answer += 1

    return answer

print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))