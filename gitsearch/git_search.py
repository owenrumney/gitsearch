import requests
import parsedatetime as pdt

from datetime import datetime
from gitsearch import git_entities
from gitsearch.output import display_table

base_url = "https://api.github.com/search/%s?q=%s"

headings = {'users': ['username', 'url'], 'repositories': ['name', 'owner', 'url']}


def display_results(results, scope):
    display_table(results, headings[scope])


def execute_search(config, query):
    query_string = create_query_string(config, query)
    request_url = base_url % (config.scope, "+".join(query_string))
    r = requests.get(request_url)
    process_result(config, r)


def process_result(config, r):
    if r.status_code != 200:
        print("")
    data = r.json()
    results = []
    for item in data.get('items'):
        results.append(git_entities.create_git_object(config.scope, item))
    display_results(results, config.scope)


def get_real_date(natural_date):
    now = datetime.now()
    cal = pdt.Calendar()
    result, success = cal.parseDT(natural_date, now)
    if success == 1:
        return result.strftime("%Y-%m-%d")
    print("Couldn't parse the date: %s. Using default of the beginning of time (1979)" % natural_date)
    return "1979-10-30"


def create_query_string(config, query):
    if config.language:
        query.append("language:%s" % config.language)
    if config.user:
        query.append("user:%s" % config.user)
    if config.nameonly:
        query.append("in:name")
    if config.descriptiononly:
        query.append("in:description")
    if config.created:
        query.append("created:>%s" % get_real_date(config.created))
    if config.updated:
        query.append("pushed:>%s" % get_real_date(config.updated))
    return query
