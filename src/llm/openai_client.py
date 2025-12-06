"""OpenAI LLM Client Implementation."""

from openai import OpenAI
from typing import List, Dict, Optional
from .base_client import BaseLLMClient


class OpenAIClient(BaseLLMClient):
    """OpenAI GPT client implementation."""
    
    def __init__(self, api_key: str, model: str):
        super().__init__(api_key, model)
        self.client = OpenAI(api_key=api_key)
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        tools: Optional[List[Dict]] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> Dict:
        """Send chat request to OpenAI."""
        
        # Build request parameters
        params = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        # Add tools if provided
        if tools:
            params["tools"] = tools
        
        # Make API call
        response = self.client.chat.completions.create(**params)
        
        # Extract response
        message = response.choices[0].message
        
        return {
            "content": message.content if message.content else "",
            "tool_calls": message.tool_calls if hasattr(message, 'tool_calls') else None,
            "finish_reason": response.choices[0].finish_reason,
            "raw_response": message
        }
    
    def supports_tools(self) -> bool:
        """OpenAI supports function calling."""
        return True