from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import Main

delay = 5


def navigate():
    driver = webdriver.Firefox(
        executable_path=r'/media/jowi/jowi/Pycharm/Pycharm Projects/SheWhoCodesProj/geckodriverLinux')
    # driver = webdriver.Firefox(executable_path=r'E:\Pycharm\Pycharm Projects\SheWhoCodesProj\geckodriverLinux')
    driver.get("http://www.assist.org")
    # Page 1 Settings

    for x in range(1, 35):
        print("#############################################")
        print("loop: " + str(x))
        print("#############################################")
        try:
            # Page 1 settings
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, "ia")))
            Select(driver.find_element_by_name("ia")).select_by_index(34)

            # Page 2 Settings
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, "other_inst")))
            optionBox = driver.find_element_by_name("oia")
            options = [t.text for t in optionBox.find_elements_by_tag_name("option")]
            Select(driver.find_element_by_name("oia")).select_by_index(x)

            # Page 3 Settings
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, "dora")))
            major = driver.find_elements_by_class_name('major')
            listmajor = major[0].text.split('\n')
            print(listmajor)
            a = 100

            for i in listmajor:
                if 'computer science' in i.lower():
                    a = listmajor.index(i)
                    break
                else:
                    pass

            if a == 100:
                print(options[x] +":  no computer science course")
                pass
            else:
                Select(driver.find_element_by_class_name('major')).select_by_index(a)

                WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "reportblock")))
                data = Main.get_src(driver.current_url)
                try:
                    print("Data Scrape 1 testing")
                    #Main.scrape_data(data[0], r"{}.text".format(options[x][4:]))
                    Main.scrape_data(data[0], r"{}.txt".format(options[x][4:]))
                except:
                    print("Main 2 Tested")
                    #Main.scrape_data(data[1], r"{}.text".format(options[x][4:]))
                    Main.scrape_data(data[1], r"{}.txt".format(options[x][4:]))

                driver.get("http://www.assist.org")
        except:
            print("error")
            pass



if __name__ == "__main__":
    navigate()

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()