#!/usr/bin/env bash
set -euo pipefail

cyan(){ printf '\033[1;36m%s\033[0m\n' "$1"; }
green(){ printf '\033[1;32m%s\033[0m\n' "$1"; }
err(){ printf '\033[1;31m%s\033[0m\n' "$1"; exit 1; }

cyan "== Installation & lancement sur Kali =="

# 1) Installer paquets système
cyan "[1/4] Installation paquets APT"
sudo apt-get update -y
sudo apt-get install -y python3 python3-venv python3-pip nmap nikto exploitdb git curl

# 2) Créer et activer l'environnement Python
cyan "[2/4] Configuration Python"
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# 3) VS Code settings (optionnel)
cyan "[3/4] Configuration VS Code"
mkdir -p .vscode
cat > .vscode/settings.json << EOF
{
  "python.defaultInterpreterPath": "\${workspaceFolder}/.venv/bin/python",
  "python.analysis.extraPaths": ["\${workspaceFolder}/modules"]
}
EOF

# 4) Lancement de Streamlit
cyan "[4/4] Lancement de l'application"
exec streamlit run streamlit_app.py
