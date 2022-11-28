from __future__ import division

class Record():
    win: int
    loss: int
    draw: int
    time_per_move: int
    timeout_percent: float

    
    def winrate(self):
        total_games = self.win + self.loss + self.draw
        return (self.win * 100) / total_games

    def __str__(self) -> str:
        print('STR called')
        return 'win: ' + self.win + 'loss: ' + self.loss + 'draw: ' + self.draw + 'time_per_move: ' + self.time_per_move + 'timeout_percent: ' + self.timeout_percent

    