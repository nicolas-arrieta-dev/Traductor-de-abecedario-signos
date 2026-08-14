# Traductor de Abecedario por Lenguaje de Señas

Sistema de inteligencia artificial capaz de reconocer mediante una cámara las señas manuales correspondientes a las letras del abecedario y mostrar en pantalla la letra identificada.

El proyecto utiliza un modelo de aprendizaje profundo entrenado con imágenes del ASL Alphabet Dataset, utilizando Python, TensorFlow y Google Colab. Posteriormente, el modelo entrenado fue integrado en una aplicación desarrollada en Python para realizar el reconocimiento en tiempo real mediante la cámara.

## Descripción

La comunicación es un aspecto fundamental de la vida humana. Sin embargo, la falta de conocimiento del lenguaje de señas por parte de gran parte de la población puede generar barreras de comunicación con personas sordas.

Este proyecto busca explorar cómo la inteligencia artificial y la visión por computadora pueden utilizarse para reconocer señas manuales y convertirlas en letras del abecedario.

El sistema permite utilizar la cámara del computador para realizar una seña manual y obtener la letra correspondiente mediante el modelo de inteligencia artificial.

## Características

- Reconocimiento de señas manuales mediante cámara.
- Clasificación de letras del abecedario.
- Modelo de inteligencia artificial basado en aprendizaje profundo.
- Procesamiento de imágenes en tiempo real.
- Modelo previamente entrenado e incluido en el proyecto.
- Implementación mediante un único archivo Python.
- Uso de tecnologías de código abierto.

## Tecnologías utilizadas

- Python
- TensorFlow
- OpenCV
- NumPy
- Google Colab
- Jupyter Notebook
- Kaggle

## Estructura del proyecto

```text
Traductor-de-abecedario-signos/
│
├── app.py
├── model_seved/
│   └── modelo_entrenado
└── README.md
```

## app.py

Es el archivo principal de la aplicación.

Al ejecutar este archivo se inicia el sistema de reconocimiento y se activa la cámara del computador. Una vez iniciada la cámara, el usuario puede comenzar a realizar las diferentes señas correspondientes al abecedario frente a ella.

El modelo procesa las imágenes capturadas y realiza una predicción sobre la letra representada.

## model_seved

Esta carpeta contiene el modelo de inteligencia artificial previamente entrenado.

El modelo fue entrenado utilizando el dataset ASL Alphabet disponible en Kaggle.

## Dataset

Para el entrenamiento del modelo se utilizó el siguiente dataset público:

ASL Alphabet Dataset - Kaggle

https://www.kaggle.com/datasets/grassknoted/asl-alphabet

El dataset contiene imágenes correspondientes a diferentes clases del lenguaje de señas americano (ASL), utilizadas para entrenar el modelo de clasificación.

## Entrenamiento del modelo

El modelo fue entrenado utilizando Google Colab.

Durante el proceso se realizaron las siguientes etapas:

1. Configuración del entorno de Google Colab.
2. Descarga y preparación del dataset.
3. Organización de las imágenes.
4. Preprocesamiento de las imágenes.
5. Construcción del modelo de aprendizaje profundo.
6. Entrenamiento del modelo.
7. Evaluación del modelo.
8. Guardado del modelo entrenado.
9. Integración del modelo en la aplicación Python.

El código utilizado durante el proceso de entrenamiento puede consultarse en el siguiente notebook:

https://colab.research.google.com/drive/1ozn2Bj5EQnXGq3FrBizrd7_f1C4XtjNi

## Funcionamiento

```text
┌──────────────────────┐
│       app.py         │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Activar cámara    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Capturar imagen     │
│      de la seña      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      Modelo de IA    │
│       entrenado      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Predicción de letra │
└──────────────────────┘
```

### Flujo de uso

1. Ejecutar `app.py`.
2. La aplicación activa la cámara del computador.
3. Colocar la mano frente a la cámara.
4. Realizar una seña correspondiente a una letra.
5. El modelo analiza la imagen capturada.
6. La aplicación muestra la letra correspondiente a la predicción.
7. Se pueden realizar diferentes señas para probar el reconocimiento.

## Instalación

### Requisitos

- Python 3
- Git
- Una cámara web
- Controladores necesarios para utilizar la cámara

### 1. Clonar el repositorio

```bash
git clone https://github.com/nicolas-arrieta-dev/Traductor-de-abecedario-signos.git
```

Ingresar al proyecto:

```bash
cd Traductor-de-abecedario-signos
```

### 2. Crear un entorno virtual

En Windows:

```bash
python -m venv venv
```

Activar el entorno virtual:

```bash
venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
pip install tensorflow opencv-python numpy
```

### 4. Ejecutar la aplicación

```bash
python app.py
```

Al ejecutar el archivo se abrirá la cámara y el sistema estará listo para comenzar a reconocer las señas.

## Objetivo del proyecto

El objetivo principal es desarrollar un sistema capaz de reconocer señas manuales del abecedario mediante inteligencia artificial y visión por computadora.

El proyecto busca aplicar conocimientos relacionados con:

- Inteligencia artificial.
- Aprendizaje automático.
- Redes neuronales.
- Visión por computadora.
- Procesamiento de imágenes.
- TensorFlow.
- OpenCV.
- Python.

Además, busca explorar el potencial de estas tecnologías para desarrollar herramientas que puedan contribuir a reducir las barreras de comunicación entre personas sordas y oyentes.

## Posibles mejoras

El proyecto puede utilizarse como base para desarrollar funcionalidades más avanzadas, como:

- Reconocimiento de palabras completas.
- Reconocimiento de frases.
- Traducción de conversaciones en lenguaje de señas.
- Mayor cantidad de clases de señas.
- Mejora de la precisión del modelo.
- Reconocimiento de movimientos y gestos.
- Interfaz gráfica más completa.
- Procesamiento y traducción en tiempo real.

## Fuentes

### Dataset

ASL Alphabet - Kaggle

https://www.kaggle.com/datasets/grassknoted/asl-alphabet

### Entrenamiento del modelo

Google Colab

https://colab.research.google.com/drive/1ozn2Bj5EQnXGq3FrBizrd7_f1C4XtjNi

## Conclusión

Este proyecto demuestra cómo la inteligencia artificial y la visión por computadora pueden utilizarse para desarrollar sistemas capaces de interpretar señas manuales.

Mediante Python, TensorFlow, OpenCV y un dataset público de Kaggle, se desarrolló un modelo capaz de reconocer diferentes letras del abecedario a partir de imágenes capturadas mediante una cámara.

El proyecto representa una base para continuar explorando aplicaciones relacionadas con el reconocimiento y traducción del lenguaje de señas.

## En colaboración con 
https://github.com/ingjorgemorales

<img width="736" height="736" alt="image" src="https://github.com/user-attachments/assets/d10482f4-da71-4815-905d-9d6f39da50af" />
<img width="962" height="875" alt="image" src="https://github.com/user-attachments/assets/3d350226-d470-48ad-b89b-eb2c06bf13b3" />
<img width="963" height="875" alt="image" src="https://github.com/user-attachments/assets/8b271c5e-6280-4f34-9627-0286f6601609" />
<img width="947" height="845" alt="image" src="https://github.com/user-attachments/assets/a8bea168-3233-4acb-847a-16d1eea3ec47" />
