# Pentest Toolbox

**Note de sécurité :** ne versionnez **jamais** le fichier `secrets.toml` contenant des informations sensibles. Utilisez le fichier d'exemple `secrets.toml.example`.

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

## Configuration OIDC
1. Copiez `.streamlit/secrets.toml.example` vers `.streamlit/secrets.toml` (le script le fera automatiquement si absent).
2. Remplissez vos `client_id`, `client_secret` et `cookie_secret` dans `.streamlit/secrets.toml`.
3. Ajoutez `http://localhost:8501/oauth2callback` dans les **Allowed Callback URLs** de votre application Auth0

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