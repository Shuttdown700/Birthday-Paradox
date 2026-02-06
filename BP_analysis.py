import random

num_days = 365
days = list(range(1, num_days + 1))

num_tests = 100_000
macro_tracker = {}

for _ in range(num_tests):
    num_people = 2
    num_intervals = 59
    tracker = {}
    for _ in range(num_intervals):
        # each person selects a random day on each interval
        selected_days = [random.randint(1, num_days) for _ in range(num_people)]
        # detect duplicates (meaning matching birthdays)
        if len(selected_days) != len(set(selected_days)):
            num_matches = len(selected_days) - len(set(selected_days))
        else:
            num_matches = 0
        tracker.update({num_people:tracker.get(num_people, 0) + num_matches})
        num_people += 1
    # get percentage of chance of at least one match for every number of people
    for people, matches in tracker.items():
        macro_tracker[people] = macro_tracker.get(people, 0) + 1 if matches > 0 else macro_tracker.get(people, 0)

print("\nSummary of matches:")
analysis = {}
for people, matches in macro_tracker.items():
    percentage = (matches / num_tests) * 100
    analysis[people] = round(percentage/100, 3)
    print(f"{people} people: {percentage:.2f}% chance of at least one match.")

# output summary to json file:
import json
with open("bp_analysis_summary.json", "w") as f:
    json.dump(analysis, f, indent=4)

# Plot and save line graph of the results:
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.plot(list(analysis.keys()), list(analysis.values()), marker='o')
plt.xlabel("Number of People")
plt.ylabel("Probability of At Least One Shared Birthday")
plt.title("Birthday Paradox Analysis")
plt.grid(True)
plt.savefig("birthday_paradox_analysis.png")