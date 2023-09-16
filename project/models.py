from project import db

## User Table configuration
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    membership_status = db.Column(db.VARCHAR(10), nullable=False, default='basic') # "basic", "premium", "admin"
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
