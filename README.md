# Aplicación gráfica de CRUD creada en python

![image](https://github.com/ezerosello/crud-python/assets/115735657/a30dbea4-5e7e-41af-9b58-7f4c4fb5472d)

- Botón "Create Database": crea la BBDD donde se almacenarán los usuarios registrados
- Botón "Create": crea un nuevo usuario con los datos ingresados en los campos "Nombre", "Apellido", "Email" y "Password"
- Botón "Read": busca en la BBDD algún usuario registrado con la dirección de correo electrónico que ingresemos en el campo "Búsqueda por email"
- Botón "Update": actualiza los datos del usuario encontrado con el método Read, asignandole la información que ingresemos en los campos "Nombre", "Apellido", "Email" y "Password"
- Botón "Delete": borra el usuario encontrado con el método Read
- Botón "Borrar Campos": borra los datos que hayamos ingresado en los campos

Para crear la aplicación utilicé las librerias Tkinter y email_validator, además de mysql.connector para conectar con la base de datos MySQL
