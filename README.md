<h1 align="center">Prueba técnica Middle DevOps</h1>

> [!NOTE]
> Se crea éste repositorio con el fin de almacenar el código fuente necesario para ejecutar las pruebas requeridas.

#### La prueba consta de dos partes principales: la creación del pipeline y la creación de la infraestructura.

### 1. Creación del Pipeline:
> Para éste caso en particular se hace uso de la plataforma Azure DevOps.

Se requiere configurar un pipeline CI/CD que clone un repositorio de GitHub, compile una aplicación simple y ejecute la siguiente lista de pruebas:

  - [Clonar repositorio GitHub](#clon-repo-github)
  - [Compilar una aplicación simple](#compile-simple-app)
  - [Ejecutar pruebas unitarias](#unit-test)
  - [Ejecutar análisis de código estático](#static-code-analysis)
  - [Ejecutar análisis de vulnerabilidades](#security-analysis)
  - [Construcción de imagen Docker y envío a un registro](#docker-image-acr)

### 2. Creación de la Infraestructura (IaC):
> Para la creación de la infraestructura se hace uso del servicio de CloudFormation de AWS.

Se requiere establecer e implementar una estrategia de IaC para la aplicación implementada en el apartado anterior.




<div align="center">
  <i>Una opinión constructiva es valiosa donde se te escucha. [JhonG](https://www.linkedin.com/in/jhongrisales/)</i>
</div>



