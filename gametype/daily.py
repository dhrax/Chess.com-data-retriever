from gametype.gametype import GameType
from gamedata import GameData
from record import Record

class Daily(GameType):

    def __init__(self, last: GameData, best: GameData, record: Record) -> None:
        print(type(last))
        super().__init__(last, best, record)

    
    def __str__(self) -> str:
        return super().__str__()