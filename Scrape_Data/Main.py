from bs4 import BeautifulSoup
import URL_Getter as UG


url = "http://web2.assist.org/web-assist/report.do?agreement=aa&reportPath=REPORT_2&reportScript=Rep2.pl&event=19&dir=1&sia=SFCITY&ria=UCB&ia=SFCITY&oia=UCB&aay=16-17&ay=16-17&dora=CS-AB"


def get_src(url):
    data = UG.simple_get(url)
    html = BeautifulSoup(data, 'html.parser')
    with open(r"HTML.txt", "w") as file:
        file.writelines(html.prettify())
    try:
        with open(r"HTML.txt", "r") as file:
            line = file.readlines()
            for i in line:
                if "reportUrl:" in i.split():
                    print(i.split())
                    src = i.split()
                    print(src[2] + ' ' + src[3])
                    return[(src[2] +' '+ src[3]), src[2]]
    except:
        print("get_src error")


def scrape_data(url, textfile):
    data = UG.simple_get(url)
    html = BeautifulSoup(data, 'html.parser')
    with open(textfile, 'w') as file:
        file.write(html.get_text())


if __name__ == "__main__":
     get_src(url)
