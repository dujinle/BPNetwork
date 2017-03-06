#!/usr/bin/python
#coding=utf-8
import sys,os,math
base_path = os.path.dirname(__file__);
sys.path.append(os.path.join(base_path,'./network'));

from BPNetwork import *
import numpy as np

def load_dat(ifile,sep):
	mlist = list();
	fp = open(ifile,'r');
	for m in fp.readlines():
		m = m.strip('\n').strip('\r');
		narr = m.split(sep);
		nlist = list();
		for i in narr:
			if i == '' or i == ' ': continue;
			ii = float(i)# / (math.pow(10,len(i)));
			nlist.append(ii);
		mlist.append(nlist);
	return mlist;

def normalization(mat,col_min,col_max):
	shape = mat.shape;
	rows = shape[0];
	cols = shape[1];

	for i in xrange(0, rows, 1):
		for j in xrange(0, cols, 1):
			mat[i][j] = (mat[i][j] - col_min[j]) / (col_max[j] - col_min[j])

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'Usage: %s train label' %sys.argv[0];
		sys.exit(-1);

tfile = sys.argv[1];
lfile = sys.argv[2];
test = sys.argv[3];

xa = np.array(load_dat(tfile,' '));
ya = np.array(load_dat(lfile,' '));
ta = np.array(load_dat(test,' '));

X = np.mat(xa);
Y = np.mat(ya);
T = np.mat(ta);

net = BPNetwork()
net.train(X, Y, [13,6,13], alpha = 0.1, iter_time = 10000);

p = net.predict(T);
print p;

