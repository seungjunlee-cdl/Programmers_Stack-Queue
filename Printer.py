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
