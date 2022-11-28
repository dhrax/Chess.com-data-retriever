import requests
import json
from player import Player
from gametype.daily import Daily
from gametype.gametype import GameType

class WebAPI:
    
    def getPlayer(self, playername: str) -> Player:
        r =requests.get('https://api.chess.com/pub/player/' + playername)
        return self.JSONToPlayer(r.json())

    def getPlayerStats(self, playername):
        r =requests.get('https://api.chess.com/pub/player/' + playername + '/stats')
        #print(r.json())

        data = json.dumps(r.json()['chess_daily'])
        #dict = r.json()['chess_daily']
        print(r.json()['chess_daily'])

        #d = json.loads(dict['last'])
        #print(dict['last'])

        #daily = Daily(d['last'], d['best'], d['record'])
        #print(type(daily.record))
        
        
        
    def JSONToPlayer(self, data: dict) -> Player:
        id = data['@id']

        del data['@id']

        string = json.dumps(data)

        j = json.loads(string)
        p = Player(**j)

        p.id = id
        return p

    def printDict(dict: dict):
        for key, value in dict.items():
            print(key)
            print(value)
            print('\n')