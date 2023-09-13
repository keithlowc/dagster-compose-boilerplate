"""Collection of Cereal jobs"""
from dagster import job

from dagster_app.ops.cereal import (
    display_results,
    download_cereals,
    find_highest_calorie_cereal,
    find_highest_protein_cereal,
    hello_cereal,
)
from dagster_app.ops.data_source import get_data


@job
def hello_cereal_job():
    """Example of a simple Dagster job."""
    hello_cereal()


@job
def complex_job():
    """Example of a more complex Dagster job."""
    cereals = download_cereals()
    display_results(
        most_calories=find_highest_calorie_cereal(cereals),
        most_protein=find_highest_protein_cereal(cereals),
    )


@job
def eleads_job():
    """Elead jobs gets data from jotform, process and distributes"""
    data = get_data()
