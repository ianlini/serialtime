import gzip

from six.moves import cPickle
from bistiming import SimpleTimer


def save_pklgz(obj, filename, **timer_kwargs):
    with SimpleTimer("Pickling to %s" % (filename), **timer_kwargs):
        pkl = cPickle.dumps(obj, protocol=cPickle.HIGHEST_PROTOCOL)
        with gzip.open(filename, "wb") as fp:
            fp.write(pkl)


def load_pklgz(filename, **timer_kwargs):
    with gzip.open(filename, 'rb') as fp, \
            SimpleTimer("Unpickling from %s" % (filename), **timer_kwargs):
        obj = cPickle.load(fp)
    return obj


def save_pkl(obj, filename, **timer_kwargs):
    with open(filename, "wb") as fp, \
            SimpleTimer("Pickling to %s" % (filename), **timer_kwargs):
        cPickle.dump(obj, fp, protocol=cPickle.HIGHEST_PROTOCOL)


def load_pkl(filename, **timer_kwargs):
    with open(filename, "rb") as fp, \
            SimpleTimer("Unpickling from %s" % (filename), **timer_kwargs):
        obj = cPickle.load(fp)
    return obj


def save_joblib_pkl(obj, filename, **timer_kwargs):
    try:
        from sklearn.externals import joblib
    except ImportError:
        raise ImportError("This function requires sklearn module. "
                          "You can install it via "
                          "\"pip install scikit-learn\".")
    with SimpleTimer("Pickling to %s" % (filename), **timer_kwargs):
        joblib.dump(obj, filename)


def load_joblib_pkl(filename, **timer_kwargs):
    try:
        from sklearn.externals import joblib
    except ImportError:
        raise ImportError("This function requires sklearn module. "
                          "You can install it via "
                          "\"pip install scikit-learn\".")
    with SimpleTimer("Unpickling from %s" % (filename), **timer_kwargs):
        obj = joblib.load(filename)
    return obj
