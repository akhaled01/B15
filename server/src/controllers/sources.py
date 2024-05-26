from ..utils.server_logging import server_logger
import requests
import os


def GetSources(country: str, category: str, lang: str) -> dict:
    """Fetch sources by country.

      Parameters:
      country (str): Country to search for.
      category (str): Category to search for.
      lang (str): Language to search for.

      Returns:
      dict: List of sources.

      Raises:
      NewsAPIException: If the "status" value of the response is "error" rather than "ok".
    """
    url_payload = []

    if country and country != "":
        url_payload.append(f"country={country}")
    if category and category != "":
        url_payload.append(f"category={category}")
    if lang and lang != "":
        url_payload.append(f"language={lang}")

    parsed_url_queries = "&".join(url_payload) if len(url_payload) > 0 else ""

    try:
        url = f'https://newsapi.org/v2/top-headlines/sources?{parsed_url_queries}' if parsed_url_queries != "" else f'https://newsapi.org/v2/top-headlines/sources'
        main_data = requests.get(url, headers={
            'Accept': 'application/json',
            'X-Api-Key': os.getenv('API_KEY')
        }).json()

        if main_data.get('status') != 'ok':
            raise Exception("NewsAPIException", main_data.get(
                'code'), main_data.get('message'))

        return main_data['sources'][0:15]

    except Exception as e:
        server_logger.error("error fetching sources")
        server_logger.print_exception(e)
