#!/usr/bin/env bash
set -euo pipefail

# 0) Ensure .streamlit/secrets.toml exists
if [[ ! -f .streamlit/secrets.toml ]]; then
  mkdir -p .streamlit
  cp secrets.toml.example .streamlit/secrets.toml
  echo "Copied secrets.toml.example to .streamlit/secrets.toml"
fi

# 1) Install system packages
if command -v apt-get &>/dev/null; then
  sudo apt-get update -y
  sudo apt-get install -y python3 python3-venv python3-pip nmap nikto git curl
elif command -v pacman &>/dev/null; then
  sudo pacman -Sy --noconfirm python python-virtualenv python-pip nmap nikto git curl
else
  echo "Unsupported distribution, install manually"; exit 1
fi

# 2) Ensure SearchSploit
if ! command -v searchsploit &>/dev/null; then
  sudo git clone --depth=1 https://gitlab.com/exploit-database/exploitdb.git /opt/exploitdb
  sudo ln -sf /opt/exploitdb/searchsploit /usr/local/bin/searchsploit
fi

# 3) Virtualenv & pip
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# 4) Launch
streamlit run streamlit_app.py
