from math import ceil


def solution(n, stations, w):
    answer = 0

    for i in range(len(stations)+1):
        if i == 0:  # 첫 아파트부터 첫번째 station까지의 구간
            answer += ceil((stations[i]-w-1) / (2*w+1))
        elif i == len(stations):  # 마지막 station부터 마지막 아파트까지의 구간
            answer += ceil((n-stations[i-1]-w) / (2*w+1))
        else:  # station과 station 사이.
            answer += ceil((stations[i] - stations[i-1] - (2*w) - 1) / (2*w+1))
    return answer

