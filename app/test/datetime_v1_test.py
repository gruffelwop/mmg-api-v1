from datetime import datetime

from icecream import ic

raw_date_range = [
    "31.07.2023",
    "11.09.2023"
]

raw_time_range = [
    # "17:00",
    # "18:00",
    "",
]

start_time = ""
end_time = ""

ic(raw_time_range == [""])
if raw_time_range == [""]:
    ic("1")
    start_time = datetime.fromtimestamp(0).time()
    end_time = datetime.fromtimestamp(0).time()
else:
    ic("2")
    start_time = datetime.strptime(raw_time_range[0], "%H:%M").time()
    end_time = datetime.strptime(raw_time_range[1], "%H:%M").time()

ic(start_time, end_time)

# ic(datetime.strptime(raw_date_range[0], "%d.%m.%Y").date())
# ic(datetime.strptime(raw_date_range[1], "%d.%m.%Y").date())
# ic(datetime.strptime(raw_time_range[0], "%H:%M") if raw_time_range[0] != "" else datetime.fromtimestamp(0).time())
# ic(datetime.strptime(raw_time_range[1], "%H:%M").time() if raw_time_range[1] != "" else datetime.fromtimestamp(0))

# datetime.strptime(raw_time_range[0], "%H:%M").time() if raw_time_range else datetime.fromtimestamp(0).time()
