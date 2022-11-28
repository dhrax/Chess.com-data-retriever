from gamedata import GameData
from record import Record


class GameType:
    last: GameData
    best: GameData
    record: Record

    def __init__(self, last: GameData, best: GameData, record: Record) -> None:
        self.last = last
        self.best = best
        self.record = record

    def __str__(self) -> str:
        return "Last: " + str(self.last) + ", Best: " + str(self.best) + ", Record: " + str(self.record)
    