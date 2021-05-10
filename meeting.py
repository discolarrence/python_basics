attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_invitees = ["Ben", "Dave"]
potential_attendees = attendees + optional_invitees
print("There are", len(attendees), "possible attendees")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)
print("To: " + to_line)
print("cc: " + cc_line)
