""" utils.py """
import logging
from functools import wraps

logger = logging.getLogger(__name__)

def log_negative_id(func):
    """ log negative id """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        """ wrapper """
        pk = self.kwargs.get("pk")
        if pk is not None and int(pk) < 0:
            logger.warning("Se solicitó nave con ID negativo: %s", pk)
        return func(self, *args, **kwargs)
    return wrapper
