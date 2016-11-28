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

import abc

import six

from tacker._i18n import _
from tacker.api import extensions
from tacker.api.v1 import attributes as attr
from tacker.api.v1 import resource_helper
from tacker.common import exceptions
from tacker.plugins.common import constants
from tacker.services import service_base


RESOURCE_ATTRIBUTE_MAP = {

    'vpps': {
            'id': {
            'allow_post': False,
            'allow_put': False,
            'validate': {'type:uuid': None},
            'is_visible': True,
            'primary_key': True,
        },
    }

}

class Vpp(extensions.ExtensionDescriptor):
    @classmethod
    def get_name(cls):
        return 'VPP Orchestrator'

    @classmethod
    def get_alias(cls):
        return 'VPP'

    @classmethod
    def get_description(cls):
        return "Extension for VPP Orchestrator"

    @classmethod
    def get_namespace(cls):
        return 'http://wiki.openstack.org/Tacker'

    @classmethod
    def get_updated(cls):
        return "2015-12-21T10:00:00-00:00"

    @classmethod
    def get_resources(cls):
        special_mappings = {}
        plural_mappings = resource_helper.build_plural_mappings(
            special_mappings, RESOURCE_ATTRIBUTE_MAP)
        attr.PLURALS.update(plural_mappings)
        action_map = {
            "vpp": {
                "create_vpp_interface": "PUT",
                "delete_vpp_interface": "PUT",
            }
        }
        return resource_helper.build_resource_info(
            plural_mappings, RESOURCE_ATTRIBUTE_MAP, constants.VPP,
            translate_name=True, action_map=action_map)

    @classmethod
    def get_plugin_interface(cls):
        return VPPPluginBase


@six.add_metaclass(abc.ABCMeta)
class VPPPluginBase(service_base.NFVPluginBase):
    def get_plugin_name(self):
        return constants.VPP

    def get_plugin_type(self):
        return constants.VPP

    def get_plugin_description(self):
        return 'Tacker VPP Orchestrator plugin'

    @abc.abstractmethod
    def create_vpp_interface(self, context, vpp_id, interface_info=None):
        pass

    @abc.abstractmethod
    def delete_vpp_interface(self, context, vpp_id, interface_info=None):
        pass

    @abc.abstractmethod
    def get_vpps(self, context, filters=None, fields=None):
        pass

    @abc.abstractmethod
    def get_vpp(self, context, filters=None, fields=None):
        pass

    @abc.abstractmethod
    def create_vpp(self, context, vpp):
        pass

    @abc.abstractmethod
    def delete_vpp(self, context, vpp):
        pass

    @abc.abstractmethod
    def update_vpp(self, context, vpp):
        pass
