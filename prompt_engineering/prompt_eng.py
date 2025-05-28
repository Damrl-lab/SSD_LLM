import os
import re
import argparse

import pandas as pd
import numpy as np
import openai

import gptAPI.prompt as prompt  # your prompt.py must define a top-level variable `prompt`

def evaluate(
    data_path: str,
    gt_col: str,
    api_key: str,
    model: str = "gpt-4",
    n_examples: int = None
):
    """
    Loads data, formats your imported prompt per row, calls GPT, parses a number,
    then computes MSE and relative MSE%.
    """
    openai.api_key = api_key

    # 1) load the file
    if data_path.lower().endswith((".xls", ".xlsx")):
        df = pd.read_excel(data_path)
    else:
        df = pd.read_csv(data_path)

    if n_examples:
        df = df.iloc[:n_examples]

    y_true = []
    y_pred = []

    # 2) for each example...
    for idx, row in df.iterrows():
        # fill your prompt template
        filled = prompt.prompt.format(**row.to_dict())

        # call the chat endpoint
        resp = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": filled}]
        )
        text = resp.choices[0].message.content.strip()

        # pull the first numeric token
        m = re.search(r"[-+]?\d*\.?\d+", text)
        if not m:
            print(f"[row {idx}] no number in response; skipping:\n{text}\n")
            continue

        pred = float(m.group())
        true = float(row[gt_col])

        y_pred.append(pred)
        y_true.append(true)

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    # 3) compute errors
    mse = np.mean((y_pred - y_true) ** 2)
    rel_mse_pct = mse / np.mean(y_true ** 2) * 100

    print(f"Evaluated {len(y_true)} examples")
    print(f"MSE           = {mse:.6f}")
    print(f"Relative MSE% = {rel_mse_pct:.2f}%")

    return mse, rel_mse_pct


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Evaluate a fixed prompt against ground-truth values with MSE%"
    )
    parser.add_argument(
        "--data", "-d",
        required=True,
        help="Path to your CSV or Excel file"
    )
    parser.add_argument(
        "--gt-col", "-g",
        required=True,
        help="Name of the ground-truth column"
    )
    parser.add_argument(
        "--api-key", "-k",
        required=True,
        help="Your OpenAI API key"
    )
    parser.add_argument(
        "--model", "-m",
        default="gpt-4",
        help="Which ChatCompletion model to use (default: gpt-4)"
    )
    parser.add_argument(
        "--limit", "-n",
        type=int,
        default=None,
        help="Only evaluate on the first N rows (for testing)"
    )

    args = parser.parse_args()
    evaluate(
        data_path=args.data,
        gt_col=args.gt_col,
        api_key=args.api_key,
        model=args.model,
        n_examples=args.limit
    )

    """
    python prompt_eng.py \
  --data path/to/your_data.xlsx \
  --gt-col tail_latency \
  --api-key sk-…YOUR_KEY… \
  --model gpt-4 \
  --limit 100
    """
