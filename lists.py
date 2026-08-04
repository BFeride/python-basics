languages = [
    "Python",
    "SQL",
    "Excel"
]

languages.append("Power BI")

languages.sort()

print("Programming Skills")

for language in languages:
    print("-", language)

print(f"\nTotal Skills: {len(languages)}")
