SerialTime
==========
SerialTime is a Python serialization tool containing many serialization and deserialization shortcuts with timing. There are many modules that can serialize Python object such as:

- `Joblib <https://pythonhosted.org/joblib/>`_
- `PyYAML <http://pyyaml.org/>`_
- `Python built-in pickle/cPickle <https://docs.python.org/3/library/pickle.html>`_
- `Python built-in json <https://docs.python.org/3/library/json.html>`_
- `Python built-in pickle/cPickle + gzip <https://docs.python.org/3/library/gzip.html>`_

However, remembering their API is very difficult, and there are many differences in their API.
For example, ``json.dump`` only accept file-like object as its argument, so we need to open the file first, and then give the function the file-like object, while ``joblib.dump`` only accept file path as its argument.
Besides, there is no compression shortcut for Python built-in pickle/cPickle, so we also need to remember how to use something like gzip.

This package aims to solve these problems and provides very simple and unified API shortcuts for some popular serialization methods.
In addition, we use `BisTiming <https://github.com/ianlini/bistiming>`_ to calculate the execution time, so you can also easily know how quick the serialization is.


Installation
------------
- Install ``serialtime``

  .. code:: bash

     pip install serialtime

- If you want to use ``save_joblib_pkl`` or ``load_joblib_pkl``:

  .. code:: bash

     pip install scikit-learn scipy

- If you want to use ``try_load_yaml``:

  .. code:: bash

     pip install PyYAML


Documentation
-------------

Shortcuts
+++++++++
- Python built-in pickle/cPickle

  .. code:: python

     serialtime.save_pkl(obj, path, log_description=None, logger=None,
                         logging_level=logging.INFO, verbose_start=True,
                         verbose_end=True, end_in_new_line=True, log_prefix="...")

  .. code:: python

     obj = serialtime.load_pkl(path, log_description=None, logger=None,
                               logging_level=logging.INFO, verbose_start=True,
                               verbose_end=True, end_in_new_line=True, log_prefix="...")

- Python built-in pickle/cPickle + gzip

  .. code:: python

     serialtime.save_pklgz(obj, path, log_description=None, logger=None,
                           logging_level=logging.INFO, verbose_start=True,
                           verbose_end=True, end_in_new_line=True, log_prefix="...")

  .. code:: python

     obj = serialtime.load_pklgz(path, log_description=None, logger=None,
                                 logging_level=logging.INFO, verbose_start=True,
                                 verbose_end=True, end_in_new_line=True, log_prefix="...")

- Joblib

  .. code:: python

     serialtime.save_joblib_pkl(obj, path, log_description=None, logger=None,
                                logging_level=logging.INFO, verbose_start=True,
                                verbose_end=True, end_in_new_line=True, log_prefix="...")

  .. code:: python

     obj = serialtime.load_joblib_pkl(path, log_description=None, logger=None,
                                      logging_level=logging.INFO, verbose_start=True,
                                      verbose_end=True, end_in_new_line=True, log_prefix="...")

Interactive trying of loading YAML
++++++++++++++++++++++++++++++++++
Sometimes we want to load the configuration file in the middle of a program.
If we run the program very long and the file format is incorrect, the program may directly raise an error and exit, so we don't have any chance to fix the file.
``serialtime.try_load_yaml`` can try to load the file, and pause when it encounter any error, and ask you whether to reload the file.
We can then fix the file and continue running the program.

.. code:: python

   serialtime.try_load_yaml(yaml_path)

Dataset wrapper
+++++++++++++++
``PartialPreprocessedDataset`` is used to transparrently reindex the data without moving or copying the original memory.

Sometimes we want to reindex the data, for example:

.. code:: python

   In [1]: import numpy as np

   In [2]: dset = np.asarray([1, 2, 3])

   In [3]: dset
   Out[3]: array([1, 2, 3])

   In [4]: idx = [2, 0]

   In [5]: dset2 = dset[idx]

   In [6]: dset2
   Out[6]: array([3, 1])

However, if the data is very large or it's on disk, this may use too much memory.
We may not need all the convenient API in ``numpy.ndarray`` or ``h5py.dataset``, but some modules only accept a full ``numpy.ndarray`` or ``h5py.dataset`` (i.e., ``keras.image.ImageDataGenerator.flow()``).
Our solution is to use an object to remember the new index, and translate the index while getting the value. For example:

.. code:: python

   In [1]: import numpy as np

   In [2]: from serialtime import PartialPreprocessedDataset

   In [3]: dset = np.asarray([[0, 1], [2, 3], [4, 5]])

   In [4]: dset
   Out[4]:
   array([[0, 1],
          [2, 3],
          [4, 5]])

   In [5]: idx = [2, 0]

   In [6]: dset2 = PartialPreprocessedDataset(dset, idx, shape=(2,), preprocess_func=lambda x: x*2)

We can also use an optional ``preprocess_func`` to preprocess the instance while we are getting it.
In this example, we just double the values in the array.
The ``shape`` we give to ``PartialPreprocessedDataset`` is the shape of one instance (the shape of the array that we can get after ``preprocess_func(dset[x]))``. Then we can do something like:

.. code:: python

   In [7]: dset2.shape
   Out[7]: (2, 2)

   In [8]: len(dset2)
   Out[8]: 2

   In [9]: dset2[0]
   Out[9]: array([ 8, 10])

   In [10]: dset2[1]
   Out[10]: array([0, 2])

   In [11]: dset2[2]
   IndexError: list index out of range

Testing
-------
- For the current environment: ``python setup test``.
- For Python 2.7, 3.4, 3.5, 3.6 and installation test: ``tox``.
