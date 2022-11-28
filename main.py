from player import Player
from webapi import WebAPI

def main():
    webAPI = WebAPI()

    player = webAPI.getPlayer('hikaru')
    print(player.title)



if __name__ == "__main__":
    main()
