"""Check Gemini API access and available models."""

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ No GOOGLE_API_KEY found in .env")
    exit()

print(f"🔑 API Key found: {api_key[:10]}...")
print("\n" + "="*60)

try:
    genai.configure(api_key=api_key)
    print("✅ Gemini API configured successfully")
    
    print("\n📋 Available models for generateContent:")
    print("="*60)
    
    models_found = False
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"✅ {model.name}")
            models_found = True
    
    if not models_found:
        print("❌ No models found! Your API key may not have access.")
        
except Exception as e:
    print(f"❌ Error: {e}")
    print("\n💡 This could mean:")
    print("   1. Invalid API key")
    print("   2. API key doesn't have Gemini access")
    print("   3. Billing not set up")

print("="*60)