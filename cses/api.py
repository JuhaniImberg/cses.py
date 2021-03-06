import click
import requests

from cses.version import __version__

class API(object):
    def __init__(self):
        self.url = "http://cses.fi/api/"
        self.headers = {
            'User-Agent': 'cses.py/{}'.format(__version__)
        }

    def post(self, endpoint, values=None):
        req = requests.post(self.url + endpoint,
                            data=values,
                            headers=self.headers)
        req.raise_for_status()
        return req.json()

    def courses(self):
        return self.post("courses")

    def tasks(self, course, username="", password=""):
        return self.post("tasks",
                         {"course": course,
                          "nick": username,
                          "pass": password})

    def auth(self, username, password):
        return self.post("auth",
                         {"nick": username,
                          "pass": password})

    def send(self, username, password, task, course, lang, code):
        return self.post("send",
                         {"nick": username,
                          "pass": password,
                          "task": task,
                          "course": course,
                          "lang": lang,
                          "code": code})

    def result(self, username, password, submission):
        return self.post("result",
                         {"nick": username,
                          "pass": password,
                          "ticket": submission})

    def tests(self, username, password, task, course):
        return self.post("tests",
                         {"nick": username,
                          "pass": password,
                          "task": task,
                          "course": course})


pass_api = click.make_pass_decorator(API, ensure=True)
