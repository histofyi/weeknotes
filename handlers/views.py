from functions.app import app_context
from models.posts import Posts
from functions.helpers import build_year_month


def weeknotes_index_handler():
    return Posts().latest()


def weeknotes_post_handler(slug):
    return Posts().get(slug)


def weeknotes_tags_handler():
    return Posts().all_tags()


def weeknotes_tag_handler(tag):
    return Posts().filter('tags', tag)


def weeknotes_year_handler(year):
    return Posts().filter('years', year)


def weeknotes_month_handler(year, month):
    return Posts().filter('months', build_year_month(year, month))


