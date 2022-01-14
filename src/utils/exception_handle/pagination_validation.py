class PaginationValidationError(Exception):
    def __init__(self,item: str, message: str) -> None:
        self.item = item
        self.message = message
        super().__init__(message)
