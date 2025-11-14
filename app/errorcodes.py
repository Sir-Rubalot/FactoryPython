
class WorkerNotFoundError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.error_code = message

    def __str__(self):
        "Anställd kunde inte hittas, kontrollera att den är instämplad."