from selenium.webdriver.common.by import By


class BasePageLocators:
    SEARCH = (By.CSS_SELECTOR, ".gLFyf.gsfi")
    BUTTON = (By.CSS_SELECTOR, ".gNO89b")


class CalculatorPageLocators:
    SIN = (By.CSS_SELECTOR, '#rso > div:nth-child(1) > div > div > div.card-section > div > div > div.SKWP2e > div > table.HOoTuc > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.XRsWPe.MEdqYd.Krlpq')
    EQUALS = (By.CSS_SELECTOR, ".XRsWPe.UUhRt")
    MESSAGE_QUALS = (By.CSS_SELECTOR, "#cwos.qv3Wpe")
    INPUT_MESSAGE = (By.CSS_SELECTOR, ".vUGUtc")
    INPUT_MESSAGE1 = (By.CSS_SELECTOR, ".jlkklc")
    INPUT_ZERO = (By.CSS_SELECTOR, '#rso > div:nth-child(1) > div > div > div.card-section > div > div > div.SKWP2e > div > table.ElumCf > tbody > tr:nth-child(5) > td:nth-child(1) > div > div')
    NUMBER_ONE = (By.CSS_SELECTOR, '#rso > div:nth-child(1) > div > div > div.card-section > div > div > div.SKWP2e > div > table.ElumCf > tbody > tr:nth-child(4) > td:nth-child(1) > div > div')
    NUMBER_TWO = (By.CSS_SELECTOR, '#rso > div:nth-child(1) > div > div > div.card-section > div > div > div.SKWP2e > div > table.ElumCf > tbody > tr:nth-child(4) > td:nth-child(2) > div > div')
    NUMBER_THREE = (By.CSS_SELECTOR, '#rso > div:nth-child(1) > div > div > div.card-section > div > div > div.SKWP2e > div > table.ElumCf > tbody > tr:nth-child(4) > td:nth-child(3) > div > div')
    NUMBER_FOUR = (By.CSS_SELECTOR, '#rso > div:nth-child(1) > div > div > div.card-section > div > div > div.SKWP2e > div > table.ElumCf > tbody > tr:nth-child(3) > td:nth-child(1) > div > div')
    NUMBER_FIVE = (By.CSS_SELECTOR, '#rso > div:nth-child(1) > div > div > div.card-section > div > div > div.SKWP2e > div > table.ElumCf > tbody > tr:nth-child(3) > td:nth-child(2) > div > div')
    NUMBER_SIX = (By.CSS_SELECTOR, '#rso > div:nth-child(1) > div > div > div.card-section > div > div > div.SKWP2e > div > table.ElumCf > tbody > tr:nth-child(3) > td:nth-child(3) > div > div')
    BRACKET1 = (By.CSS_SELECTOR, '#rso > div:nth-child(1) > div > div > div.card-section > div > div > div.SKWP2e > div > table.ElumCf > tbody > tr:nth-child(1) > td:nth-child(1) > div > div')
    BRACKET2 = (By.CSS_SELECTOR, '#rso > div:nth-child(1) > div > div > div.card-section > div > div > div.SKWP2e > div > table.ElumCf > tbody > tr:nth-child(1) > td:nth-child(2) > div > div')
    INPUT_PLUS = (By.CSS_SELECTOR,'#rso > div:nth-child(1) > div > div > div.card-section > div > div > div.SKWP2e > div > table.ElumCf > tbody > tr:nth-child(5) > td:nth-child(4) > div > div')
    INPUT_MINUS = (By.CSS_SELECTOR,'#rso > div:nth-child(1) > div > div > div.card-section > div > div > div.SKWP2e > div > table.ElumCf > tbody > tr:nth-child(4) > td:nth-child(4) > div > div')
    INPUT_DIVIDE = (By.CSS_SELECTOR,'#rso > div:nth-child(1) > div > div > div.card-section > div > div > div.SKWP2e > div > table.ElumCf > tbody > tr:nth-child(2) > td:nth-child(4) > div > div')
    INPUT_MULTIPLY = (By.CSS_SELECTOR,'#rso > div:nth-child(1) > div > div > div.card-section > div > div > div.SKWP2e > div > table.ElumCf > tbody > tr:nth-child(3) > td:nth-child(4) > div > div')

