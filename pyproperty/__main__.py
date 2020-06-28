from __future__ import print_function
import sys
__import__("colorama").init()

if len(sys.argv) < 2:
    sys.exit("Usage   : {ss} <module>\nExample : {ss} os urllib.request.get".format(ss=sys.argv[0]))
sys.argv.pop(0)
import_list = []
for i in sys.argv:
    import_list.append(__import__(i))


for num , i in enumerate(import_list):
    print("\n\t Module : {}\n".format(i.__name__))
    for attr in dir(i):
        try:
            self = i.__getattribute__(attr)
        except Exception as error:
            print("Module : \033[31m{}.{}\033[0m | \033[31mError\033[0m  : {}".format(i.__name__,attr,error))
        else:
            print("Module : \033[32m{}.{}\033[0m | \033[33mOutput\033[0m : {}".format(i.__name__,attr,self))
