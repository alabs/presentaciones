!SLIDE 
# Asterisk para telefonía IP
## El futuro de la telefonía es ahora
->![logo-alabs](logo.png)<-
### 16/08/2011
### Mexico

!SLIDE transition=fade
# Asterisk para telefonía IP
## o cómo dominar el mundo
->![logo-alabs](logo.png)<-
### 16/08/2011
### Mexico

!SLIDE transition=scrollLeft
# Asterisk para telefonía IP

## Hola!
### Antonio Pardo @apardo
### Andrés Pereira

!SLIDE smbullets incremental transition=scrollLeft
# Una revolución telefónica
* Cerrando la brecha entre lo tradicional y la Red
* El proyecto Zapata
* Cambios masivos requieren una tecnología flexible 
* La PBX de los hackers
* La PBX profesional
* La comunidad de Asterisk
* El caso de negocio

!SLIDE smbullets incremental transition=scrollLeft
# Arquitectura de Asterisk
* Módulos
* Estructura de ficheros
* El dialplan
* Hardware
* Versioneado de Asterisk

!SLIDE smbullets incremental transition=scrollLeft
# Instalando Asterisk
* Chuleta de instalación
* Instalación en diferentes distribuciones
* Dependencias de software
* Descarga lo que necesites
* Cómo instalarlo
* Configuración base
* Actualizando Asterisk
* Problemas comunes
* Mejorando Asterisk

!SLIDE smbullets incremental transition=scrollLeft
# Tareas iniciales de configuración
* asterisk.conf
* modules.conf
* indications.conf
* musiconhold.conf

!SLIDE smbullets incremental transition=scrollLeft
# Configuración de dispositivos de usuarios
* Conceptos de telefonía
* Hardphones, Softphones y ATA
* Configurando Asterisk
* Cargando tus nuevas configuraciones de canales
* Asegurarse que tus dispositivos se conectan
* Teléfonos analógicos
* Un dialplan básico para testear tus dispositivos
* Tu primera llamada

!SLIDE smbullets incremental transition=scrollLeft
# Fundamentos del dialplan
* Sintáxis del dialplan
* Un dialplan simple
* Construyendo un dialplan interactivo

!SLIDE smbullets incremental transition=scrollLeft
# Conectividad con el exterior
* Fundamentos del trunking
* Fundamentos del dialplan para conectividad exterior
* Circuitos PSTN
* VoIP
* Llamadas de emergencia

!SLIDE smbullets incremental transition=scrollLeft
# Voicemail
* Comedian Mail
* Integración en el dialplan
* Backends de almacenamiento
* Utilizando Asterisk como un servidor de correo de voz independiente

!SLIDE smbullets incremental transition=scrollLeft
# Internacionalización
* Dispositivos externos al servidor Asterisk
* Conectividad PSTN, DAHDI, tarjetas Digium y teléfonos analógicos
* Asterisk

!SLIDE smbullets incremental transition=scrollLeft
# Dialplan en profundidad
* Expresiones y manipulación de variables
* Funciones del dialplan
* Bifurcación condicional
* Macros
* GoSub()
* Canales locales
* Usando la base de datos Asterisk (AstDB)
* Funciones útiles de Asterisk

!SLIDE smbullets incremental transition=scrollLeft
# Parking and paging
* features.conf
* Overhead and "Underchin" Paging (aka Public Address)

!SLIDE smbullets incremental transition=scrollLeft
# Enrutado de llamadas en Internet
* DNS y SIP URI
* ENUM y E.164
* ISN, ITAD y freenum.org
* Seguridad e identidad

!SLIDE smbullets incremental transition=scrollLeft
# Distribución automática de colas de llamadas
* Creando una cola ACD simple
* Miembros de la cola
* El fichero queues.conf
* El fichero agents.conf
* Colas avanzadas
* Estadísticas de colas, el fichero queue_log

!SLIDE smbullets incremental transition=scrollLeft
# Estado de los dispositivos
* Estados de los dispositivos
* Estado de las extensiones
* Presencia SIP
* Usando estados personalizados de dispositivos
* Estados de dispositivos distribuidos
* Apariencia de líneas compartidas

!SLIDE smbullets incremental transition=scrollLeft
# El contestador automático
* El contestador automático no es un IVR
* Diseñando tu contestador automático
* Contruyendo tu contestador automático

!SLIDE smbullets incremental transition=scrollLeft
# Integración con bases de datos relacionales
* Instalando y configurando PostreSQL y MySQL
* Instalando y configurando ODBC
* Manejando bases de datos
* Una suave introducción a func_odbc
* Usando func_odbc
* Usando tiempo real
* Salvando registros de detalles de llamadas (CDR)
* Voicemail ODBC

!SLIDE smbullets incremental transition=scrollLeft
# IVR
* ¿Qué es un IVR?
* Componentes de un IVR
* Consideraciones al diseñar un IVR
* Módulos de Asterisk para construir IVR
* Un IVR simple usando CURL
* Una aplicación para grabar menus
* Reconocimiento de voz y texto a voz

!SLIDE smbullets incremental transition=scrollLeft
# Servicios externos
* Integración con calendario
* Integración del voicemail con IMAP
* Usando XMPP con Asterisk
* Integración con Skype
* Integración con LDAP
* Utilidades de texto a voz

!SLIDE smbullets incremental transition=scrollLeft
# FAX
* ¿Qué es FAX?
* Maneras de manejar faxes en Asterisk
* spandsp
* Digium FAX para Asterisk
* Manejando FAX entrante
* Manejando FAX saliente
* FAX pass-through

!SLIDE smbullets incremental transition=scrollLeft
# Asterisk Manager Interface
* Comienzo rápido
* Configuracion
* Vistazo del protocolo
* Frameworks de desarrollo
* Aplicaciones interesantes

!SLIDE smbullets incremental transition=scrollLeft
# Asterisk Gateway Interface
* Comienzo rápido
* Variantes de AGI
* Vistazo a la comunicación AGI
* Frameworks de desarrollo

!SLIDE smbullets incremental transition=scrollLeft
# Clustering
* Call centers tradicionales
* Sistemas híbridos
* Asterisk puro, no distribuido
* Asterisk e integración con bases de datos
* Asterisk y el estado de dispositivos distribuido
* Multiples colas, multiples sitios

!SLIDE smbullets incremental transition=scrollLeft
# DUNDi
* ¿Cómo funciona DUNDi?
* El fichero dundi.conf
* Configurando Asterisk para usar DUNDi

!SLIDE smbullets incremental transition=scrollLeft
# Monitorización y logs
* logger.conf
* Registros de detalles de llamadas
* CEL (Channel Event Logging)
* SNMP

!SLIDE smbullets incremental transition=scrollLeft
# Interfaces web
* Flash Operator Panel
* Estado de las colas y reporting
* Registro de detalles de llamadas
* A2Billing

!SLIDE smbullets incremental transition=scrollLeft
# Seguridad
* Escaneando en búsqueda de cuentas válidas
* Debilidades de la autenticación
* Fail2ban
* Media cifrado
* Vulnerabilidades en el dialplan
* Securizando las API de red de Asterisk
* DoS IAX2
* Otras mitigaciones de riesgos
* Recursos

!SLIDE smbullets incremental transition=scrollLeft
# Asterisk, un futuro para la telefonía
* Los problemas con la telefonía tradicional
* Cambio de paradigma
* La promesa de la telefonía Open Source
* El futuro de Asterisk
