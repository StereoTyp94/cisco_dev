from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part = db.Column(db.String(128), index=True, unique=True)
    gpl = db.Column(db.Float)
    services = db.relationship('Service', backref='equipment', lazy='dynamic')

    def __repr__(self):
        return '<Part {}>'.format(self.part)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serv_lev = db.Column(db.String(10))
    sku = db.Column(db.String(50))
    serv_gpl = db.Column(db.Float)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __repr__(self):
        return '<SKU {}>'.format(self.sku)