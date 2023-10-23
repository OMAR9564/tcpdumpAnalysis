import re
import sqlite3

conn = sqlite3.connect('analiz.db')
con = conn.cursor()

con.execute('''CREATE TABLE IF NOT EXISTS tcpdump (
    timestamp DATETIME,
    source TEXT,
    destination TEXT,
    protocol TEXT,
    type INTEGER,
    code INTEGER,
    length INTEGER
)''')


def parse_tcpdump(output):
    for line in output.splitlines():

        fields = re.split('\s+', line)

        timestamp = fields[0]

        source = fields[2]

        destination = fields[4]

        protocol = fields[5]

        type = (fields[7])
        code = (fields[8])

        length = (fields[9])

        con.execute(
            'INSERT INTO tcpdump (timestamp, source, destination, protocol, type, code, length) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (timestamp, source, destination, protocol, type, code, length))


with open('/Users/omerfaruk/Documents/GitHub/Odevler/tcpdumpAnalysis/tcpdump.txt', 'r') as file:
    output = file.read()

parse_tcpdump(output)

conn.commit()
conn.close()
