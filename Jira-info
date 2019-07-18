# Utilizes the Jira API to list your open projects then displays more info
# on the selected issue.

from jira import JIRA

# Change these
URL = 'https://my.jira.com' # URL of Jira instance
email = 'change@me.com' # email address
token = 'paste token here' # api token
project = 'TEST' # project name

# connects to Jira instance
jira = JIRA(server=URL, basic_auth=(email, token))

# prints all issues for the project which are not closed
IDList = list() # empty list for issue keys
print('All open issues:')
for issue in jira.search_issues('project ="' + project + '" and assignee = currentUser() and status!=Done'):
    print(issue.key, issue.fields.summary)
    IDList.append(issue.key) # adds issue key to the list

# asks for an issue ID
issueID = input('\n Select an issue for more information: ')

# ensure issue ID starts with project ID
if issueID.startswith(project +'-'):
    pass
else:
    issueID = "IF-"+issueID

# ensure issue ID is in the list of issues, quits if it isn't
if issueID not in IDList:
    print('Invalid ID')
    quit()

# lists info about selected issue
for ID in jira.search_issues('key ="' + issueID + '"'):
    IDKey = ID.key
    summary = ID.fields.summary # summary
    desc = str(ID.fields.description) # description
    labels = str(ID.fields.labels) # labels
    due = str(ID.fields.duedate) # due date
# prints all the above info on the selected issue
print(IDKey, summary, '\n Description: ' + desc, '\n Labels: ' + labels, '\n Due: ' + due)


