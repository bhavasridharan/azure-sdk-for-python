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


class WorkflowRunTrigger(Model):
    """WorkflowRunTrigger

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Gets the name.
    :vartype name: str
    :ivar inputs: Gets the inputs.
    :vartype inputs: object
    :ivar inputs_link: Gets the link to inputs.
    :vartype inputs_link: :class:`ContentLink
     <azure.mgmt.logic.models.ContentLink>`
    :ivar outputs: Gets the outputs.
    :vartype outputs: object
    :ivar outputs_link: Gets the link to outputs.
    :vartype outputs_link: :class:`ContentLink
     <azure.mgmt.logic.models.ContentLink>`
    :ivar start_time: Gets the start time.
    :vartype start_time: datetime
    :ivar end_time: Gets the end time.
    :vartype end_time: datetime
    :ivar tracking_id: Gets the trackingId.
    :vartype tracking_id: str
    :ivar code: Gets the code.
    :vartype code: str
    :ivar status: Gets the status. Possible values include: 'NotSpecified',
     'Paused', 'Running', 'Waiting', 'Succeeded', 'Skipped', 'Suspended',
     'Cancelled', 'Failed', 'Faulted', 'TimedOut', 'Aborted'
    :vartype status: str
    :ivar error: Gets the error.
    :vartype error: object
    """ 

    _validation = {
        'name': {'readonly': True},
        'inputs': {'readonly': True},
        'inputs_link': {'readonly': True},
        'outputs': {'readonly': True},
        'outputs_link': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'tracking_id': {'readonly': True},
        'code': {'readonly': True},
        'status': {'readonly': True},
        'error': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': 'object'},
        'inputs_link': {'key': 'inputsLink', 'type': 'ContentLink'},
        'outputs': {'key': 'outputs', 'type': 'object'},
        'outputs_link': {'key': 'outputsLink', 'type': 'ContentLink'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'tracking_id': {'key': 'trackingId', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
        'status': {'key': 'status', 'type': 'WorkflowStatus'},
        'error': {'key': 'error', 'type': 'object'},
    }

    def __init__(self):
        self.name = None
        self.inputs = None
        self.inputs_link = None
        self.outputs = None
        self.outputs_link = None
        self.start_time = None
        self.end_time = None
        self.tracking_id = None
        self.code = None
        self.status = None
        self.error = None
