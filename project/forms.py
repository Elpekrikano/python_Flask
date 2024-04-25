from wtforms import Form
from wtforms import StringField, TextAreaField
from wtforms.fields import EmailField

from wtforms import validators
class CommentForm(Form):
    username = StringField('Username', [
        validators.input_required(message='El username es requerido.'),
        validators.Length(min=4, max=25, message='Ingrese un nombre de usuario válido.')
    ])

    email = EmailField('Correo electrónico',[
        validators.DataRequired(message='el correo es requerido'),
        validators.Email(message='Ingrese un email válido.')
    ])
    comment = TextAreaField('Comentario')
