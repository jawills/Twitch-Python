from typing import Dict, Any

from twitch.api import API
from .model import Model


class Clip(Model):

    def __init__(self, api: API, data: Dict[str, Any]):
        super().__init__(api, data)

        self.broadcaster_id: str = data.get('broadcaster_id')
        self.broadcaster_name: str = data.get('broadcaster_name')
        self.created_at: str = data.get('created_at')
        self.creator_id: str = data.get('creator_id')
        self.creator_name: str = data.get('creator_name')
        self.embed_url: str = data.get('embed_url')
        self.game_id: str = data.get('game_id')
        self.id: str = data.get('id')
        self.language: str = data.get('language')
        self.pagination: str = data.get('pagination')
        self.thumbnail_url: str = data.get('thumbnail_url')
        self.title: str = data.get('title')
        self.url: str = data.get('url')
        self.video_id: str = data.get('video_id')
        self.view_count: str = data.get('view_count')

        def __str__(self):
            return self.broadcaster_name
