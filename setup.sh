#!/usr/bin/env bash
set -euo pipefail
cyan(){ printf '\033[1;36m%s\033[0m\n' "$1"; }
green(){ printf '\033[1;32m%s\033[0m\n' "$1"; }
err(){ printf '\033[1;31m%s\033[0m\n' "$1"; exit 1; }

cyan "== Installation automatique =="
if command -v apt-get &>/dev/null; then
  sudo apt-get update -y
  sudo apt-get install -y python3 python3-venv python3-pip nmap nikto git curl
elif command -v pacman &>/dev/null; then
  sudo pacman -Sy --noconfirm python python-virtualenv python-pip nmap nikto git curl
else
  err "Distribution non supportée."
fi
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
cyan "Installation terminée ! Lancez l'application :"
echo "streamlit run streamlit_app.py"
