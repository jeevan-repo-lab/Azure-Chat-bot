#!/bin/bash
echo "Activating venv (if exists) and running app.py"
if [ -d "venv" ]; then
  source venv/bin/activate
fi
python app.py
