# encoding: utf-8
from enum import Enum


class JobState(Enum):
    NOT_FOUND = 10
    WAITING = 20
    RUNNING = 30
    FINISHED = 40
    FAILED = 50


class JobMessage(Enum):
    NOT_FOUND = "Job not found"
    WAITING = "Job Waiting for processing"
    RUNNING = "Job is running"
    FINISHED = "Job finished with success"
    FAILED = "Something wrong happened"
