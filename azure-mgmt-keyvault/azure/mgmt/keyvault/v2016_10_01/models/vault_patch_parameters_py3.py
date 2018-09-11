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

from msrest.serialization import Model


class VaultPatchParameters(Model):
    """Parameters for creating or updating a vault.

    :param tags: The tags that will be assigned to the key vault.
    :type tags: dict[str, str]
    :param properties: Properties of the vault
    :type properties:
     ~azure.mgmt.keyvault.v2016_10_01.models.VaultPatchProperties
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'VaultPatchProperties'},
    }

    def __init__(self, *, tags=None, properties=None, **kwargs) -> None:
        super(VaultPatchParameters, self).__init__(**kwargs)
        self.tags = tags
        self.properties = properties