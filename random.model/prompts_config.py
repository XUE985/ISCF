def baseline_prompt(request: str) -> str:
    return f"""
Generate IOS XR telemetry configuration for the following request:

{request}
"""

