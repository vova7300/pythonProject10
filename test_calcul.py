from .page.base_page import BasePage
from .page.calculator_page import CalculatorPage
import time
import pytest


def test_result_calculator_sin(browser):
    link = "http://google.com"
    page = BasePage(browser, link)
    page.open()
    message1 = "sin() ="
    message2 = "Error"
    search = "калькулятор"
    page.go_to_calculator_page(search)
    calculator_page = CalculatorPage(browser, browser.current_url)
    calculator_page.result_sin(message1, message2)


def test_division_by_zero(browser):
    link = "http://google.com"
    page = BasePage(browser, link)
    page.open()
    message1 = "6 ÷ 0 ="
    message2 = "Infinity"
    search = "калькулятор"
    page.go_to_calculator_page(search)
    calculator_page = CalculatorPage(browser, browser.current_url)
    calculator_page.division_by_zero(message1, message2)


def test_expression_result(browser):
    link = "http://google.com"
    page = BasePage(browser, link)
    page.open()
    message1 = "(1 + 2) × 3 - 40 ÷ 5 ="
    message2 = "1"
    search = "калькулятор"
    page.go_to_calculator_page(search)
    calculator_page = CalculatorPage(browser, browser.current_url)
    calculator_page.expression_result(message1, message2)


    #pytest -s -v test_calcul.py

