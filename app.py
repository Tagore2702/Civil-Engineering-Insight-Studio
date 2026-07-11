import os
from pathlib import Path
import runpy

project_dir = Path(__file__).parent / "project_demonstration"
os.chdir(project_dir)
runpy.run_path(project_dir / "app.py", run_name="__main__")
