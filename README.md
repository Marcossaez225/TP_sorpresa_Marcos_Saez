# Flask App

Una simple aplicación Flask con dos rutas: "home" y "contacto".

## Cómo ejecutar la aplicación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    ```

2. Ve al directorio del proyecto:

    ```bash
    cd tu-repositorio
    ```

3. Construye y ejecuta el contenedor Docker:

    ```bash
    docker-compose up --build
    ```

4. La aplicación estará disponible en:

    - Página de inicio: http://localhost:5000/
    - Página de contacto: http://localhost:5000/contacto

5. Para detener el contenedor, presiona `Ctrl + C` en la terminal y luego ejecuta:

    ```bash
    docker-compose down
    ```
