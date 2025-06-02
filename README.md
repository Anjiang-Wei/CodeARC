# CodeARC: Benchmarking Reasoning Capabilities of LLM Agents for Inductive Program Synthesis

![Version](https://img.shields.io/badge/version-1.0.0-blue)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/)


## Quick Start

### Setting Up the Environment

1. **Create and activate a Conda environment**:

   ```bash
   conda create -y -n CodeARC python=3.10.12
   conda activate CodeARC
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set API keys**:
   Ensure you have valid API keys for the required services:

   ```bash
   export OPENAI_API_KEY=<your_openai_api_key>
   export ANTHROPIC_API_KEY=<your_anthropic_api_key>
   ```


## Running Main Evaluation


   ```python
   python3 run.py --model_name openai/gpt-4o-mini --total_idx 20
   ```
   We support OpenAI models (e.g., `openai/gpt-4o`), Anthropic models (e.g., `anthropic/claude-3-7-sonnet-20250219`), and models served by Together AI (e.g., `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo`). For testing purposes, you can pass `--total_idx 20` to limit evaluation to 20 problems instead of the full dataset (1114 problems). See run.py for additional configuration options.
   
   To summarize results:
   ```python
   python3 src/compute_metrics.py
   ```

---

## HuggingFace Dataset

The CodeARC datasets are hosted on HuggingFace:

- **Problems Dataset**: **Hidden for double-blind review**
- **Invocations Dataset**: **Hidden for double-blind review**

### Setting up HuggingFace Account

1. **Obtain an access token**:
   - Go to [HuggingFace Tokens](https://huggingface.co/settings/tokens) and generate a token with `read` or `write` permissions.

2. **Login using the token**:

   **Option A**: Use the command line:

   ```bash
   huggingface-cli login
   huggingface-cli whoami
   ```

   **Option B**: Add the token to the environment variable:

   ```plaintext
   export HF_TOKEN=<your_huggingface_token>
   ```

### Accessing Datasets via the HuggingFace `datasets` Library

You can directly load the datasets using the HuggingFace `datasets` library:

```python
from datasets import load_dataset

# Define dataset paths
hf_problems_path = "Hidden for double-blind review"
hf_invocations_path = "Hidden for double-blind review"

# Load datasets
problems_dataset = load_dataset(hf_problems_path)
invocations_dataset = load_dataset(hf_invocations_path)

# Example: Access the first training sample
print(problems_dataset["train"][0])
print(invocations_dataset["train"][0])
```
---

## License

This project is licensed under the [Apache 2.0 License](https://opensource.org/licenses/Apache-2.0).
