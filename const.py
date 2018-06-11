NEWS_API_URL = 'https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={api_key}'
NEWS_FORMAT = """
Title: \n{title}
----------------------
Body:\n
{body}

Source:\n
{source}

"""
