import random
import string

# Náhodný výběr Callsigns :D
def random_OK_callsign():
    letters = "".join(random.choices(string.ascii_uppercase, k=3))
    return f"OK-{letters}"

airlines = ("CSA", "DLH", "RYR", "EZY", "BAW")

def random_airline_callsign():
    airline = random.choice(airlines)
    nmbr = random.randint(1, 999)
    suffix = random.choice(["", "A", "B", "L"])
    return f"{airline}{nmbr}{suffix}"

def random_callsign():
    if random.choice([True, False]):
        return random_OK_callsign()
    else:
        return random_airline_callsign()

# Scénáře které můžou být vybrané
def generate_scenario():
    callsign = random_callsign()
    scenario_type = random.choice(["takeoff", "taxi", "climb", "turn"])

    if scenario_type == "takeoff":
        runway = f"{random.randint(1,35)}{random.choice(['', 'L', 'R', 'C'])}"
        text = f"{callsign}, Cleared for takeoff runway {runway}"
        answerCRT = f"Cleared for takeoff runway {runway},  {callsign}"

    elif scenario_type == "taxi":
        runway = f"{random.randint(1,35)}{random.choice(['', 'L', 'R', 'C'])}"
        text = f"{callsign}, Taxi to holding point runway {runway}"
        answerCRT = f"Taxi to holding point runway {runway},  {callsign}"

    elif scenario_type == "climb":
        altitude = random.choice(range(1500, 11000, 500))
        text = f"{callsign}, Climb and maintain {altitude} feet"
        answerCRT = f"Climb and maintain {altitude} feet,  {callsign}"

    else:  # turn
        direction = random.choice(["left", "right"])
        heading = random.randint(1, 360)
        text = f"{callsign}, Turn {direction} heading {heading}"
        answerCRT = f"Turn {direction} heading {heading},  {callsign}"

    return text, answerCRT

Rounds = 5
Score = 0

for Round_Nmbr in range(1, Rounds + 1):
    text, answerCRT = generate_scenario()

    print("")
    print(f"      -----Round {Round_Nmbr}-----")
    print("ATC: ",text)
    print("------------/HELP------------")

    answer = input("Pilot: ").strip()

    def destroyer(text):
        return (
            text.lower()
            .replace(", ", "")
            .replace("  ", "")
            .strip()
        )

    if destroyer(answer) == destroyer(answerCRT):
        print("-----------------------------")
        print("ATC: Correct readback!")
        Score += 1
    elif answer == "/HELP":
        print("----------------")
        print("First copy the clearence or the request and then copy the callsign (RYR451A), doesnt matter if the letters are uppercase or lowercase!")
        print("Example: ATC: RYR451A, Cleared for takeoff runway 26R; Pilot: Cleared for takeoff runway, 26R RYR451A")
        print("----------------")
    else:
        print("-----------------------------")
        print("ATC: Incorrect readback!")
        print("Correct readback should be:")
        print(answerCRT)

print("\n=============================")
print(f"Your score: {Score} / {Rounds}")
print("=============================")

# Vše tohle udělané za jeden den
