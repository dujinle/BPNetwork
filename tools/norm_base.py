#!/usr/bin/python
#-*- coding : utf-8 -*-

import sys,struct

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'Usage: %s ifile' %sys.argv[0];
		sys.exit(-1);

	ifile = sys.argv[1]
	bdic = dict();
	fp = open(ifile,'r');
	for i in fp.readlines():
		i = i.strip('\n').strip('\r');
		i = i.decode('utf8');
		for j,m in enumerate(i):
			bm = m.encode('gbk');
			um = m.encode('utf8');
			bdic[um] = struct.unpack('>H',bm)[0];
	fp.close();
	for m in bdic.keys():
		print m,bin(bdic[m]);
