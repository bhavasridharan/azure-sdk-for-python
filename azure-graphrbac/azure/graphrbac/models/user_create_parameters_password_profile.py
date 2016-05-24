# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UserCreateParametersPasswordProfile(Model):
    """UserCreateParametersPasswordProfile

    :param password: Password
    :type password: str
    :param force_change_password_next_login: Force change password on next
     login
    :type force_change_password_next_login: bool
    """ 

    _validation = {
        'password': {'required': True},
    }

    _attribute_map = {
        'password': {'key': 'password', 'type': 'str'},
        'force_change_password_next_login': {'key': 'forceChangePasswordNextLogin', 'type': 'bool'},
    }

    def __init__(self, password, force_change_password_next_login=None):
        self.password = password
        self.force_change_password_next_login = force_change_password_next_login