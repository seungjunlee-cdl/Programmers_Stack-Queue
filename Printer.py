Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def solution(priorities, location):
    wanted = [0 for i in range(len(priorities))]
    wanted[location] = 1

    printed = []
    printed_wanted = []

    while True:
        for i in range(1,len(priorities)):
            if (priorities[0] < max(priorities)):
                priorities.append(priorities[0])
                wanted.append(wanted[0])
                priorities.pop(0)
                wanted.pop(0)
            else:
                break

        printed.append(priorities[0])
        printed_wanted.append(wanted[0])
        priorities.pop(0)
        wanted.pop(0)

        if printed_wanted[-1] == 1:
            return len(printed_wanted)