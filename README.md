# Pentest Toolbox

## Prérequis
- Python 3.8+
- Git
- Nmap, Nikto, SearchSploit installés sur votre système

## Installation automatique
```bash
git clone https://github.com/votre_utilisateur/rojet-etude-SDV.git
cd rojet-etude-SDV
bash setup.sh
```

## Configuration OIDC
Copiez le fichier `secrets.toml.example` à la racine :
```bash
cp secrets.toml.example .streamlit/secrets.toml
```
Puis modifiez `.streamlit/secrets.toml` avec vos valeurs `client_id`, `client_secret`, `cookie_secret`.

## Lancement manuel
```bash
streamlit run streamlit_app.py
```