import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

# Configuración
n_users = 2000
start_date = pd.to_datetime("2024-01-01")
end_date = pd.to_datetime("2024-06-30")
countries = ['Argentina', 'Brasil', 'Chile', 'México', 'Colombia']
channels = ['Orgánico', 'Pago', 'Redes', 'Email', 'Referido']

# Simular usuarios
user_ids = np.arange(1, n_users + 1)
signup_dates = np.random.choice(pd.date_range(start_date, end_date - pd.Timedelta(days=30)), size=n_users)

user_data = pd.DataFrame({
    'user_id': user_ids,
    'signup_date': signup_dates,
    'country': np.random.choice(countries, size=n_users),
    'acquisition_channel': np.random.choice(channels, size=n_users)
})

# Simular actividad
activity_data = []

for idx, row in user_data.iterrows():
    n_activities = np.random.poisson(3)  # cantidad de sesiones promedio por usuario
    for _ in range(n_activities):
        days_after_signup = np.random.randint(0, 120)
        activity_date = row['signup_date'] + timedelta(days=int(days_after_signup))
        if activity_date <= end_date:
            activity_data.append({
                'user_id': row['user_id'],
                'activity_date': activity_date
            })

activity_df = pd.DataFrame(activity_data)

# Merge con info del usuario
final_df = activity_df.merge(user_data, on='user_id')

# Guardar CSV
final_df.to_csv('data/user_activity.csv', index=False)
print("✅ Dataset guardado en data/user_activity.csv")
