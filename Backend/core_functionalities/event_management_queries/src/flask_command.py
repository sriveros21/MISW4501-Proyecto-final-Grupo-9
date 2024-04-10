import click
from flask.cli import with_appcontext
from .queries.events_update_listener import start_listener_in_background

@click.command('start-kafka-listener')
@with_appcontext
def start_kafka_listener_command():
    """Starts the Kafka event listener."""
    start_listener_in_background()
    click.echo('Kafka listener started.')
