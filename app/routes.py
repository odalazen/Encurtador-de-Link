from flask import (
    Blueprint,
    request,
    redirect,
    render_template
)

from app.services import (
    create_short_url,
    get_url_by_code,
    increment_clicks
)

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")


@main.route("/shorten", methods = ["POST"])
def shorten_url():

    original_url = request.form.get("url")

    if not original_url:
        return render_template(
            "index.html",
            error="Digite uma URL"
        )
    
    short_url = create_short_url(original_url)

    if not short_url:
        return render_template(
            "index.html",
            error="URL inválida."
        )

    return render_template(
        "index.html",
        short_url = short_url
    )

@main.route("/<short_code>")
def redirect_url(short_code):

    url = get_url_by_code(short_code)

    if not url:
        return "URL não encontrada"
    
    increment_clicks(url)

    return redirect(url.original_url)
    