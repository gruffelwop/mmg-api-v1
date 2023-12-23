from datetime import datetime
import pandas as pd

from icecream import ic

def split_list_into_chunks_v1(list, size):
    for i in range(0, len(list), size): 
        yield list[i:i + size]

def selenium_fetch_portal_absences_test():
    date_ranges = [
        datetime(year=2023, month=10, day=19),
        datetime(year=2023, month=10, day=20),
        datetime(year=2023, month=10, day=18),
        datetime(year=2023, month=10, day=18),
        datetime(year=2023, month=10, day=16),
        datetime(year=2023, month=10, day=16),
        datetime(year=2023, month=10, day=5),
        datetime(year=2023, month=10, day=5),
        datetime(year=2023, month=9, day=22),
        datetime(year=2023, month=9, day=22),
    ]
    reasons = [
        "",
        "Krankheit:",
        "Krankheit:",
        "Krankheit: Starke Erkältung",
        "Krankheit:",
    ]

    dates_and_reasons = []

    date_ranges = list(split_list_into_chunks_v1(date_ranges, 2))

    for date_range_index in range(0, len(date_ranges)):
        date_list = pd.date_range(date_ranges[date_range_index][0], date_ranges[date_range_index][1])
        for date in date_list:
            dates_and_reasons.append({"date": date.date(), "reason": reasons[date_range_index]})

    # for date_range in date_ranges:
    #     date_list = pd.date_range(date_range[0], date_range[1])
    #     for date in date_list:
    #         dates.append({"date": date.date(), "reason": ""})

    return dates_and_reasons

ic(selenium_fetch_portal_absences_test())