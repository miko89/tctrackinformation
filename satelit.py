import ftplib
import os
from datetime import datetime, timedelta
from datetime import datetime
from datetime import timezone


d = (datetime.today() + timedelta(days=-1)).strftime("%d")
m = (datetime.today() + timedelta(days=-1)).strftime("%m") 	
y = (datetime.today() + timedelta(days=0)).strftime("%Y")	
path = '/himawari_vol/himawari4/HIMAWARI-8/DATA/image/Indonesia/'+y+'/'+m+'/'+d+'/'
##tt00 = '0000'
##tt01 = '0100'
##tt02 = '0200'
##tt03 = '0300'
##tt04 = '0400'
##tt05 = '0500'
tt06 = '0600'
tt07 = '0700'
tt08 = '0800'
tt09 = '0900'
tt10 = '1000'
tt11 = '1100'
tt12 = '1200'
##tt13 = '1300'
##tt14 = '1400'
##tt15 = '1500'
##tt16 = '1600'

ftp = ftplib.FTP("202.90.199.64","kspdc","kspdc!@#")
ftp.cwd(path)
dataloc=os.getcwd()+'\\data\\'


H06='H08_ET_Indonesia_'+y+''+m+''+d+''+tt06+'.png'
proses=ftp.retrbinary("RETR " + H06 ,open('F:/tctrackinformation/img/satelit/H08_ET_Indonesia_'+y+''+m+''+d+''+tt06+'.png', 'wb').write)
H07='H08_ET_Indonesia_'+y+''+m+''+d+''+tt07+'.png'
proses=ftp.retrbinary("RETR " + H07 ,open('F:/tctrackinformation/img/satelit/H08_ET_Indonesia_'+y+''+m+''+d+''+tt07+'.png', 'wb').write)
H08='H08_ET_Indonesia_'+y+''+m+''+d+''+tt08+'.png'
proses=ftp.retrbinary("RETR " + H08 ,open('F:/tctrackinformation/img/satelit/H08_ET_Indonesia_'+y+''+m+''+d+''+tt08+'.png', 'wb').write)
H09='H08_ET_Indonesia_'+y+''+m+''+d+''+tt09+'.png'
proses=ftp.retrbinary("RETR " + H09 ,open('F:/tctrackinformation/img/satelit/H08_ET_Indonesia_'+y+''+m+''+d+''+tt09+'.png', 'wb').write)
H10='H08_ET_Indonesia_'+y+''+m+''+d+''+tt10+'.png'
proses=ftp.retrbinary("RETR " + H10 ,open('F:/tctrackinformation/img/satelit/H08_ET_Indonesia_'+y+''+m+''+d+''+tt10+'.png', 'wb').write)
H11='H08_ET_Indonesia_'+y+''+m+''+d+''+tt11+'.png'
proses=ftp.retrbinary("RETR " + H11 ,open('F:/tctrackinformation/img/satelit/H08_ET_Indonesia_'+y+''+m+''+d+''+tt11+'.png', 'wb').write)
H12='H08_ET_Indonesia_'+y+''+m+''+d+''+tt12+'.png'
proses=ftp.retrbinary("RETR " + H12 ,open('F:/tctrackinformation/img/satelit/H08_ET_Indonesia_'+y+''+m+''+d+''+tt12+'.png', 'wb').write)
