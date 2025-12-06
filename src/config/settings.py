import os
from dotenv import load_dotenv

# Load your secret keys from .env file
load_dotenv(override=True)


class Config:
    """All settings in one simple place"""
    
    # ========================================
    # YOUR INFORMATION
    # ========================================
    NAME = "Jibin Kunjumon"
    
    # ========================================
    # AI MODEL SETTINGS
    # ========================================
    # Which AI provider to use: "openai", "gemini", or "groq"
    AI_PROVIDER = os.getenv("AI_PROVIDER", "openai")
    
    # Your API keys (stored safely in .env file)
    OPENAI_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")
    GROQ_KEY = os.getenv("GROQ_API_KEY")
    
    # Model names
    OPENAI_MODEL = "gpt-4o-mini"
    GEMINI_MODEL = "gemini-1.5-flash"
    GROQ_MODEL = "llama-3.1-70b-versatile"
    
    # ========================================
    # NOTIFICATION SETTINGS (Pushover)
    # ========================================
    PUSHOVER_USER = os.getenv("PUSHOVER_USER")
    PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN")
    
    # ========================================
    # FILE LOCATIONS
    # ========================================
    # Where your content files are stored
    RESUME_FOLDER = "data/resumes"
    SUMMARY_FOLDER = "data/summaries"
    LINKEDIN_FILE = "data/linkedin.pdf"
    
    
    def get_api_key(self):
        """Get the right API key based on your chosen provider"""
        if self.AI_PROVIDER == "openai":
            return self.OPENAI_KEY
        elif self.AI_PROVIDER == "gemini":
            return self.GOOGLE_KEY
        elif self.AI_PROVIDER == "groq":
            return self.GROQ_KEY
        return self.OPENAI_KEY  # default
    
    
    def get_model_name(self):
        """Get the right model name based on your chosen provider"""
        if self.AI_PROVIDER == "openai":
            return self.OPENAI_MODEL
        elif self.AI_PROVIDER == "gemini":
            return self.GEMINI_MODEL
        elif self.AI_PROVIDER == "groq":
            return self.GROQ_MODEL
        return self.OPENAI_MODEL  # default
    
    
    def check_setup(self):
        """Make sure everything is configured correctly"""
        # Check if API key exists for chosen provider
        api_key = self.get_api_key()
        if not api_key:
            raise ValueError(f"❌ Missing API key for {self.AI_PROVIDER}")
        
        # Warn if notifications won't work
        if not self.PUSHOVER_USER or not self.PUSHOVER_TOKEN:
            print("⚠️  Pushover not configured - notifications disabled")
        
        print(f"✅ Config OK - Using {self.AI_PROVIDER} with {self.get_model_name()}")
        return True