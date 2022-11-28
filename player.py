from title import Title

class Player:
    player_id: int
    id: str
    url: str
    name: str
    username: str
    followers: int
    country: str
    last_online: int
    joined: int
    status: str
    is_streamer: bool
    verified: bool
    avatar: str
    title: Title
    location: str
    fide: int
    twitch_url :str

    def __init__(self, player_id, url, 
                username, followers, country, last_online,
                joined, status, is_streamer, verified, avatar = "", name = "", 
                title = Title.UNTITLED.name, location = "", fide = 0, twitch_url = "") -> None:
        self.player_id = player_id
        self.url = url
        self.name = name
        self.username = username
        self.followers = followers
        self.country = country
        self.last_online = last_online
        self.joined = joined
        self.status = status
        self.is_streamer = is_streamer
        self.verified = verified
        self.avatar = avatar
        self.title = Title[title]
        self.location = location
        self.fide = fide
        self.twitch_url = twitch_url
