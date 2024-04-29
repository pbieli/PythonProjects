Random Password Generator

Description
The Random Password Generator is a Python script that generates strong and secure random passwords. It provides advanced features such as customizable password length, character set selection, exclusion of ambiguous characters, visual strength indicator, and the option to export generated passwords to a text file. The script is designed to prioritize usability, security, and flexibility, making it suitable for a wide range of applications requiring password generation.

Features
-Customizable Password Length: Specify the desired length of each password.
-Character Set Selection: Choose from a default set of characters or customize the character set.
-Exclusion of Ambiguous Characters: Optionally exclude ambiguous characters to improve password readability.
-Strength Indicator: Visual representation of password strength based on entropy.
-Export to Text File: Option to export generated passwords to a text file for easy access and storage.

Usage
1. Clone the repository or download the script file (passwordgenerator.py).
2. Ensure you have Python installed on your system.
3. Run the script using the command line or terminal: python password_generator.py
4. Follow the prompts to specify password options interactively or use command-line arguments to customize the generation process.
5. Generated passwords will be displayed along with their entropy and strength indicator.
6. Optionally, specify the --export flag followed by the file path to export generated passwords to a text file.

Requirements
-Python 3.x
-No additional dependencies required.


Example
Generate a password of length 12 with the default character set:

python passwordgenerator.py --length 12

Generate 5 passwords of length 10, excluding ambiguous characters, and export them to a file named passwords.txt:

python passwordgenerator.py --length 10 --count 5 --exclude-ambiguous --export passwords.txt

Author
[Philipp Bielinski]

