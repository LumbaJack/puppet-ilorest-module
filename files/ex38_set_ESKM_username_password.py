# Copyright 2016 Hewlett Packard Enterprise Development, LP.
 #
 # Licensed under the Apache License, Version 2.0 (the "License"); you may
 # not use this file except in compliance with the License. You may obtain
 # a copy of the License at
 #
 #      http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 # License for the specific language governing permissions and limitations
 # under the License.

import sys
from _restobject import RestObject

def ex38_set_ESKM_username_password(restobj, username, password, accountgroup):
    sys.stdout.write("\nEXAMPLE 38: Set ESKM username, password\n")
    instances = restobj.search_for_type("ESKM.")

    for instance in instances:
        body = dict()

        body["KeyManagerConfig"] = dict()
        body["KeyManagerConfig"]["LoginName"] = username
        body["KeyManagerConfig"]["Password"] = password
        body["KeyManagerConfig"]["AccountGroup"] = accountgroup
        body["KeyManagerConfig"]["ESKMLocalCACertificateName"] = ""

        response = restobj.rest_patch(instance["href"], body)
        restobj.error_handler(response)

if __name__ == "__main__":
    # When running on the server locally use the following commented values
    # iLO_https_url = "blobstore://."
    # iLO_account = "None"
    # iLO_password = "None"

    # When running remotely connect using the iLO secured (https://) address, 
    # iLO account name, and password to send https requests
    # iLO_https_url acceptable examples:
    # "https://10.0.0.100"
    # "https://f250asha.americas.hpqcorp.net"
    eskm_username =  "admin"
    eskm_password =  "password"
    eskm_accountgroup =  "group"
    try:
        iLO_https_url = "https://" + str(sys.argv[1])
        iLO_account = str(sys.argv[2])
        iLO_password = str(sys.argv[3])
    
        #Create a REST object
        REST_OBJ = RestObject(iLO_https_url, iLO_account, iLO_password)
		ex38_set_ESKM_username_password(REST_OBJ, eskm_username, eskm_password,\
                                eskm_accountgroup)

    except Exception:
        sys.stderr.write("Credentials Error \n")
