"""Google Gemini LLM Client Implementation."""

import google.generativeai as genai
from typing import List, Dict, Optional
from .base_client import BaseLLMClient


class GeminiClient(BaseLLMClient):
    """Google Gemini client implementation."""
    
    def __init__(self, api_key: str, model: str):
        super().__init__(api_key, model)
        genai.configure(api_key=api_key)
        self.client = genai.GenerativeModel(model)
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        tools: Optional[List[Dict]] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> Dict:
        """Send chat request to Gemini."""
        
        # Convert messages to Gemini format
        # Gemini expects different format than OpenAI
        prompt = self._convert_messages_to_prompt(messages)
        
        # Configure generation
        generation_config = {
            "temperature": temperature,
            "max_output_tokens": max_tokens,
        }
        
        # Generate response
        response = self.client.generate_content(
            prompt,
            generation_config=generation_config
        )
        
        return {
            "content": response.text,
            "tool_calls": None,  # Gemini has different tool calling API
            "finish_reason": "stop",
            "raw_response": response
        }
    
    def _convert_messages_to_prompt(self, messages: List[Dict[str, str]]) -> str:
        """Convert OpenAI-style messages to a single prompt string."""
        prompt_parts = []
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "system":
                prompt_parts.append(f"Instructions: {content}\n")
            elif role == "user":
                prompt_parts.append(f"User: {content}\n")
            elif role == "assistant":
                prompt_parts.append(f"Assistant: {content}\n")
        return "\n".join(prompt_parts)
    
    def supports_tools(self) -> bool:
        """Gemini has limited tool support."""
        return False  # For simplicity, we'll handle this separately