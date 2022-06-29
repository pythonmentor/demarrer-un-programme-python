from .utils.text import slugify


def main():
    """Point d'entrée principal du programme."""
    print(
        slugify(
            "L'idéal avec les titres qui contiennent des caractères accentués est de les slugifier"
        )
    )
