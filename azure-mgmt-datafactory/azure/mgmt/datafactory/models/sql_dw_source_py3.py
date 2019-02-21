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

from .copy_source_py3 import CopySource


class SqlDWSource(CopySource):
    """A copy activity SQL Data Warehouse source.

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
    :param sql_reader_query: SQL Data Warehouse reader query. Type: string (or
     Expression with resultType string).
    :type sql_reader_query: object
    :param sql_reader_stored_procedure_name: Name of the stored procedure for
     a SQL Data Warehouse source. This cannot be used at the same time as
     SqlReaderQuery. Type: string (or Expression with resultType string).
    :type sql_reader_stored_procedure_name: object
    :param stored_procedure_parameters: Value and type setting for stored
     procedure parameters. Example: "{Parameter1: {value: "1", type: "int"}}".
     Type: object (or Expression with resultType object), itemType:
     StoredProcedureParameter.
    :type stored_procedure_parameters: object
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
        'sql_reader_query': {'key': 'sqlReaderQuery', 'type': 'object'},
        'sql_reader_stored_procedure_name': {'key': 'sqlReaderStoredProcedureName', 'type': 'object'},
        'stored_procedure_parameters': {'key': 'storedProcedureParameters', 'type': 'object'},
    }

    def __init__(self, *, additional_properties=None, source_retry_count=None, source_retry_wait=None, max_concurrent_connections=None, sql_reader_query=None, sql_reader_stored_procedure_name=None, stored_procedure_parameters=None, **kwargs) -> None:
        super(SqlDWSource, self).__init__(additional_properties=additional_properties, source_retry_count=source_retry_count, source_retry_wait=source_retry_wait, max_concurrent_connections=max_concurrent_connections, **kwargs)
        self.sql_reader_query = sql_reader_query
        self.sql_reader_stored_procedure_name = sql_reader_stored_procedure_name
        self.stored_procedure_parameters = stored_procedure_parameters
        self.type = 'SqlDWSource'
