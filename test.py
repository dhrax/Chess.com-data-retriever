import requests
import json

from webapi import WebAPI

def test():
    webAPI = WebAPI()

    webAPI.getPlayerStats('hikaru')

    


if __name__ == "__main__":
    test()
