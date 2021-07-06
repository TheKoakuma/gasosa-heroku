import time
import requests
import os
from selenium import webdriver
op = webdriver.ChromeOptions()
op.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")

driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=op)


def login():
    #sendMessage("Robô em Testes nas próximas 4 mensagens")
    login = os.environ.get("LOGIN_AM4")
    psswd = os.environ.get("PASS_AM4")
    driver.get('https://airline4.net/')
    time.sleep(5)
    driver.find_elements_by_xpath("/html/body/div[3]/div[1]/div[5]/button[1]")[0].click()
    driver.find_elements_by_id("lEmail")[0].send_keys(login)
    driver.find_elements_by_id("lPass")[0].send_keys(psswd)
    driver.find_elements_by_id("btnLogin")[0].click()
    time.sleep(5)
    goAround();

def goAround():
	#print("Atualizando Valores \n")
    getGasosa()
    getCO()
    time.sleep(1800)
    goAround()

def getGasosa():
    driver.get('https://airline4.net/fuel.php')
    rawfuel=driver.execute_script('return document.getElementById("sumCost").innerHTML.replace(",","");')
    #print(rawfuel)
    if int(rawfuel)<=850:
        msg="Corre negada, o Combustível está só $"+rawfuel
        sendMessage(msg)
    return "ok"

def getCO():
    driver.get('https://airline4.net/co2.php')
    rawco2=driver.execute_script('return document.getElementById("sumCost").innerHTML.replace(",","");')
    #print(rawco2)
    if int(rawco2)<=120:
        msg="Salve a natureza, CO2 por apenas $"+rawco2
        sendMessage(msg);
    return "ok"

def sendMessage(message):
    url="https://discord.com/api/webhooks/815741780729397278/bTgA6xl8qq899Dzy3ixZ46qw2z4BYHgm6w8O4HnIHRMQ4DlDgYPM6yDr0rYN2CGp6cs4"
    requests.post(url, json={'content':message})
    return "ok"

login()
