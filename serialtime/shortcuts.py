import gzip

from six.moves import cPickle
from bistiming import SimpleTimer


def save_pklgz(obj, path, **timer_kwargs):
    with SimpleTimer("Pickling to %s" % (path), **timer_kwargs):
        pkl = cPickle.dumps(obj, protocol=cPickle.HIGHEST_PROTOCOL)
        with gzip.open(path, "wb") as fp:
            fp.write(pkl)


def load_pklgz(path, **timer_kwargs):
    with gzip.open(path, 'rb') as fp, \
            SimpleTimer("Unpickling from %s" % (path), **timer_kwargs):
        obj = cPickle.load(fp)
    return obj


def save_pkl(obj, path, **timer_kwargs):
    with open(path, "wb") as fp, \
            SimpleTimer("Pickling to %s" % (path), **timer_kwargs):
        cPickle.dump(obj, fp, protocol=cPickle.HIGHEST_PROTOCOL)


def load_pkl(path, **timer_kwargs):
    with open(path, "rb") as fp, \
            SimpleTimer("Unpickling from %s" % (path), **timer_kwargs):
        obj = cPickle.load(fp)
    return obj


def save_joblib_pkl(obj, path, **timer_kwargs):
    try:
        from sklearn.externals import joblib
    except ImportError:
        raise ImportError("This function requires sklearn module. "
                          "You can install it via "
                          "\"pip install scikit-learn\".")
    with SimpleTimer("Pickling to %s" % (path), **timer_kwargs):
        joblib.dump(obj, path)


def load_joblib_pkl(path, **timer_kwargs):
    try:
        from sklearn.externals import joblib
    except ImportError:
        raise ImportError("This function requires sklearn module. "
                          "You can install it via "
                          "\"pip install scikit-learn\".")
    with SimpleTimer("Unpickling from %s" % (path), **timer_kwargs):
        obj = joblib.load(path)
    return obj
