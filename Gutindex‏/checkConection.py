#!/usr/bin/python2.4

import psycopg2 , os
while True :
    try:
        db = psycopg2.connect("dbname='postgres' user='postgres' host='db' password='123456'")
        # print(db)
    except:
        print("no conection")
    else:
        import subprocess
        print("conection")
        os.system("chmod +x /runFile.sh")
        import subprocess
        subprocess.call(['/runFile.sh'])
        break
    os.system("sleep 2")



        # # subprocess.call(['python3', 'manage.py', 'migrate'])
        # program_list = [
        #     'migrate', 
        #     'updatecatalog',
        #     #  'collectstatic',
        #     #  'runserver'
        #      ]
        # # os.system("echo yes | python3 manage.py collectstatic" )

        # for program in program_list:
        #     print(program)
        #     os.system("sleep 1")
        #     # echo yes | python3 manage.py collectstatic
                
        #     if program == 'collectstatic':
        #          os.system("echo yes | python3 manage.py" +program )
        #          break
        #     else :
        #         subprocess.call(['python3', 'manage.py' , program  ])
        #     os.system("sleep 1")            
        #     print("Finished:" + program)
        # # print(1)
        # # os.system("python3 /project/manage.py migrate")
        # # print(2)
        # # os.system("python3 /project/manage.py updatecatalog")
        # # print(3)
        # # os.system("python3 /project/manage.py collectstatic")
        # # print(4)
        # # os.system("python3 /project/manage.py runserver")
