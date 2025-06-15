# 📊 Stock Analyzer

This app lets you upload a company's annual report (PDF), choose key investment questions (based on Asia Analytica’s 12-point checklist), and uses **ChatGPT (OpenAI API)** to answer intelligently — with caching to save on cost and time.

---

## ⚙️ Prerequisites

- Python ≥ 3.10 (we recommend 3.12 or 3.13)
- [`uv`](https://github.com/astral-sh/uv) (for fast virtual environments)
- [OpenAI API key](https://platform.openai.com/account/api-keys)
- (Optional) [`ollama`](https://ollama.com) if you want to experiment with local LLMs later

---

## ✅ Step 1: Install Python and `uv` (one-time setup)

```bash
# Install uv (if not already)
curl -Ls https://astral.sh/uv/install.sh | bash

# Create and activate virtual environment
uv venv --python $(which python3.12)  # Replace with your preferred version
source .venv/bin/activate

# Install required packages
uv pip install -r requirements.txt
