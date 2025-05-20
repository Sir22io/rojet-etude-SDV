#!/usr/bin/env bash
set -euo pipefail

cyan()  { printf '\033[1;36m%s\033[0m\n' "$1"; }
green() { printf '\033[1;32m%s\033[0m\n' "$1"; }
err()   { printf '\033[1;31m%s\033[0m\n' "$1"; exit 1; }

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cyan "== Installation et démarrage automatique =="
echo "Dossier projet : $PROJECT_DIR"
cd "$PROJECT_DIR"

# 0) Copier l'exemple si nécessaire
if [[ ! -f .streamlit/secrets.toml ]]; then
  cyan "[0/5] Initialisation des secrets"
  mkdir -p .streamlit
  cp secrets.toml.example .streamlit/secrets.toml
fi

# 1) Paquets système
cyan "[1/5] Installation paquets système"
if command -v apt-get &>/dev/null; then
  sudo apt-get update -y
  sudo apt-get install -y python3 python3-venv python3-pip nmap nikto git curl
elif command -v pacman &>/dev/null; then
  sudo pacman -Sy --noconfirm python python-virtualenv python-pip nmap nikto git curl
else
  err "Distribution non supportée"
fi

# 2) SearchSploit
cyan "[2/5] Vérification SearchSploit"
if ! command -v searchsploit &>/dev/null; then
  sudo git clone --depth=1 https://gitlab.com/exploit-database/exploitdb.git /opt/exploitdb
  sudo ln -sf /opt/exploitdb/searchsploit /usr/local/bin/searchsploit
fi

# 3) Python env & deps
cyan "[3/5] Configuration Python"
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# 4) VS Code settings (optionnel)
cyan "[4/5] Configuration VS Code"
mkdir -p .vscode
cat > .vscode/settings.json << EOF
{
  "python.defaultInterpreterPath": "\${workspaceFolder}/.venv/bin/python",
  "python.analysis.extraPaths": ["\${workspaceFolder}/modules"]
}
EOF

# 5) Lancement de l'application
cyan "[5/5] Démarrage de Streamlit"
exec streamlit run streamlit_app.py
