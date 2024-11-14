try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

# Importer votre widget principal
from ._widget import StainSeparationWidget

# Si vous avez un reader, vous pouvez l'importer ici si nécessaire
# from ._reader import napari_get_reader

# Si vous avez des données d'exemple
# from ._sample_data import make_sample_data

# Si vous avez un writer
# from ._writer import write_single_image, write_multiple

__all__ = (
    # "napari_get_reader",
    # "write_single_image",
    # "write_multiple",
    # "make_sample_data",
    "StainSeparationWidget",
)

# Fournir le widget pour Napari
def napari_experimental_provide_dock_widget():
    return StainSeparationWidget
