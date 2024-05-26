from rich.markdown import Markdown
from rich.console import Console

C = Console()


def fmt_sources_list(sources: list[dict]):
    '''
      Takes in a list of sources and outputs it
    '''
    for index, source in enumerate(sources):
        C.print(f"[yellow] {index + 1}. {source.get('name')}")


def fmt_source_details(source: dict):
    '''
      Takes in a source and outputs it in a nice
      Markdown format
    '''
    C.print(Markdown(
        f"""
## {source.get('name')}

{source.get('description')}

- Country: {source.get('country')}
- Category: {source.get('category')}
- Language: {source.get('language')}
- URL: {source.get('url')}
    """
    ))
