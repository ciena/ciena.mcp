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
module: nsi_api_v3_fres
short_description: Handle resource of type nsi_api_v3_fres
description: Handle resource of type nsi_api_v3_fres
options:
  childFreId:
    description:
    - The child FRE identifier to return its parents
    - Used by I(state=['get'])
    type: str
  endpoint.tpe.concrete:
    description:
    - Concrete TPE identifier for endpoints
    - Used by I(state=['get'])
    type: str
  exclude:
    choices:
    - actual
    - expectation
    description:
    - (Optional) The given type would be excluded from get parents call, only combine
      with childFreId
    - Used by I(state=['get'])
    type: str
  fields:
    description:
    - (Optional) List of comma separated fields to be included in the response. Fields
      require full path (i.e. data.attributes.field)
    - Used by I(state=['get'])
    type: str
  freExpectations.equipmentIntent.id:
    description:
    - The equipment intent Id
    - Used by I(state=['get'])
    type: str
  freExpectations.serviceIntent.id:
    description:
    - The service intent Id
    - Used by I(state=['get'])
    type: str
  freType:
    description:
    - '(Optional) FRE types in comma separated list. The allowed values are: explicitRoute,
      explicitRouteGroup, snc, sncGroup'
    - Used by I(state=['get'])
    type: str
  group:
    choices:
    - dwa
    - infrastructure
    - packet
    description:
    - FRE group :<ul><li>dwa for all FREs in OTU4 and all top level FREs in ETHERNET,
      DSR, DSR_ETHERNET, OTSi(OCH), ODU2, ODU4<li>infrastructure for all FRE-APs representing
      forwarding constructs between ROADM OTS'<li>packet for all L2 nodal and top
      level FREs in ETHERNET including infrastructure</ul>
    - Used by I(state=['get'])
    type: str
  identifierKey:
    description:
    - List of comma separated keys for an identifer object
    - Used by I(state=['get'])
    type: list
  identifierValue:
    description:
    - List of comma separated values for an identifier object
    - Used by I(state=['get'])
    type: list
  include:
    description:
    - '(Optional) List of comma separated resources to be side-loaded. The allowed
      values are: tpes, expectations, planned (roadmlines), frePlanned, freDiscovered'
    - Used by I(state=['get'])
    type: str
  includeMetaData:
    description:
    - '(Optional) MetaData to be included. The allowed values are: layerRate'
    - Used by I(state=['get'])
    type: str
  layerRate:
    description:
    - '(Optional) FRE layer rates in comma separated list. The allowed values are:
      ETHERNET, OTU2, OTU4, OTSi, OMS, OS, PHY, OTS, ODU2, ODU4, DSR, DSR_10GE, DSR_100GE,
      DSR_ETHERNET'
    - Used by I(state=['get'])
    type: str
  limit:
    description:
    - (Optional) The size of a returned page
    - Used by I(state=['get'])
    type: str
  managementName:
    description:
    - (Optional) Management Name
    - Used by I(state=['get'])
    type: str
  networkConstruct.id:
    description:
    - Network Construct identifier
    - Used by I(state=['get'])
    type: str
  offset:
    description:
    - (Optional) Offset for the second page
    - Used by I(state=['get'])
    type: str
  roadmLineId:
    description:
    - (Optional) Find services configured over a roadmline based on the roadmline
      FRE identifier.
    - Used by I(state=['get'])
    type: str
  searchText:
    description:
    - (Optional) The searchable text
    - Used by I(state=['get'])
    type: str
  signalContentType:
    description:
    - (Optional) The identifier indicating type of parent to be returned. If specified,
      parent matching the criteria will be returned
    - Used by I(state=['get'])
    type: str
  srlg:
    description:
    - (Optional) Find roadmlines by srlg values separated by comma. A roadmline is
      a FRE between two SAM cards.
    - Used by I(state=['get'])
    type: str
  state:
    choices:
    - get
    description: []
    type: str
  tpeId:
    description:
    - TPE identifier for endpoints
    - Used by I(state=['get'])
    type: str
  type:
    description:
    - '(Optional) FRE types in comma separated list. The allowed values are: service,
      link, roadmline-ap, roadmline'
    - Used by I(state=['get'])
    type: str
  userLabel:
    description:
    - (Optional) User label
    - Used by I(state=['get'])
    type: str
author: []
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
    "freExpectations.serviceIntent.id",
    "freType",
    "group",
    "identifierKey",
    "identifierValue",
    "include",
    "includeMetaData",
    "layerRate",
    "limit",
    "managementName",
    "networkConstruct.id",
    "offset",
    "roadmLineId",
    "searchText",
    "signalContentType",
    "srlg",
    "tpeId",
    "type",
    "userLabel",
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
    argument_spec["userLabel"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["type"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["tpeId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["state"] = {"type": "str", "choices": ["get"]}
    argument_spec["srlg"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["signalContentType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["searchText"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["roadmLineId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["offset"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["networkConstruct_id"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["managementName"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["limit"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["layerRate"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["includeMetaData"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["include"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["identifierValue"] = {"type": "list", "operationIds": ["get"]}
    argument_spec["identifierKey"] = {"type": "list", "operationIds": ["get"]}
    argument_spec["group"] = {
        "type": "str",
        "choices": ["dwa", "infrastructure", "packet"],
        "operationIds": ["get"],
    }
    argument_spec["freType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["freExpectations_serviceIntent_id"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["freExpectations_equipmentIntent_id"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["fields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["exclude"] = {
        "type": "str",
        "choices": ["actual", "expectation"],
        "operationIds": ["get"],
    }
    argument_spec["endpoint_tpe_concrete"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["childFreId"] = {"type": "str", "operationIds": ["get"]}
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
    return "https://{mcp_hostname}/nsi/api/v3/fres".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _get(params, session):
    _url = "https://{mcp_hostname}/nsi/api/v3/fres".format(**params) + gen_args(
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
