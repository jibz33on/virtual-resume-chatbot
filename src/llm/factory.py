"""
LLM Client Factory
==================
Creates the appropriate LLM client based on configuration.
"""

from typing import Optional
from .base_client import BaseLLMClient
from .openai_client import OpenAIClient
from .gemini_client import GeminiClient
from .groq_client import GroqClient


def create_llm_client(
    provider: str,
    api_key: str,
    model: str
) -> BaseLLMClient:
    """
    Create an LLM client for the specified provider.
    
    Args:
        provider: "openai", "gemini", or "groq"
        api_key: API key for the provider
        model: Model name to use
        
    Returns:
        Configured LLM client
        
    Example:
        >>> from src.config import Config
        >>> config = Config()
        >>> client = create_llm_client(
        ...     provider=config.AI_PROVIDER,
        ...     api_key=config.get_api_key(),
        ...     model=config.get_model_name()
        ... )
        >>> response = client.chat([{"role": "user", "content": "Hello"}])
    """
    
    provider = provider.lower()
    
    if provider == "openai":
        return OpenAIClient(api_key, model)
    elif provider == "gemini":
        return GeminiClient(api_key, model)
    elif provider == "groq":
        return GroqClient(api_key, model)
    else:
        raise ValueError(f"Unknown provider: {provider}. Use 'openai', 'gemini', or 'groq'")