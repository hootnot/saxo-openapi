# -*- encoding: utf-8 -*-
"""Handle referencedata endpoints."""
from ..apirequest import APIRequest
from abc import abstractmethod


class ReferenceData(APIRequest):
    """Reference - class to handle the referencedata endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    def __init__(self, **kwargs):
        """Instantiate a ReferenceData APIRequest instance.

        Parameters
        ----------
        all parameters that get passed by the derived class __init__
        """
        endpoint = self.ENDPOINT.format(**kwargs)
        super(ReferenceData, self).__init__(endpoint, method=self.METHOD)
