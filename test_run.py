from boamp_scraper import BOAMPScraper

url = "https://www.boamp.fr/pages/recherche/?disjunctive.type_marche&disjunctive.descripteur_code&disjunctive.dc&disjunctive.code_departement&disjunctive.type_avis&disjunctive.famille&sort=dateparution&refine.dc=270&refine.type_avis=6&refine.type_avis=8&q.filtre_etat=(NOT%20%23null(datelimitereponse)%20AND%20datelimitereponse%3C%222026-01-18%22)%20OR%20(%23null(datelimitereponse)%20AND%20datefindiffusion%3C%222026-01-18%22)#resultarea"

print("Lancement du test...")
scraper = BOAMPScraper()
# On teste avec 10 avis pour voir si ça passe le 3ème
results = scraper.scrape_search_results(url, keywords=[], max_results=10)

print(f"Test terminé. {len(results)} entreprises trouvées.")
for r in results:
    print(f"- {r.get('nom')} ({r.get('lot_title')})")
