import requests
import fake_useragent

def get_html_page(url, page = None):
    user_agent = fake_useragent.UserAgent()
    user = user_agent.random
    headers = {'user-Agent': str(user)}
    print('start parsing')
    auto_url = url
    params = {
            "p": page
        }
    try:
        result = requests.get(auto_url, headers=headers, params=params)
        result.raise_for_status()
        return result.text

    except(requests.RequestException, ValueError):
        print('Network error')
        return False