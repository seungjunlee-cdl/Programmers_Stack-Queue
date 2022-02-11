def solution(progresses, speeds):
    pub = []

    while len(progresses) > 0:
        if progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        else:
            cnt=0
            for i in range(len(progresses)):
                if progresses[0] >= 100:
                    cnt += 1
                    progresses.pop(0)
                    speeds.pop(0)
                else:
                    break
            pub.append(cnt)
    return pub
