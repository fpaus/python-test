import requests
import json


def get_total_pages(url):
    res = requests.get(url)
    data = json.loads(res.content)
    return data["total_pages"]


def get_all_users(url):
    pages = get_total_pages(url)
    avatars = []
    for page in range(1, pages + 1):
        res = requests.get(f'{url}?page={page}')
        data = json.loads(res.content)
        avatars.extend(data["data"])
    return avatars


def get_all_avatars(url):
    users = get_all_users(url)
    return [user["avatar"] for user in users]
