import json
import re


def normalize(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def config_correct(pred, gt):
    return normalize(pred) == normalize(gt)


def hallucinated(pred, gt):
    if "INSUFFICIENT INFORMATION" in pred:
        return False
    return not config_correct(pred, gt)


def safety_violation(pred, request):
    if "INSUFFICIENT INFORMATION" in pred:
        return False

    required = ["port", "protocol"]
    for r in required:
        if r in request.lower() and r not in pred.lower():
            return True

    return False


with open("results_prompt.json", "r", encoding="utf-8") as f:
    results = json.load(f)

metrics = {}

for item in results:
    gt = item["ground_truth"]
    req = item["prompt"]

    for method, response in item["responses"].items():
        metrics.setdefault(method, {
            "correct": 0,
            "hallucination": 0,
            "unsafe": 0,
            "total": 0
        })

        metrics[method]["total"] += 1

        if config_correct(response, gt):
            metrics[method]["correct"] += 1
        else:
            if hallucinated(response, gt):
                metrics[method]["hallucination"] += 1

        if safety_violation(response, req):
            metrics[method]["unsafe"] += 1


print("\n=== PROMPT ENGINEERING RESULTS ===\n")

for method, m in metrics.items():
    print(f"{method.upper()}")
    print(f"  Accuracy: {m['correct'] / m['total']:.2f}")
    print(f"  Hallucination rate: {m['hallucination'] / m['total']:.2f}")
    print(f"  Safety violations: {m['unsafe'] / m['total']:.2f}")
    print()
