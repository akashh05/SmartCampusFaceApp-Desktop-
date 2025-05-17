import database

def authenticate(username, password):
    """Check if admin credentials are valid (with hashed password)."""
    return database.authenticate_admin(username, password)

def register_admin(username, password):
    """Register a new admin account with hashed password."""
    return database.add_admin(username, password)
