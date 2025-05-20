#!/usr/bin/env bash
set -euo pipefail

cyan()  { printf '\033[1;36m%s\033[0m\n' "$1"; }
green() { printf '\033[1;32m%s\033[0m\n' "$1"; }
err()   { printf '\033[1;31m%s\033[0m\n' "$1"; exit 1; }

PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cyan "== Installation et démarrage automatique =="
echo "Dossier projet : $PROJECT_DIR"
cd "$PROJECT_DIR"

# 1) Gestionnaire de paquets
if command -v apt-get &>/dev/null; then
  PKG_MANAGER="apt"
elif command -v pacman &>/dev/null; then
  PKG_MANAGER="pacman"
else
  err "Distribution non supportée : installez les dépendances manuellement."
fi

# 2) Paquets système
cyan "[1/5] Installation des paquets système (sudo)…"
if [[ $PKG_MANAGER == "apt" ]]; then
  sudo apt-get update -y
  sudo apt-get install -y python3 python3-venv python3-pip nmap nikto git curl
else
  sudo pacman -Sy --noconfirm python python-virtualenv python-pip nmap nikto git curl
fi

# 3) SearchSploit
cyan "[2/5] Vérification de SearchSploit…"
if ! command -v searchsploit &>/dev/null; then
  sudo git clone --depth=1 https://gitlab.com/exploit-database/exploitdb.git /opt/exploitdb
  sudo ln -sf /opt/exploitdb/searchsploit /usr/local/bin/searchsploit
  sudo cp /opt/exploitdb/.searchsploit_rc /etc/searchsploit_rc || true
  green "SearchSploit installé."
else
  green "SearchSploit déjà présent."
fi

# 4) Virtualenv & pip
VENV_DIR=".venv"
cyan "[3/5] Création de l'environnement virtuel…"
rm -rf "$VENV_DIR"
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

cyan "[4/5] Installation des dépendances Python…"
pip install --upgrade pip setuptools wheel
if [[ -f requirements.txt ]]; then
  pip install -r requirements.txt
else
  err "requirements.txt introuvable !"
fi

# 5) VS Code settings (optionnel)
cyan "[5/5] Configuration VS Code…"
mkdir -p .vscode
cat > .vscode/settings.json << EOF
{
  "python.defaultInterpreterPath": "\${workspaceFolder}/.venv/bin/python",
  "python.analysis.extraPaths": ["\${workspaceFolder}/modules"]
}
EOF
green "VS Code prêt à l'emploi."

# 6) Lancement de l'application
green "Installation terminée ! Démarrage de Streamlit…"
exec streamlit run streamlit_app.py
