# AI Evaluation Framework

A Python-based pipeline designed to benchmark Large Language Model (LLM) responses against defined structural and content rubrics. This tool helps in minimizing hallucinations and ensuring strict compliance with technical parameters.

## Key Features
- **Automated Benchmarking:** Processes model outputs against standardized rubric criteria.
- **Configurable Rubrics:** Uses JSON configuration to easily update evaluation standards.
- **Metrics Tracking:** Calculates consistency and accuracy scores and outputs them to a CSV report.

## Tech Stack
- Python 3.x
- Pandas (for data manipulation and reporting)

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Run the evaluator: `python evaluate.py`
3. View the generated `evaluation_results.csv` file for the final scores.
