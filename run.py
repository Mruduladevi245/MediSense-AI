import subprocess
import threading
import time


def run_backend():
    subprocess.run(["python", "backend/app.py"])


def run_frontend():
    time.sleep(3)
    subprocess.run(["streamlit", "run", "frontend/app.py"])


if __name__ == "__main__":
    backend = threading.Thread(target=run_backend)
    frontend = threading.Thread(target=run_frontend)

    backend.start()
    frontend.start()

    backend.join()
    frontend.join()