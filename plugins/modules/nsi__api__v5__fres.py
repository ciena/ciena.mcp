from __future__ import absolute_import, division, print_function

__metaclass__ = type
import socket
import json

DOCUMENTATION = """
module: nsi__api__v5__fres
short_description: Handle resource of type nsi__api__v5__fres
description: Handle resource of type nsi__api__v5__fres
options:
  childFreId:
    description:
    - The child FRE identifier to return its parents
    type: str
  endpoint.tpe.concrete:
    description:
    - Concrete TPE identifier for endpoints
    type: str
  exclude:
    description:
    - '(Optional) A single given type to be excluded used in conjunction with the
      `childFreId` parameter. The allowed values are: actual, expectation'
    type: str
  fields:
    description:
    - (Optional) List of comma separated fields to be included in the response. Fields
      require full path (i.e. data.attributes.field)
    type: str
  freExpectations.equipmentIntent.id:
    description:
    - The equipment intent Id
    type: str
  freExpectations.intent.id:
    description:
    - The intent Id
    type: str
  freExpectations.serviceIntent.id:
    description:
    - The service intent Id
    type: str
  freType:
    description:
    - '(Optional) FRE types in comma separated list. The allowed values are: explicitRoute,
      explicitRouteGroup, snc, sncGroup'
    type: str
  identifierKey:
    description:
    - List of comma separated keys for an identifer object
    type: list
  identifierValue:
    description:
    - List of comma separated values for an identifier object
    type: list
  include:
    description:
    - '(Optional) List of comma separated resources to be side-loaded. The allowed
      values are: tpes, expectations, frePlanned, freDiscovered'
    type: str
  layerRate:
    description:
    - '(Optional) FRE layer rates in comma separated list. Only applied when Network
      Construct identifier is provided. The allowed values are: ETHERNET, OTU2, OTU4,
      OTSi, OMS, OS, PHY, OTS, ODU2, ODU4, DSR, DSR_10GE, DSR_100GE, DSR_ETHERNET'
    type: str
  limit:
    description:
    - (Optional) The size of a returned page
    type: str
  networkConstruct.id:
    description:
    - Network Construct identifier
    type: str
  offset:
    description:
    - (Optional) Offset for the second page
    type: str
  roadmLineId:
    description:
    - (Optional) Find services configured over a roadmline based on the roadmline
      FRE identifier.
    type: str
  signalContentType:
    description:
    - (Optional) The identifier indicating type of parent to be returned. If specified,
      parent matching the criteria will be returned
    type: str
  state:
    choices:
    - get
    description: []
    type: str
  tpeId:
    description:
    - TPE identifier for endpoints
    type: str
author:
- Jeff Groom
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = [
    "childFreId",
    "endpoint.tpe.concrete",
    "exclude",
    "fields",
    "freExpectations.equipmentIntent.id",
    "freExpectations.intent.id",
    "freExpectations.serviceIntent.id",
    "freType",
    "identifierKey",
    "identifierValue",
    "include",
    "layerRate",
    "limit",
    "networkConstruct.id",
    "offset",
    "roadmLineId",
    "signalContentType",
    "tpeId",
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
    argument_spec["tpeId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["state"] = {"type": "str", "choices": ["get"]}
    argument_spec["signalContentType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["roadmLineId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["offset"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["networkConstruct.id"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["limit"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["layerRate"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["include"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["identifierValue"] = {"type": "list", "operationIds": ["get"]}
    argument_spec["identifierKey"] = {"type": "list", "operationIds": ["get"]}
    argument_spec["freType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["freExpectations.serviceIntent.id"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["freExpectations.intent.id"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["freExpectations.equipmentIntent.id"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["fields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["exclude"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["endpoint.tpe.concrete"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["childFreId"] = {"type": "str", "operationIds": ["get"]}
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
    return "https://{mcp_hostname}/nsi/api/v5/fres".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _get(params, session):
    _url = "https://{mcp_hostname}/nsi/api/v5/fres".format(**params) + gen_args(
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


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
