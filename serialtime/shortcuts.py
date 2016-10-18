import gzip
import logging

from six.moves import cPickle
from bistiming import SimpleTimer


def save_pklgz(obj, path, log_description=None, logger=None,
               logging_level=logging.INFO, verbose_start=True,
               verbose_end=True, end_in_new_line=True, log_prefix="..."):
    if log_description is None:
        log_description = "Pickling to " + (path)
    with SimpleTimer(log_description, logger, logging_level, verbose_start,
                     verbose_end, end_in_new_line, log_prefix):
        pkl = cPickle.dumps(obj, protocol=cPickle.HIGHEST_PROTOCOL)
        with gzip.open(path, "wb") as fp:
            fp.write(pkl)


def load_pklgz(path, log_description=None, logger=None,
               logging_level=logging.INFO, verbose_start=True,
               verbose_end=True, end_in_new_line=True, log_prefix="..."):
    if log_description is None:
        log_description = "Unpickling from " + path
    with gzip.open(path, 'rb') as fp, \
            SimpleTimer(log_description, logger, logging_level, verbose_start,
                        verbose_end, end_in_new_line, log_prefix):
        obj = cPickle.load(fp)
    return obj


def save_pkl(obj, path, log_description=None, logger=None,
             logging_level=logging.INFO, verbose_start=True,
             verbose_end=True, end_in_new_line=True, log_prefix="..."):
    if log_description is None:
        log_description = "Pickling to " + (path)
    with open(path, "wb") as fp, \
            SimpleTimer(log_description, logger, logging_level, verbose_start,
                        verbose_end, end_in_new_line, log_prefix):
        cPickle.dump(obj, fp, protocol=cPickle.HIGHEST_PROTOCOL)


def load_pkl(path, log_description=None, logger=None,
             logging_level=logging.INFO, verbose_start=True,
             verbose_end=True, end_in_new_line=True, log_prefix="..."):
    if log_description is None:
        log_description = "Unpickling from " + path
    with open(path, "rb") as fp, \
            SimpleTimer(log_description, logger, logging_level, verbose_start,
                        verbose_end, end_in_new_line, log_prefix):
        obj = cPickle.load(fp)
    return obj


def save_joblib_pkl(obj, path, log_description=None, logger=None,
                    logging_level=logging.INFO, verbose_start=True,
                    verbose_end=True, end_in_new_line=True, log_prefix="..."):
    try:
        from sklearn.externals import joblib
    except ImportError:
        raise ImportError("This function requires sklearn module. "
                          "You can install it via "
                          "\"pip install scikit-learn\".")
    if log_description is None:
        log_description = "Pickling to " + (path)
    with SimpleTimer(log_description, logger, logging_level, verbose_start,
                     verbose_end, end_in_new_line, log_prefix):
        joblib.dump(obj, path)


def load_joblib_pkl(path, log_description=None, logger=None,
                    logging_level=logging.INFO, verbose_start=True,
                    verbose_end=True, end_in_new_line=True, log_prefix="..."):
    try:
        from sklearn.externals import joblib
    except ImportError:
        raise ImportError("This function requires sklearn module. "
                          "You can install it via "
                          "\"pip install scikit-learn\".")
    if log_description is None:
        log_description = "Unpickling from " + path
    with SimpleTimer(log_description, logger, logging_level, verbose_start,
                     verbose_end, end_in_new_line, log_prefix):
        obj = joblib.load(path)
    return obj
