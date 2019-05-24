from os import getenv
from jira import JIRA

JIRA_URL = getenv('JIRA_URL')
JIRA_USERNAME = getenv('JIRA_USERNAME')
JIRA_API_KEY = getenv('JIRA_API_KEY')


def get_jira_client():
    jira = JIRA(JIRA_URL, basic_auth=(JIRA_USERNAME, JIRA_API_KEY))
    return jira


def get_tasks(client=None):
    if not client:
        client = get_jira_client()
    return client.search_issues("assignee = currentUser()")


def main():
    client = get_jira_client()
    for t in get_tasks(client):
        print(t.key, t.fields.summary, t.fields.resolution)


if __name__ == "__main__":
    main()
