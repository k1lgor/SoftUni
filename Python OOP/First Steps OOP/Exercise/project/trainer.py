from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if any(x.name == pokemon.name for x in self.pokemons):
            return 'This pokemon is already caught'
        self.pokemons.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon_name == pokemon.name:
                self.pokemons.remove(pokemon)
                return f'You have released {pokemon_name}'
        return 'Pokemon is not caught'

    def trainer_data(self):
        result = ''.join(
            f'- {pokemon.pokemon_details()}\n' for pokemon in self.pokemons
        )

        return f'Pokemon Trainer {self.name}\n' \
               f'Pokemon count {len(self.pokemons)}\n' \
               f'{result}'
