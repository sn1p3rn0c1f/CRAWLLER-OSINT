# CRAWLLER-OSINT

🔎 OSINT-Crawler
Un outil d’OSINT (Open Source Intelligence) écrit en Python pour automatiser la collecte d’informations sur une cible : pseudo, email, domaine, nom & prénom.
Parfait pour les pentesters, investigateurs ou curieux ! 😈

🚀 Fonctionnalités
🔍 Recherche de pseudo sur plusieurs sites (réseaux sociaux, forums, plateformes)
📧 Vérification d’emails dans les bases de données leaks
🌐 Recherche WHOIS sur un domaine pour récupérer infos d’enregistrement
👤 Scraping automatique basé sur nom & prénom via Google/Bing avec dorks OSINT
📝 Export des résultats en JSON et CSV pour analyse ultérieure
📥 Installation
bash
Copier
Modifier
git clone https://github.com/tonpseudo/OSINT-Crawler.git
cd OSINT-Crawler
pip install -r requirements.txt
Les modules requis :

requests
beautifulsoup4
whois
colorama
🛠️ Usage
Lance simplement :

bash
Copier
Modifier
python main.py
Puis suis les instructions :

Entrez un pseudo → le tool cherche sur les réseaux.
Entrez un email → il vérifie s'il est compromis.
Entrez un nom de domaine → WHOIS lookup.
Entrez un nom + prénom → il scrape des infos sur plusieurs sites.
Les résultats sont exportés automatiquement dans le dossier /exports/.

📂 Structure du projet
javascript
Copier
Modifier
OSINT-Crawler/
├── modules/
│   ├── social_scan.py
│   ├── email_leak.py
│   ├── whois_lookup.py
│   ├── search_engine.py
│   └── export.py
├── exports/
│   └── (résultats ici)
├── main.py
├── README.md
└── requirements.txt
