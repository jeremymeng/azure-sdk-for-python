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

from .copy_source import CopySource


class SalesforceSource(CopySource):
    """A copy activity Salesforce source.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param source_retry_count: Source retry count. Type: integer (or
     Expression with resultType integer).
    :type source_retry_count: object
    :param source_retry_wait: Source retry wait. Type: string (or Expression
     with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type source_retry_wait: object
    :param max_concurrent_connections: The maximum concurrent connection count
     connectioned to source data store. Type: integer (or Expression with
     resultType integer).
    :type max_concurrent_connections: object
    :param type: Required. Constant filled by server.
    :type type: str
    :param query: Database query. Type: string (or Expression with resultType
     string).
    :type query: object
    :param read_behavior: The read behavior for the operation. Default is
     Query. Possible values include: 'Query', 'QueryAll'
    :type read_behavior: str or
     ~azure.mgmt.datafactory.models.SalesforceSourceReadBehavior
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'source_retry_count': {'key': 'sourceRetryCount', 'type': 'object'},
        'source_retry_wait': {'key': 'sourceRetryWait', 'type': 'object'},
        'max_concurrent_connections': {'key': 'maxConcurrentConnections', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'query': {'key': 'query', 'type': 'object'},
        'read_behavior': {'key': 'readBehavior', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SalesforceSource, self).__init__(**kwargs)
        self.query = kwargs.get('query', None)
        self.read_behavior = kwargs.get('read_behavior', None)
        self.type = 'SalesforceSource'
