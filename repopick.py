import sys
import urllib
import urllib2
import json
import os

for change in sys.argv[1:]:
    print change
    f = urllib2.urlopen('http://review.cyanogenmod.com/query?q=change:%s' % change)
    d = f.read()
    # gerrit doesnt actually return json. returns two json blobs, separate lines. bizarre.
    d = d.split('\n')[0]
    data = json.loads(d)
    project = data['project']
    project = project.replace('CyanogenMod/', '').replace('android_', '').replace('_', '/')
    print project
    number = data['number']
    os.system('repo download %s %s' % (project, number))
