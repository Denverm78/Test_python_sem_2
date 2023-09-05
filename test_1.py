import yaml
from module import Site
import time

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
site = Site(testdata['address'])

def test_step1(): # Негативный тест
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys('test')
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys("test")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == "401"


def test_step2():
# Вход с валидными данными
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys("Roman83")
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys("5a45102d64")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    time.sleep(3)
#создание поста
    x_selector3 = """//*[@id="create-btn"]"""
    input1 = site.find_element("xpath", x_selector3)
    input1.click()
    time.sleep(3)
#заполнение обязательных полей
    x_selector4 = """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
    input1 = site.find_element("xpath", x_selector4)
    input1.send_keys("Название 2")
    x_selector5 = """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""
    input2 = site.find_element("xpath", x_selector5)
    input2.send_keys("Описание 2")
    x_selector6 = """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""
    input3 = site.find_element("xpath", x_selector6)
    input3.send_keys("Содержимое 2")
    time.sleep(3)
    
#сохранение поста
    x_selector7 = """//*[@id="create-item"]/div/div/div[7]/div/button/span"""
    input4 = site.find_element("xpath", x_selector7)
    input4.click()
    time.sleep(3)

#проверка наличия схраненного поста
    x_selector_x = """//*[@id="app"]/main/div/div[1]/h1"""
    text_label = site.find_element("xpath", x_selector_x)
    assert text_label.text == 'Название 2'
