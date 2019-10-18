import urllib2
import urllib
import json
import base64
import time
import sys

base64string = base64.b64encode("{0}:{1}".format(user, password))

id_dependencies = []
for dep in dependencies:
    dep = urllib.quote(dep)
    print("dep = {0}".format(dep))
    url = "http://localhost:5516/api/v1/releases/byTitle?releaseTitle={0}".format(dep)
    req = urllib2.Request(url)
    req.add_header("Authorization", "Basic %s" % base64string)
    req.add_header('Content-Type','application/json')
    microserviceFound = False
    while not microserviceFound:
        response = urllib2.urlopen(req)
        data = json.load(response)
        print("Total de registros para microservicio {0} = {1}".format(dep, len(data)))
        if len(data) > 0:
            microserviceFound = True
            # Ahora debemos obtener el ID de la release
            id_release = data[0]["id"]
            id_dependencies = id_dependencies + [id_release]
            print("ID release = {0}".format(id_release))
        else:
            time.sleep(10)

# Abortamos el proceso si no hemos encontrado dependencias
if len(id_dependencies) == 0:
    sys.exit(0)

# Obtenemos los IDs de las fases de los microservicios
id_phases = []
for id_dep in id_dependencies:
    # Obtenemos el ID de la fase de los microservicios de los que depende este microservicio
    # Como ejemplo tomamos como referencia la fase de nombre PRUEBAS
    url = "http://localhost:5516/api/v1/phases/byTitle?phaseTitle={0}&releaseId={1}".format(phaseName, id_dep)
    req = urllib2.Request(url)
    req.add_header("Authorization", "Basic %s" % base64string)
    req.add_header('Content-Type','application/json')
    response = urllib2.urlopen(req)
    data = json.load(response)
    # Ahora debemos obtener el ID de la fase
    id_phase = data[0]["id"]
    id_phases = id_phases + [id_phase]
    print("ID phase = {0}".format(id_phase))

listIdsDependentPhases = id_phases