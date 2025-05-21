#!/usr/bin/env bash
set -euo pipefail
# 0) init secrets
if [[ ! -f .streamlit/secrets.toml ]]; then
  mkdir -p .streamlit
  cp secrets.toml.example .streamlit/secrets.toml
fi
# inject
sed -i 's#client_id.*#client_id = "8BAb9oH8YY8aaHWRk44lt32YGrtUHDvB"#' .streamlit/secrets.toml
sed -i 's#client_secret.*#client_secret = "_dgDcOxV5Z6wGOWQKvMAY8TaigQJMMlmccfBkAcbD0dAHrVNAJTiKMj1pTRSdVy9"#' .streamlit/secrets.toml
sed -i 's#server_metadata_url.*#server_metadata_url = "https://dev-kpr0aaljq6domnhv.us.auth0.com/.well-known/openid-configuration"#' .streamlit/secrets.toml
# install sys deps
if command -v apt-get &>/dev/null; then
  sudo apt-get update; sudo apt-get install -y python3-venv python3-pip nmap nikto git curl
elif command -v pacman &>/dev/null; then
  sudo pacman -Sy --noconfirm python-virtualenv python-pip nmap nikto git curl
fi
# venv
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
# run
streamlit run streamlit_app.py
