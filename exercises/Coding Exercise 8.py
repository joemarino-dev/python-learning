# Determine the number of flights that connect through Rome and the average flight time for all connections 
# Source data structured as flight from, flight to, num minutes for trip
connections = [
	('Amsterdam', 'Dublin', 100),
	('Amsterdam', 'Rome', 140),
	('Rome', 'Warsaw', 130),
	('Minsk', 'Prague', 95),
	('Stockholm', 'Rome', 190),
	('Copenhagen', 'Paris', 120),
	('Madrid', 'Rome', 135),
	('Lisbon', 'Rome', 170),
	('Dublin', 'Rome', 170),
	]

flight_times = []
	
for destination in connections:
	if destination[1] == 'Rome':
		flight_times.append(destination[2])

flight_time_avg = sum(flight_times) / len(flight_times)
		
print(len(flight_times), 'connections lead to Rome with an average flight time of', flight_time_avg, 'minutes.')

# answer key
check_flight_time = (140 + 190 + 135 + 170 + 170) / 5
print(check_flight_time)
