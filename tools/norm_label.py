#!/usr/bin/python
#-*- coding : utf-8 -*-

import sys

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'Usage: %s ifile' %sys.argv[0];
		sys.exit(-1);

	bfile = sys.argv[1];

	fp = open(bfile,'r');
	for i in fp.readlines():
		i = i.strip('\n').strip('\r');
		tlist = ['0' for t in range(13)];
		i = list(i.decode('utf8'));
		j = 0;
		while True:
			if j >= len(i):
				tlist[j - 1] = '1';
				break;
			m = i[j];
			m = m.encode('utf8');
			if m == ' ':
				tlist[j - 1] = '1';
				del i[j];
				j = j - 1;
			else:
				tlist[j] = '0';
			j = j + 1;
		print '\t'.join(tlist);
	fp.close();
