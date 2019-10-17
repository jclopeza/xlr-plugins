import json

request = HttpRequest({'url': valueProvider.artifactoryServer.url}, valueProvider.artifactoryServer.username, valueProvider.artifactoryServer.password)
endPoint = "/api/storage/{0}/{1}".format(releaseVariables['repository'], releaseVariables['artifact'])
response = request.get(endPoint, contentType = 'application/json')
data = json.loads(response.getResponse())
result = []
for version in data['children']:
    result = result + [version['uri']]