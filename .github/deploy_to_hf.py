#!/usr/bin/env python3
"""
Deploy script for HuggingFace Spaces
This script uploads the repository to HuggingFace Spaces
"""
import os
import sys
from huggingface_hub import HfApi, login

def main():
    # Get credentials from environment
    hf_token = os.getenv("HF_TOKEN")
    hf_username = os.getenv("HF_USERNAME")
    space_name = os.getenv("SPACE_NAME")
    
    # Validate credentials
    if not all([hf_token, hf_username, space_name]):
        print("❌ Error: Missing environment variables!")
        print(f"HF_TOKEN: {'✅' if hf_token else '❌'}")
        print(f"HF_USERNAME: {'✅' if hf_username else '❌'}")
        print(f"SPACE_NAME: {'✅' if space_name else '❌'}")
        sys.exit(1)
    
    print(f"🔑 Logging in to HuggingFace...")
    login(token=hf_token)
    
    print(f"📦 Uploading to {hf_username}/{space_name}...")
    api = HfApi()
    
    repo_id = f"{hf_username}/{space_name}"
    
    try:
        # Upload the entire folder
        api.upload_folder(
            folder_path=".",
            repo_id=repo_id,
            repo_type="space",
            ignore_patterns=[".git/*", ".github/*", "__pycache__/*", "*.pyc", ".env"],
        )
        
        print("✅ Deployment complete!")
        print(f"🚀 Visit: https://huggingface.co/spaces/{repo_id}")
        
    except Exception as e:
        print(f"❌ Deployment failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
