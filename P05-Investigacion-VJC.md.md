# Proyecto 5: Incident on Linux Server I - Investigación

En esta sección, nos embarcaremos en una búsqueda exhaustiva de evidencia digital que arroje luz sobre el incidente de seguridad. A través del análisis de las adquisiciones aportadas por el cliente intentaremos responder a las siguientes preguntas:

1. Identificar la vulnerabilidad en la aplicación web que fue explotada por el atacante.

2. Determinar la IP, el cliente y el sistema operativo utilizado por el atacante durante el ataque.

   Como podemos ver en el contenido del archivo `access.log` en el directorio `/var/log/apache2`, los datos del ataque son los siguientes:

   ![Attack.png](/img/attackLogs.png)

   - IP: 192.168.1.28
   - Cliente: Mozilla/5.0
   - OS: Linux x86_64

3. Descubrir qué datos fueron exfiltrados del servidor comprometido.

4. Analizar por qué el archivo original no muestra actividad durante el incidente.

5. Proponer soluciones para reparar la vulnerabilidad explotada.
