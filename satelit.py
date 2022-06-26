import ftplib
import os
from datetime import datetime, timedelta
from datetime import datetime
from datetime import timezone


d = (datetime.today() + timedelta(days=-1)).strftime("%d")
m = (datetime.today() + timedelta(days=0)).strftime("%m") 	
y = (datetime.today() + timedelta(days=0)).strftime("%Y")	
path = '/himawari_vol/himawari4/HIMAWARI-8/DATA/image/Indonesia/'+y+'/'+m+'/'+d+'/'
tt00 = '0000'
tt01 = '0100'
tt02 = '0200'
tt03 = '0300'
tt04 = '0400'
tt05 = '0500'
tt06 = '0600'
tt07 = '0700'
tt08 = '0800'
tt09 = '0900'
tt10 = '1000'
tt11 = '1100'
tt12 = '1200'
tt13 = '1300'
tt14 = '1400'
tt15 = '1500'
tt16 = '1600'

ftp = ftplib.FTP("202.90.199.64","kspdc","kspdc!@#")
ftp.cwd(path)
dataloc=os.getcwd()+'\\data\\'


H00='H08_ET_Indonesia_'+y+''+m+''+d+''+tt00+'.png'
proses=ftp.retrbinary("RETR " + H00 ,open('F:/tctrackinformation/img/satelit/H08_ET_Indonesia_'+y+''+m+''+d+''+tt00+'.png', 'wb').write)
H01='H08_ET_Indonesia_'+y+''+m+''+d+''+tt01+'.png'
proses=ftp.retrbinary("RETR " + H01 ,open('F:/tctrackinformation/img/satelit/H08_ET_Indonesia_'+y+''+m+''+d+''+tt01+'.png', 'wb').write)
H02='H08_ET_Indonesia_'+y+''+m+''+d+''+tt02+'.png'
proses=ftp.retrbinary("RETR " + H02 ,open('F:/tctrackinformation/img/satelit/H08_ET_Indonesia_'+y+''+m+''+d+''+tt02+'.png', 'wb').write)
H03='H08_ET_Indonesia_'+y+''+m+''+d+''+tt03+'.png'
proses=ftp.retrbinary("RETR " + H03 ,open('F:/tctrackinformation/img/satelit/H08_ET_Indonesia_'+y+''+m+''+d+''+tt03+'.png', 'wb').write)
H04='H08_ET_Indonesia_'+y+''+m+''+d+''+tt04+'.png'
proses=ftp.retrbinary("RETR " + H04 ,open('F:/tctrackinformation/img/satelit/H08_ET_Indonesia_'+y+''+m+''+d+''+tt04+'.png', 'wb').write)
H05='H08_ET_Indonesia_'+y+''+m+''+d+''+tt05+'.png'
proses=ftp.retrbinary("RETR " + H05 ,open('F:/tctrackinformation/img/satelit/H08_ET_Indonesia_'+y+''+m+''+d+''+tt05+'.png', 'wb').write)
H06='H08_ET_Indonesia_'+y+''+m+''+d+''+tt06+'.png'
proses=ftp.retrbinary("RETR " + H06 ,open('F:/tctrackinformation/img/satelit/H08_ET_Indonesia_'+y+''+m+''+d+''+tt06+'.png', 'wb').write)
