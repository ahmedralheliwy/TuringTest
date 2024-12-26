# 🤖 reCAPTCHA Turing Test

A modern Django application implementing Google reCAPTCHA v2 for form validation and bot prevention.

## ✨ Features

- 🔒 Secure form submission with Google reCAPTCHA v2
- 📱 Responsive design for all devices
- 🎯 Clean and modern UI
- ⚡ Fast and lightweight
- 🌐 Cross-browser compatibility

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- Django 5.1+
- Google reCAPTCHA site and secret keys

### 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/ahmedralheliwy/TuringTest.git
cd recaptcha-turing-test
```

2. Create and activate virtual environment:
```bash
python -m venv .venv_Turing
source .venv_Turing/bin/activate  # On Windows use: .venv_Turing\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🛠️ Configuration

Add your reCAPTCHA keys to your Django settings:

```python
RECAPTCHA_PUBLIC_KEY = 'your_site_key'
RECAPTCHA_PRIVATE_KEY = 'your_secret_key'
```
**Or add your reCAPTCHA keys to your Django config:**
```
Edit config_py file with your reCAPTCHA and change _ to .
```

## 📦 Project Structure

```
TuringTest/
├── manage.py
├── TuringTest/
│   ├── __init__.py
│   ├── settings.py
│   ├── config.py
│   ├── urls.py
│   └── wsgi.py
└── reCAPTCHA/
    ├── __init__.py
    ├── forms.py
    ├── views.py
    ├── models.py
    └── templates/
        └── form.html
```

## 🚦 Usage

1. Start the development server:
```bash
python manage.py runserver
```

2. Visit `http://127.0.0.1:8000` in your browser
3. Fill out the form and verify you're human!


## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details.

## 👥 Authors

- Ahmed Ramadan Alheliwy - [GitHub Profile](https://github.com/ahmedralheliwy)

## 🙏 Acknowledgments

- Google reCAPTCHA team
- Django community
- All contributors

## 📮 Contact

- Email: ahmed.alheliwy0.99@gmail.com
- Project Link: https://github.com/ahmedralheliwy/TuringTest
