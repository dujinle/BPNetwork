#!/usr/bin/python
#-*- coding : utf-8 -*-

import sys

def load_bfile(bfile):
	fp = open(bfile,'r');
	tmap = dict();
	for i in fp.readlines():
		i = i.strip('\n').strip('\r');
		w,n = i.split(' ');
		tmap[w] = str(n);
	fp.close();
	return tmap;

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print 'Usage: %s bfile ifile' %sys.argv[0];
		sys.exit(-1);

	bfile = sys.argv[1];
	ifile = sys.argv[2]
	bmap = load_bfile(bfile);

	fp = open(ifile,'r');
	for i in fp.readlines():
		i = i.strip('\n').strip('\r');
		tlist = ['0' for t in range(13)];
		i = i.decode('utf8');
		for j,m in enumerate(i):
			m = m.encode('utf8');
			if bmap.has_key(m):
				tlist[j] = bmap[m];
			else:
				tlist[j] = '0';
		print '\t'.join(tlist);
	fp.close();
