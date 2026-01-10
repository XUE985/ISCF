#Define prompt templates for different strategies
def baseline_prompt(yang_text, question):
    return f"""
Here is a YANG model:

{yang_text}

Answer the following question:
{question}
"""


def role_prompt(yang_text, question):
    return f"""
You are a network engineer specialized in YANG data models and NETCONF.

Here is a YANG model:

{yang_text}

Question:
{question}
"""


def constrained_prompt(yang_text, question):
    return f"""
You are an expert in YANG models.

Rules:
- Use only the provided YANG model
- If the answer is not explicitly stated, say "Not specified in the model"
- Be concise (1–2 sentences)

YANG model:
{yang_text}

Question:
{question}
"""


def structured_prompt(yang_text, question):
    return f"""
You are a YANG model analyst.

Follow these steps:
1. Identify the relevant container, list, or leaf
2. Extract the required information
3. Provide the final answer

YANG model:
{yang_text}

Question:
{question}
"""
