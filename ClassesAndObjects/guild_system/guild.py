from ClassesAndObjects.guild_system.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        
    def kick_player(self, player_name):
        found = False
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = 'Unaffiliated'
                found = True
                break
        if found:
            return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."
    
    def guild_info(self):
        players = '\n'.join(x.player_info() for x in self.players)
        return f"Guild: {self.name}\n{players}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())