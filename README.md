# 🐍 Proyectos con Entornos Virtuales – Proyecto 1 y Proyecto 2

## 📘 Descripción General

Este repositorio contiene dos proyectos de Python creados con entornos virtuales independientes. Cada proyecto demuestra la creación, activación y uso de entornos virtuales, así como la instalación y ejecución de paquetes específicos (`jupyter` y `pandas`).

## ⚙️ Versión de Python Utilizada

**Python 3.11.2**

## 📂 Estructura del Repositorio

```
PROYECTOS_PYTHON/
│
├─ proyecto1/
│  ├─ v_proyecto1/          ← No se sube al repositorio
│  ├─ img/                  ← Evidencias (capturas)
│  ├─ .gitignore
│  ├─ proyecto1.py
│  ├─ proyecto1.ipynb
│  ├─ requirements.txt
│  └─ readme.md
│
└─ proyecto2/
   ├─ v_proyecto2/          ← No se sube al repositorio
   ├─ .gitignore
   ├─ proyecto2.py
   ├─ proyecto2_1.py
   └─ requirements.txt
```

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
```

#### 2️⃣ Activar el entorno virtual

**Windows (CMD o PowerShell):**
```bash
v_proyecto1\Scripts\activate
```

**Linux/MacOS:**
```bash
source v_proyecto1/bin/activate
```

#### 3️⃣ Instalar los paquetes

```bash
pip install jupyter
```

#### 4️⃣ Generar el archivo requirements.txt

```bash
pip freeze > requirements.txt
```

#### 5️⃣ Ejecutar el script o notebook

```bash
python proyecto1.py
jupyter notebook proyecto1.ipynb
```

---

## 📊 Proyecto 2

- **Carpeta:** `proyecto2`
- **Entorno virtual:** `v_proyecto2`
- **Paquete instalado:** `pandas`

### Archivos incluidos

- `proyecto2.py` → Script que realiza un procesamiento simple o cálculo.
- `proyecto2_1.py` → Segundo script con otra operación o algoritmo.
- `requirements.txt` → Lista de paquetes instalados.
- `.gitignore` → Archivo para excluir el entorno virtual.

### 📘 Ejecución del Proyecto 2

#### 1️⃣ Crear el entorno virtual

```bash
python -m venv v_proyecto2
```

#### 2️⃣ Activar el entorno virtual

**Windows (CMD o PowerShell):**
```bash
v_proyecto2\Scripts\activate
```

**Linux/MacOS:**
```bash
source v_proyecto2/bin/activate
```

#### 3️⃣ Instalar los paquetes

```bash
pip install pandas
```

#### 4️⃣ Generar el archivo requirements.txt

```bash
pip freeze > requirements.txt
```

#### 5️⃣ Ejecutar los scripts

```bash
python proyecto2.py
python proyecto2_1.py
```

---

## 🚫 Archivos y Carpetas Ignorados

Los entornos virtuales no deben subirse al repositorio. Cada proyecto incluye su propio `.gitignore` con las siguientes líneas para excluir sus respectivos directorios de entorno:

```
v_proyecto1/
v_proyecto2/
```

---

## 🧠 Recomendaciones Generales

- Ejecutar cada proyecto desde su carpeta correspondiente.
- Asegurarse de activar el entorno virtual antes de instalar o ejecutar paquetes.
- No modificar manualmente los archivos `requirements.txt`; deben generarse con `pip freeze`.

---

## 🖼️ Evidencias (Capturas Requeridas)

Guarda tus imágenes dentro de la carpeta `proyecto1/img` o insértalas directamente aquí.

- ✅ Creación de los entornos virtuales (`v_proyecto1` y `v_proyecto2`)
- ✅ Activación de los entornos
- ✅ Instalación de los paquetes (`jupyter` y `pandas`)
- ✅ Ejecución de los scripts y notebooks
- ✅ Contenido de los `requirements.txt`
- ✅ Vista de la estructura del proyecto en Visual Studio Code o terminal

### Ejemplo de inserción de imágenes:

```markdown
![Creación del entorno virtual](img/creacion_entorno.png)
![Activación del entorno](img/activacion_entorno.png)
![Instalación de paquetes](img/instalacion_paquetes.png)
```

---

## 📝 Notas Finales

Este proyecto es ideal para aprender sobre:
- Gestión de entornos virtuales en Python
- Aislamiento de dependencias por proyecto
- Buenas prácticas con `.gitignore` y `requirements.txt`
- Uso básico de Jupyter Notebooks y pandas

**¡Feliz codificación! 🚀**