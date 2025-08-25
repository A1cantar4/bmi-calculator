from flask import Blueprint, render_template, request
from flask_babel import _
from .utils import calculate_bmi, bmi_category

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            height = float(request.form["height"])
            weight = float(request.form["weight"])
            bmi = calculate_bmi(weight, height)
            category = bmi_category(bmi)
            return render_template(
                "result.html",
                bmi=round(bmi, 2),
                category=category
            )
        except ValueError:
            return render_template("index.html", error=_("Entrada inválida"))
    return render_template("index.html")