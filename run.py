# run.py

import subprocess
import os

if __name__ == "__main__":
    path_to_app = os.path.join("app", "streamlit_ui.py")
    subprocess.run(["streamlit", "run", path_to_app])
