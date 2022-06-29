import re
import unicodedata


def slugify(text):
    """Fonction de slugification naïve pour le test."""
    text = text.lower()
    # On enlève les espaces
    text = re.sub(r'\s+', '-', text)
    # On enlève les caractères accentués
    text = (
        unicodedata.normalize('NFD', text)
        .encode('ascii', 'ignore')
        .decode("utf-8")
    )
    # On enlève les caractères non alpha-numériques
    text = re.sub(r'[^a-zA-Z0-9-]', '-', text)
    # On normalise le nombre de tirets
    text = re.sub(r'-+', '-', text)
    return text
