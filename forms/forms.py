from wtforms import Form, validators
from wtforms.fields import StringField, IntegerField

class Product(Form):
    name = StringField(validators=[
        validators.data_required(message='El nombre del producto es obligatorio'),
        validators.length(min=2, max=150, message='Escribe un nombre adecuado para el producto')
    ])


class CreateProduct(Product):
    val = IntegerField(validators=[
        validators.data_required(message='El valor del producto es obligatorio')
    ])
    cant = IntegerField(validators=[
        validators.data_required(message='Ingresa una cantidad inicial')
    ])


class UpdateProduct(Product):
    u_name = StringField(validators=[
        validators.data_required(message='El nombre del producto a actualizar es obligatorio')
    ])
    u_cant = IntegerField(validators=[
        validators.data_required(message='Ingresa una cantidad a actualizar')
    ])


class Pay_product(Product):
    pay_cant = IntegerField(validators=[
        validators.data_required(message='Ingresa una cantidad a comprar')
    ])