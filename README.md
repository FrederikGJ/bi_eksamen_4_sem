# Business Intelligence Exam 2024

This repository contains the code and documentation for the Business Intelligence Exam 2024.

Group: OLA_Gruppe14

#### Group Members

Frederik Geisler Johannessen

Signe Krusell Larsen

Natasja Karoline Duckfeldt Vitoft Nordstedt

### Technology Stack

![Python](https://img.shields.io/badge/Python-%233776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-%235F8FFF?style=flat-square&logo=streamlit&logoColor=white)

## Introduction

Somethihng with health data and predictive modeling...

We calcualte the mean of our data -

<img src="https://latex.codecogs.com/svg.image?\bar{x}&space;=&space;\frac{1}{n}\sum_{i=1}^{n}x_i" title="\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i" />

```python
mean = sum(data) / len(data)
```

The mean of height data is ???

We calculate the variance of our data -

<img src="https://latex.codecogs.com/svg.image?s^2&space;=&space;\frac{1}{n-1}\sum_{i=1}^{n}(x_i&space;-&space;\bar{x})^2" title="s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2" />

```python
variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
```

The variance of height data is ???

## App environment setup

### Start virtual environment on Mac/Linux, you must be in the terminal inside the project folder (e.g., vscode terminal):

```bash
python3 -m venv env
```

### activate the environment:

```bash
source env/bin/activate
```

### deactivate the environment:

```bash
deactivate
```

### for Windows:

```bash
python -m venv env
```

### start the environment:

```bash
.\env\Scripts\activate
```

### deactivate the environment:

```bash
deactivate
```

### thereafter you write:

```bash
streamlit run app.py
```

### in your terminal - then the app runs in the browser
