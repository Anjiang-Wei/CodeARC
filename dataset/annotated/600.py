def verify_login(username: str, password: str) -> str:
    # Check for injected code in the password
    if '||' in password or '//' in password:
        return "Wrong username or password!"
    
    # Valid username and password combinations
    valid_credentials = {
        'Timmy': 'password',
        'Alice': 'alice',
        'Johny': 'Hf7FAbf6',
        'Roger': 'pass',
        'Simon': 'says',
        'Admin': 'ads78adsg7dasga'
    }
    
    # Check if the provided credentials are valid
    if username in valid_credentials and valid_credentials[username] == password:
        return 'Successfully Logged in!'
    else:
        return 'Wrong username or password!'

