class EmailValidationError(Exception):
    """Custom error that is raised when both email is not valid."""

    def __init__(self,email: str, message: str) -> None:
        self.email = email
        self.message = message
        super().__init__(message)
