# Utilizes the Jira API to create a new task.

from jira import JIRA

# Change these
URL = 'URL' # URL of Jira instance
email = 'email' # email address
token = 'API token' # api token
project = 'TEST'

# connects to Jira instance
jira = JIRA(server=URL, basic_auth=(email, token))

# informs the user which project this task will be added to
print('This new task will be added to the ' + project + ' project. ')

# prompts user for a summary, description, and name (assignee)
summary = input('What needs to be done? ')

description = input('Tell me more about it: ')

name = input('Who is going to work on this? (Needs to be username!) ')

issue_dict = { # place all the info into a dict
    'project': {'key': project},
    'summary': summary,
    'description': description,
    'issuetype': {'name': 'Task'},
    'assignee': {'name': name},
    }

# create the issue
new_issue = jira.create_issue(fields=issue_dict)
