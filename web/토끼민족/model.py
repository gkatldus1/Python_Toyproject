from app import db

class rabbitUser(db.Model):

    __tablename__ = 'rabbitUser'

    id          = db.Column(db.String(20), primary_key=True, nullable=False)
    password    = db.Column(db.String(255), nullable=False)
    nickname    = db.Column(db.String(20))
    point       = db.Column(db.Integer)
    address     = db.Column(db.String(255))
    telephone   = db.Column(db.String(11))
    rank        = db.Column(db.Integer)

    def __init__(self, id, password, nickname, telephone):
        self.id         = id
        self.password   = password
        self.nickname   = nickname
        self.telephone  = telephone
        self.point      = 0
        self.rank       = 0


class rabbitStore(db.Model):
    
    __tablename__ = 'rabbitStore'
    
    id          = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name        = db.Column(db.String(20), nullable=False)
    location    = db.Column(db.String(50))
    rating      = db.Column(db.Integer)
    open_time   = db.Column(db.String(5))
    close_time  = db.Column(db.String(5))
    stars       = db.Column(db.Integer)
    thumbnail   = db.Column(db.String(255))


class rabbitMenu(db.Model):

    __tablename__ = 'rabbitMenu'

    id          = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    food_name   = db.Column(db.String(20), nullable=False)
    store_id    = db.Column(db.Integer, db.ForeignKey('rabbitStore.id'))
    description = db.Column(db.String(255))
    price       = db.Column(db.Integer, nullable=False)
    thumbnail   = db.Column(db.String(255))


class rabbitReview(db.Model):

    __tablename__ = 'rabbitReview'

    id          = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id     = db.Column(db.Integer, db.ForeignKey('rabbitUser.id'), nullable=False)
    store_id    = db.Column(db.Integer, db.ForeignKey('rabbitStore.id'), nullable=False)
    rating      = db.Column(db.Float)
    content     = db.Column(db.Text())