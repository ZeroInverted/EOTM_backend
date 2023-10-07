from schemas.auth_schema import LoginModel
import requests

def employee_login(login_credentials: LoginModel) -> dict:
    # Hit Django with GET to fetch a csrf token,
    get_csrf = requests.get("http://localhost:7777/login/")
    csrf_token = get_csrf.cookies.get("csrftoken")
    # Use token as cookie and header
    cookies = {"csrftoken": csrf_token}
    headers = {"X-CSRFToken": csrf_token}
    
    response = requests.post("http://localhost:7777/login/", data=login_credentials.model_dump_json(), headers=headers, cookies=cookies)
    return response.json()

def employee_logout() -> dict:
    # Hit Django with GET to fetch a csrf token,
    get_csrf = requests.get("http://localhost:7777/logout/")
    csrf_token = get_csrf.cookies.get("csrftoken")
    # Use token as cookie and header
    cookies = {"csrftoken": csrf_token}
    headers = {"X-CSRFToken": csrf_token}
    
    response = requests.post("http://localhost:7777/logout/", headers=headers, cookies=cookies)
    return response.json()