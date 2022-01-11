class PhoneNumberValidationError(Exception):
    """Custom error that is raised when both phone is not valid."""

    def __init__(self,phone: str, message: str) -> None:
        self.phone = phone
        self.message = message
        super().__init__(message)
