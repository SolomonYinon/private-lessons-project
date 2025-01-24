import json

def validate_data(name, email):
    if not name or not email:
        return False
    if '@' not in email:
        return False
    return True


def user_exists(email):
    try:
        with open('data.json', 'r') as f:
            users = f.readlines()
            for user in users:
                if json.loads(user)['email'] == email:
                    return True
    except FileNotFoundError:
        return False
    return False
