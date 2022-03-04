# Client MongoDB - mongodbcloud and AWSdocumentDB configuration
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import pymongo

from pymongo.server_api import ServerApi
from dotenv import load_dotenv

def client_mongo(name_cloud):
    if name_cloud == 'mongodbcloud':
        return pymongo.MongoClient(
            os.environ['MONGODBCLOUD_PARAMS_URI'],
            server_api= ServerApi('1'),
            serverSelectionTimeoutMS= 5000 
        )
    elif name_cloud == 'AWSdocumentDB':
        return pymongo.MongoClient(
            os.environ['AWSDOCUMENTDB_PARAMS_URI'],
            ssl= True,
            ssl_ca_certs= os.environ['AWSDOCUMENTDB_PARAMS_SSLCA'],
            serverSelectionTimeoutMS= 5000 
        )    
    else:
        raise Exception("Not Found Cloud")