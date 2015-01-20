import click

from cses.cli import cli
from cses.api import API
from cses.db import DB
from cses.shorthand_group import ShorthandGroup

@cli.group(cls=ShorthandGroup)
@click.pass_context
def courses(ctx):
    "Stuff about courses"

def show_courses(courses, id=None):
    for course in courses:
        click.echo("{}: {} {}".format(course["id"],
                                      course["name"],
                                      "(Selected)" if id is course["id"] else ""))

@courses.command()
@click.pass_context
def show(ctx):
    "Lists the various available courses"
    api = ctx.ensure_object(API)
    db = ctx.ensure_object(DB)
    show_courses(api.courses(), db.course)

@courses.command()
@click.pass_context
def select(ctx):
    "Allows you to select the current course"
    api = ctx.ensure_object(API)
    db = ctx.ensure_object(DB)
    id = db.course
    courses = api.courses()
    valid_ids = [x["id"] for x in courses]
    show_courses(courses, id)
    while 1:
        id = click.prompt("Enter a course id", default=id, type=int)
        if id not in valid_ids:
            if not click.confirm("Invalid course id, try again", default=True):
                ctx.fail("Could not select a course")
        else:
            break
    db.course = id