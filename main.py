from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from random import choice
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5173/"}})
app.config['CORS_HEADERS'] = 'Content-Type'

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

## User Table configuration
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    membership_status = db.Column(db.VARCHAR(10), nullable=False) # "basic", "premium", "admin"
    # weight should be either kg or lbs
    weight_value = db.Column(db.Float, nullable=False)
    weight_unit = db.Column(db.VARCHAR(5), nullable=False)
    height_value = db.Column(db.Float, nullable=False)
    height_unit = db.Column(db.VARCHAR(5), nullable=False)


    def to_dict(self):
        # I'm returning a dictionary representation of the User object.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
        # dict = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     dict[column.name] = getattr(self, column.name)
        # return dict


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
        # dict = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     dict[column.name] = getattr(self, column.name)
        # return dict



with app.app_context():
    db.create_all()

@app.route("/")
def home():
    print()
    return render_template("index.html")

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    updated_cafe = db.session.query(Cafe).filter_by(id=cafe_id) .first()
    if updated_cafe:
        new_price = request.args.get("new_price")
        updated_cafe.coffee_price = new_price
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found."})




@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    delete_cafe = db.session.query(Cafe).filter_by(id=cafe_id) .first()
    pick_cafe = request.args.get("api-key")
    if delete_cafe and pick_cafe == "TopSecretAPIKey":
        db.session.delete(delete_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe."})
    else:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found."})



@app.route("/allcafe")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def location():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafes=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

@app.route("/all")
def all_users():
    users = db.session.query(User).all()
    return jsonify(users=[user.to_dict() for user in users])

# Route for all the users
@app.route("/adduser", methods=["GET", "POST"])
def create_new_user():
    data = request.get_json()
    if data:
        new_user = User(
            email=data.get("email"),
            name=data.get("name"),
            password=data.get("password"),
            membership_status=data.get("membership_status"),
            weight_value=data.get("weight_value"),
            weight_unit=data.get("weight_unit"),
            height_value=data.get("height_value"),
            height_unit=data.get("height_unit"),
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    else:
        return jsonify({"error": "Invalid JSON data"}), 400
@app.route("/add", methods=["GET", "POST"])
def post_new_cafe():
    cafes = db.session.query(Cafe).all()
    cafe_length = len(cafes)
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        has_sockets=bool(request.form.get("sockets")),
        can_take_calls=bool(request.form.get("calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route("/random")
def random():
    cafe = choice(Cafe.query.all())
    return jsonify(cafe.to_dict())


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
