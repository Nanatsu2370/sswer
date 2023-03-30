import pyrogram
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

# Inicializar api
app = pyrogram.Client('my_pycho_bot', api_id='ID1', api_hash='HASH1', bot_token='TOKEN')

# URL de la página web de la Serie Nacional de Béisbol de Cuba
url = 'http://www.beisbolencuba.com/'

# Obtener el contenido de la página web
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar la tabla de la Serie Nacional de Béisbol de Cuba
table = soup.find('table', {'class': 'tabla'})

# Crear una lista vacía para almacenar los datos de la tabla
data = []

# Obtener los datos de la tabla y almacenarlos en la lista
for row in table.find_all('tr'):
    columns = row.find_all('td')
    if columns:
        data.append([column.get_text(strip=True) for column in columns])

# Enviar los datos de la tabla al usuario
@app.on_message()
def send_table(client, message):
    table_str = tabulate(data, headers=['Equipo', 'JG', 'JP', 'Ave', 'Dif'], tablefmt='orgtbl')
    client.send_message(chat_id=message.chat.id, text=table_str)

app.run()



