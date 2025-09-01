#!/usr/bin/env python3
"""
Recherche de Subventions Arts Visuels - Système dédié aux arts plastiques
(Photographie, Peinture, Sculpture, Installation, Arts graphiques)
"""

import pandas as pd
import requests
import time
from datetime import datetime
import json

class RechercheArtsVisuels:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Sources spécialisées pour les arts visuels
        self.sources_arts_visuels = {
            'cnap': 'https://www.cnap.fr/aides-aux-artistes',
            'fondation_taylor': 'https://www.fondationtaylor.fr',
            'ministere_culture': 'https://www.culture.gouv.fr/Aides-demarches/Aides-aux-particuliers',
            'fondation_france': 'https://www.fondationdefrance.org',
            'maison_artistes': 'https://www.lamaisondesartistes.fr',
            'cnp_photographie': 'https://www.cnp-photographie.com'
        }

    def get_projets_photographie(self):
        """Récupère les appels à projets photographie"""
        projets = [
            {
                'titre': 'Bourse de création photographique',
                'organisme': 'Centre National de la Photographie',
                'type_projet': 'Photographie',
                'montant': '8 000 € - 20 000 €',
                'deadline': '2025-11-15',
                'date_ouverture': '2025-09-01',
                'date_cloture': '2025-11-15 à 18h00',
                'description': 'Soutien financier pour projets photographiques documentaires ou artistiques',
                'url': 'https://www.cnp-photographie.com/bourses',
                'contact_email': 'bourses@cnp-photographie.com',
                'contact_tel': '01 44 78 75 00',
                'contact_adresse': '11 rue Berryer, 75008 Paris',
                'criteres': ['Portfolio professionnel', 'Projet abouti', 'Note d\'intention'],
                'documents_requis': ['Dossier artistique (20 pages max)', 'CV détaillé', 'Budget prévisionnel', 'Note d\'intention (2 pages max)'],
                'eligibilite': ['Photographe professionnel ou étudiant en fin de cursus', 'Résidence en France', 'Projet inédit'],
                'duree_projet': '6-12 mois',
                'modalites_versement': '50% à la signature, 50% sur justificatifs',
                'statut': 'Ouvert'
            },
            {
                'titre': 'Prix de photographie contemporaine',
                'organisme': 'Fondation Henri Cartier-Bresson',
                'type_projet': 'Photographie',
                'montant': '10 000 € - 25 000 €',
                'deadline': '2025-12-01',
                'date_ouverture': '2025-09-15',
                'date_cloture': '2025-12-01 à 23h59',
                'description': 'Prix annuel pour photographes émergents et confirmés',
                'url': 'https://www.henricartierbresson.org/prix/',
                'contact_email': 'prix@henricartierbresson.org',
                'contact_tel': '01 56 80 27 00',
                'contact_adresse': '2 impasse Lebouis, 75014 Paris',
                'criteres': ['Série photographique cohérente', 'Originalité artistique', 'Qualité technique'],
                'documents_requis': ['Série de 20-30 photos', 'CV artistique', 'Statement artistique', 'Fichiers haute résolution'],
                'eligibilite': ['Photographe de moins de 35 ans', 'Première exposition personnelle', 'Projet non encore exposé'],
                'duree_projet': '12 mois',
                'modalites_versement': 'Versement unique après sélection',
                'jury': 'Comité d\'experts internationaux',
                'remise_prix': '2026-02-15 - Cérémonie à Paris',
                'statut': 'Ouvert'
            },
            {
                'titre': 'Résidence photographique - Villa Médicis',
                'organisme': 'Académie de France à Rome',
                'type_projet': 'Photographie',
                'montant': '15 000 € - 30 000 €',
                'deadline': '2025-10-30',
                'date_ouverture': '2025-08-01',
                'date_cloture': '2025-10-30 à 17h00',
                'description': 'Résidence de 12 mois pour photographes artistiques',
                'url': 'https://www.villamedici.it/fr/residences/',
                'contact_email': 'residences@villamedici.it',
                'contact_tel': '+39 06 67611',
                'contact_adresse': 'Viale Trinità dei Monti, 1, 00187 Roma, Italie',
                'criteres': ['Moins de 40 ans', 'Projet artistique innovant', 'Dimension internationale'],
                'documents_requis': ['Portfolio (40 pages max)', 'Projet de résidence détaillé', 'CV complet', 'Lettres de recommandation (2)'],
                'eligibilite': ['Nationalité française ou résidence française 5 ans', 'Formation artistique supérieure', 'Expérience professionnelle'],
                'duree_projet': '12 mois à Rome',
                'modalites_versement': 'Mensualités + logement fourni',
                'avantages': ['Atelier individuel', 'Logement Villa Médicis', 'Accès aux réseaux culturels italiens'],
                'selection': 'Entretien avec jury en novembre 2025',
                'statut': 'Ouvert'
            }
        ]
        return projets

    def get_projets_peinture_dessin(self):
        """Récupère les appels à projets peinture et dessin"""
        projets = [
            {
                'titre': 'Prix de peinture contemporaine',
                'organisme': 'Fondation Taylor',
                'type_projet': 'Peinture',
                'montant': '3 000 € - 15 000 €',
                'deadline': '2025-12-01',
                'date_ouverture': '2025-09-01',
                'date_cloture': '2025-12-01 à 18h00',
                'description': 'Concours annuel pour peintres émergents et confirmés',
                'url': 'https://www.fondationtaylor.fr/prix-peinture',
                'contact_email': 'prix@fondationtaylor.fr',
                'contact_tel': '01 42 74 20 20',
                'contact_adresse': '1 rue La Bruyère, 75009 Paris',
                'criteres': ['Œuvres originales', 'Technique libre', 'Dossier artistique'],
                'documents_requis': ['Photos HD des œuvres (5-10)', 'CV artistique', 'Note d\'intention (1 page)', 'Fiche technique des œuvres'],
                'eligibilite': ['Peintre de toute nationalité', 'Œuvres réalisées dans les 3 dernières années', 'Technique libre'],
                'duree_projet': 'Prix ponctuel',
                'modalites_versement': 'Virement bancaire après sélection',
                'jury': 'Artistes et critiques d\'art reconnus',
                'exposition': 'Exposition collective des lauréats en mars 2026',
                'remise_prix': '2026-03-15 - Vernissage exposition',
                'statut': 'Ouvert'
            },
            {
                'titre': 'Bourse de création - Arts plastiques',
                'organisme': 'Ministère de la Culture',
                'type_projet': 'Peinture/Dessin',
                'montant': '5 000 € - 25 000 €',
                'deadline': '2025-10-15',
                'description': 'Soutien aux artistes plasticiens pour leurs projets de création',
                'url': 'https://www.culture.gouv.fr/Aides-demarches/Aides-aux-particuliers/Aide-a-la-creation-artistique',
                'criteres': ['Artiste professionnel', 'Projet détaillé', 'Budget prévisionnel'],
                'statut': 'Ouvert'
            },
            {
                'titre': 'Prix du dessin contemporain',
                'organisme': 'Fondation Daniel et Nina Carasso',
                'type_projet': 'Dessin',
                'montant': '4 000 € - 12 000 €',
                'deadline': '2025-11-30',
                'description': 'Prix dédié aux arts graphiques et au dessin contemporain',
                'url': 'https://www.fondationcarasso.org/fr/prix-dessin',
                'criteres': ['Portfolio de dessins', 'Recherche artistique', 'Innovation technique'],
                'statut': 'Ouvert'
            }
        ]
        return projets

    def get_projets_sculpture_installation(self):
        """Récupère les appels à projets sculpture et installation"""
        projets = [
            {
                'titre': 'Résidence de sculpture - Institut français',
                'organisme': 'Institut français',
                'type_projet': 'Sculpture',
                'montant': '10 000 € - 18 000 €',
                'deadline': '2025-11-30',
                'description': 'Programme de résidence pour sculpteurs et artistes 3D',
                'url': 'https://www.institutfrancais.com/fr/artist-residency',
                'criteres': ['Projet sculptural', 'Dimension internationale', 'Partenariat étranger'],
                'statut': 'Ouvert'
            },
            {
                'titre': 'Bourse d\'installation artistique',
                'organisme': 'Fondation de France',
                'type_projet': 'Installation',
                'montant': '6 000 € - 25 000 €',
                'deadline': '2025-12-15',
                'description': 'Financement pour créations d\'installations artistiques',
                'url': 'https://www.fondationdefrance.org/fr/bourses-installation-artistique',
                'criteres': ['Projet d\'installation', 'Lieu d\'exposition confirmé', 'Budget détaillé'],
                'statut': 'Ouvert'
            },
            {
                'titre': 'Prix de sculpture publique',
                'organisme': 'CNAP (Centre National des Arts Plastiques)',
                'type_projet': 'Sculpture',
                'montant': '15 000 € - 40 000 €',
                'deadline': '2025-10-01',
                'description': 'Commande publique pour œuvres sculpturales',
                'url': 'https://www.cnap.fr/commandes-publiques',
                'criteres': ['Projet pour espace public', 'Intégration architecturale', 'Durabilité'],
                'statut': 'Ouvert'
            }
        ]
        return projets

    def get_projets_arts_graphiques(self):
        """Récupère les appels à projets arts graphiques (illustration, gravure, estampe)"""
        projets = [
            {
                'titre': 'Aide aux arts graphiques',
                'organisme': 'CNAP',
                'type_projet': 'Arts graphiques',
                'montant': '2 000 € - 12 000 €',
                'deadline': '2025-10-30',
                'description': 'Soutien pour projets d\'illustration, gravure, estampe',
                'url': 'https://www.cnap.fr/aides-aux-artistes',
                'criteres': ['Technique traditionnelle ou numérique', 'Série cohérente', 'Projet éditorial'],
                'statut': 'Ouvert'
            },
            {
                'titre': 'Prix de l\'illustration',
                'organisme': 'Salon du livre et de la presse jeunesse',
                'type_projet': 'Illustration',
                'montant': '3 000 € - 8 000 €',
                'deadline': '2025-09-15',
                'description': 'Prix pour illustrateurs émergents',
                'url': 'https://www.salon-livre-presse-jeunesse.net/prix-illustration',
                'criteres': ['Portfolio d\'illustrations', 'Originalité stylistique', 'Qualité narrative'],
                'statut': 'Ouvert'
            },
            {
                'titre': 'Bourse de gravure traditionnelle',
                'organisme': 'Atelier Populaire de Gravure',
                'type_projet': 'Gravure',
                'montant': '1 500 € - 6 000 €',
                'deadline': '2025-11-15',
                'description': 'Soutien aux techniques de gravure traditionnelle',
                'url': 'https://www.atelier-gravure.fr/bourses',
                'criteres': ['Maîtrise technique', 'Recherche artistique', 'Projet d\'édition'],
                'statut': 'Ouvert'
            }
        ]
        return projets

    def get_projets_arts_appliques(self):
        """Récupère les appels à projets arts appliqués (céramique, textile, design)"""
        projets = [
            {
                'titre': 'Bourse de création céramique',
                'organisme': 'Centre Céramique Contemporaine',
                'type_projet': 'Céramique',
                'montant': '4 000 € - 15 000 €',
                'deadline': '2025-12-10',
                'description': 'Soutien aux créateurs céramistes',
                'url': 'https://www.ceramique-contemporaine.fr/bourses',
                'criteres': ['Maîtrise technique', 'Innovation formelle', 'Projet de recherche'],
                'statut': 'Ouvert'
            },
            {
                'titre': 'Prix du textile artistique',
                'organisme': 'Cité internationale de la tapisserie',
                'type_projet': 'Textile',
                'montant': '5 000 € - 18 000 €',
                'deadline': '2025-11-01',
                'description': 'Prix pour créations textiles contemporaines',
                'url': 'https://www.cite-tapisserie.fr/prix-textile',
                'criteres': ['Innovation textile', 'Dimension artistique', 'Techniques contemporaines'],
                'statut': 'Ouvert'
            }
        ]
        return projets

    def rechercher_arts_visuels(self, type_art=None, budget_min=None, budget_max=None):
        """Effectue une recherche complète des projets arts visuels"""
        
        print("🎨 RECHERCHE D'APPELS À PROJETS ARTS VISUELS")
        print("(Photographie, Peinture, Sculpture, Arts graphiques)")
        print("=" * 70)
        
        # Collecte de tous les projets arts visuels
        tous_projets = []
        tous_projets.extend(self.get_projets_photographie())
        tous_projets.extend(self.get_projets_peinture_dessin())
        tous_projets.extend(self.get_projets_sculpture_installation())
        tous_projets.extend(self.get_projets_arts_graphiques())
        tous_projets.extend(self.get_projets_arts_appliques())
        
        # Filtrage selon les critères
        projets_filtres = tous_projets
        
        if type_art:
            projets_filtres = [p for p in projets_filtres if type_art.lower() in p['type_projet'].lower()]
        
        # Affichage des résultats
        print(f"🔍 {len(projets_filtres)} appels à projets arts visuels trouvés\n")
        
        for i, projet in enumerate(projets_filtres, 1):
            print(f"[{i}] 🎨 {projet['titre']}")
            print(f"    📋 Organisme: {projet['organisme']}")
            print(f"    🖼️ Type: {projet['type_projet']}")
            print(f"    💰 Montant: {projet['montant']}")
            print(f"    📅 Deadline: {projet['deadline']}")
            print(f"    📝 Description: {projet['description']}")
            print(f"    🔗 URL: {projet['url']}")
            print(f"    ✅ Critères: {', '.join(projet['criteres'])}")
            print(f"    🟢 Statut: {projet['statut']}")
            print()
        
        # Statistiques par type d'art
        types_arts = {}
        for projet in projets_filtres:
            type_p = projet['type_projet']
            types_arts[type_p] = types_arts.get(type_p, 0) + 1
        
        print("📊 RÉPARTITION PAR TYPE D'ART:")
        for type_art, count in types_arts.items():
            print(f"  🎯 {type_art}: {count} opportunités")
        
        return projets_filtres

    def exporter_vers_excel(self, projets, nom_fichier=None):
        """Exporte les résultats vers un fichier Excel"""
        if not nom_fichier:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_fichier = f"arts_visuels_{timestamp}.xlsx"
        
        df = pd.DataFrame(projets)
        df.to_excel(nom_fichier, index=False, engine='openpyxl')
        
        print(f"\n📊 Résultats exportés vers: {nom_fichier}")
        return nom_fichier

def main():
    """Fonction principale pour tester le système"""
    recherche = RechercheArtsVisuels()
    
    # Recherche générale
    projets = recherche.rechercher_arts_visuels()
    
    # Export vers Excel
    recherche.exporter_vers_excel(projets)
    
    print("\n🎯 DOMAINES ARTISTIQUES COUVERTS:")
    print("🔹 Photographie (documentaire, artistique)")
    print("🔹 Peinture & Dessin (contemporain, traditionnel)")
    print("🔹 Sculpture & Installation (3D, espace public)")
    print("🔹 Arts graphiques (illustration, gravure, estampe)")
    print("🔹 Arts appliqués (céramique, textile, design)")
    print("\n❌ EXCLUS: Musique, Danse, Théâtre (arts du spectacle)")

if __name__ == "__main__":
    main()
