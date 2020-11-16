# encoding=utf-8
import requests
import re
import datetime
from threading import Thread
session = requests.session()
version_start_time = "2020-11-04"


def login():
    base_url = "http://gitlab.enmotech.com"
    url = '{}/users/sign_in'.format(base_url)
    html = session.get(url).text
    csrf_token_regex = re.compile('name="csrf-token" content="(.*)"')
    result = csrf_token_regex.findall(html)[0]
    data = {
        "user[login]": "lei.yang@enmotech.com",
        "user[password]": "yang130740",
        "user[remember_me]": 0,
        "authenticity_token": result

    }
    last_component_update_time = {}
    html = session.post(url, data=data).text
    zdbm_component_regex = re.compile('class="project" href="/ZDBM/([^\"]*)"')
    zdbm_components = zdbm_component_regex.findall(html)
    for component in zdbm_components:
        branch_time = {}
        thread_list = []
        url = base_url + "/ZDBM/" + component
        branch_regex = re.compile('name="repository_ref" id="repository_ref" value="([^"]*)"')
        branch = branch_regex.findall(session.get(url).text)[0]
        get_branchs_url = url + "/refs?ref={}&search=".format(branch)
        branchs = session.get(get_branchs_url).json()['Branches']
        for b in branchs:
            thread = Thread(target=get_component_time, args=(url, b, branch_time))
            thread_list.append(thread)
        for t in thread_list:
            t.start()
        for t in thread_list:
            t.join()
        last_component_update_time[component] = branch_time
    for update_time in last_component_update_time:
        print(update_time, ':', last_component_update_time[update_time])
    # print(r)


def get_component_time(url, b, branch_time):
    get_commits_url = url + '/commits/' + b
    last_commit_time_regex = re.compile('<time class="js-timeago" title="([^"]*)"')
    t = session.get(get_commits_url).text
    last_commit_time = last_commit_time_regex.findall(t)[0]
    parse_time = parse_ymd(last_commit_time)
    if parse_time >= datetime.datetime.strptime(version_start_time, "%Y-%m-%d"):
        branch_time[b] = str(parse_time)[:10]


def parse_ymd(source_time):
    time_dict = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
                 "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

    source_time_list = source_time.replace(',', '')
    mon_s, day_s, year_s = source_time_list.split(' ')[:3]
    parse_time = datetime.datetime(int(year_s), time_dict[mon_s], int(day_s))
    return parse_time


def start():
    login()


if __name__ == '__main__':
    start()