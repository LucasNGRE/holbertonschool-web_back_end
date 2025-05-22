import bcrypt


def hash_password(password: str) -> bytes:
    """
    hash_password function that expects one string argument
    named password and returns a salted,
    hashed password, which is a byte string.
    """
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
