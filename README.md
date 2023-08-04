<div align="center">

# :smiley: PROYECTO FINAL CODERHOUSE PYTHON - SITIO DE VENTA DE ARTE

</div>

<div align="center">

FALTA INGRESAR UN VIDEO CORTO ACA

</div>

# Indice

- [About the Project](#rocketabout-the-project)
- [About Me](#rocketabout-me)
- [External Resources Dependencies & Editors](#linkexternal-resources-dependencies-and-editors)

### Authors

- [@Julian_Stradolini](https://github.com/Julesarg)

## :rocket:About the project

Se trabaja un sitio falso de compraventa de arte de todo tipo. De acuerdo a los privilegios del visitante, las funcionalidades permitidas tanto para la edicion, como para la navegacion dentro del mismo. A saber:

- **Usuario sin registro:** Permite el acceso a la pagina principal, sign in, login, about, gallery (sin listados, solo al main).
- **Usuario registado:** Adicionalmente a los privilegios del usuario sin registro, permite navegar en la galeria, buscar algun item por filtro de materiales o crearlo, ver detalles de item, crear ver y editar el propio perfil e ingresar al sector de mensajes(no implementado)
- **Usuario admin:** Tiene todos los privilegios anteriores, y permite editar y borrar items, y acceder al menu de superusuario escondido por defecto en el navbar (no implementado, pero permitiria editar y borrar usuarios tambien)

  <div align="center">

## Notas

</div>

**-La carga de registro debe ser integramente completada**

**-El buscador arroja mensajes de error dependiendo**

- Si no ingresa valor.
- Si el valor es inexistente en la base de datos.
- Si existe el valor buscado.

**-Se implementan animaciones, transiciones, estilos de bootstrap y lógica de Javascript para correrlas.**

**-Se entremezcla Django con Python nativo para metodos, classes y forms.**

**-El sitio es totalmente responsivo para todos los dispositivos.**

**-Todas los hipervinculos tienen conexion entre si. Se modifican las vistas de acuerdo a la condicion del usuario(los 3 tipos comentados)**

**-Se accede desde la direccion raiz.**

**-Las paginas se discriminan en:**

`HOME`

`GALLERY` **/** `paintings` `sculptures` `nfts` `woodcraft` `other` **/** `view` `detail` `edit` `delete`

`ABOUT US`

`MESSAGES`

`ACCOUNT` **/** `login` `register` **or** `signout` `profile` **/** `create` `edit`

<div align="center">

## Pasos para correr el sitio

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

### :link:External Resources Dependencies and Editors

Se utilizan diversidad de recursos de estilo

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![SASS](https://img.shields.io/badge/SASS-hotpink.svg?style=for-the-badge&logo=SASS&logoColor=white)

### :rocket:About Me

Estudiante de carrera de **FullStack Developer** (React, Angular) y Python en CoderHouse, emprendedor y trabajador. De Buenos Aires, Argentina. Adquiriendo conocimientos con ansias de incursionar en el mundo IT.
