Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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