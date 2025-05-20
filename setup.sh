#!/usr/bin/env bash
set -euo pipefail

cyan()  { printf '\033[1;36m%s\033[0m\n' "$1"; }
green() { printf '\033[1;32m%s\033[0m\n' "$1"; }
err()   { printf '\033[1;31m%s\033[0m\n' "$1"; exit 1; }

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cyan "== Installation et démarrage automatique =="
echo "Projet : $PROJECT_DIR"
cd "$PROJECT_DIR"

# 0) Copier l'exemple si nécessaire
if [[ ! -f .streamlit/secrets.toml ]]; then
  cyan "[0/6] Initialisation des secrets"
  mkdir -p .streamlit
  cp secrets.toml.example .streamlit/secrets.toml
fi

# 0b) Injecter les vraies valeurs d'Auth0
cyan "[0b/6] Injection des credentials Auth0"
sed -i 's#client_id.*#client_id           = "8BAb9oH8YY8aaHWRk44lt32YGrtUHDvB"#' .streamlit/secrets.toml
sed -i 's#client_secret.*#client_secret       = "_dgDcOxV5Z6wGOWQKvMAY8TaigQJMMlmccfBkAcbD0dAHrVNAJTiKMj1pTRSdVy9"#' .streamlit/secrets.toml
sed -i 's#server_metadata_url.*#server_metadata_url = "https://dev-kpr0aaljq6domnhv.us.auth0.com/.well-known/openid-configuration"#' .streamlit/secrets.toml

# 1) Paquets système
cyan "[1/6] Installation des paquets système"
if command -v apt-get &>/dev/null; then
  sudo apt-get update -y
  sudo apt-get install -y python3 python3-venv python3-pip nmap nikto git curl
elif command -v pacman &>/dev/null; then
  sudo pacman -Sy --noconfirm python python-virtualenv python-pip nmap nikto git curl
else
  err "Distribution non supportée."
fi

# 2) SearchSploit
cyan "[2/6] Vérification de SearchSploit"
if ! command -v searchsploit &>/dev/null; then
  sudo git clone --depth=1 https://gitlab.com/exploit-database/exploitdb.git /opt/exploitdb
  sudo ln -sf /opt/exploitdb/searchsploit /usr/local/bin/searchsploit
fi

# 3) Python venv & dépendances
cyan "[3/6] Configuration de l'environnement Python"
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# 4) Config VS Code (optionnel)
cyan "[4/6] Configuration VS Code"
mkdir -p .vscode
cat > .vscode/settings.json << EOF
{
  "python.defaultInterpreterPath": "\${workspaceFolder}/.venv/bin/python",
  "python.analysis.extraPaths": ["\${workspaceFolder}/modules"]
}
EOF

# 5) Nettoyage éventuel
cyan "[5/6] Nettoyage"
# (pas d'étape spécifique ici)

# 6) Lancement de Streamlit
cyan "[6/6] Démarrage de l'application Streamlit"
exec streamlit run streamlit_app.py
