import json
import os
# Import your logic from your other files
from load_yang import load_yang_models
from prompts import (
    baseline_prompt,
    role_prompt,
    constrained_prompt,
    structured_prompt
)

# 1. Load YANG models from your local folder
# Sidebar shows your folder is named "yang_files"
yang_models = load_yang_models("./yang_files")

# 2. Load the QA dataset
json_path = "qa_dataset.json"

if os.path.exists(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        qa_data = json.load(f)

    # Map your prompt strategies to their functions
    prompt_strategies = {
        "baseline": baseline_prompt,
        "role": role_prompt,
        "constrained": constrained_prompt,
        "structured": structured_prompt
    }

    # 3. Process each question in the dataset
    for item in qa_data:
        model_name = item["model"]
        
        # Ensure the required YANG file was actually loaded
        if model_name in yang_models:
            yang_text = yang_models[model_name]
            question = item["question"]

            print("\n" + "="*40)
            print(f"MODEL: {model_name}")
            print(f"QUESTION: {question}")
            print("="*40)

            # Generate and display each version of the prompt
            for strategy_name, func in prompt_strategies.items():
                print(f"\n>>> STRATEGY: {strategy_name.upper()}")
                generated_prompt = func(yang_text, question)
                
                # Print the first 400 characters of each result for review
                print(generated_prompt[:400] + "... [truncated]")
        else:
            print(f"\n[!] Missing Model: '{model_name}' not found in yang_files.")

else:
    print(f"Error: Could not find {json_path} in the current directory.")