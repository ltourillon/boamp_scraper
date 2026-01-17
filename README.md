# 🚀 BOAMP Scraper - Extracteur d'entreprises

Scraper Python gratuit pour extraire les entreprises de BOAMP (ou autres sites) avec filtrage par mots-clés.

## ⚙️ Installation

1. **Clone ou copie les fichiers dans VS Code**

2. **Installe les dépendances** (dans le terminal VS Code):
```bash
pip install -r requirements.txt
```

## 🎯 Utilisation

### Interface Graphique (Recommandé)
Pour lancer l'interface visuelle facile à utiliser :
```bash
streamlit run app.py
```
Cela ouvrira automatiquement une page dans votre navigateur où vous pourrez tout configurer.

### Ligne de commande (Avancé):
```bash
python boamp_scraper.py
```

### Le script va te demander:
1. **URL de la page** à scraper (ex: page d'avis d'attribution BOAMP)
2. **Mots-clés** séparés par virgules (ex: `plomberie, CVC, sanitaire`)

### Exemple:
```
📎 URL: https://www.boamp.fr/avis/detail/...
🔑 Mots-clés: plomberie, CVC, chauffage
```

## 📊 Résultat

Le script génère un fichier **`entreprises_boamp.csv`** avec:
- Nom de l'entreprise
- Email (si trouvé)
- Téléphone (si trouvé)
- Ville
- URL source
- Mots-clés matchés

## 💡 Conseils

### Pour BOAMP:
1. Va sur boamp.fr
2. Recherche "avis d'attribution" + "plomberie" + ta région
3. Clique sur un avis
4. Copie l'URL complète
5. Lance le scraper avec cette URL

### Mots-clés efficaces:
- Génériques: `plomberie, CVC, sanitaire, chauffage`
- Spécifiques: `VMC, robinetterie, tuyauterie`
- Multi-corps: `plomberie chauffage`

### Enrichissement après scraping:
1. Export CSV → Import dans Notion
2. Pour les emails manquants: Hunter.io (25 gratuits/mois)
3. Pour les tél manquants: Recherche Google/Pages Jaunes

## 🔧 Amélioration du scraper

Le scraper détecte automatiquement:
- Noms d'entreprises (SARL, SAS, SASU, etc.)
- Emails (format standard)
- Téléphones français (tous formats)
- Codes postaux + villes

### Si tu veux scraper plusieurs pages:
Modifie le script pour boucler sur une liste d'URLs.

## ⚠️ Notes légales

- Scraping de données **publiques** uniquement
- Respect du RGPD pour l'utilisation des données
- Pas d'utilisation abusive (rate limiting)
- Pour usage professionnel légitime uniquement

## 🆘 Problèmes fréquents

**"Module not found"** → Lance `pip install -r requirements.txt`

**Aucun résultat** → 
- Vérifie l'URL (doit être une page de détail, pas la recherche)
- Teste avec d'autres mots-clés
- La page peut avoir un format différent

**Trop de résultats parasites** →
- Utilise des mots-clés plus spécifiques
- Le script peut être amélioré avec des règles custom

## 📈 Prochaines étapes

1. ✅ Scraper une page
2. 🔄 Automatiser pour plusieurs pages
3. 📧 Enrichir avec Hunter.io API
4. 📊 Import automatique dans Notion via API
5. 🤖 Ajouter détection entreprise via SIREN/SIRET

Besoin d'aide ? Demande-moi !
