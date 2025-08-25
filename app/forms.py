from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from flask_babel import _

class BMIForm(FlaskForm):
    height = FloatField(
        label=_("Altura (m):"),
        validators=[DataRequired(message=_("Campo obrigatório")), NumberRange(min=0.5, max=2.5)]
    )
    weight = FloatField(
        label=_("Peso (kg):"),
        validators=[DataRequired(message=_("Campo obrigatório")), NumberRange(min=2, max=500)]
    )
    submit = SubmitField(_("Calcular"))