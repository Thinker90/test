import os
import dotenv

#
#
#

dotenv.load_dotenv()


print('Test')
print(os.getenv('token', 'No token'))
