# 🐍 Proyectos con Entornos Virtuales – Proyecto 1 y Proyecto 2

## 📘 Descripción General
Este repositorio contiene dos proyectos de Python creados con entornos virtuales independientes.  
Cada proyecto demuestra la creación, activación y uso de entornos virtuales, así como la instalación y ejecución de paquetes específicos (`jupyter` y `pandas`).

---

## ⚙️ Versión de Python Utilizada
**Python 3.11.2**

---

## 📂 Estructura del Repositorio
PROYECTOS_PYTHON/
│
├─ proyecto1/
│ ├─ v_proyecto1/ ← No se sube al repositorio
│ ├─ img/ ← Evidencias (capturas)
│ ├─ .gitignore
│ ├─ proyecto1.py
│ ├─ proyecto1.ipynb
│ ├─ requirements.txt
│ └─ readmi.md
│
└─ proyecto2/
├─ v_proyecto2/ ← No se sube al repositorio
├─ .gitignore
├─ proyecto2.py
├─ proyecto2_1.py
└─ requirements.txt

markdown
Copiar código

---

## 🧩 Proyecto 1

- **Carpeta:** `proyecto1`  
- **Entorno virtual:** `v_proyecto1`  
- **Paquete instalado:** `jupyter`

### Archivos incluidos
- `proyecto1.py` → Script que ejecuta un algoritmo en Python.  
- `proyecto1.ipynb` → Notebook con demostración o análisis.  
- `requirements.txt` → Lista de paquetes instalados.  
- `.gitignore` → Archivo para excluir el entorno virtual.  

### 📘 Ejecución del Proyecto 1

#### 1️⃣ Crear el entorno virtual
```bash
python -m venv v_proyecto1
2️⃣ Activar el entorno virtual
Windows (CMD o PowerShell):

bash
Copiar código
v_proyecto1\Scripts\activate
Linux/MacOS:

bash
Copiar código
source v_proyecto1/bin/activate
3️⃣ Instalar los paquetes
bash
Copiar código
pip install jupyter
4️⃣ Generar el archivo requirements.txt
bash
Copiar código
pip freeze > requirements.txt
5️⃣ Ejecutar el script o notebook
bash
Copiar código
python proyecto1.py
jupyter notebook proyecto1.ipynb
📊 Proyecto 2
Carpeta: proyecto2

Entorno virtual: v_proyecto2

Paquete instalado: pandas

Archivos incluidos
proyecto2.py → Script que realiza un procesamiento simple o cálculo.

proyecto2_1.py → Segundo script con otra operación o algoritmo.

requirements.txt → Lista de paquetes instalados.

.gitignore → Archivo para excluir el entorno virtual.

📘 Ejecución del Proyecto 2
1️⃣ Crear el entorno virtual
bash
Copiar código
python -m venv v_proyecto2
2️⃣ Activar el entorno virtual
Windows (CMD o PowerShell):

bash
Copiar código
v_proyecto2\Scripts\activate
Linux/MacOS:

bash
Copiar código
source v_proyecto2/bin/activate
3️⃣ Instalar los paquetes
bash
Copiar código
pip install pandas
4️⃣ Generar el archivo requirements.txt
bash
Copiar código
pip freeze > requirements.txt
5️⃣ Ejecutar los scripts
bash
Copiar código
python proyecto2.py
python proyecto2_1.py
🚫 Archivos y Carpetas Ignorados
Los entornos virtuales no deben subirse al repositorio.
Cada proyecto incluye su propio .gitignore con las siguientes líneas:

bash
Copiar código
v_proyecto1/
v_proyecto2/