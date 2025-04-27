def obfuscate_email(email: str) -> str:
    return email.replace("@", " [at] ").replace(".", " [dot] ")

