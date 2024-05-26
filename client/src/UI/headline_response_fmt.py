from rich.markdown import Markdown
from rich.console import Console
from datetime import datetime


C = Console(force_terminal=True)


def fmt_headline_response(articles: list[dict]):
    '''
      Formats the response from the server and prints it.
    '''
    C.clear()
    for index, article in enumerate(articles):
        # construct Markdown, and then print
        C.print(Markdown(
            "\n" + f'''
#### {index + 1}. {article['title']}           
- Source name: {article['source']['name']}. 
- Written By: {article['author']}
          ''' + "\n" + ">---------------------------------------------------------------------<" + "\n"
        ))


def fmt_headline_details(article: dict):
    '''
      Takes in a article headline, and then prints out
      the details
    '''

    # parse the article publish date
    C.clear()
    try:
        datetime_obj = datetime.strptime(
            article.get('publishedAt'), "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        datetime_obj = datetime.fromtimestamp(0)

    # Extract date and time
    date = datetime_obj.date()
    time = datetime_obj.time()

    C.print(Markdown(
        f'''
## {article['title'] if article['title'] or article['title'] != '[Removed]' else "No title available"}
        
description: {article['description'] if article['description'] or article['description'] != '[Removed]' else "No description available"}
 
- url : {article['url'] if article['url'] else "Unavailable"}
- Date of publish: {date.strftime("%d/%m/%Y")}
- time of publish: {time.strftime("%H:%M")}
- Source name: {article['source']['name'] if article['source']['name'] else "unknown"}
- Written By: {article['author'] if article['author'] else "unknown"}
        '''
    ))
