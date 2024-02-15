import asyncio
import httpx

import app.constants.v1.exception as exception_v1
from app.services.v1.plan.httpx.get_plan import get_plan as get_plan_v1

async def fetch_all_plans(username: str, password: str):
    urls = [
        f"https://{username}:{password}@www.montgelas-gymnasium.de/verps/M_Vertretungsplan_Schueler_heute.htm",
        f"https://{username}:{password}@www.montgelas-gymnasium.de/verps/M_Vertretungsplan_Schueler_naechster_Schultag.htm",
        f"https://{username}:{password}@www.montgelas-gymnasium.de/verps/M_Vertretungsplan_Schueler_uebernaechster_Schultag.htm",
    ]
    async with httpx.AsyncClient() as client:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get_plan_v1(client, url)))
        # try:
        return await asyncio.gather(*tasks)
        # except httpx.HTTPStatusError as e:
        #     raise exception_v1.InvalidPlanCredentialsException
        # except httpx.RequestError as e:
        #     print(f"Request error occurred: {e}")
        # except Exception as e:
        #     print(f"An unexpected error occurred: {e}")


# async def fetch_all_plans(username: str, password: str):
#     urls = [
#         f"https://{username}:{password}@www.montgelas-gymnasium.de/verps/M_Vertretungsplan_Schueler_heute.htm",
#         f"https://{username}:{password}@www.montgelas-gymnasium.de/verps/M_Vertretungsplan_Schueler_naechster_Schultag.htm",
#         f"https://{username}:{password}@www.montgelas-gymnasium.de/verps/M_Vertretungsplan_Schueler_uebernaechster_Schultag.htm",
#     ]
#     async with httpx.AsyncClient() as client:
#         tasks = []
#         for url in urls:
#             tasks.append(asyncio.ensure_future(get_plan_v1(client, url)))
#         return await asyncio.gather(*tasks)
