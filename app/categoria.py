from flask import Flask,jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:P455W0RD@db_container:3306/dbpythonapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
ma = Marshmallow(app)


#Creacion de la tabla categoria
class Categoria(db.Model):
    cat_id = db.Column(db.Integer, primary_key = True)
    cat_nom = db.Column(db.String(100))
    cat_dep = db.Column(db.String(100))

    def __init__(self, cat_nom,cat_dep):
        self.cat_nom = cat_nom
        self.cat_dep = cat_dep

with app.app_context():
    db.create_all()


#Esquema categoria
class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('cat_id','cat_nom','cat_dep')  

#Para cuando es una sola respuesta
categoria_schema = CategoriaSchema()
#Para cuando sean multiples respuestas
categorias_schema = CategoriaSchema(many = True)
 
#GET
@app.route('/categoria',methods=['GET'])
def get_categorias():
    all_categorias = Categoria.query.all()
    result = categorias_schema.dump(all_categorias)
    return jsonify(result)

#GET for ID
@app.route('/categoria/<id>', methods = ['GET'])
def get_categoriaID(id):
    una_categoria = Categoria.query.get(id)
    return categoria_schema.jsonify(una_categoria)

#POST 
@app.route('/categoria', methods = ['POST'])
def insert_categoria():
    data = request.get_json(force = True)
    cat_nom = data['cat_nom']
    cat_dep= data['cat_dep']

    nuevaCategoria = Categoria(cat_nom,cat_dep)
    db.session.add(nuevaCategoria)
    db.session.commit()
    return categoria_schema.jsonify(nuevaCategoria)

#PUT
@app.route('/categoria/<id>', methods=['PUT'])
def update_categoria(id):
    data = request.get_json(force = True)
    UpdateCat = Categoria.query.get(id)

    cat_nom = data['cat_nom']
    cat_dep = data['cat_dep']

    UpdateCat.cat_nom = cat_nom
    UpdateCat.cat_dep = cat_dep

    db.session.commit()

    return categoria_schema.jsonify(UpdateCat)

#DELETE 
@app.route('/categoria/<id>', methods=['DELETE'])
def delete_categoria(id):
    eliminar_categoria = Categoria.query.get(id)
    db.session.delete(eliminar_categoria)
    db.session.commit()
    return categoria_schema.jsonify(eliminar_categoria)


#Mensaje de bienvenida
@app.route('/',methods = ['GET'])
def index():
    return jsonify({'Mensaje':'Bienvenido'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug = True)