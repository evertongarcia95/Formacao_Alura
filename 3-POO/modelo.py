class Program:

    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def give_likes(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    def __str__(self):
        return (f'{self._name} - {self.year} : {self._likes}')


class Film(Program):
    def __init__(self, name, year, duration) -> None:
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return (f'{self._name} - {self.year} - {self.duration} min : {self._likes} Likes')


class Series(Program):
    def __init__(self, name, year, seasons) -> None:
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return (f'{self._name} - {self.year} - {self.seasons} temporadas : {self._likes} Likes')


class Playlist:
    def __init__(self, name, program) -> None:
        self.name = name
        self._program = program

    def __getitem__(self, item):
        return self._program[item]

    @property
    def listing(self):
        return self._program

    def __len__(self):
        return len(self._program)


vingadores = Film('vingadores - guerra infinita', 2018, 160)
tmep = Film('todo mundo em panico', 1999, 100)
atlanta = Series('atlanta', 2018, 2)
demolidor = Series('demolidor', 2016, 3)

vingadores.give_likes()
atlanta.give_likes()
atlanta.give_likes()
vingadores.give_likes()
vingadores.give_likes()
demolidor.give_likes()
demolidor.give_likes()
tmep.give_likes()
tmep.give_likes()

film_and_series = [vingadores, atlanta, demolidor, tmep]
weekend_playlist = Playlist('fim de semana', film_and_series)

print(f'tamanho da playlist: {len(weekend_playlist)}')

for program in weekend_playlist:
    print(program)
