from fastapi import HTTPException

class ConfigurationNotFoundException(HTTPException):
    def __init__(self, country_code: str):
        super().__init__(status_code=404, detail=f"Configuration for country code {country_code} not found")
