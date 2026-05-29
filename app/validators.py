import validators

def normalize_url(url):

    url = url.strip()

    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"

    return url
    
def is_valid_url(url):
    return validators.url(url)