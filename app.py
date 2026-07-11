import os
from pathlib import Path
import runpy

project_dir = Path(__file__).parent / "7. Project Demonstration"
os.chdir(project_dir)
runpy.run_path(project_dir / "app.py", run_name="__main__")
