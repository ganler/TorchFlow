import mysql.connector
from pip_module_scanner.scanner import Scanner, ScannerException

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="torchflow",  # 数据库用户名
        passwd="TorchFlow@Jiawei233",  # 数据库密码
        database = "torchflow"
    )

    mycursor = mydb.cursor()

    mycursor.execute("select * from env")

    for x in mycursor:
        print(x)

    # from pip_module_scanner.scanner import Scanner, ScannerException

    try:
        scanner = Scanner()
        scanner.run()

        # do whatever you want with the results here
        # example:
        for lib in scanner.libraries_found:
            print("Found module %s at version %s" % (lib.key, lib.version))

    except ScannerException as e:
        print("Error: %s" % str(e))