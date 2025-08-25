<div align="center">
  <picture>
    <img src="assets/img/logo.png" alt="Logo" width="50%">
  </picture>
</div>

<div align="center">
  <h1>bmi-calculator (flask)</h1>
</div>

A simple and elegant **Body Mass Index (BMI) Calculator**, built with **Flask**, featuring **multilingual support (11 languages)** using Flask-Babel.  
The app allows users to calculate their BMI, view the classification, and switch languages instantly.

---

## Features

- Multilingual support (pt, en, es, fr, de, ru, ar, hi, bn, ur, zh)
- BMI calculation with categorized results
- Clean UI with CSS animations
- Form validation with JavaScript
- Configurable via `.env`
- Unit tests included (Pytest)

---

## Step-by-Step to Installation

##### 1- First clone the repository:
```bash
git clone https://github.com/your-username/bmi-calculator.git
```

##### 2- Enter in the folder
```bash
cd bmi-calculator
```

##### 3- Create a Virtual Environment
```bash
python -m venv venv
```

##### 4- Activate the Venv
```bash
source venv/bin/activate   # On Linux/Mac
```
```bash
venv\Scripts\activate    # On Windows
```

##### 5- To install the requirements (see more detailed on final of this documentation)
Paste this in terminal:
```bash
pip install -r requirements.txt
```

---

## Environment Setup

You can create your own `.env` using the `.env.example` as template or run the script:

```bash
python generate_env.py
```
The `generate_env.py` will create a `.env` file fast for you.

Example `.env`:

```env
SECRET_KEY=your_secret_key

FLASK_ENV=development
FLASK_DEBUG=1

BABEL_DEFAULT_LOCALE=pt
BABEL_SUPPORTED_LOCALES=pt,en,es,fr,de,ru,ar,hi,bn,ur,zh
```

---

## Run the App

Open with Python or put in terminal:
```bash
python run.py
```

And after, access in your browser: [http://127.0.0.1:5000](http://127.0.0.1:5000) or [http://localhost:5000](http://localhost:5000)

---

## Running Tests

Paste in your terminal:
```bash
pytest
```

---

## Project Structure

```
bmi-calculator/
│── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── forms.py
│   ├── utils.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── result.html
│   └── static/
│       ├── css/styles.css
│       └── js/script.js
│── tests/
│── translations/ (PO files)
│── babel.cfg
│── generate_env.py
│── run.py
│── requirements.txt
│── .env.example
│── .env
│── .gitignore
│── LICENSE
│── CONTRIBUTING.md
│── CHANGELOG.md
└── README.md
```

---

## Translations

Translations are managed with **Flask-Babel**.  

To **extract new translatable strings** from the source code and update your `.po` files, run:

```bash
# Extract all translatable strings into messages.pot
pybabel extract -F babel.cfg -o messages.pot .

# Update existing translations with new strings
pybabel update -i messages.pot -d translations
```

After updating translations, remember to compile them:

```bash
pybabel compile -d translations
```

This ensures that any new or modified text in your app is available for translation in all supported languages.

---

## Requirements

Before running the project, make sure you have the following installed:

- **Python 3.11+**  
- **Git** (if cloning from GitHub)  
- **Modern web browser** (Chrome, Firefox, Edge, etc.)

### Python Dependencies
All dependencies are listed in `requirements.txt`.  
Install them with:

```bash
pip install -r requirements.txt
```

### Minimum required packages:

- [Flask](https://flask.palletsprojects.com/)
- [Flask-Babel](https://python-babel.github.io/flask-babel/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/)
- python-dotenv

### Optional (for development)
- pytest → run automated tests

- Babel CLI (pybabel) → manage and compile translations

---

## Notes

![Versão](https://img.shields.io/badge/version-2.0.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Babel](https://img.shields.io/badge/Babel-11_languages-green.svg)


---

## Contributing

Contributions are welcome!

See more in [CONTRIBUTING](CONTRIBUTING.md)

---


## License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

## Author

**Lucas Alcântara**  
GitHub: [@A1cantar4](https://github.com/A1cantar4)