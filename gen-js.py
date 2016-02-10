#!/usr/bin/python

import sys

titles = ['S/N', 'REGION', 'AREA', 'CLINIC NAME', 'ADDRESS', 'TEL',\
	'WEEKDAYS', 'WEEKDAYS (EVENING)', 'SATURDAY', 'SUNDAY', 'PUBLIC HOLIDAY',\
	'REMARKS']
NF = len(titles)

def load_clinics(filename):
	clinics = []
	for line in open(filename).read().splitlines():
		if line.startswith('PARSE_RESULT'):
			arr = line.split('\t')
			assert len(arr) == NF + 1
			d = {}
			for i in range(0, 12):
				d[titles[i]] = arr[i+1]
			clinics.append(d)
	return clinics

def load_postal_gps(filename):
	postal_gps = {}
	for line in open(filename).read().splitlines():
		arr = line.split(' ')
		assert len(arr) == 3
		postal_gps[arr[0]] = (arr[1], arr[2])
	return postal_gps

assert len(sys.argv) == 3
clinics = load_clinics(sys.argv[1])
postal_gps = load_postal_gps(sys.argv[2])

for clinic in clinics:
	p = clinic['ADDRESS'][-6:]
	if p in postal_gps:
		clinic['POSTAL'] = p
	l = []
	for k,v in clinic.iteritems():
		#k = k.lower().replace(' (', '_').replace(')', '').replace('/', '_').replace(' ', '_')
		l.append('"%s": "%s"' % (k, v.replace('"', '\\"')))
	print "var c%s = {%s};" % (clinic['S/N'], ', '.join(l))
print "var clinics = [" + ', '.join(map(lambda x : 'c' + x['S/N'], clinics)) + "];"

print "var postal_gps = new Array();"
for p,c in postal_gps.iteritems():
	#print "var p%s = {lat: %s, lng: %s};" % (p, c[0], c[1])
	print 'postal_gps[\"%s\"] = {lat: %s, lng: %s};' % (p, c[0], c[1])
