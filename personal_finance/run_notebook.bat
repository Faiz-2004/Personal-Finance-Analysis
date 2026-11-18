@echo off
echo ========================================================
echo Launching Jupyter Notebook with Finance Analysis Kernel
echo ========================================================

if not exist "venv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment 'venv' not found.
    echo Please run setup_venv.bat first to set up the environment.
    pause
    exit /b 1
)

call venv\Scripts\activate.bat
echo [INFO] Starting Jupyter Notebook in Notebooks folder...
cd Notebooks
jupyter notebook Personal_Finance_Analysis.ipynb
pause
