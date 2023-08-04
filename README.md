<div align="center">

# :smiley: PROYECTO FINAL CODERHOUSE PYTHON - SITIO DE VENTA DE ARTE

</div>

<div align="center">

FALTA INGRESAR UN VIDEO CORTO ACA

</div>

# Indice

- [About the Project](:rocket:about-the-project)
- [About Me](#rocketabout-me)
- [External Resources Dependencies & Editors](#linkexternal-resources-dependencies-and-editors)
- [Authors](#authors)

## :rocket:About the project

Se trabaja un sitio falso de compraventa de arte de todo tipo. De acuerdo a los privilegios del visitante, las funcionalidades permitidas tanto para la edicion, como para la navegacion dentro del mismo. A saber:

- Usuario sin registro: Permite el acceso a la pagina principal, sign in, login, about, gallery (sin listados, solo al main).
- Usuario registado: Adicionalmente a los privilegios del usuario sin registro, permite navegar en la galeria, ver detalles de item, ver y editar el propio perfil e ingresar al sector de
  Realizado en Python y Django. Permite navegar entre diferentes pestañas, teniendo cada una un formulario de carga, y un buscador de las mismas en la base de datos que arroja los resultados.
  Se accede desde la direccion raiz al index.html de la app.
  Están en existencias las páginas de index(Home), students, courses y teachers.
  Cada pagina contiene sus propios formularios para agregar a la base de datos, y su propio boton de busqueda. Se encuentran señalizados con ayuda visual con qué completar los campos.

<div align="center">

## Pasos para correr la aplicacion

</div>

Es necesario instalar determinados programas y dependencias:

- Python: Desde Microsoft Store (ultima version)

- Bootstrap (estan copiadas manualmente las carpetas necesarias en el proyecto por lo que no es necesario realizar la instalacion)

- Django(en consola)

```bash
pip install django
```

- Pillow (libreria de python para trabajar sobre imagenes)

```bash
pip install pillow
```

- Lanzar aplicacion, desde carpeta raiz, en consola

```bash
python manage.py runserver
```

<div align="center">

## Notas

</div>

Los forms deben cargarse integramente o no permite el envío del mismo.

El buscador arroja mensajes de error dependiendo

- Si no ingresa valor.
- Si el valor es inexistente en la base de datos.
- Si existe el valor buscado.

Se implementan animaciones, transiciones, estilos de bootstrap y pequeña lógica de Javascript para correrlas.
Se realizan modelos y forms traidos de las clases, y se incorpora funcionalidad de agregar imagen en los mismos.

### :link:External Resources Dependencies and Editors

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![SASS](https://img.shields.io/badge/SASS-hotpink.svg?style=for-the-badge&logo=SASS&logoColor=white)

### :rocket:About Me

Estudiante de carrera de FullStack Developer (React, Angular) y Python en CoderHouse, emprendedor y trabajador. De Buenos Aires, Argentina. Adquiriendo conocimientos con ansias de incursionar en el mundo IT.

### Authors

- [@Julian_Stradolini](https://github.com/Julesarg)
