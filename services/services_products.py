from models.models import Product

def get_product(db, data):
    result = db.session.query(Product).filter(Product.name == data['name']).first()
    return result


class Services():
    def __init__(self, db) -> None:
        self.db = db

    def create_product(self, data):
        result = get_product(self.db, data)

        if not result:
            product = Product(
                name = data['name'],
                val = data['val'],
                cant = data['cant']
            )
            self.db.session.add(product)
            self.db.session.commit()
            self.db.session.close()

            return {'message': 'Producto creado', 'status_code': 201}

        else:
            return {'message': 'Producto ya existente', 'status_code': 404}


    def read_product(self, data):
        result = get_product(self.db, data)

        if result:
            return {'message': {
                'name': result.name,
                'val': result.val,
                'cant': result.cant,
            }, 'status_code': 201}

        else:
            return {'message': 'Producto no encontrado', 'status_code': 404}


    def update_product(self, data):
        result = get_product(self.db, data)

        if result:
            print(f'-- {result}')
            result.name = data['u_name']
            result.cant = data['u_cant']
            self.db.session.add(result)
            self.db.session.commit()
            self.db.session.close()

            return {'message': 'Producto actualizado', 'status_code': 201}

        else:
            return {'message': 'Producto no existente', 'status_code': 404}
    

    def delete_product(self, data):
        result = get_product(self.db, data)

        if result:
            self.db.session.delete(result)
            self.db.session.commit()
            self.db.session.close()

            return {'message': 'Producto eliminado', 'status_code': 201}

        else:
            return {'message': 'Producto no existente', 'status_code': 404}


    def pay_product(self, data):
        result = get_product(self.db, data)

        if result:
            if result.cant >= data['pay_cant']:
                result.cant -= data['pay_cant']
                self.db.session.add(result)
                self.db.session.commit()
                self.db.session.close()
                return {'message': 'Compra realizada', 'status_code': 201}
            
            else:
                return {'message': 'No hay suficientes productos', 'status_code': 201}

        else:
            return {'message': 'Producto no existente', 'status_code': 404}