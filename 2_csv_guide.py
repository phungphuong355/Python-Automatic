import csv

# Comma separate value CSV
# Write csv
hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open("hosts.csv", 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

# Read csv
with open("hosts.csv") as hosts_csv:
    h_csv = csv.reader(hosts_csv)
    for row in h_csv:
        host, ip = row
        print("{} = {}".format(host, ip))

# Write Dict
users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
         {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
         {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open("by_department.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

# Read Dict
with open("by_department.csv") as file:
    f_csv = csv.DictReader(file)
    for row in f_csv:
        print("{}, {}, {}".format(row['name'], row['username'], row['department']))