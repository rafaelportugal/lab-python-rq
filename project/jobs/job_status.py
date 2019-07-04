# encoding: utf-8
import flask_restful as restful

from worker.job_status import get_job_state
from worker.enumerable import JobState
from project.auth import login_required


class JobStatus(restful.Resource):
    @login_required
    def get(self, job_key):
        result = get_job_state(job_key)
        status_code = 200

        job_status = result.get("job_state")
        response = {
            "jobStatus": {
                "id": job_status.value,
                "name": job_status.name
            }
        }

        response.update(content=result.get("content"))

        if job_status == JobState.NOT_FOUND:
            status_code = 404

        return response, status_code
