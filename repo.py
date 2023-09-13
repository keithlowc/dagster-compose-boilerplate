"""Definitions that provide Dagster code locations."""
from dagster import Definitions

from dagster_app.assets.cereal import cereals, highest_calorie_cereal, highest_protein_cereal
from dagster_app.jobs import complex_job, eleads_job, hello_cereal_job
from dagster_app.schedules import every_weekday_9am

defs = Definitions(
    assets=[cereals, highest_calorie_cereal, highest_protein_cereal],
    jobs=[complex_job, hello_cereal_job, eleads_job],
    schedules=[every_weekday_9am],
)
