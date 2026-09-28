def run_vacuum_agent(location: str, room_a: str, room_b: str):
    actions = []
    current_location = location
    status_a = room_a
    status_b = room_b

    if current_location == "A":

        if status_a == "DIRTY":
            actions.append("SUCK")
            status_a = "CLEAN"

        if status_b == "DIRTY":
            actions.append("MOVE RIGHT")
            current_location = "B"
            actions.append("SUCK")
            status_b = "CLEAN"

    elif current_location == "B":

        if status_b == "DIRTY":
            actions.append("SUCK")
            status_b = "CLEAN"

        if status_a == "DIRTY":
            actions.append("MOVE LEFT")
            current_location = "A"
            actions.append("SUCK")
            status_a = "CLEAN"

    if not actions:
        actions_str = "No cleaning required"
    else:
        actions_str = " → ".join(actions)

    final_state = f"A={status_a}, B={status_b}"
    return actions_str, final_state


# Running all 8 test cases from the table
test_cases = [
    ("TC1", "DIRTY", "CLEAN", "A"),
    ("TC2", "CLEAN", "DIRTY", "A"),
    ("TC3", "DIRTY", "DIRTY", "A"),
    ("TC4", "CLEAN", "CLEAN", "A"),
    ("TC5", "CLEAN", "DIRTY", "B"),
    ("TC6", "DIRTY", "CLEAN", "B"),
    ("TC7", "DIRTY", "DIRTY", "B"),
    ("TC8", "CLEAN", "CLEAN", "B"),
]

# Display results in table format
print(
    f"{'Test Case':<10} | {'Room A':<7} | {'Room B':<7} | {'Pos':<5} | {'Expected Actions':<30} | {'Final State'}"
)
print("-" * 85)

for tc, room_a, room_b, pos in test_cases:
    actions, final_state = run_vacuum_agent(pos, room_a, room_b)
    print(
        f"{tc:<10} | {room_a:<7} | {room_b:<7} | {pos:<5} | {actions:<30} | {final_state}"
    )