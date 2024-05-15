import requests
import os
import base64
import schedule # type: ignore
import time
import pyautogui # type: ignore

def press_space():
    pyautogui.press("space")
    print("Botón de espacio presionado")

def download_latest_release(download_path='.'):
    mirror = "https://elyxdev.github.io/latest"
    pet = requests.get(mirror)
    if pet.status_code == 200:
        data = pet.json()
        url = data.get('url')
        version = url.split("/")[-1]
        pathto = os.path.join(download_path, version)
        with open(pathto, 'wb') as archivo:
            archivo.write(requests.get(url).content)
        return version

def main():
    # Programar la ejecución de press_space() cada 3 horas
    schedule.every(3).hours.do(press_space)

    if not os.path.exists("./.gitignore"):
        big = "L3dvcmtfYXJlYQ0KL3NlcnZpZG9yX21pbmVjcmFmdA0KL21pbmVjcmFmdF9zZXJ2ZXINCi9zZXJ2aWRvcl9taW5lY3JhZnRfb2xkDQovdGFpbHNjYWxlLWNzDQovdGhhbm9zDQovYmtkaXINCi92ZW5kb3INCmNvbXBvc2VyLioNCmNvbmZpZ3VyYXRpb24uanNvbg0KY29uZmlndXJhY2lvbi5qc29uDQoqLnR4dA0KKi5weWMNCioub3V0cHV0"
        dec = base64.standard_b64decode(big).decode()
        with open(".gitignore", 'w') as giti:
            giti.write(dec)
    flnm = download_latest_release()
    if flnm.split(".")[-1] == "pyc":
        os.system(f"python3 {flnm}")
    else:
        os.system(f"chmod +x {flnm} && ./{flnm}")

    # Ejecutar el bucle principal de schedule
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Verificar y configurar DISPLAY
    if "DISPLAY" not in os.environ:
        os.environ["DISPLAY"] = ":99"
    main()



