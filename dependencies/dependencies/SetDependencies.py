import urllib2
import urllib
import json
import base64
import time
import sys

base64string = base64.b64encode("{0}:{1}".format(user, password))

# Primero obtenemos el ID de la tarea de tipo GATE
taskName = urllib.quote(taskName)
phaseName = urllib.quote(phaseName)
url = "http://localhost:5516/api/v1/tasks/byTitle?taskTitle={0}&phaseTitle={1}&releaseId={2}".format(taskName, phaseName, releaseId)
req = urllib2.Request(url)
req.add_header("Authorization", "Basic %s" % base64string)
req.add_header('Content-Type','application/json')
response = urllib2.urlopen(req)
data = json.load(response)
# Ahora debemos obtener el ID de la fase
id_task = data[0]["id"]
print("ID de tarea = {0}".format(id_task))

# Ahora modificamos la tarea y establecemos las dependencias
for id_phase in listIdsDependentPhases:
    url = "http://localhost:5516/api/v1/tasks/{0}/dependencies/{1}".format(id_task, id_phase)
    req = urllib2.Request(url)
    req.add_header("Authorization", "Basic %s" % base64string)
    req.add_header('Content-Type','application/json')
    req.add_data({})
    response = urllib2.urlopen(req)
