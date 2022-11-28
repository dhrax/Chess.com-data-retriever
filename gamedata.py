class GameData:

    rating: int
    date: int
    rd: int
    url: str

    def __init__(self, rating, date, rd = 0, game = '') -> None:
        print("In gameData")
        self.rating = rating
        self.date = date
        self.rd = rd
        self.url = game

    def __str__(self) -> str:
        return "Rating: " + self.rating + "Date: " + self.date + "RD: " + self.rd + "URL: " + self.url