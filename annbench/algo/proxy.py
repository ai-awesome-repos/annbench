from .annoy import AnnoyANN
from .ivfpq import IvfpqANN
from .hnsw import HnswANN
from .linear import LinearANN

def instantiate_algorithm(name):
    """
    Instantiate an algorithm class
    Args:
        name: the name of the target algorithm

    Returns:
        an instance of the specified algorithm class
    """

    if name == "annoy":
        return AnnoyANN()
    elif name == "ivfpq":
        return IvfpqANN()
    elif name == "hnsw":
        return HnswANN()
    elif name == "linear":
        return LinearANN()
    else:
        return None



