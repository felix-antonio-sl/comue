# Co-MUE - Copiloto Médico de Urgencias

## Descripción

Co-MUE es una aplicación web diseñada para gestionar pacientes en un entorno de urgencias médicas. Permite crear y gestionar atenciones médicas, procesar texto no estructurado para extraer información de pacientes y ofrece funcionalidades de asistencia con modelos de lenguaje avanzados.

## Características

- Gestión de pacientes y sus atenciones de urgencia.
- Procesamiento de texto no estructurado utilizando modelos de lenguaje.
- Interfaz de usuario intuitiva y responsiva con Bootstrap.
- Modularidad y escalabilidad siguiendo las mejores prácticas de Flask.

## Instalación

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/felix-antonio-sl/co_mue.git
   cd co_mue
   ```

2. **Crear y activar un entorno virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar las dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar las variables de entorno**

   Crea un archivo `.env` en la raíz del proyecto y añade tus claves y configuraciones:

   ```
   SECRET_KEY=tu_clave_secreta
   OPENAI_API_KEY=tu_clave_openai
   ANTHROPIC_API_KEY=tu_clave_anthropic
   DATABASE_URL=sqlite:///co_mue.db
   ```

5. **Inicializar la base de datos**

   ```bash
   python manage.py db init
   python manage.py db migrate -m "Inicializar base de datos"
   python manage.py db upgrade
   ```

## Contribución

Las contribuciones son bienvenidas. Por favor, crea un fork del repositorio, realiza tus cambios y envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT.
