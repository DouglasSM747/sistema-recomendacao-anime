from pywebio.output import *
from pywebio.input import *


def login():
    put_text("Entre Com Suas Crêdenciais")
    login_c = input("Digite seu Login")
    password_c = input("Digite sua Senha", type=PASSWORD)
    return {'login': login_c, 'password': password_c}


def createAccount():
    m_login = input("Digite seu Login Desejavel")
    m_password = input("Digite sua Senha")
    m_password_confirm = input("Digite sua senha novamente")
    if m_password == m_password_confirm:
        return {'login': m_login, 'password': m_password}
