from dotenv import load_dotenv
from sys import argv

from . import jira_tasks
from . import wunderlist_tasks
# import jira_tasks
# import wunderlist_tasks

load_dotenv()


def check_task_status(jira_task, w_task_name, wunderlist_task):

    if w_task_name == wunderlist_task['title']:
        if not (bool(jira_task.fields.resolution) == wunderlist_task['completed']):
            return 'update_wunderlist'
            # TODO: figure out how to bi-directionally sync
        return 'nothing'
    return False


def main():
    list_name = ""
    if len(argv) > 1:
        list_name = argv[1]
    else:
        exit("You must provide a Wunderlist list name")

    wunderlist_list = wunderlist_tasks.fetch_list_with_title(list_name)
    wunderlist_tasklist = wunderlist_tasks.get_tasks(list_name)
    jira_tasklist = jira_tasks.get_tasks()

    for j_task in jira_tasklist:
        operation = 'create'
        update_w_task = {}
        w_task_name = "[{}] {}".format(j_task.key, j_task.fields.summary)
        for w_task in wunderlist_tasklist:

            task_operation = check_task_status(j_task, w_task_name, w_task)
            if task_operation:
                operation = task_operation
                update_w_task = w_task

        if operation == 'create':
            wunderlist_tasks.create_task(
                wunderlist_list['id'], w_task_name, bool(j_task.fields.resolution))
        elif operation == 'update_wunderlist':
            wunderlist_tasks.update_task(
                list_name, update_w_task, bool(j_task.fields.resolution))
        # elif operation == 'update_notion':
        #     update_notion_status(nt)


if __name__ == '__main__':
    main()
