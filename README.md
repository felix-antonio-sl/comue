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
   source venv/bin/activate
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

## Despliegue en Producción con Gunicorn y Nginx

### Configuración de Gunicorn

1. **Instalar Gunicorn** en el entorno virtual:

   ```bash
   pip install gunicorn
   ```

2. **Crear archivo de servicio para Gunicorn** en `/etc/systemd/system/comue.service` para gestionar Gunicorn con `systemd`:

   ```ini
   [Unit]
   Description=Gunicorn instance to serve comue
   After=network.target

   [Service]
   User=fx
   Group=www-data
   WorkingDirectory=/home/fx/fx0/fxdev/comue
   Environment="PATH=/home/fx/fx0/fxdev/comue/venv/bin"
   ExecStart=/home/fx/fx0/fxdev/comue/venv/bin/gunicorn --workers 5 --bind 127.0.0.1:8000 wsgi:app

   [Install]
   WantedBy=multi-user.target
   ```

3. **Activar y ejecutar el servicio**:

   ```bash
   sudo systemctl enable comue
   sudo systemctl start comue
   sudo systemctl status comue
   ```

### Configuración de Nginx como Proxy Inverso

1. **Crear archivo de configuración para Nginx** en `/etc/nginx/sites-available/comue`:

   ```nginx
   server {
       listen 80;
       server_name static.145.64.78.5.clients.your-server.de;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }

       location /static/ {
           alias /home/fx/fx0/fxdev/comue/app/static/;
           autoindex on;
       }
   }
   ```

2. **Activar la configuración y reiniciar Nginx**:

   ```bash
   sudo ln -s /etc/nginx/sites-available/comue /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

3. **Ajustar permisos de archivos estáticos**:

   ```bash
   sudo chown -R fx:www-data /home/fx/fx0/fxdev/comue/app/static
   sudo chmod -R 755 /home/fx/fx0/fxdev/comue/app/static
   ```

4. **Verificación de Accesibilidad**: Realizar pruebas de acceso a la aplicación y archivos estáticos para confirmar que todo funciona como esperado.

### **Consideraciones Adicionales**

- **Inicio Automático de Servicios**: Gunicorn y Nginx están configurados para iniciarse automáticamente con el sistema.
- **Pruebas y Monitoreo**: Verificar que Gunicorn esté escuchando en el puerto `8000` y que Nginx esté redirigiendo correctamente al puerto `80`.
- **SSL**: Para mayor seguridad, se recomienda configurar certificados SSL en Nginx.

## Contribución

Las contribuciones son bienvenidas. Por favor, crea un fork del repositorio, realiza tus cambios y envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT.