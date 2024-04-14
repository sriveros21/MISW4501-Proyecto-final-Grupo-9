from ..models.services import Service
from ..extensions import db
import requests

def get_services_and_events():
    services = Service.query.all()
    events = fetch_events()  # Assuming external API call
    return services, events

def fetch_events():
    response = requests.get('http://event_management_queries_container:3002/events')
    return response.json()