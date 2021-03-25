from typing import Optional, List

from twitch.api import API
from twitch.helix.resources.resource import T
from .resource import Resource


class Clips(Resource['helix.Clip']):

    def __init__(self, api: API, **kwargs: Optional):
        super().__init__(api=api, path='clips')
        self._kwargs = kwargs
        print(kwargs)
        if len(kwargs) > 0:
            self._data = [helix.Clip(api=self._api, data=clip) for clip in
                          self._api.get(self._path, params=kwargs)['data']]

    def _can_paginate(self) -> bool:
        return False

    def _handle_pagination_response(self, response: dict) -> List[T]:
        pass
