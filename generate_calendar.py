from icalendar import Calendar, Event
from yaml import safe_load
import datetime
import re

with open('events.yaml') as fh:
    events = safe_load(fh)
#print(events)

now = datetime.datetime.now()

cal = Calendar()
#cal.add('prodid', '-//My calendar product//mxm.dk//')
cal.add('version', '2.0')

for entry in events:
    event = Event()
    event.add('summary', entry['title'])
    datetime.date
    start_dt = datetime.datetime.fromisoformat(entry['begin'])
    #print(start_dt)
    end_dt = datetime.datetime.fromisoformat(entry['end'])
    event.add('dtstart', start_dt)
    event.add('dtend', end_dt)
    event.add('location', entry['url'])
    event.add('description', entry['text'])
    uid = re.sub(r'[^a-zA-Z0-9]', '', entry['text'])[0:30]
    event['uid'] = f'{uid}@ladino.szabgab.com'
    cal.add_component(event)

with open('ladino.ics', 'wb') as fh:
    fh.write(cal.to_ical())
