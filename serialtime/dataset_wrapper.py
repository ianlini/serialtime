from copy import deepcopy

import numpy as np


class PartialPreprocessedDataset(object):
    def __init__(self, dataset, idx, shape, preprocess_func=None):
        self._dataset = dataset
        self._idx = deepcopy(idx)
        self.shape = (len(idx),) + shape
        self._preprocess_func = preprocess_func

    def _get_single_item(self, key):
        raw_data = self._dataset[self._idx[key]]
        if self._preprocess_func is None:
            data = raw_data
        else:
            data = self._preprocess_func(raw_data)
        if data.shape != self.shape[1:]:
            raise ValueError("wrong data shape, expect {} but get {}"
                             .format(self.shape[1:], data.shape))
        return data

    def __getitem__(self, key):
        if hasattr(key, "__iter__"):
            return np.asarray([self._get_single_item(k) for k in key],
                              dtype=self._dataset.dtype)
        else:
            return self._get_single_item(key)

    def __len__(self):
        return self.shape[0]
