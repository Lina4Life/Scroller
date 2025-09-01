"""
Colombian Visual Arts Funding API
Comprehensive database of Colombian arts, culture, and creative funding opportunities
"""

import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ColombianVisualArtsFunding:
    """Colombian Visual Arts and Cultural Funding Database"""
    
    def __init__(self):
        self.funding_database = self._initialize_colombian_arts_database()
        logger.info("Colombian Visual Arts Funding API initialized")
    
    def _calculate_days_until(self, deadline_str: str) -> int:
        """Calculate days until deadline"""
        try:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
            today = datetime.now()
            delta = deadline - today
            return max(0, delta.days)
        except:
            return 999
    
    def _initialize_colombian_arts_database(self) -> List[Dict]:
        """Initialize comprehensive Colombian arts funding database"""
        
        # Colombian regions and cities
        colombian_locations = [
            "Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena", 
            "Bucaramanga", "Pereira", "Santa Marta", "Manizales", "Pasto",
            "Armenia", "Villavicencio", "Neiva", "Soledad", "Soacha"
        ]
        
        # Colombian art types
        art_types = [
            "Pintura", "Escultura", "Fotografía", "Arte Digital", "Instalación",
            "Performance", "Video Arte", "Arte Conceptual", "Grabado", "Dibujo",
            "Arte Urbano", "Cerámica", "Textiles", "Joyería", "Arte Sonoro"
        ]
        
        funding_opportunities = [
            # Ministry of Culture - National Programs
            {
                'title': 'Programa Nacional de Estímulos - Artes Visuales 2025',
                'description': 'Convocatoria nacional del Ministerio de Cultura para apoyar la creación, investigación y circulación en artes visuales. Incluye categorías de creación individual, proyectos de investigación curatorial, y residencias artísticas.',
                'organisme': 'Ministerio de Cultura de Colombia',
                'montant': 'COP 25,000,000 - COP 80,000,000',
                'montant_min': 25000000,
                'montant_max': 80000000,
                'currency': 'COP',
                'deadline': '2025-09-30',
                'days_until_deadline': self._calculate_days_until('2025-09-30'),
                'url': 'https://www.mincultura.gov.co/areas/artes/estimulos/Paginas/default.aspx',
                'country': 'Colombia',
                'city': 'Nacional',
                'type_projet': 'Beca de Creación',
                'statut': 'Activo',
                'contact_email': 'estimulos@mincultura.gov.co',
                'contact_tel': '+57 1 342 4100',
                'contact_adresse': 'Carrera 8 No. 8-43, Bogotá, Colombia',
                'date_ouverture': '2025-07-01',
                'date_cloture': '2025-09-30',
                'eligibilite': ['Artistas colombianos mayores de 18 años', 'Extranjeros residentes en Colombia por más de 5 años'],
                'documents_requis': ['Hoja de vida artística', 'Propuesta de proyecto', 'Portafolio digital', 'Presupuesto detallado'],
                'duree_projet': '12 meses',
                'modalites_versement': 'Tres desembolsos: 40% inicial, 40% intermedio, 20% final',
                'co_financing': 'No requerido',
                'additional_support': 'Acompañamiento curatorial y mentoría'
            },
            
            # IDARTES Bogotá
            {
                'title': 'Becas de Creación IDARTES - Artes Visuales',
                'description': 'Programa del Instituto Distrital de las Artes de Bogotá para apoyar procesos de creación en artes visuales con énfasis en arte contemporáneo, arte digital y nuevos medios.',
                'organisme': 'IDARTES - Instituto Distrital de las Artes',
                'montant': 'COP 30,000,000 - COP 60,000,000',
                'montant_min': 30000000,
                'montant_max': 60000000,
                'currency': 'COP',
                'deadline': '2025-10-15',
                'days_until_deadline': self._calculate_days_until('2025-10-15'),
                'url': 'https://www.idartes.gov.co/becas-estimulos',
                'country': 'Colombia',
                'city': 'Bogotá',
                'type_projet': 'Beca Distrital',
                'statut': 'Activo',
                'contact_email': 'becas@idartes.gov.co',
                'contact_tel': '+57 1 379 5750',
                'contact_adresse': 'Carrera 8 No. 15-46, Bogotá',
                'eligibilite': ['Residentes en Bogotá por mínimo 2 años', 'Artistas emergentes y consolidados'],
                'art_focus': ['Arte Contemporáneo', 'Arte Digital', 'Instalación', 'Performance']
            },
            
            # Medellín Cultural Programs
            {
                'title': 'Programa de Estímulos Culturales - Medellín Artes Visuales',
                'description': 'Convocatoria de la Secretaría de Cultura Ciudadana de Medellín para fortalecer el sector de artes visuales con énfasis en arte urbano, fotografía documental y arte comunitario.',
                'organisme': 'Secretaría de Cultura Ciudadana - Medellín',
                'montant': 'COP 20,000,000 - COP 45,000,000',
                'montant_min': 20000000,
                'montant_max': 45000000,
                'currency': 'COP',
                'deadline': '2025-08-20',
                'days_until_deadline': self._calculate_days_until('2025-08-20'),
                'url': 'https://www.medellin.gov.co/irj/portal/medellin?NavigationTarget=navurl://cultura',
                'country': 'Colombia',
                'city': 'Medellín',
                'type_projet': 'Estímulo Municipal',
                'statut': 'Activo',
                'contact_email': 'cultura@medellin.gov.co',
                'contact_tel': '+57 4 385 5555',
                'art_focus': ['Arte Urbano', 'Fotografía Documental', 'Arte Comunitario']
            },
            
            # Cali Cultural Institute
            {
                'title': 'Becas de Arte y Creatividad - Valle del Cauca',
                'description': 'Programa del Instituto Municipal de Cultura y Turismo de Cali para el fomento de las artes visuales con enfoque en diversidad cultural y patrimonio afrodescendiente.',
                'organisme': 'Instituto Municipal de Cultura y Turismo - Cali',
                'montant': 'COP 18,000,000 - COP 40,000,000',
                'montant_min': 18000000,
                'montant_max': 40000000,
                'currency': 'COP',
                'deadline': '2025-11-10',
                'days_until_deadline': self._calculate_days_until('2025-11-10'),
                'url': 'https://www.cali.gov.co/cultura/',
                'country': 'Colombia',
                'city': 'Cali',
                'type_projet': 'Beca Cultural',
                'statut': 'Activo',
                'contact_email': 'cultura@cali.gov.co',
                'contact_tel': '+57 2 660 3218',
                'art_focus': ['Arte Afrodescendiente', 'Patrimonio Cultural', 'Arte Contemporáneo']
            },
            
            # Cartagena Arts Foundation
            {
                'title': 'Residencias Artísticas Cartagena - Arte Caribe',
                'description': 'Programa de residencias artísticas en Cartagena enfocado en el intercambio cultural caribeño, arte colonial contemporáneo y nuevas narrativas urbanas.',
                'organisme': 'Fundación Festival Internacional de Música de Cartagena',
                'montant': 'COP 35,000,000 - COP 70,000,000',
                'montant_min': 35000000,
                'montant_max': 70000000,
                'currency': 'COP',
                'deadline': '2025-09-05',
                'days_until_deadline': self._calculate_days_until('2025-09-05'),
                'url': 'https://www.festivaldemusica.org/residencias-artisticas',
                'country': 'Colombia',
                'city': 'Cartagena',
                'type_projet': 'Residencia Artística',
                'statut': 'Activo',
                'contact_email': 'residencias@festivaldemusica.org',
                'contact_tel': '+57 5 660 0537',
                'art_focus': ['Arte Caribeño', 'Arte Colonial Contemporáneo', 'Narrativas Urbanas']
            },
            
            # Private Foundation - Banco de la República
            {
                'title': 'Programa de Arte Joven - Banco de la República',
                'description': 'Convocatoria anual del Banco de la República para apoyar artistas jóvenes menores de 35 años en todas las disciplinas visuales con énfasis en investigación y experimentación.',
                'organisme': 'Banco de la República - Área Cultural',
                'montant': 'COP 40,000,000 - COP 90,000,000',
                'montant_min': 40000000,
                'montant_max': 90000000,
                'currency': 'COP',
                'deadline': '2025-12-01',
                'days_until_deadline': self._calculate_days_until('2025-12-01'),
                'url': 'https://www.banrepcultural.org/convocatorias',
                'country': 'Colombia',
                'city': 'Nacional',
                'type_projet': 'Beca de Investigación',
                'statut': 'Activo',
                'contact_email': 'convocatorias@banrep.gov.co',
                'contact_tel': '+57 1 343 1212',
                'eligibilite': ['Artistas menores de 35 años', 'Proyectos de investigación en artes visuales'],
                'art_focus': ['Investigación Artística', 'Arte Experimental', 'Nuevos Medios']
            },
            
            # Barranquilla Cultural Programs
            {
                'title': 'Becas Distritales de Arte - Barranquilla Caribe',
                'description': 'Programa distrital de Barranquilla para el fomento de las artes visuales con enfoque en cultura caribeña, carnaval contemporáneo y arte popular.',
                'organisme': 'Secretaría de Cultura y Patrimonio - Barranquilla',
                'montant': 'COP 22,000,000 - COP 50,000,000',
                'montant_min': 22000000,
                'montant_max': 50000000,
                'currency': 'COP',
                'deadline': '2025-10-20',
                'days_until_deadline': self._calculate_days_until('2025-10-20'),
                'url': 'https://www.barranquilla.gov.co/cultura',
                'country': 'Colombia',
                'city': 'Barranquilla',
                'type_projet': 'Beca Distrital',
                'statut': 'Activo',
                'contact_email': 'cultura@barranquilla.gov.co',
                'contact_tel': '+57 5 339 9999',
                'art_focus': ['Arte Caribeño', 'Carnaval Contemporáneo', 'Arte Popular']
            },
            
            # International Cooperation
            {
                'title': 'Programa de Cooperación Artística Colombia-España',
                'description': 'Convocatoria bilateral para intercambio artístico entre Colombia y España, residencias, exposiciones y proyectos curatoriales conjuntos.',
                'organisme': 'Embajada de España en Colombia - AECID',
                'montant': 'EUR 15,000 - EUR 35,000',
                'montant_min': 15000,
                'montant_max': 35000,
                'currency': 'EUR',
                'deadline': '2025-11-25',
                'days_until_deadline': self._calculate_days_until('2025-11-25'),
                'url': 'https://www.aecid.es/ES/Paginas/Inicio.aspx',
                'country': 'Colombia',
                'city': 'Nacional',
                'type_projet': 'Cooperación Internacional',
                'statut': 'Activo',
                'contact_email': 'cultura.bogota@aecid.es',
                'contact_tel': '+57 1 629 2800',
                'art_focus': ['Intercambio Cultural', 'Arte Contemporáneo', 'Curaduría']
            },
            
            # Regional Programs - Coffee Region
            {
                'title': 'Becas de Arte y Patrimonio - Eje Cafetero',
                'description': 'Programa conjunto de Pereira, Armenia y Manizales para promover el arte visual relacionado con el patrimonio cultural cafetero y paisaje cultural.',
                'organisme': 'Corporación Cultural del Eje Cafetero',
                'montant': 'COP 28,000,000 - COP 55,000,000',
                'montant_min': 28000000,
                'montant_max': 55000000,
                'currency': 'COP',
                'deadline': '2025-09-12',
                'days_until_deadline': self._calculate_days_until('2025-09-12'),
                'url': 'https://www.ejcafetero.gov.co/cultura',
                'country': 'Colombia',
                'city': 'Eje Cafetero',
                'type_projet': 'Beca Regional',
                'statut': 'Activo',
                'contact_email': 'cultura@ejcafetero.gov.co',
                'contact_tel': '+57 6 315 8000',
                'art_focus': ['Patrimonio Cafetero', 'Paisaje Cultural', 'Arte Rural']
            },
            
            # Private Foundation - Fundación Gilberto Alzate
            {
                'title': 'Programa de Arte Digital y Nuevos Medios',
                'description': 'Convocatoria especializada en arte digital, realidad virtual, arte interactivo y nuevas tecnologías aplicadas al arte contemporáneo colombiano.',
                'organisme': 'Fundación Gilberto Alzate Avendaño',
                'montant': 'COP 45,000,000 - COP 85,000,000',
                'montant_min': 45000000,
                'montant_max': 85000000,
                'currency': 'COP',
                'deadline': '2025-08-15',
                'days_until_deadline': self._calculate_days_until('2025-08-15'),
                'url': 'https://fgaa.gov.co/convocatorias',
                'country': 'Colombia',
                'city': 'Bogotá',
                'type_projet': 'Beca Especializada',
                'statut': 'Activo',
                'contact_email': 'convocatorias@fgaa.gov.co',
                'contact_tel': '+57 1 282 9491',
                'art_focus': ['Arte Digital', 'Realidad Virtual', 'Arte Interactivo', 'Nuevas Tecnologías']
            },
            
            # University Programs
            {
                'title': 'Becas de Investigación-Creación - Universidad Nacional',
                'description': 'Programa de la Universidad Nacional de Colombia para proyectos de investigación-creación en artes visuales con componente académico y experimental.',
                'organisme': 'Universidad Nacional de Colombia - Facultad de Artes',
                'montant': 'COP 35,000,000 - COP 70,000,000',
                'montant_min': 35000000,
                'montant_max': 70000000,
                'currency': 'COP',
                'deadline': '2025-10-05',
                'days_until_deadline': self._calculate_days_until('2025-10-05'),
                'url': 'https://artes.unal.edu.co/convocatorias',
                'country': 'Colombia',
                'city': 'Bogotá',
                'type_projet': 'Beca Universitaria',
                'statut': 'Activo',
                'contact_email': 'convocatorias_fartes@unal.edu.co',
                'contact_tel': '+57 1 316 5000',
                'art_focus': ['Investigación-Creación', 'Arte Experimental', 'Arte Académico']
            },
            
            # Youth Programs
            {
                'title': 'Programa Joven Crea - Arte Visual Juvenil',
                'description': 'Convocatoria nacional para artistas jóvenes entre 18 y 28 años enfocada en arte urbano, grafiti legal, muralismo y expresiones juveniles contemporáneas.',
                'organisme': 'Instituto Nacional de la Juventud - INJUV',
                'montant': 'COP 15,000,000 - COP 35,000,000',
                'montant_min': 15000000,
                'montant_max': 35000000,
                'currency': 'COP',
                'deadline': '2025-08-30',
                'days_until_deadline': self._calculate_days_until('2025-08-30'),
                'url': 'https://www.injuv.gov.co/convocatorias',
                'country': 'Colombia',
                'city': 'Nacional',
                'type_projet': 'Beca Juvenil',
                'statut': 'Activo',
                'contact_email': 'joven.crea@injuv.gov.co',
                'contact_tel': '+57 1 312 7000',
                'eligibilite': ['Jóvenes entre 18 y 28 años', 'Proyectos de arte urbano y contemporáneo'],
                'art_focus': ['Arte Urbano', 'Grafiti Legal', 'Muralismo', 'Arte Juvenil']
            },
            
            # Indigenous and Afro-Colombian Art
            {
                'title': 'Becas de Arte Étnico y Diversidad Cultural',
                'description': 'Programa especial para promover el arte visual de comunidades indígenas, afrocolombianas, raizales y ROM con enfoque en preservación e innovación cultural.',
                'organisme': 'Ministerio del Interior - Dirección de Asuntos Étnicos',
                'montant': 'COP 30,000,000 - COP 65,000,000',
                'montant_min': 30000000,
                'montant_max': 65000000,
                'currency': 'COP',
                'deadline': '2025-11-15',
                'days_until_deadline': self._calculate_days_until('2025-11-15'),
                'url': 'https://www.mininterior.gov.co/grupos-etnicos',
                'country': 'Colombia',
                'city': 'Nacional',
                'type_projet': 'Beca Étnica',
                'statut': 'Activo',
                'contact_email': 'etnicos@mininterior.gov.co',
                'contact_tel': '+57 1 444 3600',
                'art_focus': ['Arte Indígena', 'Arte Afrocolombiano', 'Arte Raizal', 'Diversidad Cultural']
            },
            
            # Environmental Art
            {
                'title': 'Arte y Medio Ambiente - Colombia Verde',
                'description': 'Convocatoria para proyectos de arte visual que aborden temáticas ambientales, sostenibilidad, cambio climático y biodiversidad colombiana.',
                'organisme': 'Ministerio de Ambiente y Desarrollo Sostenible',
                'montant': 'COP 25,000,000 - COP 60,000,000',
                'montant_min': 25000000,
                'montant_max': 60000000,
                'currency': 'COP',
                'deadline': '2025-12-10',
                'days_until_deadline': self._calculate_days_until('2025-12-10'),
                'url': 'https://www.minambiente.gov.co/cultura-ambiental',
                'country': 'Colombia',
                'city': 'Nacional',
                'type_projet': 'Beca Ambiental',
                'statut': 'Activo',
                'contact_email': 'cultura.ambiental@minambiente.gov.co',
                'contact_tel': '+57 1 332 3400',
                'art_focus': ['Arte Ambiental', 'Sostenibilidad', 'Biodiversidad', 'Cambio Climático']
            },
            
            # Women in Arts
            {
                'title': 'Programa Mujeres Creadoras - Arte Visual Femenino',
                'description': 'Convocatoria exclusiva para mujeres artistas visuales con enfoque en equidad de género, liderazgo femenino y narrativas de la mujer en el arte contemporáneo.',
                'organisme': 'Consejería Presidencial para la Equidad de la Mujer',
                'montant': 'COP 20,000,000 - COP 50,000,000',
                'montant_min': 20000000,
                'montant_max': 50000000,
                'currency': 'COP',
                'deadline': '2025-09-25',
                'days_until_deadline': self._calculate_days_until('2025-09-25'),
                'url': 'https://www.equidadmujer.gov.co/convocatorias',
                'country': 'Colombia',
                'city': 'Nacional',
                'type_projet': 'Beca de Género',
                'statut': 'Activo',
                'contact_email': 'mujeres.creadoras@presidencia.gov.co',
                'contact_tel': '+57 1 562 9300',
                'eligibilite': ['Exclusivo para mujeres artistas', 'Mayores de 18 años'],
                'art_focus': ['Arte Femenino', 'Equidad de Género', 'Narrativas de Mujer']
            }
        ]
        
        # Add calculated urgency for each opportunity
        for opportunity in funding_opportunities:
            days_until = opportunity['days_until_deadline']
            if days_until <= 7:
                opportunity['urgency'] = 'very_high'
            elif days_until <= 30:
                opportunity['urgency'] = 'high'
            elif days_until <= 90:
                opportunity['urgency'] = 'medium'
            else:
                opportunity['urgency'] = 'low'
        
        return funding_opportunities
    
    def search_colombian_visual_arts_funding(self, 
                                           city: Optional[str] = None,
                                           art_type: Optional[str] = None,
                                           min_amount: Optional[int] = None,
                                           max_amount: Optional[int] = None) -> List[Dict]:
        """
        Search Colombian visual arts funding opportunities with filters
        
        Args:
            city: Filter by Colombian city (e.g., 'bogota', 'medellin', 'cali')
            art_type: Filter by art type (e.g., 'pintura', 'arte_digital', 'fotografia')
            min_amount: Minimum funding amount in COP
            max_amount: Maximum funding amount in COP
        
        Returns:
            List of matching funding opportunities
        """
        results = self.funding_database.copy()
        
        # Filter by city
        if city and city.lower() != 'all':
            city_normalized = city.lower().replace('_', ' ')
            city_map = {
                'bogota': 'bogotá',
                'medellin': 'medellín',
                'nacional': 'nacional',
                'all_cities': 'nacional'
            }
            
            target_city = city_map.get(city_normalized, city_normalized)
            
            results = [
                opportunity for opportunity in results
                if target_city.lower() in opportunity.get('city', '').lower() or
                   opportunity.get('city', '').lower() == 'nacional'
            ]
        
        # Filter by art type/focus
        if art_type and art_type.lower() != 'all':
            art_keywords = {
                'pintura': ['pintura', 'painting'],
                'escultura': ['escultura', 'sculpture'],
                'fotografia': ['fotografía', 'fotografia', 'photography'],
                'arte_digital': ['arte digital', 'digital', 'nuevos medios', 'nuevas tecnologías'],
                'arte_urbano': ['arte urbano', 'grafiti', 'muralismo'],
                'performance': ['performance', 'arte conceptual'],
                'instalacion': ['instalación', 'installation'],
                'arte_contemporaneo': ['contemporáneo', 'contemporary'],
                'arte_tradicional': ['patrimonio', 'tradicional', 'étnico', 'cultural'],
                'arte_ambiental': ['ambiental', 'sostenibilidad', 'biodiversidad']
            }
            
            keywords = art_keywords.get(art_type.lower(), [art_type])
            
            results = [
                opportunity for opportunity in results
                if any(keyword.lower() in str(opportunity.get('art_focus', [])).lower() or
                      keyword.lower() in opportunity.get('description', '').lower() or
                      keyword.lower() in opportunity.get('title', '').lower()
                      for keyword in keywords)
            ]
        
        # Filter by funding amount (convert EUR to COP if needed)
        if min_amount is not None or max_amount is not None:
            filtered_results = []
            for opportunity in results:
                amount_min = opportunity.get('montant_min', 0)
                amount_max = opportunity.get('montant_max', 0)
                currency = opportunity.get('currency', 'COP')
                
                # Convert EUR to COP (approximate rate)
                if currency == 'EUR':
                    amount_min = amount_min * 4500  # 1 EUR ≈ 4500 COP
                    amount_max = amount_max * 4500
                
                # Check if opportunity meets amount criteria
                meets_criteria = True
                if min_amount is not None and amount_max < min_amount:
                    meets_criteria = False
                if max_amount is not None and amount_min > max_amount:
                    meets_criteria = False
                
                if meets_criteria:
                    filtered_results.append(opportunity)
            
            results = filtered_results
        
        # Sort by urgency (most urgent first) and then by funding amount (highest first)
        urgency_order = {'very_high': 0, 'high': 1, 'medium': 2, 'low': 3}
        
        results.sort(key=lambda x: (
            urgency_order.get(x.get('urgency', 'low'), 3),
            -x.get('montant_max', 0)
        ))
        
        logger.info(f"Found {len(results)} Colombian visual arts funding opportunities")
        return results
    
    def get_funding_statistics(self) -> Dict:
        """Get statistics about Colombian visual arts funding"""
        total_opportunities = len(self.funding_database)
        
        # Calculate total funding available
        total_funding_cop = sum(opp.get('montant_max', 0) for opp in self.funding_database if opp.get('currency') == 'COP')
        total_funding_eur = sum(opp.get('montant_max', 0) for opp in self.funding_database if opp.get('currency') == 'EUR')
        
        # Convert EUR to COP for total
        total_funding_cop += total_funding_eur * 4500
        
        # Urgency breakdown
        urgency_counts = {'very_high': 0, 'high': 0, 'medium': 0, 'low': 0}
        for opp in self.funding_database:
            urgency = opp.get('urgency', 'low')
            urgency_counts[urgency] += 1
        
        # City distribution
        city_counts = {}
        for opp in self.funding_database:
            city = opp.get('city', 'Unknown')
            city_counts[city] = city_counts.get(city, 0) + 1
        
        return {
            'total_opportunities': total_opportunities,
            'total_funding_cop': total_funding_cop,
            'average_funding_cop': total_funding_cop / total_opportunities if total_opportunities > 0 else 0,
            'urgency_breakdown': urgency_counts,
            'city_distribution': city_counts,
            'currencies_supported': ['COP', 'EUR']
        }

# Example usage and testing
if __name__ == "__main__":
    # Initialize the API
    colombian_arts = ColombianVisualArtsFunding()
    
    # Test searches
    print("=== All Colombian Visual Arts Opportunities ===")
    all_opportunities = colombian_arts.search_colombian_visual_arts_funding()
    print(f"Found {len(all_opportunities)} total opportunities")
    
    print("\n=== Bogotá Opportunities ===")
    bogota_opportunities = colombian_arts.search_colombian_visual_arts_funding(city="bogota")
    print(f"Found {len(bogota_opportunities)} opportunities in Bogotá")
    
    print("\n=== Digital Art Opportunities ===")
    digital_opportunities = colombian_arts.search_colombian_visual_arts_funding(art_type="arte_digital")
    print(f"Found {len(digital_opportunities)} digital art opportunities")
    
    print("\n=== High Funding Opportunities (>50M COP) ===")
    high_funding = colombian_arts.search_colombian_visual_arts_funding(min_amount=50000000)
    print(f"Found {len(high_funding)} high-funding opportunities")
    
    print("\n=== Funding Statistics ===")
    stats = colombian_arts.get_funding_statistics()
    print(f"Total funding available: {stats['total_funding_cop']:,} COP")
    print(f"Average funding: {stats['average_funding_cop']:,.0f} COP")
    print(f"Urgency breakdown: {stats['urgency_breakdown']}")
