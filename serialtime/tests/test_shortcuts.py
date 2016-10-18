import os
from tempfile import NamedTemporaryFile

from serialtime import (
    load_pkl,
    save_pkl,
    load_pklgz,
    save_pklgz,
    load_joblib_pkl,
    save_joblib_pkl,
)


def test_pkl():
    obj = [1, 2, 3]
    with NamedTemporaryFile(suffix=".pkl", delete=False) as fp:
        path = fp.name
    save_pkl(obj, path, verbose_start=False, verbose_end=False)
    obj2 = load_pkl(path, verbose_start=False, verbose_end=False)
    os.remove(path)

    assert obj == obj2

def test_pklgz():
    obj = [1, 2, 3]
    with NamedTemporaryFile(suffix=".pkl.gz", delete=False) as fp:
        path = fp.name
    save_pklgz(obj, path, verbose_start=False, verbose_end=False)
    obj2 = load_pklgz(path, verbose_start=False, verbose_end=False)
    os.remove(path)

    assert obj == obj2

def test_joblib_pkl():
    obj = [1, 2, 3]
    with NamedTemporaryFile(suffix=".pkl.gz", delete=False) as fp:
        path = fp.name
    save_joblib_pkl(obj, path, verbose_start=False, verbose_end=False)
    obj2 = load_joblib_pkl(path, verbose_start=False, verbose_end=False)
    os.remove(path)

    assert obj == obj2
