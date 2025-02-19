import time
import itertools

common_passwords = [
    'password', 'asdfghjkl', 'qwertyuiop', '123456',
    'mnbvcxz', '1234567890', '0987654321', '123456789',
    'qwerty', 'admin', 'letmein', 'welcome', '123abc',
    'password1', '12345', 'zxcvbnm', 'poiuytrewq', 'lkjhgfdsa',
    'dummy', 'guessthis', 'password2'
]

def check_password_strength(password):
    skip = False
    # check against common passwords
    if password in common_passwords:
        return ("Weak", "Password is too common and easily guessable")  # Return a tuple

    # check length
    length = len(password)
    if length < 8:
        return ("Weak", "Password must be at least 8 characters long")  # Return a tuple

    # check password char diversity
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    # make a strength score for password
    score = 0

    # incentivise longer passwords
    if length <= 12 or skip:
        score = 0
    elif length <= 14:
        score = 1
    else:
        score = 2

    # each of the following is 1 point each
    score += sum([has_lower, has_upper, has_digit, has_special])

    # generate password feedback
    feedback = []
    if not has_lower: feedback.append("add lowercase letters")
    if not has_upper: feedback.append("add uppercase letters")
    if not has_digit: feedback.append("include numbers")
    if not has_special: feedback.append("use special characters")

    # calculate strength rating
    if score <= 3:
        strength = "Weak"
    elif score <= 5:
        strength = "Alright"
    else:
        strength = "Strong"

    feedback_msg = "Consider taking the following actions: " + "\n".join(feedback) if feedback else "Nice password, make sure you don't reuse it!"

    return strength, feedback_msg  # Return a tuple

def hack_me(target):
    start_time = time.time()

    # try dictionary attack, with small/limited dict
    print("\n Password cracking simulation!")
    print("\n Trying common passwords...")
    for common in common_passwords:
        if common == target:
            return True, "dictionary attack", time.time() - start_time

    charset = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{};:/?.>,<`~'

    # this can be adjusted, but anything above 4 will take quite a while
    max_length = 4

    if len(target) < max_length:
        print("Trying brute-force combinations...")
        for length in range(1, max_length + 1):
            total = len(charset) ** length
            print(f"Testing all {length}-character combinations ({total} possibilities)")

            for guess in itertools.product(charset, repeat=length):
                guess_str = ''.join(guess)
                if guess_str == target:
                    return True, "brute-force", time.time() - start_time
    else:
        return False, "too big to brute force", time.time() - start_time

    return False, "", time.time() - start_time

def main():
    password = input("Enter password to analyze: ")
    result = check_password_strength(password)
    if isinstance(result, tuple):
        strength, feedback = result
        print(f"\n Strength: {strength}\n{feedback}")
    else:
        print(f"\n Strength: {result}")

    hacked, method, duration = hack_me(password)
    if hacked:
        print(f"\n Password hacked via {method} in {duration:.2f} seconds!")
        if method == "brute-force":
            print("Use longer passwords with mixed characters to prevent brute-force attacks!")
        else:
            print("Use non-common passwords with plenty of mixed characters to prevent dictionary attacks!")
    else:
        print(f"\n Could not hack password via {method}!")
        print("Good job! But remember I threw this together in a couple minutes, real password cracking is much more powerful :)")

if __name__ == "__main__":
    main()