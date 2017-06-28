# coding=utf-8
from sqlalchemy.orm.util import aliased
from sqlalchemy.sql.expression import or_, and_

from base import db


class Kontkurs(db.Model):
    id = db.Column('id_1', db.Integer, primary_key=True)
    title = db.Column("obozn", db.String(20))
    shup = db.Column(db.Integer)
    spclntion = db.Column(db.Integer)
    kurs = db.Column(db.Integer)
    fil = db.Column(db.Integer)
    fac_id = db.Column("fac", db.Integer, db.ForeignKey('vacfac.id_5'))
    aobozn_id = db.Column("aobozn", db.Integer, db.ForeignKey('vacaobozn.id_6'))
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

    groupslist = db.relationship('Kontgrp', backref='kontkurs', lazy='joined')
    kontlist = db.relationship('Kontlist', backref='kontkurs', lazy='select')
    raspnagr = db.relationship("Raspnagr", backref=db.backref('kontkurs', lazy='select'))

    def __str__(self, *args, **kwargs):
        return "<Kontkurs: {}>".format(self.title.strip())

    def __repr__(self):
        return str(self)

    def get_title(self):
        return self.title.replace("(И,О)", "")


class Obozn(db.Model):
    __tablename__ = "vacaobozn"
    id = db.Column('id_6', db.Integer, primary_key=True)
    title = db.Column("aobozn", db.String(50))

    kontkurs = db.relationship("Kontkurs", backref=db.backref("aobozn", lazy="joined"))


class Kontgrp(db.Model):
    id = db.Column('id_7', db.Integer, primary_key=True)
    kont_id = db.Column("kont", db.Integer, db.ForeignKey('kontkurs.id_1'))
    title = db.Column("obozn", db.String(20))
    ngroup = db.Column(db.Integer)
    students = db.Column(db.Integer)
    parent_id = db.Column("parent", db.Integer, db.ForeignKey('kontgrp.id_7'))
    depth = db.Column(db.Integer)
    budzh = db.Column(db.Integer)
    spclntion = db.Column(db.Integer)

    op = db.relationship("Kontgrplist", backref=db.backref("kontgrp", lazy="joined"), lazy='joined')
    raspnagr = db.relationship("Raspnagr", backref=db.backref('kontgrp', lazy='joined'))
    children = db.relationship("Kontgrp", backref=db.backref('parent', remote_side=[id], lazy="joined"))

    def __str__(self, *args, **kwargs):
        return "<Kontgrp: {}>".format(self.title.strip())

    def __repr__(self):
        return str(self)

    def get_title(self):
        return self.title.replace("(И,О)", "")
        # if self.parent_id:
        #     return "{}-{}-{}-{}".format(
        #         self.kontkurs.kurs,
        #         self.kontkurs.aobozn.title,
        #         self.parent.ngroup,
        #         self.ngroup,
        #     )
        # else:
        #     return "{}-{}-{}".format(
        #         self.kontkurs.kurs,
        #         self.kontkurs.aobozn.title,
        #         self.ngroup,
        #     )


class Kontlist(db.Model):
    id = db.Column('id_9', db.Integer, primary_key=True)
    op = db.Column(db.Integer, db.ForeignKey('raspnagr.op'))
    kontkurs_id = db.Column("kont", db.Integer, db.ForeignKey('kontkurs.id_1'))


class Kontgrplist(db.Model):
    id = db.Column('id_', db.Integer, primary_key=True)
    op = db.Column(db.Integer, db.ForeignKey('raspnagr.op'))
    kontgrp_id = db.Column("kontid", db.Integer, db.ForeignKey('kontgrp.id_7'))


class Raspnagr(db.Model):
    id = db.Column('id_51', db.Integer, primary_key=True)
    kontkurs_id = db.Column("kont", db.Integer, db.ForeignKey('kontkurs.id_1'))
    kontgrp_id = db.Column("kontid", db.Integer, db.ForeignKey('kontgrp.id_7'))
    op = db.Column("op", db.Integer)
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

    raspis = db.relationship('Raspis', backref=db.backref('raspnagr', lazy='joined'), lazy='dynamic')
    kontlist = db.relationship('Kontlist', backref='raspnagr', lazy='subquery')
    kontgrplist = db.relationship('Kontgrplist', backref='raspnagr', lazy='subquery')

    @classmethod
    def get_for_kontgrp(self, kontgrp):
        raspnagrs = Raspnagr.query.filter(
            or_(Raspnagr.kontgrp_id == kontgrp.id, Raspnagr.kontkurs_id == kontgrp.kont_id)
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

    raspnagr = db.relationship('Raspnagr', backref=db.backref('auditory', lazy='joined'), lazy='dynamic')
    raspis = db.relationship('Raspis', backref=db.backref('auditory', lazy='joined'), lazy='dynamic')


class Discipline(db.Model):
    __tablename__ = "vacpred"
    id = db.Column('id_15', db.Integer, primary_key=True)
    title = db.Column("pred", db.String(250))
    titles = db.Column("preds", db.String(250))

    raspnagr = db.relationship('Raspnagr', backref=db.backref('discipline', lazy='joined'), lazy='dynamic')


class Teacher(db.Model):
    __tablename__ = "prepods"
    id = db.Column('id_61', db.Integer, primary_key=True)
    full_name = db.Column('prep', db.String(100))
    name = db.Column('preps', db.String(50))

    raspnagr = db.relationship('Raspnagr', backref=db.backref('teacher', lazy='joined'), lazy='dynamic')


class Faculty(db.Model):
    __tablename__ = "vacfac"
    id = db.Column('id_5', db.Integer, primary_key=True)
    title = db.Column("fac", db.String(65))

    kontkurs = db.relationship('Kontkurs', backref=db.backref('faculty', lazy='joined'), lazy='dynamic')


class Chair(db.Model):
    __tablename__ = "vackaf"
    id = db.Column('id_17', db.Integer, primary_key=True)
    title = db.Column("kaf", db.String(100))
    short_title = db.Column("sokr", db.String(10))

    raspnagr = db.relationship('Raspnagr', backref=db.backref('chair', lazy='joined'), lazy='dynamic')


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
    def _get_table(cls, rows, group_by_lesson=False, key_template=None, *args, **kwargs):
        schedule = {
            para: {
                day: {
                    'everyweek': [],
                    'odd': [],
                    'even': [],
                } for day in [1, 2, 3, 4, 5, 6]
                } for para in [0, 1, 2, 3, 4, 5, 6, 7, 8]
            }

        if key_template is None:
            key_template = "{discipline_id}_{nt}"

        for lesson in rows.order_by(Raspis.day, Raspis.para):
            setattr(lesson, 'groups', [])

            if lesson.raspnagr.kontgrp:
                lesson.groups = [lesson.raspnagr.kontgrp, ]
                lesson.faculty = lesson.raspnagr.kontgrp.kontkurs.faculty
            elif lesson.raspnagr.kontkurs:
                lesson.groups = [lesson.raspnagr.kontkurs, ]
                lesson.faculty = lesson.raspnagr.kontkurs.faculty
            elif lesson.raspnagr.kontgrplist:
                lesson.groups = [i.kontgrp for i in lesson.raspnagr.kontgrplist]
                lesson.faculty = lesson.groups[0].kontkurs.faculty
            elif lesson.raspnagr.kontlist:
                lesson.groups = [i.kontkurs for i in lesson.raspnagr.kontlist]
                lesson.faculty = lesson.groups[0].faculty

            if lesson.everyweek == 1:
                if lesson.day > 7:
                    week = 'even'
                else:
                    week = 'odd'
            else:
                week = 'everyweek'

            schedule[lesson.para][(lesson.day - 1) % 7 + 1][week].append(lesson)
            schedule[lesson.para][(lesson.day - 1) % 7 + 1][week].sort(key=lambda l: l.groups[0].title)
            lesson.kurs_list = {getattr(i, 'kurs') if hasattr(i, 'kurs') else i.kontkurs.kurs for i in lesson.groups}


        if group_by_lesson:
            for para, days in schedule.items():
                for day, weeks in days.items():
                    for week, lessons in weeks.items():
                        weeks[week] = {}
                        for lesson in lessons:
                            for kont in lesson.groups:
                                kont.kurs = kont.kontkurs.kurs if hasattr(kont, 'kontkurs') else kont.kurs
                                key = key_template.format(**{
                                    'discipline_id': lesson.raspnagr.discipline.id,
                                    'nt': lesson.raspnagr.nt,
                                    'fac_id': lesson.faculty.id,
                                    'kurs': kont.kurs
                                })
                                weeks[week].setdefault(key, [])
                                weeks[week][key].append(lesson)
                        for key, dlessons in weeks[week].items():
                            weeks[week][key] = dlessons[0] if dlessons else None
                            for lesson in dlessons[1:]:
                                weeks[week][key].groups += lesson.groups
                            weeks[week][key].groups.sort(key=lambda l: l.title)
                        weeks[week] = list(weeks[week].values())

        return schedule

    @classmethod
    def get_for_chair(cls, chair, *args, **kwargs):
        raspis = Raspis.query.filter(
            Raspis.raspnagr.has(kaf_id=chair.id)
        )

        return cls._get_table(raspis, *args, **kwargs)

    @classmethod
    def get_for_kontgrp(cls, kontgrp, *args, **kwargs):
        raspis = Raspis.query.filter(
            or_(
                Raspis.raspnagr.has(and_(
                    Raspnagr.kontgrp_id == 0,
                    Raspnagr.kontkurs_id == kontgrp.kont_id
                )),
                Raspis.raspnagr.has(kontgrp_id=kontgrp.id),
                Raspis.raspnagr.has(and_(
                    Raspnagr.kontgrp.has(kont_id=kontgrp.kont_id),
                    Raspnagr.kontgrp.has(or_(
                        and_(
                            Kontgrp.depth < kontgrp.depth,
                            or_(
                                Kontgrp.id == kontgrp.parent_id,
                                Kontgrp.children.any(id=kontgrp.parent_id),
                            ),
                        ),
                        and_(
                            Kontgrp.depth > kontgrp.depth,
                            Kontgrp.parent_id == kontgrp.id,
                        )
                    )),
                )),
                Raspis.raspnagr.has(Raspnagr.kontlist.any(kontkurs_id=kontgrp.kont_id)),
                Raspis.raspnagr.has(Raspnagr.kontgrplist.any(kontgrp_id=kontgrp.id)),
            )
        )

        return cls._get_table(raspis, *args, **kwargs)

    @classmethod
    def get_for_kontkurs(cls, kontkurs, *args, **kwargs):
        Kontgrp2 = aliased(Kontgrp)
        Kontkurs2 = aliased(Kontkurs)
        raspis = Raspis.query \
            .join(Raspnagr) \
            .outerjoin(Kontgrp, Raspnagr.kontgrp_id == Kontgrp.id) \
            .outerjoin(Kontgrplist, Kontgrplist.op == Raspnagr.op) \
            .outerjoin(Kontlist, Kontlist.op == Raspnagr.op) \
            .outerjoin(Kontgrp2, Kontgrp2.id == Kontgrplist.kontgrp_id) \
            .outerjoin(Kontkurs2, Kontkurs2.id == Kontlist.kontkurs_id) \
            .filter(
            or_(
                Raspnagr.kontkurs_id == kontkurs.id,
                Kontgrp.kont_id == kontkurs.id,
                Kontgrp2.kont_id == kontkurs.id,
                Kontkurs2.id == kontkurs.id,
            ))

        return cls._get_table(raspis, *args, **kwargs)

    @classmethod
    def get_for_auditory(cls, auditory, *args, **kwargs):
        raspis = Raspis.query.filter(
            Raspis.aud_id == auditory.id
        )

        return cls._get_table(raspis, *args, **kwargs)

    @classmethod
    def get_for_teacher(cls, teacher, *args, **kwargs):
        raspis = Raspis.query.filter(
            or_(
                Raspis.raspnagr.has(prep_id=teacher.id),
            )
        )

        return cls._get_table(raspis, *args, **kwargs)

    @classmethod
    def get_for_discipline(cls, discipline, *args, **kwargs):
        raspis = Raspis.query.filter(
            or_(
                Raspis.raspnagr.has(pred_id=discipline.id),
            )
        )

        return cls._get_table(raspis, *args, **kwargs)
