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


class MongoDbV2Source(CopySource):
    """A copy activity source for a MongoDB database.

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
    :param filter: Specifies selection filter using query operators. To return
     all documents in a collection, omit this parameter or pass an empty
     document ({}). Type: string (or Expression with resultType string).
    :type filter: object
    :param cursor_methods: Cursor methods for Mongodb query
    :type cursor_methods:
     ~azure.mgmt.datafactory.models.MongoDbCursorMethodsProperties
    :param batch_size: Specifies the number of documents to return in each
     batch of the response from MongoDB instance. In most cases, modifying the
     batch size will not affect the user or the application. This property�s
     main purpose is to avoid hit the limitation of response size. Type:
     integer (or Expression with resultType integer).
    :type batch_size: object
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
        'filter': {'key': 'filter', 'type': 'object'},
        'cursor_methods': {'key': 'cursorMethods', 'type': 'MongoDbCursorMethodsProperties'},
        'batch_size': {'key': 'batchSize', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(MongoDbV2Source, self).__init__(**kwargs)
        self.filter = kwargs.get('filter', None)
        self.cursor_methods = kwargs.get('cursor_methods', None)
        self.batch_size = kwargs.get('batch_size', None)
        self.type = 'MongoDbV2Source'
