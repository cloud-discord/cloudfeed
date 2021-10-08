import asyncio
from dataclasses import dataclass
from datetime import datetime
import logging

from cloudfeed import config

logger = logging.getLogger(__name__)


@dataclass
class Article:
    title: str
    link: str
    description: str
    creation_date: datetime = datetime.now()


class ArticleQueue:
    def __init__(self) -> None:
        self.queue: asyncio.Queue = asyncio.Queue(
            maxsize=int(config.QUEUE_MAXSIZE))
        self.lock: asyncio.Lock = asyncio.Lock()

    async def queue_size(self) -> int:
        async with self.lock:
            return self.article_queue.qsize()

    async def enqueue(self, article: Article) -> None:
        async with self.lock:
            self.queue.put(article)
