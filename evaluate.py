import json

def score_correctness(prediction, ground_truth):
    return int(ground_truth.lower() in prediction.lower())


with open("results.json", "r", encoding="utf-8") as f:
    results = json.load(f)

scores = {}

for item in results:
    gt = item["ground_truth"]

    for prompt_type, response in item["responses"].items():
        scores.setdefault(prompt_type, []).append(
            score_correctness(response, gt)
        )

print("\nAccuracy per prompt type:\n")
for prompt_type, values in scores.items():
    accuracy = sum(values) / len(values)
    print(f"{prompt_type}: {accuracy:.2f}")
