@echo off
echo ========================================================
echo Setting up Virtual Environment for Personal Finance Analysis
echo ========================================================

REM Step 1: Check Python installation
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed or not added to PATH.
    echo Please install Python 3.10+ and try again.
    pause
    exit /b 1
)

echo [INFO] Python detected successfully.

REM Step 2: Create virtual environment if it does not exist
if not exist "venv" (
    echo [INFO] Creating virtual environment 'venv'...
    python -m venv venv
) else (
    echo [INFO] Virtual environment 'venv' already exists.
)

REM Step 3: Activate virtual environment and install dependencies
echo [INFO] Activating virtual environment and upgrading pip...
call venv\Scripts\activate.bat

python -m pip install --upgrade pip

if exist "requirements.txt" (
    echo [INFO] Installing dependencies from requirements.txt...
    pip install -r requirements.txt
) else (
    echo [INFO] Installing required packages...
    pip install pandas numpy matplotlib seaborn plotly jupyter ipykernel nbformat
)

REM Step 4: Register Jupyter kernel
echo [INFO] Registering Jupyter Notebook kernel 'Python (Finance Analysis)'...
python -m ipykernel install --user --name finance-analysis --display-name "Python (Finance Analysis)"

echo ========================================================
echo Setup completed successfully!
echo You can now run run_notebook.bat to start Jupyter Notebook.
echo ========================================================
pause
