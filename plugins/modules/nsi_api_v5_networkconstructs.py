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
module: nsi_api_v5_networkconstructs
short_description: Handle resource of type nsi_api_v5_networkconstructs
description: Handle resource of type nsi_api_v5_networkconstructs
options:
  concrete:
    description:
    - (Optional) Id of the concrete networkConstruct
    - Used by I(state=['get'])
    type: str
  data:
    description:
    - 'Validate attributes are:'
    - ' - C(attributes) (dict): '
    - ' - C(id) (str): The unique identifier for the NetworkConstruct resource'
    - ' - C(meta) (dict): A metadata object that contains non-standard meta information'
    - ' - C(relationships) (dict): The relationships of a network construct'
    - ' - C(type) (str): The Network Construct resource type'
    - Used by I(state=['post'])
    type: dict
  fields:
    description:
    - (Optional) List of comma separated fields to be included in the response. Fields
      require full path (i.e. data.attributes.field)
    - Used by I(state=['get'])
    type: str
  identifierKey:
    description:
    - The identifier key list
    - Used by I(state=['get'])
    type: list
  identifierValue:
    description:
    - The identifier value list
    - Used by I(state=['get'])
    type: list
  include:
    description:
    - 'List of comma separated resources to be side-loaded. The allowed values are:
      expectations, physicalLocation, parentNetworkConstruct, networkConstructDiscovered,
      networkConstructPlanned'
    - Used by I(state=['get'])
    type: str
  included:
    description:
    - Referenced resources (discovered, planned, expectations, physical locations,
      or parent/child Network Constructs)
    - Used by I(state=['post'])
    type: list
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
  meta:
    description:
    - A metadata object that contains non-standard meta information
    - 'Validate attributes are:'
    - ' - C(absoluteTotal) (int): The unfiltered total number of entities in the data'
    - ' - C(aggregations) (list): The aggregated data based on a requested aggregation
      name and criteria'
    - ' - C(filtered) (bool): Flags whether the current object is filtered using `fields`
      query param or not'
    - ' - C(missingReferenceIds) (list): The list of missing resource IDs'
    - ' - C(missingReferences) (bool): boolean detailing if the GET FRE tree has any
      missing references'
    - ' - C(total) (int): The total number of entities in the data'
    - Used by I(state=['post'])
    type: dict
  name:
    description:
    - (Optional) List of device name values
    - Used by I(state=['get'])
    type: str
  networkConstructExpectations.equipmentIntent.id:
    description:
    - (Optional) The equipment intent Id
    - Used by I(state=['get'])
    type: str
  networkConstructExpectations.serviceIntent.id:
    description:
    - (Optional) The service intent Id
    - Used by I(state=['get'])
    type: str
  networkConstructType:
    description:
    - '(Optional) Network Construct type. The allowed values are: networkElement,
      shelf, osrpNode, manual, branchingUnit, submarineRepeater'
    - Used by I(state=['get'])
    type: str
  offset:
    description:
    - Offset for the second page
    - Used by I(state=['get'])
    type: str
  physicalLocationId:
    description:
    - (Optional) Physical location id
    - Used by I(state=['get'])
    type: str
  sessionId:
    description:
    - (Optional) Management Session Id
    - Used by I(state=['get'])
    type: str
  state:
    choices:
    - get
    - post
    description: []
    type: str
author: []
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = [
    "concrete",
    "fields",
    "identifierKey",
    "identifierValue",
    "include",
    "ipAddress",
    "limit",
    "name",
    "networkConstructExpectations.equipmentIntent.id",
    "networkConstructExpectations.serviceIntent.id",
    "networkConstructType",
    "offset",
    "physicalLocationId",
    "sessionId",
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
    argument_spec["state"] = {"type": "str", "choices": ["get", "post"]}
    argument_spec["sessionId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["physicalLocationId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["offset"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["networkConstructType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["networkConstructExpectations_serviceIntent_id"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["networkConstructExpectations_equipmentIntent_id"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["name"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["meta"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["limit"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["ipAddress"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["included"] = {"type": "list", "operationIds": ["post"]}
    argument_spec["include"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["identifierValue"] = {"type": "list", "operationIds": ["get"]}
    argument_spec["identifierKey"] = {"type": "list", "operationIds": ["get"]}
    argument_spec["fields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["data"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["concrete"] = {"type": "str", "operationIds": ["get"]}
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
    return "https://{mcp_hostname}/nsi/api/v5/networkConstructs".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _get(params, session):
    _url = "https://{mcp_hostname}/nsi/api/v5/networkConstructs".format(
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


async def _post(params, session):
    accepted_fields = ["data", "included", "meta"]
    spec = {}
    for i in accepted_fields:
        if params[i] is not None:
            spec[i] = params[i]
    _url = "https://{mcp_hostname}/nsi/api/v5/networkConstructs".format(
        **params
    ) + gen_args(params, IN_QUERY_PARAMETER)
    async with session.post(_url, json=spec) as resp:
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
        return await update_changed_flag(_json, resp.status, "post")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
