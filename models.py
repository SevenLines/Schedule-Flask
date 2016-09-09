from sqlalchemy.sql.expression import or_

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
    # kontlist = db.relationship('Kontlist', backref='kontkurs', lazy='dynamic')
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


class Kontlist(db.Model):
    id = db.Column('id_ 9', db.Integer, primary_key=True)
    op = db.Column(db.Integer, db.ForeignKey('raspnagr.op'))
    kontkurs_id = db.Column("kont", db.Integer, db.ForeignKey('kontkurs.id_1'))


class Kontgrplist(db.Model):
    id = db.Column('id_ 9', db.Integer, primary_key=True)
    op = db.Column(db.Integer, db.ForeignKey('raspnagr.op'))
    kontgrp_id = db.Column("kontid", db.Integer, db.ForeignKey('kontgrp.id_7'))


class Raspnagr(db.Model):
    id = db.Column('id_51', db.Integer, primary_key=True)
    kontkurs_id = db.Column("kont", db.Integer, db.ForeignKey('kontkurs.id_1'))
    kontgrp_id = db.Column("kontid", db.Integer, db.ForeignKey('kontgrp.id_7'))
    op = db.Column("op", db.Integer)
    # op_grp = db.Column("op", db.Integer)
    nt = db.Column(db.Integer, db.ForeignKey("normtime.id_40"))
    sem = db.Column(db.Integer)
    pred_id = db.Column("pred", db.Integer, db.ForeignKey("vacpred.id_15"))
    kaf_id = db.Column("kaf", db.Integer, db.ForeignKey("vackaf.id_17"))
    fobuch = db.Column(db.SmallInteger)
    afobuch = db.Column(db.SmallInteger)
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

    raspis = db.relationship('Raspis', backref='raspnagr', lazy='dynamic')
    kontlist = db.relationship('Kontlist', backref='raspnagr', lazy='dynamic')
    kontgrplist = db.relationship('Kontgrplist', backref='raspnagr', lazy='dynamic')

    @classmethod
    def get_for_kontgrp(self, kontgrp):
        raspnagrs = Raspnagr.query.filter(
            or_(Raspnagr.kontgrp_id==kontgrp.id, Raspnagr.kontkurs_id==kontgrp.kont_id)
        )
        return raspnagrs


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

    raspnagr = db.relationship('Raspnagr', backref='auditory', lazy='dynamic')
    raspis = db.relationship('Raspis', backref='auditory', lazy='dynamic')


class Discipline(db.Model):
    __tablename__ = "vacpred"
    id = db.Column('id_15', db.Integer, primary_key=True)
    title = db.Column("pred", db.String(250))
    titles = db.Column("preds", db.String(250))

    raspnagr = db.relationship('Raspnagr', backref='discipline', lazy='dynamic')


class Teacher(db.Model):
    __tablename__ = "prepods"
    id = db.Column('id_61', db.Integer, primary_key=True)
    full_name = db.Column('prep', db.String(100))
    name = db.Column('preps', db.String(50))

    raspnagr = db.relationship('Raspnagr', backref='teacher', lazy='dynamic')


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
    id = db.Column('id_55', db.Integer, primary_key=True)
    raspnagr_id = db.Column("raspnagr", db.Integer, db.ForeignKey('raspnagr.id_51'))
    everyweek = db.Column(db.SmallInteger)
    day = db.Column(db.SmallInteger)
    para = db.Column(db.SmallInteger)
    kol_par = db.Column(db.SmallInteger)
    aud_id = db.Column("aud", db.Integer, db.ForeignKey('auditories.id_60'))
    n_zan = db.Column(db.Integer)
    num_zant = db.Column(db.Integer)
    insdate = db.Column(db.DateTime)

    @classmethod
    def get_for_kontgrp(self, kontgrp):
        raspis = Raspis.query.outerjoin().filter(
            or_(
                Raspis.raspnagr.has(kontkurs_id=kontgrp.kont_id),
                Raspis.raspnagr.has(kontgrp_id=kontgrp.id),
                Raspis.raspnagr.has(Raspnagr.kontlist.any(kontkurs_id=kontgrp.kont_id)),
                Raspis.raspnagr.has(Raspnagr.kontgrplist.any(kontgrp_id=kontgrp.id)),
                # Raspis.raspnagr.kontlist.has(kontgrp_id=kontgrp.id),
            )
        ).order_by(Raspis.day, Raspis.para)

        return raspis
