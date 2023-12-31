from firebase_admin import credentials, firestore, storage
import uuid
from firebase_connection import db_firestore
import datetime 

class FormAdoptedModel:
    def save_form_data(self, nombre, raza, image, horario, ubicacion,descripcion):
        filename = image.filename
        document_id = str(uuid.uuid4())
        bucket = storage.bucket('back-flutter-a83ed.appspot.com')
        blob = bucket.blob(f'formAdopted/{filename}')
        blob.content_type = 'image/jpeg'
        blob.upload_from_file(image)
        
        # Obtener el enlace público a la imagen con el token de acceso
        image_url = blob.generate_signed_url(datetime.timedelta(days=10), method='GET')
        
        data_firestore = {
            'nombre': nombre,
            'raza': raza,
            'image': image_url,  # Guardar el enlace público en lugar del nombre de la imagen
            'horario': horario,
            'ubicacion': ubicacion,
            'descripcion': descripcion,
        }
        db_firestore.collection('FormAdopted').document(document_id).set(data_firestore)
        return document_id
