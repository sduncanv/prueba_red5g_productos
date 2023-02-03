from flask import Flask, request
from config.database import Database
from forms.forms import Product, CreateProduct, UpdateProduct, Pay_product
from werkzeug.datastructures import ImmutableMultiDict
from services.services_products import Services

app = Flask(__name__)

@app.route('/product/create', methods=['POST'])
def create():
    try:
        form = CreateProduct(ImmutableMultiDict(request.json))

        if request.method == 'POST' and form.validate():
            db = Database()
            res = Services(db).create_product(request.json)
            return res

        else:
            return form.errors

    except Exception as e:
        return {'Error': str(e)}


@app.route('/product/read', methods=['GET'])
def read():
    try:
        form = Product(ImmutableMultiDict(request.json))

        if request.method == 'GET' and form.validate():
            db = Database()
            res = Services(db).read_product(request.json)
            return res

    except Exception as e:
        return {'Error': str(e)}


@app.route('/product/update', methods=['PUT'])
def update():
    try:
        form = UpdateProduct(ImmutableMultiDict(request.json))

        if request.method == 'PUT' and form.validate():
            db = Database()
            res = Services(db).update_product(request.json)
            print(form.validate())
            return res

        else:
            return form.errors

    except Exception as e:
        return {'Error': str(e)}


@app.route('/product/delete', methods=['DELETE'])
def delete():
    try:
        form = Product(ImmutableMultiDict(request.json))

        if request.method == 'DELETE' and form.validate():
            db = Database()
            res = Services(db).delete_product(request.json)
            return res
        
        else:
            return form.errors

    except Exception as e:
        return {'Error': str(e)}


@app.route('/product/pay', methods=['PUT'])
def pay_product():
    try:
        form = Pay_product(ImmutableMultiDict(request.json))

        if request.method == 'PUT' and form.validate():
            db = Database()
            res = Services(db).pay_product(request.json)
            return res
        
        else:
            return form.errors

    except Exception as e:
        return {'Error': str(e)}


if __name__ == '__main__':
    app.run(
        debug = True
    )