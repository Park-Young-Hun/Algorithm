function solution(participant, completion) {
    var answer = '';
    var nameCnt = new Map();

    for (var i = 0; i < participant.length; i++) {
        if (nameCnt.has(participant[i])) {
            nameCnt.set(participant[i], nameCnt.get(participant[i]) + 1)
        }
        else {
            nameCnt.set(participant[i], 1)
        }
    }

    for (var i = 0; i < completion.length; i++) {
        if (nameCnt.has(completion[i])) {
            nameCnt.set(completion[i], nameCnt.get(completion[i]) - 1)
        }
    }

    for (var key of nameCnt.keys()) {
        if (nameCnt.get(key) == 1) {
            answer = key
        }
    }
    return answer;
}
