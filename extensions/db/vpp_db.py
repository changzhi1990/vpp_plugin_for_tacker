# Copyright 2015 UnitedStack.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from tacker.extensions import vpp

class VPPPluginDB(vpp.VPPPluginBase):

    def __init__(self):
        super(VPPPluginDB, self).__init__()

    def get_vpps(self, context, filters=None, fields=None):
        print "calling get_vpps"
        return [{'id': 123}, {'id': 456}]

    def get_vpp(self, context, filters=None, fields=None):
        print "calling get_vpp"
        return {'id': 123}

    def create_vpp(self, context, vpp):
        pass

    def delete_vpp(self, context, vpp):
        pass

    def update_vpp(self, context, vpp):
        pass
