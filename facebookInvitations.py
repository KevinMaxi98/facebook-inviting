# !!!!Importante debido a que no tengo una cuenta de facebook business las pruebas pude realizar solamente con pocas
# reacciones Facebook suele mostrar botones para seguir desplegando las reacciones pero como no tengo la referencia
# no puedo programar esa acción Sin embargo el proceso sería similar al mostrado en los comentarios de instagram Para
# los comentarios no he encontrado la manera de acceder al listado de personas que ha comentado, supongo se debe a la
# naturaleza de la cuenta que estuce usando

from selenium import webdriver
import time
import sys

# Getting varaibles
email = sys.argv[1]
password = sys.argv[2]
post_url = sys.argv[3]

# Setting driver and window
chromedriver_location = "./drivers/chromedriver"
driver = webdriver.Chrome(chromedriver_location)
driver.maximize_window()

# URL
driver.get("https://www.facebook.com")

# Autologin
search_field = driver.find_element_by_id("email")
search_field.send_keys(email)
time.sleep(5)
search_field = driver.find_element_by_id("pass")
search_field.send_keys(password)
time.sleep(5)
search_field.submit()

# Go to specific post
time.sleep(5)
driver.get(post_url)

# Getting all reactions
engagement_div = driver.find_element_by_class_name("l9j0dhe7")
like_image = engagement_div.find_element_by_xpath("//img[@role='presentation']//parent::div")
driver.execute_script("arguments[0].click();", like_image)
time.sleep(1)
reactions_div = engagement_div.find_element_by_xpath("//div[@aria-label='Reacciones']")
change_to_all_tab = reactions_div.find_elements_by_xpath("//span[contains(text(), "
                                                         "'Todo')]//parent::span//parent::div//parent::div//parent::div")
driver.execute_script("arguments[0].click();", change_to_all_tab[8])
time.sleep(2)
# Inviting people
invite_buttons = driver.find_elements_by_xpath("//div[@aria-label='Invitar']")
for invite_button in invite_buttons:
    driver.execute_script("arguments[0].click();", invite_button)


