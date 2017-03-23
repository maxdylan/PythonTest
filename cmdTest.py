import os
apkName = input("应用名: ")
sign = 'java -jar signapk.jar platform.x509.pem platform.pk8 '+apkName+".apk out"+apkName+".apk"
install = "adb install -r out"+apkName+".apk"
os.system(sign)
os.system(install)
