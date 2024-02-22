class UserAlreadyExistsOrNoSuchRoleSystemError(Exception):
    message = 'User already exists or no such role'


class UserNotFoundError(Exception):
    message: str = "User not found"
