# Name Convention Generator

A Streamlit web application that generates a name convention based on user inputs.



## Table of Contents

- [Description](#description)
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Docker](#docker)


## Description

The Name Convention Generator is a web application built using Streamlit that helps users generate a naming convention for various purposes. The naming convention includes components like environment, location, usage type, server function, and a 2-digit ID. This app simplifies the process of creating consistent and standardized names for different elements.

## Features

- Select environment from predefined options.
- Choose location from a dropdown or input a custom location.
- Enter usage type, server function, and a 2-digit ID.
- Generate a naming convention based on the provided inputs.
- Check if the generated name already exists in the audit log.
- Display success or error messages based on inputs and generated name.
- Display helpful information about the naming convention rules.

## Usage

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the app with `streamlit run app.py`.

## Installation

To run the Name Convention Generator on your local machine, follow these steps:

1. Clone the repository:
```bash
git clone pip install -r requirements.txt 
cd name-convention-generator
pip install -r requirements.txt
streamlit run app.py
```

## Docker
```bash
docker build -t name-convention-generator .
docker run -p 8501:8501 name-convention-generator
docker run -it -d --name name_gen_app -p 8501:8501 name-convention-generator
```

