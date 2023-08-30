#! /usr/bin/env python
import os
import subprocess as sp

# sp.run(["date"])
# sp.run(['sleep', '2'])
# sp.run(["pwd"])
# result = sp.run(["ls", "modules"])
# print(result.returncode)
#
# result = sp.run(["host", "8.8.8.8"], capture_output=True)
# print(result.returncode)
#
# print(result.stdout)
# print(result.stdout.decode().split())
#
# result = sp.run(["rm", "does_not_exist"], capture_output=True)
# print("Return code= {}, stdout = {}, stderr = {}".format(result.returncode, result.stdout, result.stderr))
#
# sp.run(['pip', 'list'])

my_env = os.environ.copy()
my_env['PATH'] = os.pathsep.join(['/opt/myapp/', my_env['PATH']])
print(my_env['PATH'])
# result = sp.run(["myapp"], env=my_env)
