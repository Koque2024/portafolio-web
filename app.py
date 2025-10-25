import os
from flask import Flask, render_template
import requests
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

app = Flask(__name__, static_folder="static", template_folder="templates")

# Configuración básica desde .env (con valores por defecto)
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "Koque2024")
LINKEDIN_URL = os.getenv("LINKEDIN_URL", "#")
EMAIL = os.getenv("EMAIL", "#")
SITE_TITLE = os.getenv("SITE_TITLE", "Benjamin Gasem — Software Developer")

def get_repos(username, per_page=10):
    """Obtiene los repos públicos más recientes del usuario en GitHub"""
    url = f"https://api.github.com/users/{username}/repos"
    params = {"sort": "updated", "per_page": per_page}
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        repos = r.json()
        return [
            {
                "name": repo.get("name"),
                "description": repo.get("description") or "Sin descripción",
                "url": repo.get("html_url"),
                "language": repo.get("language"),
                "stars": repo.get("stargazers_count", 0)
            }
            for repo in repos
        ]
    except Exception as e:
        print("Error obteniendo repositorios:", e)
        return []

@app.route("/")
def index():
    repos = get_repos(GITHUB_USERNAME)
    profile = {
        "name": "Benjamín Gasem",
        "title": "Software Developer",
        "summary": (
            "Ingeniero en informática enfocado en el desarrollo con Python y Flask. "
            "Experiencia en proyectos con React, migración de bases de datos y soluciones web escalables. "
            "Dominio del inglés y francés."
        ),
        "skills": ["Python", "Flask", "SQL", "REST APIs", "Git", "Docker", "React (básico)"],
        "github": f"https://github.com/{GITHUB_USERNAME}",
        "linkedin": LINKEDIN_URL,
        "email": EMAIL,
    }
    return render_template("index.html", repos=repos, profile=profile, site_title=SITE_TITLE)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
