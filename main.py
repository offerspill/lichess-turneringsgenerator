import requests
from keys import LICHESS_API_TOKEN
import datetime

API_ENDPOINT = "https://lichess.org/api/tournament"
headers = {"Authorization": "Bearer " + LICHESS_API_TOKEN}

def next_weekday(weekday, d = datetime.date.today()):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def to_unix_time_ms(dt):
	return int(str(int(datetime.datetime.timestamp(dt))) + "000")

monday = next_weekday(0)
wednesday = next_weekday(2)
saturday = next_weekday(5)

monday_20 = datetime.datetime.combine(monday, datetime.time(20, 00))
wednesday_19 = datetime.datetime.combine(wednesday, datetime.time(19, 00))
saturday_12 = datetime.datetime.combine(saturday, datetime.time(12, 00))

timestamp_monday_20 = to_unix_time_ms(monday_20)
timestamp_wednesday_19 = to_unix_time_ms(wednesday_19)
timestamp_saturday_12 = to_unix_time_ms(saturday_12)

payload_monday = {
	"name": "Offerspill Bullet",
	"clockTime": 1,
	"clockIncrement": 0,
	"minutes": 60,
	"startDate": timestamp_monday_20,
	"variant": "standard",
	"conditions.teamMember.teamId": "offerspill-sjakklubb"
}

payload_wednesday = {
	"name": "Offerspill Lynsjakk",
	"clockTime": 3,
	"clockIncrement": 2,
	"minutes": 120,
	"startDate": timestamp_wednesday_19,
	"variant": "standard",
	"conditions.teamMember.teamId": "offerspill-sjakklubb"
}

payload_saturday = {
	"name": "Offerspill Fischersjakk",
	"clockTime": 3,
	"clockIncrement": 2,
	"minutes": 120,
	"startDate": timestamp_saturday_12,
	"variant": "chess960",
	"conditions.teamMember.teamId": "offerspill-sjakklubb",
	"conditions.teamMember.teamId": "offerspill-sjakklubb"
}

print("GENERERER TURNERINGER")

r_m = requests.post(headers = headers, url = API_ENDPOINT, data = payload_monday)
print("TURNERING MANDAG:\n\n")
print(r_m.json())
print("=================\n\n")

r_w = requests.post(headers = headers, url = API_ENDPOINT, data = payload_wednesday)
print("TURNERING ONSDAG:\n\n")
print(r_w.json())
print("=================\n\n")

r_s = requests.post(headers = headers, url = API_ENDPOINT, data = payload_saturday)
print("TURNERING LØRDAG:\n\n")
print(r_s.json())
