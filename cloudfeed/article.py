from dataclasses import dataclass
from datetime import datetime


@dataclass
class Article:
    title: str
    link: str
    description: str
    creation_date: datetime = datetime.now()
