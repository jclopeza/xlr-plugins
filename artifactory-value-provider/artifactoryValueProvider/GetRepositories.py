import json

request = HttpRequest({'url': valueProvider.artifactoryServer.url}, valueProvider.artifactoryServer.username, valueProvider.artifactoryServer.password)
response = request.get(valueProvider.endPoint, contentType = 'application/json')
data = json.loads(response.getResponse())
result = []
for repository in data:
    result = result + [repository['key']]