import pkg_resources

from .shortcuts import (
    load_pkl,
    save_pkl,
    load_pklgz,
    save_pklgz,
    load_joblib_pkl,
    save_joblib_pkl,
)
from .interactive_trying import try_load_yaml
from .dataset_wrapper import PartialPreprocessedDataset


__all__ = ['shortcuts', 'interactive_trying', 'dataset_wrapper']
__version__ = pkg_resources.get_distribution("serialtime").version
