def solution(X, Y):
    same = []
    ylist = []
    for i in range(len(Y)):
        ylist.append(Y[i])
    for x in X:
        if x in ylist:
            same.append(x)
            ylist.remove(x)
    if answer[0] == "0":
        return "0"
    if len(same) == 0:
        return "-1"
    same.sort(reverse=True)
    answer = int(''.join(map(str, same)))
    return str(answer)
