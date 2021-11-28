import ftplib
import os
import shutil
FTP_HOST = ''
FTP_USER = ''
FTP_PASS = ''
ftp = ftplib.FTP(FTP_HOST,FTP_USER,FTP_PASS)
ftp.encoding = 'utf-8'
#ftp.retrlines('LIST')
filename = r'[FILENAME]'
with open(filename, "rb") as file:
    ftp.storbinary(f"STOR {filename}", file)
