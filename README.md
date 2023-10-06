# Employee of The Month

Employee of The Month backend repo.

The backend will utilise Python's Django and FastAPI as per project's requirements.

Yes. This is redundant, yet this project shows how two well-known frameworks' best features are brought out.

To keep the code modular, two ORMs are used in this project. SQLAlchemy for FastAPI, which handles the RU operations, and Django ORM which handles the CD operations.

This ultimately means that each framework can work independently if the respective missing operations are added.

## 1.0 Installation

1.1 Clone the repo
```bash
git clone https://github.com/ZeroInverted/EOTM_backend.git
```

1.2 Create a virtual environment (optional)

1.3 Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements file.

```bash
pip install -r requirements.txt
```

## 2.0 Usage

2.1 Run Django server replace <port> with any number of your choosing, other than 5555 or any taken port.
```bash
python manage.py runserver <port>

e.g.,
python manage.py runserver 7777
```
2.2 Run FastAPI server.
```bash
cd api
python fastapi_main
```

## 3.0 API Usage, Architecture
```
Visit <hostname>:<port>/docs for examples on how to use the APIs. 
```
Where hostname is the host that the FastAPI server is listening on, and its port.

e.g.,
localhost:5555/docs for default settings.

Also check the Postman collection for examples on how to send valid requests.

## License

[MIT](https://choosealicense.com/licenses/mit/)
