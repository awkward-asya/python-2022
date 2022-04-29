class Hotel:
    def __init__(self, num_rooms):
        self._rooms = {"SGL": [0 for _ in range(num_rooms)], "DBL": [0 for _ in range(num_rooms)],
                       "Junior Suite": [0 for _ in range(num_rooms)], "Suite": [0 for _ in range(num_rooms)]}

        self._prices = {"SGL": 100, "DBL": 200, "Junior Suite": 300,
                        "Suite": 350}

    def occupy(self, room, room_id):
        if self._rooms[room][room_id] == 0:
            self._rooms[room][room_id] = 1
        else:
            raise RuntimeError("Номер занят")

    def occupy_all(self):
        for room in self._rooms:
            for i in range(len(self._rooms) + 1):
                self._rooms[room][i] = 1

    def free(self, room, room_id):
        self._rooms[room][room_id] = 0  # освобождаем номер

    def free_all(self):
        for room in self._rooms:
            for i in range(len(self._rooms) + 1):
                self._rooms[room][i] = 0

    def occupied_part(self, ):
        summa = 0
        for room in self._rooms:
            for i in range(len(self._rooms) + 1):
                if self._rooms[room][i] == 1:
                    summa += 1
        res = summa*100/((len(self._rooms)+1)*(len(self._rooms)))
        return f'Занято {res}% номеров'

    def income(self):
        income = 0
        for room in self._rooms:
            for i in range(len(self._rooms) + 1):
                if self._rooms[room][i] == 1:
                    income += self._prices[room]
        return f'Текущая выручка равна: {income}'

    def __str__(self):
        a = ''
        for room in self._rooms:
            for i in range(len(self._rooms)):
                if self._rooms[room][i] == 0:
                    a += 'Номер ' + room + ' ' + str(i + 1) + " свободен\n"
                else:
                    a += 'Номер ' + room + ' ' + str(i + 1) + " занят\n"
        return a


hotel = Hotel(5)
print(hotel._rooms)
print(hotel._prices)

hotel.occupy("SGL", 3)
print(hotel._rooms)
print(hotel.income())
print(hotel.occupied_part())

hotel.free("SGL", 3)
print(hotel._rooms)

hotel.occupy_all()
print(hotel._rooms)
print(hotel.income())
print(hotel.occupied_part())

hotel.free_all()
print(hotel._rooms)
print(hotel.income())
print(hotel.occupied_part())

print(hotel.__str__())
