# Password Strength Checker
# This script checks the strength of a password based on various criteria such as length, character variety, and common password patterns. It provides feedback to the user and allows them to generate strong passwords or save checked passwords to a file.

# Future features:
# pytest
# save encrypted passwords
# add option to show password as you type
# add option to check password against known data breaches (haveibeenpwned API)

from colorama import Fore, Style
import getpass
import random
import string
import json
import os

last_password = ""

# Default settings
DEFAULT_SETTINGS = {
    "min_length": 8,
    "require_uppercase": True,
    "require_lowercase": True,
    "require_numbers": True,
    "require_special": True,
    "check_common_passwords": True,
    "check_dictionary_words": True,
    "check_keyboard_patterns": True,
    "check_breaches": False,
    "max_repeated_chars": 2,
    "special_chars": "!@#$%",
    "password_length_for_generation": 16,
    "mask_password_input": False
}

SETTINGS_FILE = "password_checker_settings.json"

def load_settings():
    """Load settings from file or create default"""
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r") as f:
                return json.load(f)
        except:
            return DEFAULT_SETTINGS.copy()
    return DEFAULT_SETTINGS.copy()

def save_settings(settings):
    """Save settings to file"""
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=2)
    print("Settings saved!")

def show_settings(settings):
    """Display current settings"""
    print("\n" + "="*40)
    print("CURRENT SETTINGS")
    print("="*40)
    print(f"Minimum password length: {settings['min_length']}")
    print(f"Require uppercase: {settings['require_uppercase']}")
    print(f"Require lowercase: {settings['require_lowercase']}")
    print(f"Require numbers: {settings['require_numbers']}")
    print(f"Require special chars: {settings['require_special']}")
    print(f"Special characters allowed: {settings['special_chars']}")
    print(f"Max repeated characters: {settings['max_repeated_chars']}")
    print(f"Mask password input: {settings['mask_password_input']}")
    print(f"\nChecks enabled:")
    print(f"  - Common passwords: {settings['check_common_passwords']}")
    print(f"  - Dictionary words: {settings['check_dictionary_words']}")
    print(f"  - Keyboard patterns: {settings['check_keyboard_patterns']}")
    print(f"  - Data breach check: {settings['check_breaches']}")
    print(f"\nPassword generation length: {settings['password_length_for_generation']}")
    print("="*40)

def settings_menu(settings):
    """Interactive settings menu"""
    while True:
        show_settings(settings)
        print("\n1. Change minimum length")
        print("2. Toggle uppercase requirement")
        print("3. Toggle lowercase requirement")
        print("4. Toggle number requirement")
        print("5. Toggle special character requirement")
        print("6. Change special characters")
        print("7. Toggle common password check")
        print("8. Toggle dictionary word check")
        print("9. Toggle keyboard pattern check")
        print("10. Toggle breach database check")
        print("11. Change max repeated characters")
        print("12. Change generation password length")
        print("13. Toggle password masking")
        print("14. Reset to defaults")
        print("15. Back to main menu")
        
        try:
            choice = int(input("\nChoose: "))
            
            if choice == 1:
                new_length = int(input("New minimum length (4-32): "))
                if 4 <= new_length <= 32:
                    settings['min_length'] = new_length
                    save_settings(settings)
                else:
                    print("Length must be between 4 and 32")
            
            elif choice == 2:
                settings['require_uppercase'] = not settings['require_uppercase']
                save_settings(settings)
                print(f"Uppercase requirement: {settings['require_uppercase']}")
            
            elif choice == 3:
                settings['require_lowercase'] = not settings['require_lowercase']
                save_settings(settings)
                print(f"Lowercase requirement: {settings['require_lowercase']}")
            
            elif choice == 4:
                settings['require_numbers'] = not settings['require_numbers']
                save_settings(settings)
                print(f"Numbers requirement: {settings['require_numbers']}")
            
            elif choice == 5:
                settings['require_special'] = not settings['require_special']
                save_settings(settings)
                print(f"Special characters requirement: {settings['require_special']}")
            
            elif choice == 6:
                new_chars = input("Enter special characters to allow: ")
                if new_chars:
                    settings['special_chars'] = new_chars
                    save_settings(settings)
            
            elif choice == 7:
                settings['check_common_passwords'] = not settings['check_common_passwords']
                save_settings(settings)
                print(f"Common password check: {settings['check_common_passwords']}")
            
            elif choice == 8:
                settings['check_dictionary_words'] = not settings['check_dictionary_words']
                save_settings(settings)
                print(f"Dictionary word check: {settings['check_dictionary_words']}")
            
            elif choice == 9:
                settings['check_keyboard_patterns'] = not settings['check_keyboard_patterns']
                save_settings(settings)
                print(f"Keyboard pattern check: {settings['check_keyboard_patterns']}")
            
            elif choice == 10:
                settings['check_breaches'] = not settings['check_breaches']
                save_settings(settings)
                print(f"Breach database check: {settings['check_breaches']}")
            
            elif choice == 11:
                new_max = int(input("New max repeated characters (1-5): "))
                if 1 <= new_max <= 5:
                    settings['max_repeated_chars'] = new_max
                    save_settings(settings)
                else:
                    print("Must be between 1 and 5")
            
            elif choice == 12:
                new_gen_length = int(input("New generation length (8-64): "))
                if 8 <= new_gen_length <= 64:
                    settings['password_length_for_generation'] = new_gen_length
                    save_settings(settings)
                else:
                    print("Length must be between 8 and 64")
            
            elif choice == 13:
                settings['mask_password_input'] = not settings['mask_password_input']
                save_settings(settings)
                print(f"Password masking: {settings['mask_password_input']}")
            
            elif choice == 14:
                confirm = input("Reset all settings to defaults? (yes/no): ")
                if confirm.lower() == "yes":
                    settings = DEFAULT_SETTINGS.copy()
                    save_settings(settings)
                    print("Reset to defaults!")
            
            elif choice == 15:
                return settings
            
            else:
                print("Invalid input")
        
        except ValueError:
            print("Enter a valid number")

def generate_strong_password(settings):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + settings['special_chars']
    password = "".join(random.choice(chars) for _ in range(settings['password_length_for_generation']))
    return password

def contains_common_words(password):
    common_words = ["password", "letmein", "welcome", "admin", "login", "hello"]
    lower_pwd = password.lower()
    for word in common_words:
        if word in lower_pwd:
            return True, word
    return False, None

def has_keyboard_patterns(password):
    patterns = ["qwerty", "asdfgh", "zxcvbn", "123456", "qazwsx"]
    lower_pwd = password.lower()
    for pattern in patterns:
        if pattern in lower_pwd:
            return True, pattern
    return False, None

def show_strength_bar(score, max_score=5):
    filled = int((score / max_score) * 10)
    bar = "█" * filled + "░" * (10 - filled)
    print(f"Strength: [{bar}] {score}/{max_score}")

def save_password_to_file(password):
    with open("checked_passwords.txt", "a") as f:
        f.write(f"{password}\n")
    print("Saved!")

def check_password(settings):
    global last_password
    score = 0
    feedback = []
    
    if settings['mask_password_input']:
        password = getpass.getpass("Enter password (hidden): ")
    else:
        password = input("Enter password (visible): ")
    
    last_password = password
    
    # Length check
    if len(password) >= settings['min_length']:
        score += 1
    else:
        feedback.append(f"Password too short (min {settings['min_length']} characters)")
    
    # Repeated characters
    for x in password:
        if password.count(x) > settings['max_repeated_chars']:
            score -= 1
            feedback.append(f"Don't use '{x}' more than {settings['max_repeated_chars']} times")
            break
    
    # Uppercase
    if settings['require_uppercase']:
        found_upper = any(c.isupper() for c in password if c.isalpha())
        if found_upper:
            score += 1
        else:
            feedback.append("Add uppercase letter(s)")
    
    # Lowercase
    if settings['require_lowercase']:
        found_lower = any(c.islower() for c in password if c.isalpha())
        if found_lower:
            score += 1
        else:
            feedback.append("Add lowercase letter(s)")
    
    # Numbers
    if settings['require_numbers']:
        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("Add number(s)")
    
    # Special characters
    if settings['require_special']:
        if any(c in settings['special_chars'] for c in password):
            score += 1
        else:
            feedback.append(f"Add special character(s) from: {settings['special_chars']}")
    
    # Common passwords
    if settings['check_common_passwords']:
        if password in ["password", "123456", "123456789", "qwerty", "abc123"]:
            score -= 1
            feedback.append(f"Don't use '{password}'")
    
    # Dictionary check
    if settings['check_dictionary_words']:
        found, word = contains_common_words(password)
        if found:
            score -= 1
            feedback.append(f"Contains common word: '{word}'")
    
    # Keyboard patterns
    if settings['check_keyboard_patterns']:
        found, pattern = has_keyboard_patterns(password)
        if found:
            score -= 1
            feedback.append(f"Contains keyboard pattern: '{pattern}'")
    
    # Cap score at 0-5
    score = max(0, min(score, 5))
    
    # Display results
    show_strength_bar(score)
    print()
    
    if score <= 2:
        print(Fore.RED + "WEAK")
    elif score <= 4:
        print(Fore.YELLOW + "MEDIUM")
    else:
        print(Fore.GREEN + "STRONG")
    print(Style.RESET_ALL)
    
    print()
    for msg in feedback:
        print(msg)

# Main program
settings = load_settings()

print("=== Password Strength Checker ===")
print("           welcome!\n")
check_password(settings)

print("\n" + "="*35)
while True:
    print("\n1. Check another password")
    print("2. Generate a strong password")
    print("3. Save last password checked")
    print("4. Settings")
    print("5. Quit")
    try:  
        x = int(input("\nChoose: "))
        if x == 1:
            print()
            check_password(settings)
        elif x == 2:
            pwd = generate_strong_password(settings)
            print(f"\nGenerated: {pwd}")
        elif x == 3:
            if last_password:
                save_password_to_file(last_password)
            else:
                print("Check a password first!")
        elif x == 4:
            settings = settings_menu(settings)
        elif x == 5:
            print("\nBye!")
            break
        else:
            print("Invalid input")
    except ValueError:
        print("Enter a number")