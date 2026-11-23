file = open("telemetry.txt", "r")

content = file.read()

print(content)

file.close()
with open("telemetry.txt", "r") as file:
    content = file.read()
    print(content)