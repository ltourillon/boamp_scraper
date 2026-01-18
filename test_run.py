from boamp_scraper import BOAMPScraper

url = "https://www.boamp.fr/pages/recherche/?disjunctive.type_marche&disjunctive.descripteur_code&disjunctive.dc&disjunctive.code_departement&disjunctive.type_avis&disjunctive.famille&sort=dateparution&refine.type_marche=SERVICES&refine.type_marche=TRAVAUX&refine.dc=270&refine.code_departement=14&refine.code_departement=16&refine.code_departement=17&refine.code_departement=22&refine.code_departement=24&refine.code_departement=27&refine.code_departement=28&refine.code_departement=29&refine.code_departement=33&refine.code_departement=35&refine.code_departement=36&refine.code_departement=37&refine.code_departement=40&refine.code_departement=41&refine.code_departement=44&refine.code_departement=49&refine.code_departement=50&refine.code_departement=53&refine.code_departement=56&refine.code_departement=61&refine.code_departement=64&refine.code_departement=72&refine.code_departement=79&refine.code_departement=85&refine.code_departement=86&refine.code_departement=87&refine.type_avis=6&refine.type_avis=8&q.timerange.dateparution=dateparution:%5B2024-01-01%20TO%202026-01-18%5D#"

print("Lancement du test...")
scraper = BOAMPScraper()
# On teste avec 10 avis pour voir si ça passe le 3ème
results = scraper.scrape_search_results(url, keywords=[], max_results=10)

print(f"Test terminé. {len(results)} entreprises trouvées.")
for r in results:
    print(f"- {r.get('nom')} ({r.get('lot_title')})")
