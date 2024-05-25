from rich.markdown import Markdown
from rich.console import Console
from datetime import datetime

C = Console(force_terminal=True)


def fmt_headline_response(articles: list[dict]):
    '''
      Formats the response from the server and prints it.
    '''

    for index, article in enumerate(articles):
        # construct Markdown, and then print
        C.print(Markdown(
            f"""
            ### {index + 1}. {article['title']}
            Source name: {article['source']['name']}. 
            Written By: {article['author']}
          """ + '\n'
        ))


def fmt_headline_details(article: dict):
    '''
      Takes in a article headline, and then prints out
      the details
    '''

    # parse the article publish date
    datetime_obj = datetime.strptime(
        article.get('publishedAt'), "%Y-%m-%dT%H:%M:%SZ")

    # Extract date and time
    date = datetime_obj.date()
    time = datetime_obj.time()

    C.print(Markdown(
        f"""
        ## {article['title']}
        
        description: {article['description'] if article['description'] else "No description available"}
        
        url : {article['url']}
        Date of publish: {date.strftime("%d/%m/%Y")}
        time of publish: {time.strftime("%H:%M")}
        Source name: {article['source']['name']}.
        Written By: {article['author']}
        """
    ))
