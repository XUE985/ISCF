import json
from prompts_config import (
    baseline_prompt,
)

DATASET_PATH = "subsampled_random_dataset.jsonl"
OUTPUT_PATH = "results_prompt.json"


def load_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


dataset = load_jsonl(DATASET_PATH)[:10]

results = []

for idx, item in enumerate(dataset):
    request = item["prompt"]
    expected = item["completion"]

    print("\n" + "=" * 80)
    print(f"EXAMPLE {idx + 1}")
    print("=" * 80)
    print("REQUEST:\n", request)

    prompts = {
        "baseline": baseline_prompt(request)
    }

    responses = {}

    for name, prompt in prompts.items():
        print("\n" + "-" * 60)
        print(f"{name.upper()} PROMPT:")
        print("-" * 60)
        print(prompt)

        print("\nPaste LLM output below. End with an empty line:")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)

        responses[name] = "\n".join(lines)

    results.append({
        "prompt": request,
        "ground_truth": expected,
        "responses": responses
    })

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"\nSaved results to {OUTPUT_PATH}")
