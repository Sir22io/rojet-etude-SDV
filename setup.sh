#!/usr/bin/env bash
set -euo pipefail

# Installer paquets système
if command -v apt-get &>/dev/null; then
  sudo apt-get update -y
  sudo apt-get install -y python3 python3-venv python3-pip nmap nikto git curl
elif command -v pacman &>/dev/null; then
  sudo pacman -Sy --noconfirm python python-virtualenv python-pip nmap nikto git curl
fi

# Environnement Python
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Lancer Streamlit
streamlit run streamlit_app.py
