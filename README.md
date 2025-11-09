# Azure Chatbot Project
This repository contains a simple Python chatbot that demonstrates how to connect to Azure AI Language (Text Analytics) for sentiment analysis.

## Contents
- `app.py` - Main runnable chatbot (console-based). Uses Azure Text Analytics if the SDK and environment variables are available; otherwise falls back to a mock sentiment analyzer.
- `config.py` - Configuration class (`DefaultConfig`) that reads endpoint and key from environment variables.
- `echo_bot.py` - Simple bot logic that echoes user messages and augments replies with sentiment results.
- `requirements.txt` - Python dependencies.
- `run_demo.sh` / `run_demo.bat` - Convenience scripts for Linux/macOS and Windows.
- `LICENSE` - MIT license.

## Assignment Submission Notes
- Include this zip file and the GitHub repository URL when submitting to your instructor.
- Replace the placeholder GitHub URL in this README with your repository link before submission.

## Setup (local)
1. Create a Python 3.8+ virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate    # Windows (PowerShell)
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Set Azure environment variables (if you want real Azure sentiment):
   - Windows (PowerShell):
     ```powershell
     $env:MicrosoftAIServiceEndpoint = "https://<your-resource-name>.cognitiveservices.azure.com/"
     $env:MicrosoftAPIKey = "<your-key>"
     ```
   - macOS / Linux:
     ```bash
     export MicrosoftAIServiceEndpoint="https://<your-resource-name>.cognitiveservices.azure.com/"
     export MicrosoftAPIKey="<your-key>"
     ```
4. Run the chatbot:
   ```bash
   python app.py
   ```
5. Interact in the console. Type `exit` or `quit` to stop.

