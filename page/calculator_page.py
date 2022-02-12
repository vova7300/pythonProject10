from .base_page import BasePage
from .locators import CalculatorPageLocators


class CalculatorPage(BasePage):
    def result_sin(self, message1, message2):
        button_sin = self.browser.find_element(*CalculatorPageLocators.SIN)
        button_sin.click()
        self.button_equals()
        self.input_message(message1)
        self.equals_message(message2)

    def division_by_zero(self, message1, message2):
        self.input_number_six()
        self.input_divide()
        self.input_zero()
        self.button_equals()
        self.input_message(message1)
        self.equals_message(message2)

    def expression_result(self, message1, message2):
        self.bracket1()
        self.input_number_one()
        self.input_plus()
        self.input_number_two()
        self.bracket2()
        self.input_multiply()
        self.input_number_three()
        self.input_minus()
        self.input_number_four()
        self.input_zero()
        self.input_divide()
        self.input_number_five()
        self.button_equals()
        self.input_message(message1)
        self.equals_message(message2)

    def button_equals(self):
        button_equals = self.browser.find_element(*CalculatorPageLocators.EQUALS)
        button_equals.click()

    def equals_message(self, message2):
        message = self.browser.find_elements(*CalculatorPageLocators.MESSAGE_QUALS)[0].text
        assert message == message2, "Неверный результат"

    def input_message(self, message1):
        message = self.browser.find_elements(*CalculatorPageLocators.INPUT_MESSAGE)[0].text
        assert message == message1, "Неверный ввод"

    def input_message1(self, message1):
        input1 = self.browser.find_element(*CalculatorPageLocators.INPUT_MESSAGE1)
        input1.send_keys(message1)

    def input_zero(self):
        button = self.browser.find_element(*CalculatorPageLocators.INPUT_ZERO)
        button.click()

    def input_number_one(self):
        button = self.browser.find_element(*CalculatorPageLocators.NUMBER_ONE)
        button.click()

    def input_number_two(self):
        button = self.browser.find_element(*CalculatorPageLocators.NUMBER_TWO)
        button.click()

    def input_number_three(self):
        button = self.browser.find_element(*CalculatorPageLocators.NUMBER_THREE)
        button.click()

    def input_number_four(self):
        button = self.browser.find_element(*CalculatorPageLocators.NUMBER_FOUR)
        button.click()

    def input_number_five(self):
        button = self.browser.find_element(*CalculatorPageLocators.NUMBER_FIVE)
        button.click()

    def input_number_six(self):
        button = self.browser.find_element(*CalculatorPageLocators.NUMBER_SIX)
        button.click()

    def bracket1(self):
        button = self.browser.find_element(*CalculatorPageLocators.BRACKET1)
        button.click()

    def bracket2(self):
        button = self.browser.find_element(*CalculatorPageLocators.BRACKET2)
        button.click()

    def input_plus(self):
        button = self.browser.find_element(*CalculatorPageLocators.INPUT_PLUS)
        button.click()

    def input_minus(self):
        button = self.browser.find_element(*CalculatorPageLocators.INPUT_MINUS)
        button.click()

    def input_divide(self):
        button = self.browser.find_element(*CalculatorPageLocators.INPUT_DIVIDE)
        button.click()

    def input_multiply(self):
        button = self.browser.find_element(*CalculatorPageLocators.INPUT_MULTIPLY)
        button.click()

