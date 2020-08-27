from __future__ import absolute_import, division, print_function

__metaclass__ = type
import socket
import json

DOCUMENTATION = """
module: discovery__api__managementSessions
short_description: Handle resource of type discovery__api__managementSessions
description: Handle resource of type discovery__api__managementSessions
options:
  aliasName:
    description:
    - (Optional) Key that holds the alias name
    type: str
  aliasValue:
    description:
    - (Optional) List of alias name values
    type: str
  associationState:
    description:
    - '(Optional) List of the management session associationState. The valid values
      are: GOA, LOA'
    type: str
  associationStateQualifier:
    description:
    - (Optional) List of associationStateQualifiers. The allowed values are MANUAL,
      NETWORK, SYSTEM
    type: str
  associationStateQualifierReason:
    description:
    - (Optional) Reason for putting a Management Session to 'inMaintenance'.
    type: str
  data:
    description:
    - 'Validate attributes are:'
    - ' - C(attributes) (dict): '
    - ' - C(id) (str): The unique identifier for the NetworkConstruct resource'
    - ' - C(relationships) (dict): The relationships of a managmemnt session'
    - ' - C(type) (str): The management session resource type'
    type: dict
  displayAlternativeConnectionIPs:
    description:
    - (Optional) List of comma seperated display alternative connection IPs
    type: str
  displayAlternativeConnectionNames:
    description:
    - (Optional) List of comma seperated display alternative connection names
    type: str
  displayName:
    description:
    - (Optional) List of device displayName values
    type: str
  displayPartitions:
    description:
    - (Optional) List of comma separated display partitions
    type: str
  displayPreferredConnectionName:
    description:
    - (Optional) Name of preferred connection
    type: str
  displayState:
    description:
    - '(Optional) List of comma separated display states. The allowed values are:
      Pending, Connecting, Not connected, Connected, Failed'
    type: str
  ipAddress:
    description:
    - (Optional) Ip Address of management sessions
    type: str
  limit:
    description:
    - (Optional) The size of a returned page
    type: str
  longName:
    description:
    - (Optional) List of comma separated longName values
    type: str
  metaDataFields:
    description:
    - '(Optional) List of meta data to be included. The allowed values are: resourceType,
      associationState, discoveryState, displayState, typeGroup, profileName, resourcePartitionInfo,
      shortResourceType'
    type: str
  name:
    description:
    - (Optional) List of comma separated name values
    type: str
  offset:
    description:
    - (Optional) Offset for current index of data to return
    type: str
  profileId:
    description:
    - (Optional) List of NE security connection profile identifiers
    type: str
  profileName:
    description:
    - (Optional) List of comma separated profileName values
    type: str
  resourcePartitionInfo:
    description:
    - (Optional) List of comma separated resource partitions, 'none' to search unpartitioned
      resource if user has sufficient privilege
    type: str
  resourceType:
    description:
    - (Optional) List of the management session resourceType
    type: str
  searchFields:
    description:
    - (Optional) List of comma separated fields to search on. If none are specified,
      all supported fields are implied. Fields require full path (e.g. data.attributes.name)
    type: str
  searchText:
    description:
    - (Optional) The searchable text
    type: str
  shortResourceType:
    description:
    - (Optional) List of the management session shortResourceType
    type: str
  sortBy:
    description:
    - (Optional) List of comma separated fields by which to sort the result. Fields
      require full path (i.e. data.attributes.field). A dash or negative sign before
      a field indicates descending order; by default ascending order is used
    type: str
  state:
    choices:
    - get
    - post
    description: []
    type: str
  states:
    description:
    - '(Optional) List of comma separated discoveryStates. <p> Valid values are: <table><tr><td>PENDING</td><td>
      - prior to enrollment</td></tr><tr><td>AUTO_DISCOVERED</td><td> - prior to enrollment
      and added by the enrollment of another network element</td></tr><tr><td>VALIDATING</td><td>
      - attempting to communicate with the network element</td></tr><tr><td>VALIDATING_FAILED</td><td>
      - communication with the network element failed</td></tr><tr><td>CONNECTING</td><td>
      - creating a session to the network element</td></tr><tr><td>POKING</td><td>
      - checking available accesses to the network element</td></tr><tr><td>CONNECTED</td><td>
      - session established with network element</td></tr><tr><td>DISCOVERING</td><td>
      - retrieving session data from network element</td></tr><tr><td>COMPLETED</td><td>
      - management session is fully operational and connected to the network element</td></tr><tr><td>DISCOVERY_RETRY</td><td>
      - failed to retrieve session data from the network element</td></tr><tr><td>CHANGE_SESSION</td><td>
      - attempting to changing the active session to the network element</td></tr><tr><td>DEENROLLING</td><td>
      - disconnecting from the network element and removing the management session</td></tr></table>'
    type: str
  typeGroup:
    description:
    - (Optional) List of the management session typeGroup
    type: str
author:
- Jeff Groom
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = [
    "aliasName",
    "aliasValue",
    "associationState",
    "associationStateQualifier",
    "associationStateQualifierReason",
    "displayAlternativeConnectionIPs",
    "displayAlternativeConnectionNames",
    "displayName",
    "displayPartitions",
    "displayPreferredConnectionName",
    "displayState",
    "ipAddress",
    "limit",
    "longName",
    "metaDataFields",
    "name",
    "offset",
    "profileId",
    "profileName",
    "resourcePartitionInfo",
    "resourceType",
    "searchFields",
    "searchText",
    "shortResourceType",
    "sortBy",
    "states",
    "typeGroup",
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
    argument_spec["typeGroup"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["states"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["state"] = {"type": "str", "choices": ["get", "post"]}
    argument_spec["sortBy"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["shortResourceType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["searchText"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["searchFields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["resourceType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["resourcePartitionInfo"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["profileName"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["profileId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["offset"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["name"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["metaDataFields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["longName"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["limit"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["ipAddress"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["displayState"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["displayPreferredConnectionName"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["displayPartitions"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["displayName"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["displayAlternativeConnectionNames"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["displayAlternativeConnectionIPs"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["data"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["associationStateQualifierReason"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["associationStateQualifier"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["associationState"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["aliasValue"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["aliasName"] = {"type": "str", "operationIds": ["get"]}
    return argument_spec


async def get_device_info(params, session, _url, _key):
    async with session.get(((_url + "/") + _key)) as resp:
        _json = await resp.json()
        entry = _json["value"]
        entry["_key"] = _key
        return entry


async def list_devices(params, session):
    existing_entries = []
    _url = url(params)
    async with session.get(_url) as resp:
        _json = await resp.json()
        devices = _json["value"]
    for device in devices:
        _id = list(device.values())[0]
        existing_entries.append((await get_device_info(params, session, _url, _id)))
    return existing_entries


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
    return "https://{mcp_hostname}/discovery/api/managementSessions".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _get(params, session):
    _url = "https://{mcp_hostname}/discovery/api/managementSessions".format(
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
    accepted_fields = ["data"]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = "https://{mcp_hostname}/discovery/api/managementSessions".format(**params)
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
