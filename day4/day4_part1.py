''' NOTE: this would be so simple with pandas but don't have it on pythonista! '''

class Event:
	
	# attributes
	def __init__(self, time, status):
		self.time = time
		self.status = status
		self.guard = ''
		self.duration = ''
	
		# print string	
	def __str__(self):
		return "%s %s" % (self.datetime, self.event)


''' parse input and create events '''
from datetime import datetime

event_log = []

with open("puzzle_input.txt", "r") as f:
	for item in f:
		time = datetime.strptime(item.split('] ')[0], '[%Y-%m-%d %H:%M')
		status = item.split('] ')[1]
		event = Event(time,status)
		event_log.append(event)


''' sort event log on datetime '''
	
event_log.sort(key=lambda r: r.time)


for e in event_log:
	if e.status[0] == 'G':
		guard = e.status.split()[1][1:]
		e.guard = guard
		e.status = "start"
	elif e.status[0] == 'f':
		e.status = "asleep"
		e.guard = guard
	elif e.status[0] == 'w':
		e.status = "awake"
		p.duration = e.time - p.time
	else:
		pass
	# remember previous for next loop
	p = e
		
for e in event_log[:25]:
	if e.status == "asleep":
		print(e.time)
		print(e.status)
		print(e.duration)
		print(e.guard)
		print('. . .')


''' now that i have durations and guards, i only need to care about the "asleep" events '''	

sleep = [e for e in event_log if e.status == "asleep"]

''' which guard has most minutes asleep? '''
#this would be one line of code in pandas! 

guards = []
for e in sleep:
	guards.append(e.guard)
	
guards = list(set(guards))

print(guards)




guard_sums = {}
for g in guards:
	guard_sums[g] = 0
	
for e in sleep:
	guard_sums[e.guard] = 


	





