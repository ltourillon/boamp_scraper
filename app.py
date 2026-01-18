
import streamlit as st
from boamp_scraper import BOAMPScraper
import csv
import io

# Configuration de la page
st.set_page_config(
    page_title="BOAMP Scraper",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS pour le look aux couleurs EDAO
st.markdown("""
<style>
    /* --- BUTTONS --- */
    /* Force white text on ALL buttons (Primary and Secondary) */
    .stButton > button, 
    .stDownloadButton > button,
    div[data-testid="stButton"] > button,
    div[data-testid="stDownloadButton"] > button {
        background-color: #00A1C8 !important;
        border: none !important;
        transition: all 0.3s ease;
    }
    
    /* Text Color Force White */
    .stButton > button p, 
    .stDownloadButton > button p,
    div[data-testid="stButton"] > button p {
        color: #FFFFFF !important; 
        font-weight: bold !important;
    }

    /* Hover Effects */
    .stButton > button:hover, 
    .stDownloadButton > button:hover {
        background-color: #0088AA !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        color: #FFFFFF !important;
    }

    /* --- CHECKBOXES --- */
    /* Label text color */
    div[data-testid="stCheckbox"] label p {
       color: #1F2937 !important;
       font-weight: 500;
    }

    /* The Checkbox Box itself (Unchecked) */
    div[data-testid="stCheckbox"] span[role="checkbox"] {
        border-color: #00A1C8 !important; /* Light Blue Border */
    }

    /* The Checkbox Box itself (CHECKED) */
    /* Targeting the aria-checked state */
    div[data-testid="stCheckbox"] span[role="checkbox"][aria-checked="true"] {
        background-color: #0B2C4A !important; /* Navy Blue */
        border-color: #0B2C4A !important;
    }
    
    /* Fix for some streamlit versions using svg inside */
    div[data-testid="stCheckbox"] span[role="checkbox"][aria-checked="true"] > div {
         background-color: #0B2C4A !important;
    }

    /* --- GENERAL UI --- */
    div[data-testid="stExpander"] {
        border: 1px solid #E5E7EB;
        border-radius: 8px;
        background-color: #F9FAFB;
        color: #1F2937;
    }
    h1, h2, h3 {
        color: #1F2937 !important;
    }
    /* Accent line / secondary color touches */
    .highlight-span {
        color: #00A1C8;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🚀 BOAMP Scraper")
st.markdown("Extracteur d'entreprises intelligent pour les avis de marché.")

# Sidebar pour les inputs
with st.sidebar:
    st.header("Configuration")
    
    url = st.text_input(
        "URL de l'avis",
        placeholder="https://www.boamp.fr/pages/avis/...",
        help="Collez ici l'URL complète de l'avis d'attribution."
    )
    
    keywords_input = st.text_area(
        "Mots-clés (séparés par virgules)",
        value="",
        placeholder="Laisser vide pour tout extraire, ou : plomberie, chauffage...",
        height=100
    )
    
    st.subheader("Champs à exporter")
    col1, col2 = st.columns(2)
    with col1:
        show_nom = st.checkbox("Nom", True)
        show_email = st.checkbox("Email", True)
        show_tel = st.checkbox("Téléphone", True)
        show_id = st.checkbox("N° Avis", True)
    with col2:
        show_ville = st.checkbox("Ville", True)
        show_url = st.checkbox("URL Source", True)
        show_match = st.checkbox("Matchs", False)
        show_lot = st.checkbox("Lot", True)

    launch_btn = st.button("Lancer l'extraction")

# Main content
if launch_btn and url:
    raw_keywords = keywords_input.split(',')
    keywords = [k.strip() for k in raw_keywords if k.strip()]
    
    with st.spinner('Extraction en cours... (Analyse de l\'API DILA etc.)'):
        try:
            scraper = BOAMPScraper()
            
            # Détection du type d'URL (Avis unique ou Recherche)
            if "pages/recherche" in url:
                st.info("🔎 Détection d'une page de recherche BOAMP. Passage en mode extraction de masse...")
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                def update_progress(current, total, msg):
                    progress_bar.progress(current / total)
                    status_text.text(f"{msg} ({current}/{total})")
                
                results = scraper.scrape_search_results(url, keywords, progress_callback=update_progress)
                status_text.text("Extraction terminée !")
                progress_bar.empty()
                
            else:
                results = scraper.scrape_page(url, keywords)
            
            if results:
                st.success(f"✅ {len(results)} entreprises trouvées !")
                
                # Filtrage des colonnes
                display_data = []
                for r in results:
                    entry = {}
                    if show_id: entry['N° Avis'] = r.get('avis_id') or r.get('source_avis_id')
                    if show_nom: entry['Nom'] = r.get('nom')
                    if show_lot: entry['Lot'] = r.get('lot_title')
                    if show_email: entry['Email'] = r.get('email')
                    if show_tel: entry['Téléphone'] = r.get('telephone')
                    if show_ville: entry['Ville'] = r.get('ville')
                    if show_url: entry['URL Source'] = r.get('url_source')
                    if show_match: entry['Matchs'] = r.get('mots_cles_matches')
                    display_data.append(entry)
                
                # Affichage tableau
                st.dataframe(display_data, use_container_width=True)
                
                # Export CSV
                csv_buffer = io.StringIO()
                if display_data:
                    writer = csv.DictWriter(csv_buffer, fieldnames=display_data[0].keys())
                    writer.writeheader()
                    writer.writerows(display_data)
                
                st.download_button(
                    label="📥 Télécharger CSV",
                    data=csv_buffer.getvalue(),
                    file_name="entreprises_boamp.csv",
                    mime="text/csv",
                )
                
            else:
                st.warning("⚠️ Aucune entreprise trouvée avec ces critères.")
                
        except Exception as e:
            st.error(f"❌ Une erreur est survenue : {e}")

elif launch_btn and not url:
    st.error("⚠️ Veuillez entrer une URL valide.")
else:
    st.info("👈 Configurez votre recherche dans la barre latérale pour commencer.")
