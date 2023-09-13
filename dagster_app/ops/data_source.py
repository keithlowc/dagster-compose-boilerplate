"""Collection of ops for data sourcing in this case Leads"""

import os

from dagster import Field, op

from dagster_app.clients.jotform_client import JotformCustomClient


@op(
    config_schema={
        "submission_form_id": Field(
            str, description="ID of the form you are trying to get submissions from"
        ),
        "hours_back": Field(
            int,
            description="How many hours back from now do you want to pull submissions from",
            default_value=1,
        ),
    }
)
def get_data(context) -> list:
    """
    Gets data from a source
    """
    api_key: str = os.getenv("JOTFORM_API_KEY")
    client: JotformCustomClient = JotformCustomClient(api_key)

    submission_form_id = context.op_config["submission_form_id"]
    hours_back = context.op_config["hours_back"]

    submissions: list[dict] = client.get_past_submissions_of_hours(
        submission_id=submission_form_id, hours_back=hours_back
    )

    context.log.info(f"{dir(context)}")

    context.log.info(f"Submissions printed! {submissions}")

    return submissions
