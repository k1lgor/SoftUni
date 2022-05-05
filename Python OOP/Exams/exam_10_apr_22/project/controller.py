from project.player import Player
from project.supply.supply import Supply

from project.supply.food import Food

from project.supply.drink import Drink


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player.name not in [curr_player.name for curr_player in self.players]:
                added_players.append(player.name)
                self.players.append(player)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in ['Drink', 'Food']:
            return
        curr_player = ''
        curr_supply = ''
        for player in self.players:
            if player.name == player_name:
                curr_player = player
        if curr_player == '':
            return
        if curr_player.stamina == 100:
            return f"{player_name} have enough stamina."
        for supply in self.supplies[::-1]:
            if supply.__class__.__name__ == sustenance_type:
                curr_supply = supply
                self.supplies.remove(curr_supply)
                break
        if curr_supply == '':
            if sustenance_type == 'Drink':
                raise Exception("There are no drink supplies left!")
            elif sustenance_type == 'Food':
                raise Exception("There are no food supplies left!")
        if curr_player.stamina + curr_supply.energy > 100:
            curr_player.stamina = 100
            curr_player.need_sustenance = False
        else:
            curr_player.stamina += curr_supply.energy
        return f"{player_name} sustained successfully with {curr_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = ''
        second_player = ''
        winner = ''
        for player in self.players:
            if player.name == first_player_name:
                first_player = player
            elif player.name == second_player_name:
                second_player = player
        if first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina." + '\n' + \
                   f"Player {second_player.name} does not have enough stamina."
        elif first_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina."
        elif second_player.stamina == 0:
            return f"Player {second_player.name} does not have enough stamina."
        if first_player.stamina < second_player.stamina:
            second_player.stamina -= first_player.stamina / 2
            if second_player.stamina < 0:
                second_player.stamina = 0
                second_player.need_sustenance = True
                winner = first_player
                return f"Winner: {winner.name}"
            first_player.stamina -= second_player.stamina / 2
            if first_player.stamina < 0:
                first_player.stamina = 0
                first_player.need_sustenance = True
                winner = second_player
                return f"Winner: {winner.name}"
        elif first_player.stamina > second_player.stamina:
            first_player.stamina -= second_player.stamina / 2
            if first_player.stamina < 0:
                first_player.stamina = 0
                first_player.need_sustenance = True
                winner = second_player
                return f"Winner: {winner.name}"
            second_player.stamina -= first_player.stamina / 2
            if second_player.stamina < 0:
                second_player.stamina = 0
                second_player.need_sustenance = True
                winner = first_player
                return f"Winner: {winner.name}"
        if winner == '':
            if first_player.stamina > second_player.stamina:
                winner = first_player
            else:
                winner = second_player
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            stamina_after = player.stamina - (player.age * 2)
            if stamina_after < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        result = ''
        for player in self.players:
            player.need_sustenance = player.stamina < 100
            result += player.__str__() + '\n'
        for supply in self.supplies:
            result += supply.details() + '\n'

        return result.strip()
