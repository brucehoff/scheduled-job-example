import json, os, synapseclient

secrets=json.loads(os.getenv("SCHEDULED_JOB_SECRETS"))

auth_token = secrets["PAT"]

project_id = os.getenv("PROJECT_ID")


syn=synapseclient.Synapse()

syn.login(authToken=auth_token)


for child in syn.getChildren(project_id):
	print(child['name'])

