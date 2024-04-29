"""
Random Password Generator
Author: [Philipp Bielinski]
"""

import secrets
import string
import argparse
import math

def generate_password(length, characters):
    """
    Generate a secure random password of specified length.
    Args:
        length (int): Length of the password.
        characters (str): Characters to use for generating the password.
    Returns:
        str: Generated password.
    """
    return ''.join(secrets.choice(characters) for _ in range(length))

def calculate_entropy(password):
    """
    Calculate the entropy of a password.
    Args:
        password (str): Password to calculate entropy for.
    Returns:
        float: Entropy of the password in bits.
    """
    character_set_size = len(set(password))
    password_length = len(password)
    return math.log2(character_set_size ** password_length)

def main():
    print("--- Random Password Generator ---")
    parser = argparse.ArgumentParser(description='Random Password Generator')
    parser.add_argument('--length', type=int, help='Length of each password')
    parser.add_argument('--count', type=int, default=1, help='Number of passwords to generate (default: 1)')
    parser.add_argument('--exclude-ambiguous', action='store_true', help='Exclude ambiguous characters (l, 1, I, 0, O)')
    parser.add_argument('--export', metavar='FILE', help='Export passwords to a text file')
    args = parser.parse_args()

    if args.length is None:
        args.length = int(input("Enter the length of each password: "))
    if args.length <= 0:
        print("Error: Password length must be a positive integer.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    if args.exclude_ambiguous:
        characters = ''.join(char for char in characters if char not in 'l1IO0')

    passwords = []
    print(f"\nGenerating {args.count} {'password' if args.count == 1 else 'passwords'}:")
    for _ in range(args.count):
        password = generate_password(args.length, characters)
        entropy = calculate_entropy(password)
        strength_indicator = 'Weak' if entropy < 50 else 'Moderate' if entropy < 80 else 'Strong'
        passwords.append(password)
        print(f"Password: {password} (Entropy: {entropy:.2f} bits) - {strength_indicator}")

    if args.export:
        with open(args.export, 'w') as f:
            f.write('\n'.join(passwords))
        print(f"\nPasswords exported to '{args.export}'.")

if __name__ == "__main__":
    main()

