# Proyecto 5: Incident on Linux Server I - Informe Pericial

**Código**: P05

**Nombre**: Incident on Linux Server I

**Analista forense**: Víctor Jiménez

**Fecha**: 24/03/2025

## Índice

1. [Resumen Ejecutivo](#1-resumen-ejecutivo)
2. [Glosario de términos](#2-glosario-de-términos)
3. [Introducción](#3-introducción)  
   3.1. [Datos del analista](#31-datos-del-analista)  
   3.2. [Antecedentes](#32-antecedentes)  
   3.3. [Objetivos](#33-objetivos)  
   3.4. [Verificación](#34-verificación)
4. [Fuente de información](#4-fuente-de-información)  
   4.1. [Cadena de custodia](#41-cadena-de-custodia)
5. [Análisis](#5-análisis)  
   5.1. [Herramientas](#51-herramientas)  
   5.2. [Metodología](#52-metodología)
6. [Procesos](#6-procesos)  
   6.1. [{PROCESO 1}](#61)  
   6.2. [{PROCESO 2}](#62)
7. [Línea de tiempo](#7-línea-de-tiempo)
8. [Limitaciones](#8-limitaciones)
9. [Conclusión](#9-conclusión)
10. [Anexos](#10-anexos)

## 1. Resumen Ejecutivo

{RESUMEN EJECUTIVO}

## 2. Glosario de términos

{GLOSARIO DE TÉRMINOS}

## 3. Introducción

### 3.1 Datos del analista

El perito forense informático especializado en ciberseguridad en entornos de las tecnologías de la información responsable de la redacción de este informe es Víctor Jiménez Corada. Sus datos son los siguientes:

- Numero de identificación: _011002-A_
- Correo electrónico: <vjimcor955@g.educaand.es>

### 3.2. Antecedentes

En un día de trabajo común, una alarma rompió el silencio en el centro de datos. Vicente, un técnico, recibió una alerta sobre un posible incidente de seguridad: la extracción de datos sensibles desde un servidor a través de una aplicación web aparentemente segura.

Esa aplicación, creada para escanear redes de forma remota, escondía una vulnerabilidad crítica.

### 3.3. Objetivos

El objetivo del análisis forense es seguir el rastro digital dejado por el intruso, asi como identificar su identidad y la motivación que existía detrás del ataque. Esto incluye los siguientes apartados:

- Identificar la vulnerabilidad en la aplicación web que fue explotada por el atacante.
- Determinar la IP, el cliente y el sistema operativo utilizado por el atacante.
- Descubrir qué datos fueron exfiltrados del servidor comprometido.
- Analizar por qué el archivo original no muestra actividad durante el incidente.
- Proponer soluciones para reparar la vulnerabilidad explotada.

### 3.4. Verificación

Como se puede ver en la Figura 1 del anexo adjunto, se ha procedido al cálculo de la imagen de disco del servidor comprometido, la captura de memoria RAM y el perfil de la memoria, coincidiendo estos con los de los hashes proporcionados.

## 4. Fuente de información

Se nos ha proporcionado una imagen de disco del servidor comprometido, una captura de memoria RAM, el perfil de la memoria y un archivo de hashes para verificar la integridad de la imagen del disco.

### 4.1 Cadena de custodia

#### 1. Información del caso

| **Sección**           | **Campo**                            |
| --------------------- | ------------------------------------ |
| Número de Caso        | P05                                  |
| Tipo de Investigación | Análisis Forense                     |
| Fecha de Adquisición  | 13 de marzo de 2025, 08:00           |
| Lugar de Adquisición  | C/ Amiel, s/n – 11012, Cádiz (Cádiz) |

#### 2. Descripción de la evidencia original

| **Sección**                           | **Campo**                                                        |
| ------------------------------------- | ---------------------------------------------------------------- |
| Tipo de Dispositivo                   | Perfil de la Memoria, 337 KB (345.635 bytes)                     |
| Nombre del archivo                    | perfil_memoria.zip                                               |
| Hash SHA-256 de la Evidencia Original | 18b30b973223b8ab233aa1581bccd35bef6c678b29e671b3fe3a7ee5ea24b076 |

| **Sección**                           | **Campo**                                                        |
| ------------------------------------- | ---------------------------------------------------------------- |
| Tipo de Dispositivo                   | Memoria RAM comprimida, 214 MB (224.424.789 bytes)               |
| Nombre del archivo                    | captura_ram.lime.zip                                             |
| Hash SHA-256 de la Evidencia Original | 632d3d95260753029d7c9ade15e0dcab69b8fe7eb08d7001d9f923b22ddf003f |

| **Sección**                           | **Campo**                                                        |
| ------------------------------------- | ---------------------------------------------------------------- |
| Tipo de Dispositivo                   | Memoria RAM, 0,99 GB (1.073.282.112 bytes)                       |
| Nombre del archivo                    | captura_ram.lime                                                 |
| Hash SHA-256 de la Evidencia Original | 0f5d751208b08450e298b8d27f22451dd2ae158dfc1cb80b974f360e9a88ff05 |

| **Sección**                           | **Campo**                                                        |
| ------------------------------------- | ---------------------------------------------------------------- |
| Tipo de Dispositivo                   | Imagen de disco comprimida, 1,54 GB (1.656.779.434 bytes)        |
| Nombre del archivo                    | imagen_disco.dd.zip                                              |
| Hash SHA-256 de la Evidencia Original | b0189203fa682fd086ed3c52a3723ac46ab896a2fb8e4daf49ed6228bc7d3b76 |

| **Sección**                           | **Campo**                                                        |
| ------------------------------------- | ---------------------------------------------------------------- |
| Tipo de Dispositivo                   | Imagen de disco, 8,00 GB (8.589.934.592 bytes)                   |
| Nombre del archivo                    | imagen_disco.dd                                                  |
| Hash SHA-256 de la Evidencia Original | 9f2b2dace6cfebec1b6f956fc231e199c00f39e05d50286b8f284043537d65d9 |

## 5. Análisis

### 5.1. Herramientas

Las herramientas usadas durante las investigación y sus versiones son las siguientes:

- FTKImages 4.2.0.13
- Volatility 2.6.1
- Get-FileHash

### 5.2. Metodología

{METODOLOGÍA APLICADA}

## 6. Procesos

### 6.1. {PROCESO 1}

{INFORMACIÓN DEL PROCESO 1}

### 6.2. {PROCESO 2}

{INFORMACIÓN DEL PROCESO 2}

## 7. Línea de tiempo

{LINEA DE TIEMPO DE LOS HECHOS}

## 8. Limitaciones

{LIMITACIONES ENCONTRADAS DURANTE LA INVESTIGACIÓN}

## 9. Conclusión

{CONCLUSIÓN}

## 10. Anexos

La Declaración de abstención y tacha, el Juramento de promesa, así como las figuras y hallazgos relacionados con el caso, se encuentran recogidos en el siguiente anexo:

[Proyecto 5: Incident on Linux Server I - Anexo](./P05-Anexos_IncidentLinuxServer-VJC.md)

---

Documento redactado por el perito forense informático Víctor Jiménez Corada.

Fdo:

<img src="./img/victorSignWhite.png" width="200">
