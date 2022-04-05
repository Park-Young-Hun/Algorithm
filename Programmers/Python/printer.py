class Document:
    def __init__(self, priority, target):
        self.priority = priority
        self.target = target


def solution(priorities, location):
    answer = 0
    queue = []
    print_count = 0

    for i in range(len(priorities)):  # queue를 생성하여 Document 객체를 초기화 시켜서 넣어준다.
        doc = Document(priorities[i], False)
        if i == location:
            doc.target = True
        queue.append(doc)

    while True:  # target이 인쇄 될때까지 하나씩 queue에서 꺼내서 우선순위가 제일 높으면 인쇄하고 아니면 다시 queue에 넣는다.
        doc = queue.pop(0)
        max_val = 0

        for i in queue:  # queue에 남아있는 것들 중 가장 높은 우선순위를 찾는다.
            if i.priority > max_val:
                max_val = i.priority

        if max_val > doc.priority:  # 보류하고 다시 queue에 넣는다.
            queue.append(doc)
        else:  # 인쇄한다.
            print_count += 1
            if doc.target:
                break

    answer = print_count
    return answer

