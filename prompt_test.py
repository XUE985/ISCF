import json
from load_yang import load_yang_models

# 1. Load YANG models from the local folder
# Make sure the folder name matches exactly: "yang_files"
yang_models = load_yang_models("./yang_files")

# 2. Load QA dataset directly from your JSON file
with open("./qa_dataset.json", "r", encoding="utf-8") as f:
    qa_data = json.load(f)

# 3. Check if we have data and generate a prompt
if len(qa_data) > 0:
    sample = qa_data[0]
    model_filename = sample["model"]

    # Safety check: does the model exist in our loaded dictionary?
    if model_filename in yang_models:
        yang_text = yang_models[model_filename]
        
        prompt = f"""
Here is a YANG model:

{yang_text}

Question:
{sample['question']}
"""
        print("--- PROMPT GENERATED SUCCESSFULLY ---")
        print(prompt[:1000]) # Print first 1000 characters to verify
    else:
        print(f"Error: Model '{model_filename}' not found in yang_files folder.")
        print("Available files:", list(yang_models.keys()))