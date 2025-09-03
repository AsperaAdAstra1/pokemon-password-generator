# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# 1. (DOCUMENTATION AND IMPORTS)
# -----------------------------------------------------------------------------

"""
Secure Password Generator
This program creates random passwords based on user specifications,
such as length, inclusion of different character types, and the option
to embed a random Pokémon name for a fun touch (it will be revealed at the end).
"""

import random
import string

# -----------------------------------------------------------------------------
# (THIS IS A FUNCTIONAL PROGRAM, IT WON'T CLOSE UNEXPECTEDLY)
# -----------------------------------------------------------------------------

POKEMON_LIST = [
    "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree",
    "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata",
    "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu",
    "Sandshrew", "Sandslash", "NidoranF", "Nidorina", "Nidoqueen", "NidoranM",
    "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales",
    "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom",
    "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett",
    "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape",
    "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra",
    "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout",
    "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude",
    "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro",
    "Magnemite", "Magneton", "Farfetchd", "Doduo", "Dodrio", "Seel",
    "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter",
    "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb",
    "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee",
    "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon",
    "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen",
    "Seaking", "Staryu", "Starmie", "MrMime", "Scyther", "Jynx", "Electabuzz",
    "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto",
    "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte",
    "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno",
    "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"
]

# -----------------------------------------------------------------------------
# 2. MAIN GENERATION FUNCTION (adapted for Pokémon)
# -----------------------------------------------------------------------------

def generate_password(length, use_uppercase, use_numbers, use_symbols, use_pokemon):
    """
    Generates a random password and returns the password and the name of the Pokémon used.
    """
    base_chars = string.ascii_lowercase
    if use_uppercase:
        base_chars += string.ascii_uppercase
    if use_numbers:
        base_chars += string.digits
    if use_symbols:
        base_chars += string.punctuation

    if not base_chars:
        return "Error: No character type was selected.", None

    final_password_list = []
    selected_pokemon = None # Variable to store the Pokémon

    if use_pokemon:
        selected_pokemon = random.choice(POKEMON_LIST) # Yes, it might seem lazy, but if I adapted the algorithm to choose the Pokémon based on the password length, it would become predictable, and the main idea is to generate passwords that are hard to replicate!

        if len(selected_pokemon) >= length:
            print(f"\nWarning: The name '{selected_pokemon}' is too long. Generating a normal password.")
            selected_pokemon = None # --- CHANGED: If it's too long, we reset it to None
        else:
            final_password_list.extend(list(selected_pokemon))
    
    remaining_length = length - len(final_password_list)

    for _ in range(remaining_length):
        final_password_list.append(random.choice(base_chars))
    
    random.shuffle(final_password_list)

    # The function returns two values
    return "".join(final_password_list), selected_pokemon

# -----------------------------------------------------------------------------
# 3. EXECUTION FUNCTION
# -----------------------------------------------------------------------------

def main():
    """
    Main function.
    """
    print("--- Secure Password Generator: Pokémon Edition! ---")

    try:
        # ... (user input code)
        password_length = int(input("Enter the desired length for the password: "))

        if password_length <= 0:
            print("The length must be a positive number.")
            input("\nPress Enter to exit...")
            return

        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        include_pokemon = input("Do you want to include a random Pokémon name? (y/n): ").lower() == 'y'

        # --- function return values
        password, pokemon_used = generate_password(password_length, include_uppercase, include_numbers, include_symbols, include_pokemon)

        print("\nYour secure password is:")
        print(password)

        # --- Pokémon check
        if pokemon_used: # This 'if' only runs if pokemon_used is not None!
            print(f"(Secret Pokémon: {pokemon_used})")

        input("\nPress Enter to exit...")

    except ValueError:
        print("\nError: Please enter a valid number for the length.")
        input("\nPress Enter to exit...")

# -----------------------------------------------------------------------------
# 4. PROGRAM ENTRY POINT
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()