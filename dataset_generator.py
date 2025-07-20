import pandas as pd
import random
from datetime import datetime, timedelta

regions = ['Lima', 'Arequipa', 'Cusco', 'Trujillo', 'Piura', 'Puno', 'Tacna']
contents = [
    ('Stranger Things', 'Serie', 'USA', 'Drama'), ('The Office', 'Serie', 'USA', 'Comedy'),
    ('La Casa de Papel', 'Serie', 'Spain', 'Drama'), ('Narcos', 'Serie', 'USA', 'Crime'),
    ('BoJack Horseman', 'Serie', 'USA', 'Comedy'), ('Inca Gold', 'Documental', 'Peru', 'History'),
    ('The Crown', 'Serie', 'UK', 'Drama'), ('Superbad', 'Película', 'USA', 'Comedy'),
    ('Squid Game', 'Serie', 'South Korea', 'Thriller'), ('Friends', 'Serie', 'USA', 'Comedy')
]
devices = [('Smartphone', 'Android'), ('Smartphone', 'iOS'), ('TV', 'Smart TV'), ('Laptop', 'Windows'), ('Laptop', 'MacOS')]
subscriptions = ['Free Trial', 'Standard', 'Premium']

data = []
for i in range(1000, 1200): 
    age = random.randint(18, 40)
    gender = random.choice(['M', 'F'])
    region = random.choices(regions, weights=[40, 15, 15, 15, 10, 5])[0]
    content = random.choice(contents)
    device = random.choice(devices)
    subscription = random.choices(subscriptions, weights=[70, 20, 10])[0]
    signup_date = datetime(2025, random.randint(1, 3), random.randint(1, 28))
    is_south = region in ['Arequipa', 'Cusco', 'Puno']
    is_comedy_young = (age <= 25 and content[3] == 'Comedy')
    is_international = content[2] != 'Peru'
    cancels = random.random() < (0.7 if not is_comedy_young else 0.1)
    cancellation_date = (signup_date + timedelta(days=random.randint(15, 60))) if cancels else None
    viewing_time = random.randint(50, 150) if is_south and cancels else random.randint(400, 600) if is_comedy_young else random.randint(100, 500)
    data.append([i, age, gender, region, content[0], content[1], content[2], content[3], device[0], device[1], subscription, signup_date.strftime('%Y-%m-%d'), cancellation_date.strftime('%Y-%m-%d') if cancellation_date else '', viewing_time])

df = pd.DataFrame(data, columns=['user_id', 'age', 'gender', 'region', 'content_title', 'content_category', 'content_origin', 'content_genre', 'device_type', 'device_os', 'subscription_type', 'signup_date', 'cancellation_date', 'viewing_time_minutes'])
df.to_csv('netflix_cancellations_full.csv', index=False)
