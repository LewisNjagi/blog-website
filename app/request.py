import urllib.request,json
from .models import Quote

base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTES_API_BASE_URL']

def get_quotes():
    '''
    Function that gets quotes
    '''
    get_quoutes_url = base_url

    with urllib.request.urlopen(get_quoutes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None

        if get_quotes_response:
            quotes_results_list = get_quotes_response
            quotes_results = process_results(quotes_results_list)

    return quotes_results

def process_results(quotes_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain quotes source details

    Returns :
        source_results: A list of news source objects
    '''
    quotes_results = []
    for quote_item in quotes_list:
        id = quote_item.get('id')
        author = quote_item.get('author')
        quote = quote_item.get('quote')

        if author:
            quote_object = Quote(id,author,quote)
            quotes_results.append(quote_object)
            
    return quotes_results