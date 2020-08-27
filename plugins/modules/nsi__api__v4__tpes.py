from __future__ import absolute_import, division, print_function

__metaclass__ = type
import socket
import json

DOCUMENTATION = """
module: nsi__api__v4__tpes
short_description: Handle resource of type nsi__api__v4__tpes
description: Handle resource of type nsi__api__v4__tpes
options:
  active:
    choices:
    - 'false'
    - 'true'
    description:
    - (Optional) The active state of the resource
    type: str
  bookingData.lockout:
    choices:
    - 'false'
    - 'true'
    description:
    - (Optional)  Flag that enables/disables a link from having additional tunnel
      BW being consumed
    type: str
  concrete:
    description:
    - (Optional) Id of the concrete tpe
    type: str
  content:
    choices:
    - detail
    - summary
    description:
    - (Optional) The TPE content level
    type: str
  data:
    description:
    - 'Validate attributes are:'
    - ' - C(attributes) (dict): '
    - ' - C(id) (str): The unique identifier for the TPE resource'
    - ' - C(meta) (dict): A metadata object that contains non-standard meta information'
    - ' - C(relationships) (dict): '
    - ' - C(type) (str): The TPE resource type'
    type: dict
  equipmentId:
    description:
    - (Optional) Equipment identifier. In case of usage with limit parameter, paging
      will be enabled.
    type: str
  fields:
    description:
    - (Optional) List of comma separated fields to be included in the response. Fields
      require full path (i.e. data.attributes.field)
    type: str
  gneSubnetName:
    description:
    - (Optional) GNE Subnet name of the TPE
    type: str
  id:
    description:
    - (Optional) Comma separated list of TPE identifiers to retrieve
    type: str
  identifierKey:
    description:
    - (Optional) The comma separated identifier key set
    type: list
  identifierValue:
    description:
    - (Optional) The comma separated identifier value set
    type: list
  include:
    description:
    - '(Optional) List of comma separated resources to be side-loaded. The allowed
      values are: expectations, concrete, networkConstructs'
    type: str
  included:
    description:
    - Referenced sub-resources
    type: list
  limit:
    description:
    - The size of a returned page
    type: str
  location:
    description:
    - (Optional) TPE location delimited by dashes
    type: str
  locationFormat:
    description:
    - (Optional) Format for the given location; when not given, assume location is
      [[shelf-]slot-]port
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
    type: dict
  metaDataFields:
    description:
    - '(Optional) List of meta data to be included. The allowed values are: stackDirection,
      layerRate, state, cardType, structureType, structureSubType, resourceState'
    type: str
  modelType:
    description:
    - (Optional) modelType parameter used to filter results
    type: str
  namedQuery:
    description:
    - '(Optional) Comma-separated named query id list; The allowed values are: portsL2AvailableAll,
      portsL2ApplicableEPLUni, portsL2ApplicableEVPLUni, portsL2ApplicableEnni, portsL2ApplicableEPLUniWithMcLag,
      portsL2ApplicableEVPLUniWithMcLag, portsL2ApplicableEnniWithMcLag, portsTunnelsL2ApplicableAll,
      portsTDMCEApplicableAll'
    type: str
  networkConstruct.id:
    description:
    - (Optional) Network Construct identifier
    type: str
  offset:
    description:
    - Offset for the second page
    type: str
  resourceState:
    description:
    - '(Optional) List of networkConstruct planning states. By default, if no value
      for this parameter is specified, root and unknown states are filtered out. The
      allowed values are: root, planned, discovered, plannedAndDiscovered, unknown'
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
  structureType:
    description:
    - (Optional) Comma separated list of TPE structure types
    type: str
  tpeExpectations.equipmentIntent.id:
    description:
    - (Optional) The equipment intent Id
    type: str
  tpeExpectations.serviceIntent.id:
    description:
    - (Optional) The service intent Id
    type: str
author:
- Jeff Groom
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = [
    "active",
    "bookingData.lockout",
    "concrete",
    "content",
    "equipmentId",
    "fields",
    "gneSubnetName",
    "id",
    "identifierKey",
    "identifierValue",
    "include",
    "limit",
    "location",
    "locationFormat",
    "metaDataFields",
    "modelType",
    "namedQuery",
    "networkConstruct.id",
    "offset",
    "resourceState",
    "searchFields",
    "searchText",
    "sortBy",
    "structureType",
    "tpeExpectations.equipmentIntent.id",
    "tpeExpectations.serviceIntent.id",
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
    argument_spec["tpeExpectations.serviceIntent.id"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["tpeExpectations.equipmentIntent.id"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["structureType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["state"] = {"type": "str", "choices": ["get", "post"]}
    argument_spec["sortBy"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["searchText"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["searchFields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["resourceState"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["offset"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["networkConstruct.id"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["namedQuery"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["modelType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["metaDataFields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["meta"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["locationFormat"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["location"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["limit"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["included"] = {"type": "list", "operationIds": ["post"]}
    argument_spec["include"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["identifierValue"] = {"type": "list", "operationIds": ["get"]}
    argument_spec["identifierKey"] = {"type": "list", "operationIds": ["get"]}
    argument_spec["id"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["gneSubnetName"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["fields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["equipmentId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["data"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["content"] = {
        "type": "str",
        "choices": ["detail", "summary"],
        "operationIds": ["get"],
    }
    argument_spec["concrete"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["bookingData.lockout"] = {
        "type": "str",
        "choices": ["false", "true"],
        "operationIds": ["get"],
    }
    argument_spec["active"] = {
        "type": "str",
        "choices": ["false", "true"],
        "operationIds": ["get"],
    }
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
    return "https://{mcp_hostname}/nsi/api/v4/tpes".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _get(params, session):
    _url = "https://{mcp_hostname}/nsi/api/v4/tpes".format(**params) + gen_args(
        params, IN_QUERY_PARAMETER
    )
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
        if params[i]:
            spec[i] = params[i]
    _url = "https://{mcp_hostname}/nsi/api/v4/tpes".format(**params)
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
