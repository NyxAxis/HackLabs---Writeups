Instalación de HackLabs
Análisis
Scripts
Resultado
Aprendizajes

# OWASP A04 – Insecure Design

Objetivo

Explotar un mecanismo inseguro de recuperación de contraseña basado en preguntas de seguridad sin rate limiting.

----

# Instalación del laboratorio

Instalar Docker en Kali

sudo apt install -y docker.io

# Clonar repositorio

git clone https://github.com/afsh4ck/HackLabs.git

cd HackLabs

----

# Desplegar laboratorio

sudo bash deploy.sh

Al iniciar, el laboratorio asigna una IP local para acceder vía navegador:

http://192.168.28.109/

# Análisis del laboratorio

Se ingresó el usuario:

admin

La aplicación redirigió a un mecanismo de recuperación de contraseña mediante pregunta de seguridad.

# La vulnerabilidad observada fue:
- Preguntas de seguridad en texto plano
- Sin rate limiting
- Respuestas predecibles
- Contraseña expuesta en texto plan
