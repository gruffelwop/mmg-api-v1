from bs4 import BeautifulSoup

import app.constants.v1.exception as exception_v1

async def get_plan(client, url):
    resp = await client.get(url)
    status_code = resp.status_code
    if status_code == 401:
        raise exception_v1.InvalidPlanCredentialsException
    if status_code != 200:
        raise Exception(status_code)
    return BeautifulSoup(resp.content, "html.parser")
