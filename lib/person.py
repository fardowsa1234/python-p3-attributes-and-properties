#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

# lib/person.py
class Person:
    approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]

    def __init__(self, name="Unknown", job="Unemployed"):
        self.name = name
        self.job = job

    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            print(f"Setting name to {name}.")
            self._name = name.title()

    name = property(get_name, set_name)

    def get_job(self):
        print("Retrieving job.")
        return self._job

    def set_job(self, job):
        if job not in Person.approved_jobs:
            print("Job must be in list of approved jobs.")
        else:
            print(f"Setting job to {job}.")
            self._job = job

    job = property(get_job, set_job)


