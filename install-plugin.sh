#!/bin/bash
version_xlr=9.5.0
plugin=$1

display_help() {
    echo
    echo "Debe pasarse como parmetro el nombre del plugin"
    echo
    echo "   nombre del plugin: aar"
    echo "   directorio que debe existir: xlr-aar-plugin"
    echo
}

####################################################
# Verificamos que existe el plugin
####################################################
[ -d /home/jcla/Projects/xlr-plugins/xlr-${plugin}-plugin ] || {
    display_help
    exit 1
}

####################################################
# Borramos el plugin del directorio
####################################################
rm /opt/xebialabs/xl-release-${version_xlr}-server/plugins/__local__/xlr-${plugin}-plugin-1.0.0.jar
rm /opt/xebialabs/plugins/xlr-${plugin}-plugin-1.0.0.jar

####################################################
# Compilamos el plugin
####################################################
cd /home/jcla/Projects/xlr-plugins/xlr-${plugin}-plugin
jar cvf xlr-${plugin}-plugin-1.0.0.jar *

####################################################
# Movemos y copiamos el plugin al directorio plugins
####################################################
mv xlr-${plugin}-plugin-1.0.0.jar /opt/xebialabs/plugins/
cp /opt/xebialabs/plugins/xlr-${plugin}-plugin-1.0.0.jar /opt/xebialabs/xl-release-${version_xlr}-server/plugins/__local__