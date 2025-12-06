"""
Base LLM Client
===============
Abstract class that defines the interface for all LLM providers.
All providers (OpenAI, Gemini, Groq) must implement these methods.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Optional


class BaseLLMClient(ABC):
    """Abstract base class for LLM clients."""
    
    def __init__(self, api_key: str, model: str):
        """
        Initialize the LLM client.
        
        Args:
            api_key: API key for the provider
            model: Model name to use
        """
        self.api_key = api_key
        self.model = model
    
    @abstractmethod
    def chat(
        self, 
        messages: List[Dict[str, str]], 
        tools: Optional[List[Dict]] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> Dict:
        """
        Send a chat request to the LLM.
        
        Args:
            messages: List of message dicts [{"role": "user", "content": "..."}]
            tools: Optional list of tool definitions for function calling
            temperature: Sampling temperature (0-1)
            max_tokens: Maximum tokens in response
            
        Returns:
            Dict with response content and metadata
            
        Example:
            >>> client = OpenAIClient(api_key, model)
            >>> response = client.chat([{"role": "user", "content": "Hello"}])
            >>> print(response["content"])
        """
        pass
    
    @abstractmethod
    def supports_tools(self) -> bool:
        """
        Check if this provider supports function calling/tools.
        
        Returns:
            True if tools are supported
        """
        pass