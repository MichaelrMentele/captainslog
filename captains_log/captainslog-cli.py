import click
from captains_log import settings
from captains_log import helpers

# Commands
# captainslog new stardate
# captainslog new (appends or creates based on date)
# stardate (opens or creates new entry)

# I would like to just run stardate and create a new entry.
# It should create it in the right /year/month/day file.

# computer analyze captainslog
@click.command()
def captainslog():
    """Journal manager"""


@click.command()
def stardate():
    """Subcommand for creation of a new log entry"""


@click.command()
def computer():
