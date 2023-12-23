import asyncio
import httpx

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
        return await asyncio.gather(*tasks)
