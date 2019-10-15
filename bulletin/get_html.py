import requests

def get_html_page(url, page = None):
    print('start parsing')
    auto_url = url
    params = {
            "p": page
        }
    try:
        result = requests.get(auto_url, params=params)
        result.raise_for_status()
        return result.text

    except(requests.RequestException, ValueError):
        print('Network error')
        return False