# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .job_input_clip import JobInputClip


class JobInputHttp(JobInputClip):
    """Represents HTTPS job input.

    All required parameters must be populated in order to send to Azure.

    :param label: A label that is assigned to a JobInput, that is used to
     satisfy a reference used in the Transform. For example, a Transform can be
     authored so as to take an image file with the label 'xyz' and apply it as
     an overlay onto the input video before it is encoded. When submitting a
     Job, exactly one of the JobInputs should be the image file, and it should
     have the label 'xyz'.
    :type label: str
    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param files: List of files. Required for JobInputHttp.
    :type files: list[str]
    :param base_uri: Base URI for HTTPS job input. It will be concatenated
     with provided file names.   If no base uri is given, then the provided
     file list is assumed to be fully qualified uris.
    :type base_uri: str
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'files': {'key': 'files', 'type': '[str]'},
        'base_uri': {'key': 'baseUri', 'type': 'str'},
    }

    def __init__(self, *, label: str=None, files=None, base_uri: str=None, **kwargs) -> None:
        super(JobInputHttp, self).__init__(label=label, files=files, **kwargs)
        self.base_uri = base_uri
        self.odatatype = '#Microsoft.Media.JobInputHttp'