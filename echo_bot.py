from config import DefaultConfig
try:
    from azure.ai.textanalytics import TextAnalyticsClient
    from azure.core.credentials import AzureKeyCredential
    AZURE_AVAILABLE = True
except Exception:
    # If azure SDK isn't available, we'll flag and continue with a mock implementation
    TextAnalyticsClient = None
    AzureKeyCredential = None
    AZURE_AVAILABLE = False

class EchoBot:
    def __init__(self, config: DefaultConfig):
        self.config = config
        self.client = None
        if AZURE_AVAILABLE and self.config.is_configured():
            try:
                cred = AzureKeyCredential(self.config.api_key)
                self.client = TextAnalyticsClient(endpoint=self.config.endpoint, credential=cred)
                print("[EchoBot] Connected to Azure Text Analytics client.")
            except Exception as e:
                print(f"[EchoBot] Failed to initialize Azure client: {e}")
                self.client = None
        else:
            if not AZURE_AVAILABLE:
                print("[EchoBot] Azure SDK not installed. Running with mock sentiment analysis.")
            else:
                print("[EchoBot] Azure credentials not configured. Running with mock sentiment analysis.")

    def analyze_sentiment(self, text: str) -> dict:
        """Return a sentiment dict with 'sentiment' and 'score'. Uses Azure if available, otherwise mock."""
        if self.client:
            try:
                response = self.client.analyze_sentiment(documents=[text])[0]
                # Azure returns a SentimentConfidenceScores object
                score = None
                if hasattr(response, 'confidence_scores'):
                    # simple aggregated score: positive - negative
                    score = float(response.confidence_scores.positive - response.confidence_scores.negative)
                return {"sentiment": response.sentiment, "score": score}
            except Exception as e:
                # On any error, fall back to mock
                print(f"[EchoBot] Azure call failed: {e}")
        # Mock simple sentiment: positive if words like 'good'/'great' present, negative if 'bad'/'sad'
        text_lower = text.lower()
        positive_tokens = ['good','great','happy','love','awesome','fantastic','excellent']
        negative_tokens = ['bad','sad','angry','hate','upset','terrible','awful']
        pos = any(tok in text_lower for tok in positive_tokens)
        neg = any(tok in text_lower for tok in negative_tokens)
        if pos and not neg:
            return {"sentiment": "positive", "score": 0.6}
        if neg and not pos:
            return {"sentiment": "negative", "score": -0.6}
        return {"sentiment": "neutral", "score": 0.0}

    def get_reply(self, user_text: str) -> str:
        analysis = self.analyze_sentiment(user_text)
        sentiment = analysis.get('sentiment', 'neutral')
        score = analysis.get('score', 0.0)
        # Basic reply logic that uses sentiment to vary responses
        if sentiment == 'positive':
            return f"I hear positivity in your message (score={score}). You said: '{user_text}' — that's great! 😊"
        if sentiment == 'negative':
            return f"I'm sorry you're feeling that way (score={score}). You said: '{user_text}'. If you'd like, tell me more."
        return f"You said: '{user_text}' (sentiment: {sentiment}, score={score})." 
