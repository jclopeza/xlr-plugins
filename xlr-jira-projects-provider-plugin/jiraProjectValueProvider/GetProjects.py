import json

request = HttpRequest({'url': valueProvider.jiraServer.url}, valueProvider.jiraServer.username, valueProvider.jiraServer.password)
response = request.get(valueProvider.endPoint, contentType = 'application/json')
data = json.loads(response.getResponse())
result = []
for repository in data:
    result = result + [repository['name']]