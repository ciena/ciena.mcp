#!/usr/bin/env python
# Info module template

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by
#   https://github.com/jgroom33/vmware_rest_code_generator
#
# Do not edit this file manually.
#
# Changes should be made in the swagger used to
#   generate this file or in the generator
#
#############################################

from __future__ import absolute_import, division, print_function

__metaclass__ = type
import socket
import json

DOCUMENTATION = """
module: configmgmt_api_v1_neupgradedetails
short_description: Handle resource of type configmgmt_api_v1_neupgradedetails
description: Handle resource of type configmgmt_api_v1_neupgradedetails
options:
  associationState:
    description:
    - '(Optional) List of networkConstruct associationStates. The allowed values are:
      GOA, LOA'
    - Used by I(state=['get'])
    type: str
  associationStateQualifier:
    description:
    - (Optional) Association state qualifier. The allowed values are MANUAL, SYSTEM,
      NETWORK
    - Used by I(state=['get'])
    type: str
  displayName:
    description:
    - (Optional) List of device displayName values
    - Used by I(state=['get'])
    type: str
  id:
    description:
    - List of networkConstruct Ids
    - Used by I(state=['get'])
    type: str
  ipAddress:
    description:
    - (Optional) Ip Address of Network Construct
    - Used by I(state=['get'])
    type: str
  limit:
    description:
    - The size of a returned page
    - Used by I(state=['get'])
    type: str
  longName:
    description:
    - (Optional) List of comma separated longName values
    - Used by I(state=['get'])
    type: str
  manualInvokeOnCards:
    description:
    - '(Optional) Network Constructs with manual Invoke '
    - Used by I(state=['get'])
    type: str
  metaDataFields:
    description:
    - '(Optional) List of meta data to be included. The allowed values are: resourceType,
      associationState, syncState, softwareActiveVersion, associationStateQualifier,
      upgradeStage, upgradeStatus, manualInvokeOnCards'
    - Used by I(state=['get'])
    type: str
  name:
    description:
    - List of networkConstruct names
    - Used by I(state=['get'])
    type: str
  offset:
    description:
    - (Optional) Offset for current index of data to return
    - Used by I(state=['get'])
    type: str
  physicalLocationId:
    description:
    - (Optional) Physical location id
    - Used by I(state=['get'])
    type: str
  releaseMgmtSchedules:
    description:
    - (Optional) List of releaseMgmt schedules for Network Constructs
    - Used by I(state=['get'])
    type: str
  resourcePartitionInfo:
    description:
    - (Optional) Resource partition info
    - Used by I(state=['get'])
    type: str
  resourceType:
    description:
    - (Optional) List of networkConstruct resourceTypes
    - Used by I(state=['get'])
    type: str
  searchFields:
    description:
    - (Optional) List of comma separated fields to search on. If none are specified,
      all supported fields are implied. Fields require full path (e.g. data.attributes.name)
    - Used by I(state=['get'])
    type: str
  searchText:
    description:
    - (Optional) The searchable text
    - Used by I(state=['get'])
    type: str
  sessionId:
    description:
    - List of Management Session Ids
    - Used by I(state=['get'])
    type: str
  softwareActiveVersion:
    description:
    - (Optional) List of networkConstruct software versions
    - Used by I(state=['get'])
    type: str
  softwareAvailableVersion:
    description:
    - (Optional) Software version available on Network Construct
    - Used by I(state=['get'])
    type: str
  sortBy:
    description:
    - (Optional) List of comma separated fields by which to sort the result. Fields
      require full path (i.e. data.attributes.field). A dash or negative sign before
      a field indicates descending order; by default ascending order is used
    - Used by I(state=['get'])
    type: str
  state:
    choices:
    - get
    description: []
    type: str
  subnetName:
    description:
    - (Optional) SubnetName of Network Construct
    - Used by I(state=['get'])
    type: str
  syncState:
    description:
    - '(Optional) List of networkConstruct syncStates. The allowed values are: notSynchronized,
      synchronizing, synchronized, failed, aborted, deleting, deleteFailed'
    - Used by I(state=['get'])
    type: str
  typeGroup:
    description:
    - (Optional) List of networkConstruct typeGroups
    - Used by I(state=['get'])
    type: str
  upgradeSchedules:
    description:
    - (Optional) List of upgrade schedules for Network Construct
    - Used by I(state=['get'])
    type: str
  upgradeStage:
    description:
    - (Optional) List of upgrade stages for Network Constructs
    - Used by I(state=['get'])
    type: str
  upgradeStatus:
    description:
    - (Optional) List of upgrade status for Network Constructs
    - Used by I(state=['get'])
    type: str
author: []
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = [
    "associationState",
    "associationStateQualifier",
    "displayName",
    "id",
    "ipAddress",
    "limit",
    "longName",
    "manualInvokeOnCards",
    "metaDataFields",
    "name",
    "offset",
    "physicalLocationId",
    "releaseMgmtSchedules",
    "resourcePartitionInfo",
    "resourceType",
    "searchFields",
    "searchText",
    "sessionId",
    "softwareActiveVersion",
    "softwareAvailableVersion",
    "sortBy",
    "subnetName",
    "syncState",
    "typeGroup",
    "upgradeSchedules",
    "upgradeStage",
    "upgradeStatus",
]
from ansible.module_utils.basic import env_fallback

try:
    from ansible_module.turbo.module import AnsibleTurboModule as AnsibleModule
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ciena.mcp.plugins.module_utils.mcp import (
    gen_args,
    open_session,
    update_changed_flag,
)


def prepare_argument_spec():
    argument_spec = {
        "mcp_hostname": dict(
            type="str", required=False, fallback=(env_fallback, ["MCP_HOST"])
        ),
        "mcp_username": dict(
            type="str", required=False, fallback=(env_fallback, ["MCP_USER"])
        ),
        "mcp_password": dict(
            type="str",
            required=False,
            no_log=True,
            fallback=(env_fallback, ["MCP_PASSWORD"]),
        ),
    }
    argument_spec["upgradeStatus"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["upgradeStage"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["upgradeSchedules"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["typeGroup"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["syncState"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["subnetName"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["state"] = {"type": "str", "choices": ["get"]}
    argument_spec["sortBy"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["softwareAvailableVersion"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["softwareActiveVersion"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["sessionId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["searchText"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["searchFields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["resourceType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["resourcePartitionInfo"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["releaseMgmtSchedules"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["physicalLocationId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["offset"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["name"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["metaDataFields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["manualInvokeOnCards"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["longName"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["limit"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["ipAddress"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["id"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["displayName"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["associationStateQualifier"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["associationState"] = {"type": "str", "operationIds": ["get"]}
    return argument_spec


async def main():
    module_args = prepare_argument_spec()
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    session = await open_session(
        mcp_hostname=module.params["mcp_hostname"],
        mcp_username=module.params["mcp_username"],
        mcp_password=module.params["mcp_password"],
    )
    result = await entry_point(module, session)
    module.exit_json(**result)


def url(params):
    return "https://{mcp_hostname}/configmgmt/api/v1/neUpgradeDetails".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _get(params, session):
    _url = "https://{mcp_hostname}/configmgmt/api/v1/neUpgradeDetails".format(
        **params
    ) + gen_args(params, IN_QUERY_PARAMETER)
    async with session.get(_url) as resp:
        content_types = [
            "application/json-patch+json",
            "application/vnd.api+json",
            "application/json",
        ]
        try:
            if resp.headers["Content-Type"] in content_types:
                _json = await resp.json()
            else:
                print("response Content-Type not supported")
        except KeyError:
            _json = {}
        return await update_changed_flag(_json, resp.status, "get")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())