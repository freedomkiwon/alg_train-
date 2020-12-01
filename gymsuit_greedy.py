def solution(n, lost, reserve):
    answer = n
    lost_1 = lost[:]
    lost = list(set(lost)-set(reserve))
    # lost = [l for l in lost if l not in reserve]
    reserve = list(set(reserve)-set(lost_1))
    # reserve = [r for r in reserve if r not in lost]
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
        elif i+1 in reserve:
            reserve.remove(i+1)
        else :
            answer = answer - 1
    return answer

