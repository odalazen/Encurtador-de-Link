import random
import string

from app.database import db
from app.models import URL

from app.validators import (
    normalize_url,
    is_valid_url
)

def generate_short_code(length = 6):
    characters = string.ascii_letters + string.digits

    return ''.join(
        random.choice(characters)
        for _ in range(length)
    )

def create_unique_code():

    while True:
        
        short_code = generate_short_code()

        existing_url = URL.query.filter_by(
            short_code = short_code
        ).first()

        if not existing_url:
            return short_code


def create_short_url(original_url):

    original_url = normalize_url(original_url)

    if not is_valid_url(original_url):
        return None

    short_code = create_unique_code()

    new_url = URL(
        original_url = original_url,
        short_code = short_code
    )

    db.session.add(new_url)

    db.session.commit()

    return new_url

def get_url_by_code(short_code):
    
    return URL.query.filter_by(
        short_code = short_code
    ).first()

def increment_clicks(url):

    url.clicks += 1

    db.session.commit()