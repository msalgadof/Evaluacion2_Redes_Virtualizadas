# ⚔️ Elden Ring Stats CLI

## 👤 Stakeholder

Un jugador o fanático profesional de Elden Ring que necesita consultar estadísticas y datos de armas en tiempo real para optimizar sus builds de combate y tomar decisiones informadas antes de una partida.

## 💡 Propuesta de Valor

Los jugadores de Elden Ring pierden tiempo buscando datos de equipamiento en múltiples sitios web. Esta herramienta resuelve ese problema conectándose directamente a la API de Elden Ring y mostrando en segundos la información de un arma desde la terminal, sin necesidad de abrir un navegador.

---

Proyecto desarrollado para la **Evaluación 2 — DRY7122** (DuocUC).

Programa en Python que se conecta a la API pública de Elden Ring para realizar una consulta puntual, empaquetado con Docker y desplegado automáticamente con Jenkins.

---

## 📌 ¿Qué hace el programa?

* Busca un arma por su nombre usando la API REST de Elden Ring.
* Extrae y muestra 3 campos de datos: nombre, descripción oficial y daño físico base.
* Maneja 4 tipos de errores: `404` (No encontrado), `ConnectionError` (Conexión), `Timeout` y código HTTP inesperado.

---

## 🛠️ Tecnologías usadas

| Herramienta | Uso |
| :--- | :--- |
| Python 3.11 | Lenguaje principal |
| requests | Llamadas HTTP a la API |
| Docker | Empaquetado del programa |
| Jenkins | Despliegue automático |
| GitHub | Control de versiones |

---

## ⚙️ Guía de Configuración (Variables de Entorno)

El script utiliza la siguiente variable de entorno gestionada a través de la librería `os` para evitar configuraciones rígidas en el código fuente:
* `ELDEN_BUSQUEDA`: Define el nombre del ítem a consultar en la API (Por defecto: `Uchigatana` si no se declara en el sistema).

---

## ▶️ Guía de Instalación e Instrucciones de Ejecución Local

### Opción 1 — Con Python directo

```bash
# 1. Clonar el repositorio
git clone [https://github.com/msalgadof/Evaluacion2_Redes_Virtualizadas.git](https://github.com/msalgadof/Evaluacion2_Redes_Virtualizadas.git)
cd Evaluacion2_Redes_Virtualizadas

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar
python app.py

```
### Opción 2 — Con Docker

```bash 
# 1. Dar permisos de ejecución al script de automatización

chmod +x build.sh 

# 2. Ejecutar el ciclo completo (Limpia contenedores antiguos, construye y corre) 

./build.sh

```

## 🔑 API Key

* Este proyecto utiliza la API pública y abierta de Elden Ring, por lo que **no requiere una API Key** obligatoria para realizar las consultas puntuales. El script lee el entorno mediante la librería `os` para asegurar que el código fuente quede libre de credenciales expuestas.