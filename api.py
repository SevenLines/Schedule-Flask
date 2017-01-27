from flask.ext.restful import Api, Resource

from base import app
from helpers import render_template_schedule_json
from models import Kontgrp, Raspis, Kontkurs, Auditory

api = Api(app)


class GroupSchedule(Resource):
    def get(self, group_id):
        schedule = {}
        group = Kontgrp.query.get(group_id)
        if group:
            schedule = Raspis.get_for_kontgrp(group)
        else:
            group = Kontkurs.query.get(group_id)
            if group:
                schedule = Raspis.get_for_kontkurs(group)

        return {
            "group": group,
            "schedule": schedule
        }

class AuditorySchedule(Resource):
    def get(self, auditory_id):
        auditory = Auditory.query.get(auditory_id)
        schedule = Raspis.get_for_auditory(auditory)

        return {
            "auditory": auditory,
            "schedule": schedule
        }



api.add_resource(GroupSchedule, '/schedule/group/<int:group_id>')
api.add_resource(AuditorySchedule, '/schedule/group/<int:group_id>')