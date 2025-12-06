"""Test all LLM clients."""

import sys
sys.path.append('/Users/jibinkunjumon/projects/virtual-resume-chatbot')

from src.config.settings import Config
from src.llm.factory import create_llm_client


def test_client(provider_name: str):
    """Test a specific LLM provider."""
    
    print(f"\n{'='*60}")
    print(f"Testing {provider_name.upper()} Client")
    print('='*60)
    
    # Create config and client
    config = Config()
    config.AI_PROVIDER = provider_name
    
    client = create_llm_client(
        provider=config.AI_PROVIDER,
        api_key=config.get_api_key(),
        model=config.get_model_name()
    )
    
    # Test simple chat
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say 'Hello' in one word."}
    ]
    
    print(f"Sending test message to {provider_name}...")
    response = client.chat(messages)
    
    print(f"✅ Response: {response['content']}")
    print(f"   Supports tools: {client.supports_tools()}")
    

if __name__ == "__main__":
    # Test each provider
    test_client("openai")
    test_client("gemini")
    test_client("groq")
    
    print("\n" + "="*60)
    print("✅ All LLM clients tested successfully!")
    print("="*60)