import requests
from flask import Flask, render_template

app = Flask(__name__)


def fetch_data(url):
    """
    Fetch data from an API endpoint.

    Args:
        url (str): The URL of the API endpoint.

    Returns:
        list: A list of fetched data.
    """
    fetch = 1
    data = []
    while fetch == 1:
        res = requests.get(url).json()
        data.append(res['data']['data'][0])
        if res['data']['next_page_url']:
            url = res['data']['next_page_url']
        else:
            fetch = 0
    return data


def identify_citations(data):
    """
    Identify citations from the fetched data.

    Args:
        data (list): Fetched data from the API.

    Returns:
        list: A list of identified citations.
    """
    citations = []
    for dt in data:
        response = str(dt['response']).replace(" ", "")
        for d in dt['source']:
            context = str(d['context']).replace(" ", "")
            if response in context:
                citation = d
                del citation['context']
                citations.append(citation)
    return citations


@app.route('/')
def index():
    """
    Render the index page with citations.

    Returns:
        str: Rendered HTML template with citations.
    """
    url = 'https://devapi.beyondchats.com/api/get_message_with_sources'
    data = fetch_data(url)
    if not data:
        print("No data fetched from the API.")
    citations = identify_citations(data)
    return render_template('index.html', citations=citations)


if __name__ == '__main__':
    app.run(debug=True)
