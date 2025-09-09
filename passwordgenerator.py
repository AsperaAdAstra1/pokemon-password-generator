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
import secrets

# -----------------------------------------------------------------------------
# (THIS IS A FUNCTIONAL PROGRAM, IT WON'T CLOSE UNEXPECTEDLY)
# -----------------------------------------------------------------------------

def load_pokemon_list(filename="pokemon.txt"):
    """
    Loads the list of Pokémon from a file.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            pokemon_list = [line.strip() for line in file]
        return pokemon_list
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []

# -----------------------------------------------------------------------------
# 2. MAIN GENERATION FUNCTION (adapted for Pokémon)
# -----------------------------------------------------------------------------

def generate_password(length, use_uppercase, use_numbers, use_symbols, use_pokemon, pokemon_list):
    """
    Generates a random password and returns the password and the name of the Pokémon used.
    """
    char_sets = [string.ascii_lowercase]
    if use_uppercase:
        char_sets.append(string.ascii_uppercase)
    if use_numbers:
        char_sets.append(string.digits)
    if use_symbols:
        char_sets.append(string.punctuation)

    base_chars = "".join(char_sets)
    if not base_chars:
        return "Error: No character type was selected.", None

    final_password_list = []
    guaranteed_chars = []

    # Handle Pokémon selection first to determine available length
    selected_pokemon = None
    if use_pokemon and pokemon_list:
        # Filter Pokémon that are shorter than the total length
        available_pokemon = [p for p in pokemon_list if len(p) < length]
        if available_pokemon:
            selected_pokemon = random.choice(available_pokemon)
            final_password_list.extend(list(selected_pokemon))
        else:
            print(f"\nWarning: No Pokémon name is short enough. Generating a normal password.")

    # Guarantee at least one of each selected character type
    if use_uppercase:
        guaranteed_chars.append(secrets.choice(string.ascii_uppercase))
    if use_numbers:
        guaranteed_chars.append(secrets.choice(string.digits))
    if use_symbols:
        guaranteed_chars.append(secrets.choice(string.punctuation))
    
    # Always include at least one lowercase letter
    guaranteed_chars.append(secrets.choice(string.ascii_lowercase))

    # Check if length is sufficient
    if length < len(final_password_list) + len(guaranteed_chars):
        return "Error: Password length is too short for the selected options.", None

    # Fill the rest of the password
    current_length = len(final_password_list) + len(guaranteed_chars)
    remaining_length = length - current_length
    
    password_fill = [secrets.choice(base_chars) for _ in range(remaining_length)]

    # Combine all parts and shuffle
    final_password_list.extend(guaranteed_chars)
    final_password_list.extend(password_fill)
    random.shuffle(final_password_list)

    return "".join(final_password_list), selected_pokemon

# -----------------------------------------------------------------------------
# 3. EXECUTION FUNCTION
# -----------------------------------------------------------------------------

def main():
    """
    Main function.
    """
    print("--- Secure Password Generator: Pokémon Edition! ---")

    pokemon_list = load_pokemon_list()
    if not pokemon_list:
        print("Could not load Pokémon list. Pokémon names will not be available.")

    while True:
        try:
            password_length_str = input("\nEnter the desired length for the password (or type 'exit' to quit): ")
            if password_length_str.lower() == 'exit':
                break

            password_length = int(password_length_str)

            if password_length <= 0:
                print("The length must be a positive number.")
                continue

            include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
            include_pokemon = input("Do you want to include a random Pokémon name? (y/n): ").lower() == 'y'

            result = generate_password(password_length, include_uppercase, include_numbers, include_symbols, include_pokemon, pokemon_list)

            if isinstance(result, tuple):
                password, pokemon_used = result
                print("\nYour secure password is:")
                print(password)

                if pokemon_used:
                    print(f"(Secret Pokémon: {pokemon_used})")
            else:
                print(f"\nError: {result}")

        except ValueError:
            print("\nError: Please enter a valid number for the length.")

        print("-" * 20)
        another = input("Generate another password? (y/n): ").lower()
        if another != 'y':
            break

# -----------------------------------------------------------------------------
# 4. PROGRAM ENTRY POINT
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()