from ..utils.server_logging import server_logger
import requests
import traceback
import os


def GetHeadlines(keywords: list[str], country: str, category: str) -> dict:
    """Fetch headlines by keywords.

      Parameters:
      keywords (list[str]): Keywords to search for.
      country (str): Country to search for.
      category (str): Category to search for.

      Returns:
      dict: List of articles (15 to for evaluation purposes).

      Raises:
      NewsAPIException: If the "status" value of the response is "error" rather than "ok".
    """
    url_payload = []

    # construct the url payload
    if keywords and len(keywords) > 0:
        url_payload.append(f'q={"&".join(keywords)}')
    if country and country != "":
        url_payload.append(f"country={country}")
    if category and category != "":
        url_payload.append(f"category={category}")

    parsed_string_payload = "&".join(
        url_payload) if len(url_payload) > 0 else ""

    try:
        url = f'https://newsapi.org/v2/top-headlines?{parsed_string_payload}' if parsed_string_payload != "" else f'https://newsapi.org/v2/everything?q=apple'
        data = requests.get(url, headers={
            'Accept': 'application/json',
            'X-Api-Key': os.getenv('API_KEY')
        })

        main_data = data.json()

        if main_data.get('status') != 'ok':
            print(data.status_code)
            raise Exception("NewsAPIException", main_data.get(
                'code'), main_data.get('message'))

        return main_data['articles'][0:15]  # limit to 15 results

    except Exception:
        server_logger.error("error fetching headlines")
        server_logger.error(traceback.format_exc(chain=True))
