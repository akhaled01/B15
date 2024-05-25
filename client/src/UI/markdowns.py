from rich.markdown import Markdown

main_menu = Markdown("""
## Welcome to News API

This is a simple command line interface for searching news headlines and sources.

1. Search Headlines
2. Search Sources
3. Quit       
              """)

headlines_menu = Markdown("""
1. Search for keywords
2. Search by category
3. Search by country
4. List all news headlines
5. Back to the main menu
""")

sources_menu = Markdown("""
1. Search by category
2. Search by country
3. Search by language
4. List all sources
5. Back to the main menu
""")

country_menu = Markdown("""
#### Available Countries

1. Australia (AU)
2. New Zealand (NZ)
3. Canada (CA)
4. UAE (AE)
5. South Africa (ZA)
6. United Kingdom (GB)
7. United States (US)
8. Morroco (MA)
""")


language_menu = Markdown("""
#### Supported Languages

1. English
2. Arabic
""")

category_menu = Markdown("""
#### Supported categories
                         
1. Business
2. Entertainment
3. general
4. Health
5. Science
6. Sports
7. Technology
""")
