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


class InnerError(Model):
    """
    Generic resource inner error information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar trace: Gets or sets the stack trace for the error
    :vartype trace: str
    :ivar context: Gets or sets the context for the error message
    :vartype context: str
    """ 

    _validation = {
        'trace': {'readonly': True},
        'context': {'readonly': True},
    }

    _attribute_map = {
        'trace': {'key': 'trace', 'type': 'str'},
        'context': {'key': 'context', 'type': 'str'},
    }

    def __init__(self):
        self.trace = None
        self.context = None
