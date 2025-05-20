# Pentest Toolbox

## Prérequis
- Python 3.8+
- Git
- Nmap, Nikto, SearchSploit installés sur votre système

## Installation automatique
```bash
# Cloner le dépôt
git clone https://github.com/votre_utilisateur/rojet-etude-SDV.git
cd rojet-etude-SDV

# Lancer le script d'installation
bash setup.sh
```

## Utilisation manuelle
1. Créez et activez un environnement virtuel :
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Installez les dépendances :
   ```bash
   pip install --upgrade pip setuptools wheel
   pip install -r requirements.txt
   ```
3. Démarrez l'application :
   ```bash
   streamlit run streamlit_app.py
   ```