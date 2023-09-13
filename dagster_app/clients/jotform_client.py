import datetime
from typing import Iterable

import pytz
from jotform import JotformAPIClient


class JotformCustomClient:
    def __init__(self, api_key: str):
        """
        Initializes Jotformcustom client
        """
        self.api_key = api_key
        self.client = self.authenticate()

    def authenticate(self) -> JotformAPIClient:
        """
        Returns authenticated api client
        """
        return JotformAPIClient(self.api_key)

    def get_forms(self) -> Iterable:
        """
        Returns all forms for client.
        """
        return self.client.get_forms()

    def get_latest_submissions(self, n: int) -> Iterable:
        """
        Returns the n latest submissions
        """
        return self.client.get_submissions(0, n, None, "created_at")

    def get_past_submissions_of_hours(
        self, submission_id: int, timezone: str = "US/Eastern", hours_back: int = 1
    ) -> list[dict]:
        """
        Gets all past submissions for a specific form
        1 hour back from current time.

        Ie: Runs @ 2pm gets back all submissions from
        1pm - 2pm. With this we can cover submissions
        that happen in the past.
        """
        eastern_timezone = pytz.timezone(timezone)

        current_time = datetime.datetime.now().astimezone(eastern_timezone)

        end_time = current_time.replace(minute=0, second=0, microsecond=0)
        start_time = end_time - datetime.timedelta(hours=hours_back)

        # Define submission filter for the date range
        submission_filter = {
            "id:gt": f"{submission_id}",
            "created_at:gt": f"{start_time}",
            "created_at:lt": f"{end_time}",
        }

        print(submission_filter)

        submissions: list[dict] = self.client.get_submissions(0, 0, submission_filter, "")

        return submissions

    def edit_submission(self, sid: int, submission: dict):
        """
        Do not have permissions to use this for some
        reason 401 errors.c
        """
        return self.client.edit_submission(sid, submission)


if __name__ == "__main__":
    api_key = "7df0c637544022ad359b070a30e419d0"
    client = JotformCustomClient(api_key)
    forms = client.get_forms()

    submissions = client.get_past_submissions_of_hours(submission_id="232553939091058")

    print(submissions)
