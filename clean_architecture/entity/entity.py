import abc
from enum import Enum
from datetime import datetime
from dataclasses import dataclass, asdict


@dataclass()
class Entity:

    def to_dict(self):
        return asdict(self)

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
