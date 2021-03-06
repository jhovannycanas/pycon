import os
import pickle
import logging

from django.db import models
from django.conf import settings


logger = logging.getLogger(__name__)


class Result(models.Model):

    petal_width = models.DecimalField(max_digits=3, decimal_places=2)
    petal_length = models.DecimalField(max_digits=3, decimal_places=2)
    classification = models.CharField(max_length=25, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return f'{self.petal_width} - {self.petal_length} - {self.classification}'


class IrisModelConfig(object):

    CLASSIFICATION = {
        0: 'SETOSA',
        1: 'VERSICOLOR',
        2: 'VIRGINICA'
    }

    MODEL_PKL = 'iris_predictor.pkl'  # Expected name of the model, consider using a env variable


class IrisModel(object):
    """Return the model as singleton"""
    _instance = None

    def __init__(self):
        if self._instance is not None:
            raise ValueError('The model was already loaded')

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            try:
                model_path = os.path.join(settings.BASE_DIR, 'data', IrisModelConfig.MODEL_PKL)
                with open(model_path, 'rb') as model:
                    cls._instance = pickle.load(model)
            except IOError as e:
                logger.exception('Serialized model was not found')
            except pickle.UnpicklingError as e:
                logger.exception('Error while loading the model')

        return cls._instance
