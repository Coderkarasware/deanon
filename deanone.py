
import os, sys
from time import sleep
try:
    import requests
except ImportError:
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear") 
    exit('[!] Увас отсуствует requests. pip install requests')
try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
    exit('[!] Увас отсуствует BeautifulSoup. pip install bs4')

 
dataAV = []
RESET ='\033[0m'
UNDERLINE = '\033[04m'
GREEN = '\033[32m'
YELLOW = '\033[93m'
RED ='\033[31m'
CYAN = '\033[36m'
BOLD = '\033[01m'
PINK = '\033[95m'
URL_L = '\033[36m'
LI_G='\033[92m'
F_CL = '\033[0m'
DARK = '\033[90m'

def banner():
    print(RED+'''▄▄ █   █▀█ █▀▀  █▀▄▀█ █▀█ █ █'''+GREEN+'''
█▄█ █▄▄ █▀█ █▄▄ █ █ █ ▀ █ █▀█ █ █▄▄
                           '''+RESET+RED+'V: YouTube LeshaSeledka\n')
def banner_ip():
    print(CYAN+'''█▄▄ █   █▀█ █▀▀ █▄▀ █▀▄▀█ █▀█ █ █'''+PINK+'''
█▄█ █ █▀█ █ █▄▄
                           '''+RESET+CYAN+'V: YouTube LeshaSeledka\n')
def banner_mnp():
    print(PINK+'''Karas'''+CYAN+'''
 
                           '''+RESET+PINK+'V: 1\n')

def clear():
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def getVersion():
    try:
        try:
            if os.path.exists('.banner_840'):
                pass   
            else:
                clear()
                try:
                    bannerTX = open('README.md', encoding='utf-8').read()
                    print(bannerTX[219:1585].replace('#','').replace('*','').replace('-','•'))
                    sleep(10)
                    print(f'\n{LI_G}Этот текст покажется лишь один раз!{RESET}')
                    input(f'{LI_G}Нажмите ENTER чтобы продолжить: {RESET}')
                    open('.banner_840','w')
                    clear()
                except FileNotFoundError:
                    clear()
                
                except KeyboardInterrupt:
                    sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')

            if os.path.exists('dataFile.txt'):
                try:
                    clear()
                    print(f'{CYAN}{BOLD}[1] {LI_G}Перезаписать данные в файл.{RESET}')
                    print("YouTube LeshaSeledka")
                    dataV = input(f'{CYAN}{BOLD}[~] {LI_G}Выберите метод. ENTER - Добавить к остальным: {RESET}')
                    if dataV == '1':
                        try:
                            os.remove('dataFile.txt')
                            clear() 
                            print(f'{YELLOW}{BOLD}[+] {LI_G}Данные будут:{RESET} Перезаписаны')
                            sleep(0.5)
                            
                            clear()
                            print(f'{YELLOW}{BOLD}[#] {LI_G}Подготовка... {RESET}')
                        except PermissionError:
                            pass
                    else:
                        clear()
                        print(f'{YELLOW}{BOLD}[+] {LI_G}Данные будут:{RESET} Добавлены к остальным')
                        sleep(0.5)
                        
                        clear()
                        print(f'{YELLOW}{BOLD}[#] {LI_G}Подготовка... {RESET}')
                except KeyboardInterrupt:
                    sys.exit(f'\n{CYAN}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')
            else:
                clear()
                print(f'{YELLOW}{BOLD}[#] {LI_G}Подготовка... {RESET}')
            versioUR = requests.get('https://github.com/DataSC3/No-BlackM')
            versioURL = bs(versioUR.text, 'html.parser')
            get_version = versioURL.find(['span'], class_='d-none d-sm-inline').findNext(['strong']).text
            clear()
            with open('.banner_840', 'r') as fileF: 
                try:
                    versionUP = fileF.read().split(':')[1]
                    if str(get_version) != str(versionUP):
                        with open('.banner_840', 'w') as fileW:
                            fileW.write('Version:'+str(get_version))
                            clear()
                            for _ in range(3):
                                print(f'{YELLOW}{BOLD}[!]-{LI_G} Доступно новое обновление {YELLOW}-[!]')
                                sleep(0.4)
                                clear()

                                print(f'{YELLOW}{BOLD}[!]--{LI_G} Доступно новое обновление {YELLOW}--[!]')
                                sleep(0.4)
                                clear()

                                print(f'{YELLOW}{BOLD}[!]-->{LI_G} Доступно новое обновление {YELLOW}<--[!]{RESET}')
                                sleep(0.4)
                                clear()

                            print(f'{YELLOW}{BOLD}[#] {LI_G}Для обновления напишите: {RESET}git pull{LI_G} Не выходя из папки.')
                            sleep(3)
                            clear()
                    else:
                        pass
                        
                except IndexError:
                    with open('.banner_840', 'w') as fileW:
                        fileW.write('Version:'+str(get_version))
                        
                except KeyboardInterrupt:
                    sys.exit(f'\n{CYAN}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')
                
        except KeyboardInterrupt:
            sys.exit(f'\n{CYAN}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')
        except FileNotFoundError:
            print(f'\n{YELLOW}{BOLD}[!] Увас отсуствует {RESET}README.md')
            sleep(1)
            clear()
        
        banner()
        print(f'{YELLOW}{BOLD}[1] {LI_G}IP {CYAN}-{LI_G} Данные{RESET}')
        print(f'{YELLOW}{BOLD}[2] {LI_G}MNP {PINK}-{LI_G} Запросы {RESET}')
        choice = input(f'{YELLOW}{BOLD}[~] {LI_G}Выберите проверку. ENTER - Базовая проверка: {RESET}')
        if choice == '1':
            try:
                clear()
                receiving_data_ip()
            except KeyboardInterrupt:
                sys.exit(f'\n{CYAN}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')
        elif choice == '2':
            try:
                clear()
                num_mnp_request()
            except KeyboardInterrupt:
                sys.exit(f'\n{PINK}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')    
        else:
            clear()
        
    except KeyboardInterrupt:
        sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
def receiving_data_ip():
    while True:
        try:
            banner_ip()
            resIP = requests.get('https://httpbin.org/ip')
            resultIP = resIP.text.split()[2].strip('"')

            print(f'{CYAN}{BOLD}[#] {LI_G}Поддержка: {DARK}https://www.donationalerts.com/r/anonimusyoutuber/{RESET}')
            print(f'{CYAN}{BOLD}[#] {LI_G}Ваш IP: {DARK}{resultIP}{RESET}')
            ip = input(f'{CYAN}{BOLD}[~] {LI_G}Введите IP: {RESET}').strip()

            if ip == '':
                ip = resultIP
            else:
                pass 

            ip_get_data = requests.post(f'https://htmlweb.ru/geo/api.php?json&ip={str(ip)}')
            ip_data = ip_get_data.json()      
            
            fileD = open('dataFile.txt', 'a', encoding='utf-8') 
            fileD.write(f'\n[-] IP - Данные: \n')

            print(f'{CYAN}{BOLD}[~] {LI_G}Поиск данных... {RESET}\n')
            fileD.write(f'[+] IP: {str(ip)}\n')
            
            try:
                country = ip_data['country']
                region = ip_data['region']
                try:
                    print(f'{CYAN}{BOLD}[+] {LI_G}Страна:{F_CL} {country["name"]}, {country["fullname"]}{RESET}')
                    fileD.write(f'[+] Страна: {country["name"]}, {country["fullname"]} \n')
                
                except KeyError:
                    if country["country_code3"] == 'UKR':
                        print(f'{CYAN}{BOLD}[+] {LI_G}Страна:{F_CL} Украина{RESET}')
                        # Если сервис не сможет найти страны, Код Стран в помощь.

                        fileD.write(f'[+] Страна: Украина \n')
                    else:
                        print(f'{CYAN}{BOLD}[!] {LI_G}Стране:{F_CL} Неизвестно {RESET}')
                    
                    

                try:
                    print(f'{CYAN}{BOLD}[+] {LI_G}Код страны:{F_CL} {country["country_code3"]}{RESET}')
                    fileD.write(f'[+] Код страны: {country["country_code3"]}\n')

                except KeyError:
                    print(f'{CYAN}{BOLD}[!] {LI_G}Код страны:{F_CL} А я хз {RESET}')
                    

                try:
                    print(f'{CYAN}{BOLD}[+] {LI_G}Код номеров:{F_CL} {str(country["telcod"])}{RESET}')
                    fileD.write(f'[+] Код номеров: {str(country["telcod"])}\n')

                except KeyError:
                    print(f'{CYAN}{BOLD}[!] {LI_G}Код номеров:{F_CL} Неизвестно {RESET}')

                try:
                    print(f'{CYAN}{BOLD}[+] {LI_G}Локация:{F_CL} {country["location"]}{RESET}')
                    fileD.write(f'[+] Локация: {country["location"]}\n')

                except KeyError:
                    print(f'{CYAN}{BOLD}[!] {LI_G}Локация:{F_CL} А я хз {RESET}')

                try:
                    print(f'{CYAN}{BOLD}[+] {LI_G}Язык:{F_CL} {country["lang"]}{RESET}')
                    fileD.write(f'[+] Язык: {country["lang"]}\n')

                except KeyError:
                    print(f'{CYAN}{BOLD}[!] {LI_G}Язык:{F_CL} Неизвестно {RESET}')

                
                try:
                    print(f'{CYAN}{BOLD}[+] {LI_G}Город:{F_CL} {region["name"]}{RESET}')
                    fileD.write(f'[+] Город: {region["name"]}\n')

                except KeyError:
                    print(f'{CYAN}{BOLD}[!] {LI_G}Город:{F_CL} Неизвестно {RESET}')

                try:
                    print(f'{CYAN}{BOLD}[+] {LI_G}Код машин:{F_CL} {region["autocod"]}{RESET}')
                    fileD.write(f'[+] Код машин: {region["autocod"]}\n')

                except KeyError:
                    print(f'{CYAN}{BOLD}[!] {LI_G}Код машин:{F_CL} хз братиш {RESET}')

                try:
                    print(f'{CYAN}{BOLD}[+] {LI_G}Широта: {F_CL}{str(ip_data["latitude"])}{RESET}')
                    fileD.write(f'[+] Широта: {str(ip_data["latitude"])}\n')

                except KeyError:
                    print(f'{CYAN}{BOLD}[!] {LI_G}Широта:{F_CL} Неизвестно {RESET}')
                
                try:
                    print(f'{CYAN}{BOLD}[+] {LI_G}Долгота: {F_CL}{str(ip_data["longitude"])}{RESET}')
                    fileD.write(f'[+] Долгота: {str(ip_data["longitude"])}\n')

                except KeyError:
                    print(f'{CYAN}{BOLD}[!] {LI_G}Долгота:{F_CL} Неизвестно {RESET}')

            except KeyboardInterrupt:
                sys.exit(f'\n{CYAN}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
            
            except KeyError:
                print(f'{CYAN}{BOLD}[!] {LI_G}Город/Локация:{F_CL} Неизвестно {RESET}')

            fileD.close()
            print(f'\n{CYAN}{BOLD}[!] {RED}Всего лимитов 200 : {str(ip_data["limit"])}{RESET}')
            
            print(f'\n{CYAN}{BOLD}[0] {LI_G}Выход{RESET}')
            choice_try = input(f'{CYAN}{BOLD}[~] {LI_G}Выберите действие. ENTER - Продолжить: {RESET}')
            if choice_try == '0':
                clear()
                exit()
            else:
                clear()       

        except KeyboardInterrupt:
            sys.exit(f'\n{CYAN}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')
        except requests.exceptions.RequestException:
            sys.exit(f'{CYAN}{BOLD}[!] {RED}Для проверки IP включите VPN и перезапустите. Ваш провайдер не поддерживает.{RESET}')                        
        except ValueError:
            sys.exit(f'{CYAN}{BOLD}[!] {RED}Для проверки IP включите VPN и перезапустите. Ваш провайдер не поддерживает.{RESET}')
def num_mnp_request():
    while True:
        try:
            banner_mnp()
            
            print(f'{PINK}{BOLD}[#] {LI_G}Поддержка: {DARK}qiwi/r/CODERKARAS{RESET}')
            print(f'{PINK}{BOLD}[#] {LI_G}Пример: {DARK}+7 495 766 11-11{RESET}')
            number=input(f'{PINK}{BOLD}[~] {LI_G}Введите цифры дауна которого хотите деанонить: {RESET}')
            number=number.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
            if number.isdigit():
                if number[0] == '8':
                    number = number[1:]
                    number = '7'+number
                else:
                    pass
            else:
                print(f'{PINK}{BOLD}[!] {RED}"{RESET}{number}{RED}" - братиш эти цифры не является номером\n{RESET}')
                sleep(1)
                clear()
                continue
            num_mnp_data = requests.post(f'https://htmlweb.ru/json/mnp/phone/{str(number)}') 
            num_data = num_mnp_data.json()

            fileD = open('dataFile.txt', 'a', encoding='utf-8') 
            print(f'{PINK}{BOLD}[~] {LI_G}Поиск дауна... {RESET}\n')
            
            try:
                region = num_data['region']
                oper = num_data['oper']
                fileD.write(f'\n[-] MNP - Запросы: \n')
                fileD.write(f'[+] Номер: {str(number)}\n')

                try:
                    print(f'{PINK}{BOLD}[+] {LI_G}Оператор:{F_CL} {oper["brand"]}, {oper["name"]}{RESET}')
                    fileD.write(f'[+] Оператор: {oper["brand"]}, {oper["name"]} \n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Оператор:{F_CL} Неизвестно {RESET}')

                try:
                    print(f'{PINK}{BOLD}[+] {LI_G}ID Оператора:{F_CL} {oper["id"]}{RESET}')
                    fileD.write(f'[+] ID Оператора: {oper["id"]} \n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}ID Оператора:{F_CL} Неизвестно {RESET}')

                try:
                    print(f'{PINK}{BOLD}[+] {LI_G}URL Оператора:{F_CL} {oper["url"]}{RESET}')
                    fileD.write(f'[+] URL Оператора: {oper["url"]} \n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}URL Оператора:{F_CL} Неизвестно {RESET}')

                try:
                    print(f'{PINK}{BOLD}[+] {LI_G}Код страны:{F_CL} {oper["country"]}{RESET}')
                    fileD.write(f'[+] Код страны: {oper["country"]} \n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Код страны:{F_CL} Неизвестно {RESET}')

                try:
                    print(f'{PINK}{BOLD}[+] {LI_G}Город:{F_CL} {region["name"]}{RESET}')
                    fileD.write(f'[+] Город: {region["name"]} \n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Город:{F_CL} Неизвестно {RESET}')

                try:
                    print(f'{PINK}{BOLD}[+] {LI_G}Округ:{F_CL} {region["okrug"]}{RESET}')
                    fileD.write(f'[+] Округ: {region["okrug"]} \n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Округ:{F_CL} Неизвестно {RESET}')

                try:
                    print(PINK+BOLD+'[+]'+LI_G+' Код машин: '+F_CL+str(region["autocod"]).replace(',', ', ')+RESET)
                    fileD.write(f'[+] Код машин: {region["autocod"]} \n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Код машин:{F_CL} Неизвестно {RESET}')

            except KeyboardInterrupt:
                sys.exit(f'\n{PINK}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
            except KeyError:
                print(f'{YELLOW}{BOLD}[!] {LI_G}Оператор/Город:{F_CL} Неизвестно {RESET}')
            
            fileD.close()
            print(f'\n{PINK}{BOLD}[!] {RED}Всего лимитов: {str(num_data["limit"])}{RESET}')
           
            print(f'\n{PINK}{BOLD}[0] {LI_G}Выход{RESET}')
            choice_try = input(f'{PINK}{BOLD}[~] {LI_G}Выберите действие. ENTER - Продолжить: {RESET}')
            if choice_try == '0':
                clear()
                exit()
            else:
                clear()       

        except KeyboardInterrupt:
            sys.exit(f'\n{PINK}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')
        except requests.exceptions.RequestException:
            sys.exit(f'{YELLOW}{BOLD}[!] {RED}Для проверки MNP включите VPN и перезапустите. Ваш провайдер не поддерживает.{RESET}')                        
        except ValueError:
            sys.exit(f'{YELLOW}{BOLD}[!] {RED}Для проверки MNP включите VPN и перезапустите. Ваш провайдер не поддерживает.{RESET}')

def get_url_name_avito(number):
    try:
        resAV = requests.get(f'https://mirror.bullshit.agency/search_by_phone/{number}')

        contentAV = bs(resAV.text, 'html.parser')
        h1 = contentAV.find('h1')
        if resAV.status_code == 404:
            print(f'{YELLOW}{BOLD}[!] {LI_G}Авито: {F_CL}Объявлений не найдено{RESET}')
        if resAV.status_code == 503:
            print(f'{YELLOW}{BOLD}[!] {RED}Ваш запрос временно заблокирован. Пожалуйста, подождите 3-5 минут.{RESET}')
       
        count = 0
        h1T = h1.text.replace("  ","")
        print(f'\n{YELLOW}{BOLD}[~] {LI_G}Поиск данных по Авито: {RESET}')
        print(f'{YELLOW}{BOLD}[~] {LI_G}Авито: {F_CL}{h1T}{RESET}')

        for oBV in contentAV.find_all(['h4', 'span']):
            print(f'{YELLOW}{BOLD}[+] {LI_G}{oBV.text}{RESET}')  
            dataOB.append(oBV.text)
        
        with open('dataFile.txt', 'a', encoding='utf-8') as f:
            for data in dataOB:
                f.write('[-] '+ data +'\n')
        
        for url in contentAV.find_all(['a']):
            count += 1
            user_link = url['href']
            try:            
                avito_url = requests.get('https://mirror.bullshit.agency'+user_link)
                content = bs(avito_url.text, 'html.parser')
                url = content.find(['a'])
                
                linkAV = url['href']
                print(f'{YELLOW}{BOLD}[{count}] {URL_L}{UNDERLINE}{linkAV}{RESET}')
                
                u_name = bs(avito_url.text, 'html.parser')
                nameU = u_name.find('strong')
                name.append(nameU.text)
                dataAV.append(f'[{count}] {linkAV}')
            except KeyboardInterrupt:
                sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')
            except:
                pass

            

    except requests.exceptions.RequestException:
        print(f'{YELLOW}{BOLD}[!] {RED}Для проверки Avito включите VPN и перезапустите. Ваш провайдер не поддерживает.{RESET}')                        
       
    except ValueError:
        print(f'{YELLOW}{BOLD}[!] {RED}Для проверки Avito включите VPN и перезапустите. Ваш провайдер не поддерживает.{RESET}')
        
    except KeyboardInterrupt:
        sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')
        
def save():
    with open('dataFile.txt', 'a', encoding='utf-8') as fileD:
        fileD.write('[-] Номер: +'+str(number)+'\n')
        try:
            for data in dataAV:
                fileD.write(data +'\n')
            if not name:
                pass
            else:
                fileD.write('\n[-] Все имена с ссылок: ' + ', '.join(name))
        except NameError:
            pass
        fileD.write(f'\n[-] https://api.whatsapp.com/send?phone={str(number)}&text=Hello,%20this%20is%20NO-Blackmail - Поиск номера в  WhatsApp\n')
        fileD.write(f'[-] https://facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar - Поиск аккаунтов FaceBook\n')
        fileD.write(f'[-] https://linkedin.com/checkpoint/rp/request-password-reset-submit - Поиск аккаунтов Linkedin\n')
        fileD.write(f'[-] https://twitter.com/account/begin_password_reset - Поиск аккаунтов Twitter\n')
        fileD.write(f'[-] https://viber://add?number={str(number)} - Поиск номера в Viber\n')
        fileD.write(f'[-] https://skype:{str(number)}?call - Звонок на номер с Skype\n')
        fileD.write(f'[-] https://nuga.app - Поиск аккаунтов Instagram' +'\n')
        fileD.write(f'[-] tel:{str(number)} - Звонок на номер с телефона\n\n')
    try:
        if not name:
            pass
        else:
            print('\n'+YELLOW+BOLD+'[+]'+LI_G+' Все имена с ссылок: '+RESET+', '.join(name))
    except NameError:
        pass 

getVersion()
while True:
    try:
        
        banner()
        print(f'{YELLOW}{BOLD}[#] {LI_G}Поддержка: {DARK}qiwi/r/CODERKARAS{RESET}')
        print(f'{YELLOW}{BOLD}[#] {LI_G}Пример: {DARK}+7 495 766 11-11{RESET}')
        getNumber=input(f'{YELLOW}{BOLD}[~] {LI_G}Введите номер: {RESET}')
        repNumber=getNumber.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
        
        if repNumber.isdigit():
            if repNumber.startswith('8'):
                number = ''.join(('7', repNumber[1:]))
            else:
                number = repNumber
        else:
            print(f'{YELLOW}{BOLD}[!] {RED}"{RESET}{getNumber}{RED}" - Не является номером\n{RESET}')
            sleep(1)
            clear()
            continue

        fileD = open('dataFile.txt', 'a', encoding='utf-8')
        try:
            num_P = requests.post('https://htmlweb.ru/geo/api.php?json&telcod='+str(number)).json()
            interNet = num_P['limit']
            print(f'{YELLOW}{BOLD}[~] {LI_G}Поиск данных... {RESET}\n')
            fileD.write(f'[+] Номер: +{str(number)}\n')
            try:
                country = num_P['country']
            
                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Страна:{F_CL} {country["name"]}, {country["fullname"]}{RESET}')
                    fileD.write(f'[+] Страна: {country["name"]}, {country["fullname"]} \n')
                    
                except KeyError:
                    if country["country_code3"] == 'UKR':
                        print(f'{YELLOW}{BOLD}[+] {LI_G}Страна:{F_CL} Украина{RESET}')
                        fileD.write(f'[+] Страна: Украина \n')
                    else:
                        print(f'{YELLOW}{BOLD}[!] {LI_G}Страна:{F_CL} Неизвестно {RESET}')
                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Код страны:{F_CL} {country["country_code3"]}{RESET}')
                    fileD.write(f'[+] Код страна: {country["country_code3"]} \n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Код страны:{F_CL} Неизвестно {RESET}')

                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Код номера:{F_CL} {str(country["telcod"])}{RESET}')
                    fileD.write(f'[+] Код номера: {str(country["telcod"])} \n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Код номера:{F_CL} Неизвестно {RESET}')
                
                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Длина номера:{F_CL} {str(country["telcod_len"])}{RESET}')
                    fileD.write(f'[+] Длина номера: {str(country["telcod_len"])} \n')
                
                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Длина номера:{F_CL} Неизвестно {RESET}')

                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Локация:{F_CL} {country["location"]}{RESET}')
                    fileD.write(f'[+] Локация: {country["location"]} \n')
                
                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Локация:{F_CL} Неизвестно {RESET}')
                
                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Язык:{F_CL} {country["lang"]}{RESET}')
                    fileD.write(f'[+] Язык: {country["lang"]} \n')
                
                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Язык:{F_CL} Неизвестно {RESET}')
            
            except KeyboardInterrupt:
                sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
            except KeyError:
                print(f'{YELLOW}{BOLD}[!] {LI_G}Страна/Язык:{F_CL} Неизвестно {RESET}')

            try:
                region = num_P['region']
                endIndex = region['name'].split()
                    
                try:
                    if endIndex[1] == 'край':
                        print(f'{YELLOW}{BOLD}[+] {LI_G}Край:{F_CL} {region["name"]}{RESET}')
                        fileD.write(f'[+] Край: {region["name"]} \n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Край:{F_CL} Неизвестно {RESET}')

                try:
                    if endIndex[1] == 'область':
                        print(f'{YELLOW}{BOLD}[+] {LI_G}Область:{F_CL} {region["name"]}{RESET}')
                        fileD.write(f'[+] Область: {region["name"]} \n')
                    else:
                        print(f'{YELLOW}{BOLD}[+] {LI_G}Неизвестное:{F_CL} {region["name"]}{RESET}')
                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Область:{F_CL} Неизвестно {RESET}')
                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Округ:{F_CL} {region["okrug"]}{RESET}')
                    fileD.write(f'[+] Округ: {region["okrug"]} \n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Округ:{F_CL} Неизвестно {RESET}')

            except KeyboardInterrupt:
                sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
            except KeyError:
                print(f'{YELLOW}{BOLD}[!] {LI_G}Область/Край:{F_CL} Неизвестно {RESET}')

            try:
                capital = num_P['capital']
                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Столица:{F_CL} {capital["name"]}{RESET}')
                    fileD.write(f'[+] Столица: {capital["name"]} \n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Сталица:{F_CL} Неизвестно {RESET}')
                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Код домашнего номера столицы:{F_CL} +{str(capital["telcod"]).replace(",", ", ")}{RESET}')
                    fileD.write(f'[+] Код домашнего номера столицы: +{str(capital["telcod"])} \n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Код домашнего номера столицы:{F_CL} Неизвестно {RESET}')
                    
            except KeyboardInterrupt:
                sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
            except KeyError:
                print(f'{YELLOW}{BOLD}[!] {LI_G}Код/Столица:{F_CL} Неизвестно {RESET}')

            try:
                data = num_P['0']

                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Город:{F_CL} {data["name"]}{RESET}')
                    fileD.write(f'[+] Город: {data["name"]} \n')
                    
                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Город:{F_CL} Неизвестно {RESET}')
                
                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Оператор:{F_CL} {data["oper_brand"]}{RESET}')
                    fileD.write(f'[+] Оператор: {data["oper_brand"]} \n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Оператор:{F_CL} Неизвестно {RESET}')
                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Номера:{F_CL} {str(data["def"])}{RESET}')
                    fileD.write(f'[+] Номера: {str(data["def"])} \n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Номера:{F_CL} Неизвестно {RESET}')
                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Широта: {F_CL}{str(num_P["latitude"])}{RESET}')
                    fileD.write(f'[+] Широта: {str(num_P["latitude"])}\n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Широта:{F_CL} Неизвестно {RESET}')
                
                try:
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Долгота: {F_CL}{str(num_P["longitude"])}{RESET}')
                    fileD.write(f'[+] Долгота: {str(num_P["longitude"])}\n')

                except KeyError:
                    print(f'{YELLOW}{BOLD}[!] {LI_G}Долгота:{F_CL} Неизвестно {RESET}')

            except KeyboardInterrupt:
                sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
            except KeyError:
                print(f'{YELLOW}{BOLD}[!] {LI_G}Город/Оператор:{F_CL} Неизвестно {RESET}')
                
            
            if interNet == 0:
                pass
            else:    

                if country["country_code3"] == 'RUS':
                    name = []
                    dataAV = []
                    dataOB = []

                    #PhoneReview
                    try:
                        review_ph = requests.get(f'http://phoneradar.ru/phone/{number}').text
                        reviews_rev = bs(review_ph, 'html.parser').find('div', class_='alert alert-danger').text.strip()
                        print(f'{YELLOW}{BOLD}[+] {LI_G}Рейтинг: {F_CL}{reviews_rev}{RESET}')
                        fileD.write(f'[+] Рейтинг: {reviews_rev} \n')

                    except KeyboardInterrupt:
                        sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
                    except AttributeError:
                        reviews_rev = 'Рейтинг номера не определен, отзывов о номере еще нет'
                        print(f'{YELLOW}{BOLD}[+] {LI_G}Рейтинг: {F_CL}{reviews_rev}{RESET}')
                        fileD.write(f'[+] Рейтинг: {reviews_rev} \n')                    
                    except requests.exceptions.RequestException:
                        print(f'{YELLOW}{BOLD}[!] {RED}Для проверки отзывов включите VPN и перезапустите. Ваш провайдер не поддерживает.{RESET}')    
                        
                    except ValueError:
                        print(f'{YELLOW}{BOLD}[!] {RED}Для проверки отзывов включите VPN и перезапустите. Ваш провайдер не поддерживает.{RESET}')
                        
                    get_url_name_avito(number)
                else:
                    pass     
                
                save()
                print(f'\n{YELLOW}{BOLD}[+] {LI_G}Проверьте эти ссылки ( Мессенджеры и Социальные сети ): {RESET}')
                print(f'{YELLOW}{BOLD}[1] {URL_L}{UNDERLINE}https://api.whatsapp.com/send?phone={str(number)}&text=Hello,%20this%20is%20No-BlackMail {RESET}- Поиск номера в  WhatsApp')
                print(f'{YELLOW}{BOLD}[2] {URL_L}{UNDERLINE}https://facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar {RESET}- Поиск аккаунтов FaceBook')
                print(f'{YELLOW}{BOLD}[3] {URL_L}{UNDERLINE}https://linkedin.com/checkpoint/rp/request-password-reset-submit {RESET}- Поиск аккаунтов Linkedin')
                print(f'{YELLOW}{BOLD}[4] {URL_L}{UNDERLINE}https://twitter.com/account/begin_password_reset {RESET}- Поиск аккаунтов Twitter')
                print(f'{YELLOW}{BOLD}[5] {URL_L}{UNDERLINE}https://viber://add?number={str(number)} {RESET}- Поиск номера в Viber')
                print(f'{YELLOW}{BOLD}[6] {URL_L}{UNDERLINE}https://skype:{str(number)}?call {RESET}- Звонок на номер с Skype')
                print(f'{YELLOW}{BOLD}[6] {URL_L}{UNDERLINE}https://nuga.app - Поиск аккаунтов Instagram')
                print(f'{YELLOW}{BOLD}[7] {URL_L}{UNDERLINE}tel:{str(number)} {RESET}- Звонок на номер с телефона')
                
                print(f'\n{YELLOW}{BOLD}[+] {LI_G}Данные о номере: +{str(number)} добавлены в файл {RESET}dataFile.txt')
            print(f'{YELLOW}{BOLD}[!] {RED}Всего лимитов: {str(num_P["limit"])}{RESET}')
            fileD.close() 
            
            print(f'\n{YELLOW}{BOLD}[0] {LI_G}Выход{RESET}')
            choice_try = input(f'{YELLOW}{BOLD}[~] {LI_G}Выберите действие. ENTER - Продолжить: {RESET}')
            if choice_try == '0':
                clear()
                exit()
            else:
                clear()    
        except requests.exceptions.RequestException:        
            sys.exit(f'{YELLOW}{BOLD}[!] {RED}Для проверки номера включите VPN и перезапустите. Ваш провайдер не поддерживает.{RESET}')
        except ValueError:  
            pass

          
    except KeyboardInterrupt:
    	sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')
