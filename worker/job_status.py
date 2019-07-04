# encoding: utf-8
from worker.connection import conn
from worker.enumerable import JobMessage, JobState


from rq.job import Job


def get_job_state(job_key):
    response = {
        "message": JobMessage.NOT_FOUND,
        "job_state": JobState.NOT_FOUND,
        "content": {}
    }
    if not Job.exists(job_key, conn):
        return response

    job = Job.fetch(job_key, connection=conn)
    
    response["content"].update(args=job.args)
    response["content"].update(kwargs=job.kwargs)

    if job.is_finished:
        response["message"] = JobMessage.FINISHED
        response["job_state"] = JobState.FINISHED
        response["content"].update(result=job.result)

    elif job.is_failed:
        response["message"] = JobMessage.FAILED
        response["job_state"] = JobState.FAILED
        response["traceback"].update(traceback=job.exc_info)

    elif job.is_queued:
        response["message"] = JobMessage.WAITING
        response["job_state"] = JobState.WAITING

    else:
        response["message"] = JobMessage.RUNNING
        response["job_state"] = JobState.RUNNING

    return response
