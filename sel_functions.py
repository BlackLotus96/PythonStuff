import json
class ClassSelenium:
    attributes_json = json.load(x)

  def __init__(self, driver, type_attr, name_attr, wait_time):
    self.driver = driver
    self.type_attr = type_attr
    self.name_attr = name_attr
    self.wait_time = wait_time

  def WaitConditions(self):
    try:
      cookie_accepted = WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((, "onetrust-accept-btn-handler"))
          )
    finally:
        continue
