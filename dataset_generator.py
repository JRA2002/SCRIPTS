import pandas as pd
import random
from datetime import datetime, timedelta

# Configuración inicial
num_users = 400
start_date = datetime(2024, 1, 1)

# Valores posibles
regions = ['Lima', 'Arequipa', 'Cusco', 'Trujillo', 'Piura']
genres = ['Drama', 'Comedia', 'Acción', 'Documental', 'Romance']
subscription_types = ['Premium', 'Estándar', 'Básico', 'Prueba Gratuita']
devices = ['Smart TV', 'Móvil', 'Laptop', 'Tablet']

# Generación de datos
users = []
for i in range(1, num_users + 1):
    user_id = f'U{i:03d}'
    edad = random.randint(18, 60)
    genero = random.choice(['M', 'F'])
    region = random.choice(regions)
    sub_type = random.choice(subscription_types)
    join_date = start_date + timedelta(days=random.randint(0, 180))
    cancel = random.choice([True, False, False])  # Más chances de no cancelar
    cancel_date = join_date + timedelta(days=random.randint(10, 90)) if cancel else ''
    content_genre = random.choice(genres)
    horas_vista = round(random.uniform(0.5, 15.0), 1) if cancel else round(random.uniform(10.0, 40.0), 1)
    device = random.choice(devices)
    
    users.append([
        user_id, edad, genero, region, sub_type,
        join_date.date(), cancel, cancel_date if cancel else '',
        content_genre, horas_vista, device
    ])

# Crear DataFrame
df = pd.DataFrame(users, columns=[
    'UserID', 'Edad', 'Género', 'Región', 'TipoSuscripción',
    'FechaAlta', 'Cancelado', 'FechaCancelación', 'GéneroContenido',
    'HorasVista', 'Dispositivo'
])

# Guardar como Excel
df.to_excel('Netflix_Peru_BI_Dataset_400_Usuarios.xlsx', index=False)

print("Archivo generado: Netflix_Peru_BI_Dataset_400_Usuarios.xlsx")
