# firebase_connection.py
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
from decouple import config


print(config('GOOGLE_APPLICATION_CREDENTIALS'))

# Ruta al archivo de configuración de Firebase descargado
cred = credentials.Certificate(config('GOOGLE_APPLICATION_CREDENTIALS'))
# Inicializar la aplicación de Firebase con el nombre del bucket
initialize_app(cred, options={
    'storageBucket': config('BUCKET')
})

# Obtén una referencia a la colección en Firestore
db_firestore = firestore.client()
