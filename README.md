<!--Установка-->
У вас должны быть установлены: 
Python 3.10 или выше 
Pip 23.2.1 или выше 
Firefox браузер 
Docker и Docker Compose для запуска в контейнерах
Java 8+ для генерации Allure отчетов 
Allure для просмотра отчетов

Запуск в Docker
Клонируйте репозиторий: 
git clone https://github.com/iamlesya/testEM.git
cd testEM

Запустите тесты в Docker: 
Docker-compose up  --build

Просмотрите отчеты: 
allure serve allure-results

Локальный запуск
Клонируйте репозиторий: 
git clone https://github.com/iamlesya/testEM.git
cd testEM

Установите зависимости: 
pip install –r requirements.txt

Запустите тесты:
python –m pytest –v –s --alluredir=allure-results

Просмотрите отчеты: 
allure serve allure-results


