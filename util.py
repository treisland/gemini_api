import os

class GeminiAPIKey:
    """
    A utility class to handle the retrieval of the Gemini API key from environment variables.
    """

    def __init__(self):
        self._api_key = os.getenv("GEMINI_API_KEY")
        if not self._api_key:
            raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable.")

    @property
    def api_key(self):
        """Returns the Gemini API key."""
        return self._api_key
    