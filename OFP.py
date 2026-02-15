import math
import random

print("Passangers are randomly generated")
# !!! všechny vzorce a vypočty jsem našel na internetu. Chápu to jen trochu, protože jsou to středo školácké věci, ale chtel jsem to zkusit !!!

# V scritpu jsou uložené letiště s jejich souřadnicemi.
# Po zadání letišť program převede souřadnice na radiány (způsob, jak vyjádřit úhel tak, aby se s ním dalo snadno počítat)
# Pomocí Haversinova vzorce (výpočet vzdálenoti dvou bodů na zemi) spočítá vzdálenost po povrchu Země.

def distance_NM(lat1, lon1, lat2, lon2):

    R = 3440.065 # zemský průměr v NM

    # lat = latitude - zeměpisná šířka; lon = longitude - zeměpisná délka
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # a - vypočítá jak daleko jsou dva body na kouli
    a = math.sin(dlat / 2)**2 + \
        math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

    # c - úhly mezi body
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c # returne skutečnou vzdálenost mezi body

# souřadnice letišť
airports = {
    "LKPR": {"name": "Prague","lat": 50.1008, "lon": 14.26},
    "LOWW": {"name": "Vienna","lat": 48.1103, "lon": 16.5697},
    "EDDF": {"name": "Frankfurt","lat": 50.0379, "lon": 8.5622},
    "LFPG": {"name": "Paris", "lat": 49.0097, "lon": 2.5479},
    "EBBR": {"name": "Brussels", "lat": 50.9010, "lon": 4.4844},
    "EHAM": {"name": "Amsterdam", "lat": 52.3086, "lon": 4.7639},
    "EGLL": {"name": "London", "lat": 51.4700, "lon": -0.4543},
    "LSZH": {"name": "Zurich", "lat": 47.4581, "lon": 8.5555},
    "EPWA": {"name": "Warsaw", "lat": 52.1657, "lon": 20.9671},
    "LZIB": {"name": "Bratislava", "lat": 48.1702, "lon": 17.2127},
    "LIRF": {"name": "Rome", "lat": 41.8003, "lon": 12.2389},
    "LHBP": {"name": "Budapest", "lat": 47.4399, "lon": 19.2619},
    "LROP": {"name": "Bucharest", "lat": 44.5711, "lon": 26.0850},
    "KLAX": {"name": "Los Angeles", "lat": 33.9416, "lon": -118.4085},
    "KJFK": {"name": "New York", "lat": 40.6413, "lon": -73.7781},
    "RJTT": {"name": "Tokyo", "lat": 35.5494, "lon": 139.7798},
    "OMDB": {"name": "Dubai", "lat": 25.2532, "lon": 55.3657}
}

aircrafts = {
    "C172": {
        "name": "Cessna 172",
        "cruise": 110,
        "fuel_burn": 30,
        "max_fuel": 210,
        "MaxPax": random.randint(1, 4),
        "ZFW": 750
    },
    "B737": {
        "name": "Boeing 737",
        "cruise": 475,
        "fuel_burn": 2750,
        "max_fuel": 26000,
        "MaxPax": random.randint(80, 200),
        "ZFW": 50000
    },
    "A320": {
        "name": "Airbus A320",
        "cruise": 450,
        "fuel_burn": 2400,
        "max_fuel": 27200,
        "MaxPax": random.randint(80, 180),
        "ZFW": 43000
    },
    "A380": {
        "name": "Airbus A380",
        "cruise": 485,
        "fuel_burn": 17500,
        "max_fuel": 320000,
        "MaxPax": random.randint(80, 525),
        "ZFW": 277000
    },
    "B747": {
        "name": "Boeing 747",
        "cruise": 500,
        "fuel_burn": 14200,
        "max_fuel": 245000,
        "MaxPax": random.randint(80, 525),
        "ZFW": 200000
    },
    "B777": {
        "name": "Boeing 777",
        "cruise": 485,
        "fuel_burn": 7500,
        "max_fuel": 181000,
        "MaxPax": random.randint(80, 400),
        "ZFW": 144000
    },
    "F-22": {
        "name": "F-22 Raptor",
        "cruise": 1100,
        "fuel_burn": 5800,
        "max_fuel": 16000,
        "MaxPax": random.randint(1, 2),
        "ZFW": 19700
    }
}

print("")
print("Available airports:")
for code, data in airports.items():
    print(f"{code} – {data['name']}")

dep_code = input("\nDeparture airport (ICAO): ").upper()
arr_code = input("Arrival airport (ICAO): ").upper()

if dep_code == arr_code:
    print("Departure and arrival airports cannot be the same.")
    exit()

if dep_code not in airports or arr_code not in airports:
    print("Invalid airport code")
    exit()

print("\nAvailable aircraft:")
for code, data in aircrafts.items():
    print(f"{code} – {data['name']}")

ac_code = input("\nSelect aircraft: ").upper()

if ac_code not in aircrafts:
    print("Unknown aircraft type.")
    exit()

a1 = airports[dep_code]
a2 = airports[arr_code]

dist = distance_NM(
    a1["lat"], a1["lon"],
    a2["lat"], a2["lon"]
)

aircraft = aircrafts[ac_code]

ZFW = aircraft["ZFW"]
Cargo = aircraft["MaxPax"] * 15
Passangers = aircraft["MaxPax"] * 70

G_speed = aircraft["cruise"]
FlightTime = dist/G_speed

hours = int(FlightTime)
minutes = int((FlightTime - hours) * 60)

TripFuel = FlightTime * aircraft["fuel_burn"]
ReserveFuel = aircraft["fuel_burn"] * 0.75

EFOB = TripFuel + ReserveFuel

ci = random.randint(0, 100)

TOW = ZFW + Passangers + Cargo + (EFOB * 0.85)

if EFOB > aircraft["max_fuel"]:
    print("")
    print("Fuel exceeds maximum fuel!")
else:
    print("")
    print("------------------------------")
    print("OPERATIONAL FLIGHT PLAN")
    print("------------------------------")
    print("INFO")
    print(f"Aircraft: {aircraft['name']}")
    print(f"Route: {dep_code} ({a1['name']}) → {arr_code} ({a2['name']})")
    print(f"Distance: {dist:.1f} NM")
    print(f"\nPassangers on board: {aircraft['MaxPax']}")
    print(f"Cost index: {ci}")
    print("------------------------------")
    print("FLIGHT")
    print(f"Cruise speed: {G_speed} kt")
    print(f"In air time: {hours}h {minutes}m")
    minutes = minutes + 30
    if minutes >= 60:
        minutes = minutes - 60
        hours = hours + 1
    print(f"Whole flight time: {hours}h {minutes}m")
    print("------------------------------")
    print("WEIGHT")
    print(f"Zero Fuel Weight: {ZFW} kg")
    print(f"Takeoff Weight: {TOW:.1f} kg")
    print("------------------------------")
    print("FUEL")
    print(f"Trip fuel: {TripFuel:.1f} L")
    print(f"Reserve fuel (45 min): {ReserveFuel:.1f} L")
    print(f"\nEFOB REQUIRED: {EFOB:.1f} L")
    print("------------------------------")
