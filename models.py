from base import db


class Kontkurs(db.Model):
    id = db.Column('id_1', db.Integer, primary_key=True)
    title = db.Column("obozn", db.String(20))
    shup = db.Column(db.Integer)
    spclntion = db.Column(db.Integer)
    kurs = db.Column(db.Integer)
    fil = db.Column(db.Integer)
    fac = db.Column(db.Integer)
    aobozn = db.Column(db.Integer)
    stud = db.Column(db.Integer)
    groups = db.Column(db.Integer)
    pgroups = db.Column(db.Integer)
    smenao = db.Column(db.Integer)
    smenav = db.Column(db.Integer)
    groupkey = db.Column(db.Integer)
    undoworksps = db.Column(db.String(250))
    anothernumstudsps = db.Column(db.String(250))
    newnumstud = db.Column(db.SmallInteger)
    ntcgraph = db.Column(db.SmallInteger)
    syear = db.Column(db.Integer)

    groupslist = db.relationship('Kontgrp', backref='kontkurs', lazy='dynamic')

    def __str__(self, *args, **kwargs):
        return "<Kontkurs: {}>".format(self.title.strip())

    def __repr__(self):
        return str(self)


class Kontgrp(db.Model):
    id = db.Column('id_7', db.Integer, primary_key=True)
    kont_id = db.Column("kont", db.Integer, db.ForeignKey('kontkurs.id_1'))
    title = db.Column("obozn", db.String(20))
    ngroup = db.Column(db.Integer)
    students = db.Column(db.Integer)
    parent = db.Column(db.Integer)
    depth = db.Column(db.Integer)
    budzh = db.Column(db.Integer)
    spclntion = db.Column(db.Integer)

    def __str__(self, *args, **kwargs):
        return "<Kontgrp: {}>".format(self.title.strip())

    def __repr__(self):
        return str(self)


class Raspnagr(db.Model):
    id = db.Column('id_51', db.Integer, primary_key=True)
    kontkurs_id = db.Column("kont", db.Integer, db.ForeignKey('kontkurs.id_1'))
    kontgrp_id = db.Column("kontid", db.Integer, db.ForeignKey('kontgrp.id_7'))
    op = db.Column(db.Integer)
    nt = db.Column(db.Integer, db.ForeignKey("normtime.id_40"))
    sem = db.Column(db.Integer)
    pred_id = db.Column("pred", db.Integer, db.ForeignKey("vacpred.id_15"))
    kaf_id = db.Column("kaf", db.Integer, db.ForeignKey("vackaf.id_17"))
    foubch = db.Column(db.SmallInteger)
    afoubch = db.Column(db.SmallInteger)
    nagrid = db.Column(db.Integer)
    h = db.Column(db.Float)
    hy = db.Column(db.Float)
    dbeg = db.Column(db.Date)
    days = db.Column(db.Integer)
    prep_id = db.Column("prep", db.Integer, db.ForeignKey('prepods.id_61'))
    aud_id = db.Column("aud", db.Integer, db.ForeignKey('auditories.id_60'))
    nagrtype = db.Column(db.SmallInteger)
    nagrprop = db.Column(db.Integer)
    nagr_h = db.Column(db.Float)
    stud = db.Column(db.Integer)
    editstud = db.Column(db.Integer)
    rnprep = db.Column(db.Integer)
    hy1 = db.Column(db.Integer)
    hy2 = db.Column(db.Integer)
    syear = db.Column(db.Integer)


class Korpus(db.Model):
    __tablename__ = "vackorp"
    id = db.Column('id_67', db.Integer, primary_key=True)
    title = db.Column("obozn", db.String(10))
    auditories = db.relationship('Auditory', backref='korp', lazy='dynamic')

    def __str__(self, *args, **kwargs):
        return "<Korpus: {}>".format(self.title.strip())

    def __repr__(self):
        return str(self)


class Auditory(db.Model):
    __tablename__ = "auditories"

    id = db.Column('id_60', db.Integer, primary_key=True)
    title = db.Column("obozn", db.String(20))
    korp_id = db.Column("korp", db.Integer, db.ForeignKey('vackorp.id_67'))
    maxstud = db.Column(db.SmallInteger)
    specoborud = db.Column(db.SmallInteger)

    def __str__(self, *args, **kwargs):
        return "<Auditory: {}>".format(self.title.strip())

    def __repr__(self):
        return str(self)


class Discipline(db.Model):
    __tablename__ = "vacpred"
    id = db.Column('id_15', db.Integer, primary_key=True)
    title = db.Column("pred", db.String(250))
    titles = db.Column("preds", db.String(250))


class Teacher(db.Model):
    __tablename__ = "prepods"
    id = db.Column('id_61', db.Integer, primary_key=True)
    full_name = db.Column('prep', db.String(100))
    name = db.Column('preps', db.String(50))


class Faculty(db.Model):
    __tablename__ = "vacfac"
    id = db.Column('id_5', db.Integer, primary_key=True)
    title = db.Column("fac", db.String(65))


class Chair(db.Model):
    __tablename__ = "vackaf"
    id = db.Column('id_17', db.Integer, primary_key=True)
    title = db.Column("kaf", db.String(100))
    short_title = db.Column("sokr", db.String(10))


class Normtime(db.Model):
    id = db.Column('id_40', db.Integer, primary_key=True)
    vacnt = db.Column(db.Integer)
    title = db.Column("repvrnt", db.String(50))
    vrnt = db.Column(db.String(250))
    dopinfo = db.Column(db.String(250))


class Raspis(db.Model):
    id = db.Column('id_56', db.Integer, primary_key=True)
    raspnagr = db.Column(db.Integer, db.ForeignKey('id_51'))
    everyweek = db.Column(db.SmallInteger)
    day = db.Column(db.SmallInteger)
    para = db.Column(db.SmallInteger)
    kolpar = db.Column(db.SmallInteger)
    aud = db.Column(db.Integer, db.ForeignKey('id_60'))
    n_zan = db.Column(db.Integer)
    num_zan = db.Column(db.Integer)
    insdate = db.Column(db.DateTime)
