import requests
from django.conf import settings


class EldenRingAPI:
    """Cliente para consumir a API do Elden Ring"""

    BASE_URL = "https://eldenring.fanapis.com/api"

    # Dados mock para quando a API estiver indisponível
    MOCK_DATA = {
        "characters": [
            {
                "id": "atlan",
                "name": "Atlan",
                "race": "Human",
                "gender": "Male",
                "description": "A legendary warrior known for his mastery of the blade. Atlan was one of the first Tarnished to challenge the Erdtree.",
                "quote": "The Erdtree... it calls to us all.",
                "location": "Limgrave",
                "role": "Warrior"
            },
            {
                "id": "melina",
                "name": "Melina",
                "race": "Human",
                "gender": "Female",
                "description": "A mysterious maiden who offers guidance to Tarnished. She serves as a spectral steed and provides crucial information about the Lands Between.",
                "quote": "I am Melina. I offer you an accord.",
                "location": "Various",
                "role": "Guide"
            },
            {
                "id": "godrick",
                "name": "Godrick the Grafted",
                "race": "Human",
                "gender": "Male",
                "description": "The self-proclaimed Lord of Stormveil Castle. Known for grafting limbs from other beings onto himself in a desperate attempt to gain power.",
                "quote": "I am the Lord of all that is Golden!",
                "location": "Stormveil Castle",
                "role": "Demigod"
            },
            {
                "id": "rennala",
                "name": "Rennala, Queen of the Full Moon",
                "race": "Human",
                "gender": "Female",
                "description": "The queen of the Academy of Raya Lucaria. A powerful sorceress who has lost herself in her studies, endlessly repeating the same incantations.",
                "quote": "O mother... mother, mother, mother...",
                "location": "Raya Lucaria Academy",
                "role": "Sorceress"
            },
            {
                "id": "margit",
                "name": "Margit the Fell Omen",
                "race": "Omen",
                "gender": "Male",
                "description": "A formidable warrior guarding the entrance to Stormveil Castle. Known for his agility and powerful hammer strikes.",
                "quote": "Thou'rt Tarnished, it seems. Allow me to welcome thee to the lands between.",
                "location": "Stormveil Castle",
                "role": "Guardian"
            }
        ],
        "weapons": [
            {
                "id": "moonlight_greatsword",
                "name": "Moonlight Greatsword",
                "type": "Greatsword",
                "description": "A legendary greatsword said to have been wielded by a Carian knight. Its blade glows with the power of the moon.",
                "weight": 17.0,
                "attack": {"physical": 138, "magic": 0, "fire": 0, "lightning": 0, "holy": 0}
            },
            {
                "id": "bloody_helix",
                "name": "Bloody Helix",
                "type": "Curved Sword",
                "description": "A cursed sword that drains the life force of its victims. Its blade is stained with the blood of countless warriors.",
                "weight": 5.5,
                "attack": {"physical": 94, "magic": 0, "fire": 0, "lightning": 0, "holy": 0}
            }
        ],
        "bosses": [
            {
                "id": "margit",
                "name": "Margit the Fell Omen",
                "location": "Stormveil Castle",
                "description": "The first major boss encounter in Elden Ring. A skilled fighter who tests the mettle of aspiring Tarnished.",
                "health": 4200,
                "drops": ["Talisman Pouch", "Margit's Shackle"]
            },
            {
                "id": "godrick",
                "name": "Godrick the Grafted",
                "location": "Stormveil Castle",
                "description": "The lord of Stormveil Castle, defeated by countless challengers but always reborn through grafting.",
                "health": 6080,
                "drops": ["Godrick's Great Rune", "Godrick's Remembrance"]
            }
        ]
    }

    @classmethod
    def search_characters(cls, name=None):
        """Buscar personagens por nome"""
        try:
            if name:
                url = f"{cls.BASE_URL}/characters"
                params = {"name": name}
                response = requests.get(url, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()
                return data.get("data", [])
            else:
                # Retornar todos os personagens mock se não especificar nome
                return cls.MOCK_DATA["characters"]
        except (requests.RequestException, ValueError, KeyError):
            # Fallback para dados mock
            if name:
                # Filtrar dados mock por nome
                filtered = [char for char in cls.MOCK_DATA["characters"]
                          if name.lower() in char["name"].lower()]
                return filtered
            return cls.MOCK_DATA["characters"]

    @classmethod
    def get_character_by_id(cls, character_id):
        """Buscar personagem específico por ID"""
        try:
            url = f"{cls.BASE_URL}/characters/{character_id}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, ValueError):
            # Fallback para dados mock
            for char in cls.MOCK_DATA["characters"]:
                if char["id"] == character_id:
                    return {"data": char}
            return None

    @classmethod
    def get_weapons(cls):
        """Buscar armas"""
        try:
            url = f"{cls.BASE_URL}/weapons"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("data", [])
        except (requests.RequestException, ValueError, KeyError):
            return cls.MOCK_DATA["weapons"]

    @classmethod
    def get_bosses(cls):
        """Buscar chefes"""
        try:
            url = f"{cls.BASE_URL}/bosses"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("data", [])
        except (requests.RequestException, ValueError, KeyError):
            return cls.MOCK_DATA["bosses"]