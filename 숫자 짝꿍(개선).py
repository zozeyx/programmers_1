def solution(X, Y):
    answer = []
    for i in (set(X)&set(Y)) : #교집합 원소 구하기
        for j in range(min(X.count(i), Y.count(i))) : #중복된수 넣기
            answer.append(i)
    answer.sort(reverse=True)
    if len(answer) == 0:
        return "-1"
    if answer[0] == "0":
        return "0"
    answer = "".join(answer)
    return answer