from typing import Dict, List, Any
from datetime import datetime
from .request import Request

class Shlink:
    _api_key: str = None
    _url: str = None

    def __init__(self, api_key: str, url: str) -> None:
        self._api_key = api_key
        self._url = url.rstrip("/")

    def _get(self, path: str, headers: Dict[str, str] = None, params: Dict[str, str] = None):
        return Request.get(url=self._url, api_key=self._api_key, path=path, headers=headers, params=params)

    def _post(self, path: str, data: Dict = None, headers: Dict = None):
        return Request.post(url=self._url, api_key=self._api_key, path=path, data=data, headers=headers)

    def list_short_urls(self, params: Dict[str, str] = None):
        """
        List all of the short URLs
        :return:
        """
        return self._get("/rest/v3/short-urls", params=params)

    def get_short_url(self, short_code: str = None, long_url: str = None):
        """
        Get the the URL using short_code or create the short code using long_url.
        long_url has to start with http:// or https://
        """
        if long_url is None:
            return self._get(f"/rest/v3/short-urls/{short_code}")
        else:
            return self._post(f"/rest/v3/short-urls",
                              { "customSlug": short_code,
                                "longUrl": long_url,
                                "findIfExists": True })
            

    def list_visit_data(self, short_code: str):
        """
        List all of the visit data
        :return:
        """
        return self._get(f"/rest/v3/short-urls/{short_code}/visits")