import os

class DefaultConfig:
    """Configuration class. Reads Azure endpoint and key from environment variables.

    Environment variables:
      - MicrosoftAIServiceEndpoint : Azure Language / Text Analytics endpoint (e.g. https://<name>.cognitiveservices.azure.com/)
      - MicrosoftAPIKey : Azure key for the resource
    """
    # NOTE: these names match the instructions from the assignment
    AI_ENDPOINT_ENV = "MicrosoftAIServiceEndpoint"
    AI_KEY_ENV = "MicrosoftAPIKey"

    def __init__(self):
        # Use os.environ.get to avoid KeyError when variables are missing
        self.endpoint = os.environ.get(self.AI_ENDPOINT_ENV, None)
        self.api_key = os.environ.get(self.AI_KEY_ENV, None)

    def is_configured(self):
        return bool(self.endpoint and self.api_key)

    def as_dict(self):
        return {"endpoint": self.endpoint, "api_key_present": bool(self.api_key)}
