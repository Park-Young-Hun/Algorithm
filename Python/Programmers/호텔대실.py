import heapq


class Room:
    def __init__(self, ready_time):
        self.ready_time = ready_time

    def __lt__(self, other):
        if self.ready_time < other.ready_time:
            return True
        else:
            return False


def solution(book_time):
    max_room_cnt = 0
    hotel = []

    for i in range(len(book_time)):
        hour, minute = map(int, book_time[i][1].split(":"))
        minute += 10

        if minute >= 60:
            hour += 1
            minute -= 60

        hour = str(hour)
        minute = str(minute)

        if len(hour) == 1:
            hour = "0" + hour

        if len(minute) == 1:
            minute = "0" + minute

        book_time[i][1] = hour + ":" + minute

    book_time.sort()

    for start, end in book_time:
        if hotel:
            room = heapq.heappop(hotel)

            if start < room.ready_time:
                heapq.heappush(hotel, room)
                heapq.heappush(hotel, Room(end))
            else:
                room.ready_time = end
                heapq.heappush(hotel, room)
        else:
            heapq.heappush(hotel, Room(end))

        if len(hotel) > max_room_cnt:
            max_room_cnt = len(hotel)

    return max_room_cnt
