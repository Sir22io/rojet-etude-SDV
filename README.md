# Pentest Toolbox

## Installation rapide

```bash
unzip rojet-etude-SDV-release.zip
cd rojet-etude-SDV-release
chmod +x setup.sh
./setup.sh
```

L’application démarrera automatiquement sur **http://localhost:8501** et utilisera Auth0 pour l’authentification.

## Détails

- Le script `setup.sh` installe les dépendances système et Python, crée un virtuel `.venv`,  
  copie `secrets.toml.example` dans `.streamlit/secrets.toml`, puis démarre l’application.
- Vos clients n’ont **aucune** manipulation manuelle de fichiers cachés à faire.
