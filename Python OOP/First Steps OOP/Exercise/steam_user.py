class SteamUser:
    def __init__(self, username, games):
        self.hours = None
        self.game = None
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        self.game = game
        self.hours = hours
        if self.game in self.games:
            self.played_hours += self.hours
            return f'{self.username} is playing {self.game}'
        return f'{self.game} is not in library'

    def buy_game(self, game):
        self.game = game
        if self.game not in self.games:
            self.games.append(self.game)
            return f'{self.username} bought {self.game}'
        return f'{self.game} is already in your library'

    def status(self):
        return f'{self.username} has {len(self.games)} games. Total play time: {self.played_hours}'


user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())
