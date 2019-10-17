import json
import sys

artifactoryServer = artifactoryServer['url']
# username = artifactoryServer['username']
# password = artifactoryServer['password']
request = HttpRequest({'url': artifactoryServer}, 'admin', 'admin123')
response = request.get(endPoint, contentType = 'application/json')
repositories = []
data = json.loads(response.response)
for i in data:
    repositories = repositories + [i['name']]
listArtifacts = repositories
