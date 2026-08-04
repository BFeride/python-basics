python = {"Ali", "Farida", "Zarifa", "Murad"}
sql = {"Farida", "Murad", "Leyla"}

print("Students who know both Python and SQL:")
print(python & sql)

print("\nAll Students:")
print(python | sql)

print("\nOnly Python Students:")
print(python - sql)
