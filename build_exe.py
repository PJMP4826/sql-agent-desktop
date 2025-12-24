import os
import shutil
import subprocess

def clean_build():
    folders = ['build']
    for folder in folders:
        if os.path.exists(folder):
            print(f"--- Eliminando {folder}... ---")
            shutil.rmtree(folder)
    
    spec_file = "run.spec"
    if os.path.exists(spec_file):
        os.remove(spec_file)

def run_compilation():
    """ejecuta el comando de PyInstaller con todas las dependencias de Qdrant y Tiktoken."""
    command = [
        "pipenv", "run", "pyinstaller", "--onefile",
        "--collect-all", "uvicorn",
        "--collect-all", "qdrant_client",
        "--collect-all", "tiktoken",
        "--collect-data", "llama_index.core",
        "--hidden-import", "tiktoken_ext.openai_public",
        "--hidden-import", "pyodbc",
        "--hidden-import", "sqlalchemy.dialects.mssql",
        "--hidden-import", "sqlalchemy.dialects.mssql.pyodbc",
        "--collect-submodules", "pyodbc",
        "--collect-all", "pyodbc",
        "--hidden-import", "tiktoken_ext",
        "--add-data", "books;books",
        "--add-data", ".env;.",
        "--add-data", "main.py;.",
        "--add-data", "tiktoken_cache;tiktoken_cache",
        "--add-data", "index.html;.",
        "run.py"
    ]
    
    print("--- Iniciando compilacion con PyInstaller... ---")
    try:
        subprocess.run(command, check=True)
        print("\n--- ¡Compilacion exitosa! ---")
    except subprocess.CalledProcessError as e:
        print(f"\n--- ERROR en la compilacion: {e} ---")

if __name__ == "__main__":
    run_compilation()
    clean_build()
    if os.path.exists('build'): shutil.rmtree('build')
    spec_file = "run.spec"
    if os.path.exists(spec_file):
        os.remove(spec_file)