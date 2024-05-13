from ..server_logging import server_logger
import requests
import os


def GetHeadlines(keywords = [], country="", category="") -> dict:
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

    a = "&".join(url_payload) if len(url_payload) > 0 else ""
    print(a)

    try:
        url = f'https://newsapi.org/v2/top-headlines?{a}' if a != "" else f'https://newsapi.org/v2/everything?country=us'
        print(url)
        data = requests.get(url, headers={
            'Accept': 'application/json',
            'X-Api-Key': os.getenv('API_KEY')
        })
        mdata = data.json()
        if mdata.get('status') != 'ok':
            print(data.status_code)
            raise Exception("NewsAPIException", mdata.get(
                'code'), mdata.get('message'))
        return mdata['articles'][0:16]  # limit to 15 results
    except Exception as e:
        server_logger.error("error fetching headlines")
        print(e)
