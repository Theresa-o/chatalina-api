# Chatalina

This project is a Django chat application using channels and WebSockets for real-time communication.

## Run Locally
### Prerequisites

Make sure you have the following installed:

- [Python](https://www.python.org/) (version 3.9 or later)
- [Virtualenv](https://virtualenv.pypa.io/) (recommended)

Clone the project

```bash
     git clone https://github.com/Theresa-o/chatalina-api.git
```

Go to the project directory

```bash
  cd chatalina
```

Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv venv  

# Activate on Linux/Mac
source venv/bin/activate  

# or
# Activate on Windows
.\venv\Scripts\activate  
```


### Install dependencies:

```bash
  pip install -r requirements.txt
```


### Database Migration

```bash
   python manage.py migrate
```

### Run the Application
Start the development server:

```bash
   python manage.py runserver
```

The application will be accessible at http://127.0.0.1:8000/.
````



