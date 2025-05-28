# Modeling Environmental Impact on SSD using LLM

This repository accompanies the paper accepted at **ACM HotStorage 2025**, titled *"Can LLMs Model the Environmental Impact on SSD?"*

## Overview

This work explores the use of Large Language Models (LLMs) to predict how environmental factors—such as temperature, humidity, and vibration—affect the performance of Solid State Drives (SSDs). The goal is to understand whether LLMs, when combined with techniques like Chain-of-Thought prompting and Retrieval-Augmented Generation (RAG), can reason about environmental degradation patterns and provide useful forecasts of tail latency and bandwidth shifts.

The repository contains:

- Prompt templates and data files used for training and evaluation
- Processed datasets based on published SSD experiments
- Scripts for visualizing results

## Contents
- `data/` – Curated experimental datasets for temperature, humidity, and vibration
- `prompts/` – Chain-of-thought and retrieval-based prompt templates
- `results/` – LLM predictions, ground truth comparisons, and error metrics
- `scripts/` – Evaluation scripts and plotting tools

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
```
@inproceedings{ssd_llm_25,
  title     = {Can LLMs Model the Environmental Impact on SSD?},
  author    = {Mayur Akewar, Gang Quan, Sandeep Madireddy, Janki Bhimani},
  booktitle = {Proceedings of the 17th ACM Workshop on Hot Topics in Storage and File Systems (HotStorage)},
  year      = {2025},
  publisher = {ACM}
}
```

