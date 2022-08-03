#!/usr/bin/python3
"""BaseModel class"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """The BaseModel class will be inherited by other classes"""
    def __init__(self, *rgs, **kwargs):
        """__init__ method and instatianting the BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        for name, value in kwargs.items():
            """searches through dict for keys"""
            if name == "__class__"
                continue
            setattr(self, name, value)
        if "id" not in kwargs:
            models.storage.new(self)

    def __setattr__(self, name, value)
        """ Maintain correct types for non-string attributes while keeping
        the attributes as public attributes.

        Args:
            name (str) name of attribute
            value: value to associate with `name`

        Raises:
            AttributeError: If value cannot be parsed into correct format
        """
        if name in ['created_at', 'updated_at']:
            if isinstance(value, str):
                try:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                except ValueError:
                    raise AttributeError("Invalid value: ({}) for name: ({})"
                            .format(value, name))
        super().__setattr__(name, value)


