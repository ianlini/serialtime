from serialtime import PartialPreprocessedDataset
import numpy as np
from nose.tools import assert_raises


def get_partial_dset():
    dset = np.asarray([1, 2, 3])
    idx = [2, 0]
    return dset, idx, PartialPreprocessedDataset(dset, idx, shape=())


def test_partial_dataset_get_single_key():
    dset, idx, partial_dset = get_partial_dset()
    for i, idx_i in enumerate(idx):
        assert partial_dset[i] == dset[idx_i]
    with assert_raises(IndexError):
        _ = partial_dset[len(idx)]


def test_index_error():
    _, idx, partial_dset = get_partial_dset()
    with assert_raises(IndexError):
        _ = partial_dset[len(idx)]


def test_partial_dataset_get_list_of_keys():
    dset, idx, partial_dset = get_partial_dset()
    list_of_keys = [0, 1, 0, 0]
    for value, key in zip(partial_dset[list_of_keys], list_of_keys):
        assert value == dset[idx[key]]


def test_shape():
    _, idx, partial_dset = get_partial_dset()
    assert partial_dset.shape == (len(idx),)
    assert len(partial_dset) == len(idx)

