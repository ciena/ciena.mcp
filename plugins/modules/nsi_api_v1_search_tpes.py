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
module: nsi_api_v1_search_tpes
short_description: Handle resource of type nsi_api_v1_search_tpes
description: Handle resource of type nsi_api_v1_search_tpes
options:
  active:
    choices:
    - 'false'
    - 'true'
    description:
    - (Optional) The active state of the resource
    - Used by I(state=['get'])
    type: str
  adjacencyType:
    description:
    - (optional) The adjacencyType. When combined with the layerRate queryParam, only
      looks for thespecified list of adjacencyTypes within the specified layerRate.
    - Used by I(state=['get'])
    type: str
  bookingData.lockout:
    choices:
    - 'false'
    - 'true'
    description:
    - (Optional)  Flag that enables/disables a link from having additional tunnel
      BW being consumed
    - Used by I(state=['get'])
    type: str
  concrete:
    description:
    - (Optional) Id of the concrete tpe
    - Used by I(state=['get'])
    type: str
  content:
    choices:
    - detail
    - summary
    description:
    - (Optional) The TPE content level
    - Used by I(state=['get'])
    type: str
  endDateMax:
    description:
    - '(Optional) Maximum value of endDate, format is: yyyy-MM-dd''T''HH:mm:ss.SSSZ'
    - Used by I(state=['get'])
    type: str
  endDateMin:
    description:
    - '(Optional) Minimum value of endDate, format is: yyyy-MM-dd''T''HH:mm:ss.SSSZ'
    - Used by I(state=['get'])
    type: str
  equipmentId:
    description:
    - (Optional) Equipment identifier. In case of usage with limit parameter, paging
      will be enabled.
    - Used by I(state=['get'])
    type: str
  fields:
    description:
    - (Optional) List of comma separated fields to be included in the response. Fields
      require full path (i.e. data.attributes.field)
    - Used by I(state=['get'])
    type: str
  gneSubnetName:
    description:
    - (Optional) GNE Subnet name of the TPE
    - Used by I(state=['get'])
    type: str
  id:
    description:
    - (Optional) Comma separated list of TPE identifiers to retrieve
    - Used by I(state=['get'])
    type: str
  identifierKey:
    description:
    - Used by I(state=['get'])
    type: list
  identifierValue:
    description:
    - (Optional) The comma separated identifier value set
    - Used by I(state=['get'])
    type: list
  include:
    description:
    - '(Optional) List of comma separated resources to be side-loaded. The allowed
      values are: expectations, concrete, networkConstructs'
    - Used by I(state=['get'])
    type: str
  layerRate:
    description:
    - (optional) The layerRate. When combined with the adjacencyType queryParam, only
      looks for thespecified list of adjacencyTypes within the specified layerRate.
    - Used by I(state=['get'])
    type: str
  limit:
    description:
    - The size of a returned page
    - Used by I(state=['get'])
    type: str
  location:
    description:
    - (Optional) TPE location delimited by dashes
    - Used by I(state=['get'])
    type: str
  locationFormat:
    description:
    - (Optional) Format for the given location; when not given, assume location is
      [[shelf-]slot-]port
    - Used by I(state=['get'])
    type: str
  metaDataFields:
    description:
    - '(Optional) List of meta data to be included. The allowed values are: stackDirection,
      layerRate, state, cardType, structureType, structureSubType, resourceState'
    - Used by I(state=['get'])
    type: str
  metaDataQualifiers:
    description:
    - '(Optional) List of meta data options. The allowed values are: absoluteTotals'
    - Used by I(state=['get'])
    type: str
  modelType:
    description:
    - (Optional) modelType parameter used to filter results
    - Used by I(state=['get'])
    type: str
  namedQuery:
    description:
    - '(Optional) Comma-separated named query id list; The allowed values are: ptpEthernetNoClients,
      portsEthernetAvailableAll, portsL2AvailableAll, portsL2ApplicableEPLUni, portsL2ApplicableEVPLUni,
      portsL2ApplicableEnni, portsL2ApplicableEPLUniWithMcLag, portsL2ApplicableEVPLUniWithMcLag,
      portsL2ApplicableEnniWithMcLag, portsTunnelsL2ApplicableAll, portsTunnelsL2ApplicableAllWithFtpIpData,
      portsTDMCEApplicableAll, channelTxPorts, channelRxPorts, linePorts, matedTpes<br><br>matedTpes
      cannot be used in combination with other named queries and can not be used alone,
      namedQueryParam1(tpeId),namedQueryParam2(Values are CHANNEL/OTN_ACCESS) and
      namedQueryParam3(Values are Working/Protect) must be provided with this named
      query.'
    - Used by I(state=['get'])
    type: str
  namedQueryParam1:
    description:
    - First param to be used by defined namedQuery.
    - Used by I(state=['get'])
    type: str
  namedQueryParam2:
    description:
    - Second param to be used by defined namedQuery.
    - Used by I(state=['get'])
    type: str
  namedQueryParam3:
    description:
    - Third param to be used by defined namedQuery.
    - Used by I(state=['get'])
    type: str
  networkConstruct.id:
    description:
    - (Optional) Network Construct identifier
    - Used by I(state=['get'])
    type: str
  offset:
    description:
    - Offset for the second page
    - Used by I(state=['get'])
    type: str
  resourceState:
    description:
    - '(Optional) List of networkConstruct planning states. By default, if no value
      for this parameter is specified, root and unknown states are filtered out. The
      allowed values are: root, planned, discovered, plannedAndDiscovered, unknown'
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
  sortBy:
    description:
    - (Optional) List of comma separated fields by which to sort the result. Fields
      require full path (i.e. data.attributes.field). A dash or negative sign before
      a field indicates descending order; by default ascending order is used
    - Used by I(state=['get'])
    type: str
  startDateMax:
    description:
    - '(Optional) Maximum value of startDate, format is: yyyy-MM-dd''T''HH:mm:ss.SSSZ'
    - Used by I(state=['get'])
    type: str
  startDateMin:
    description:
    - '(Optional) Minimum value of startDate, format is: yyyy-MM-dd''T''HH:mm:ss.SSSZ'
    - Used by I(state=['get'])
    type: str
  state:
    choices:
    - get
    description: []
    type: str
  structureType:
    description:
    - (Optional) Comma separated list of TPE structure types
    - Used by I(state=['get'])
    type: str
  tpeExpectations.equipmentIntent.id:
    description:
    - (Optional) The equipment intent Id
    - Used by I(state=['get'])
    type: str
  tpeExpectations.intent.id:
    description:
    - (Optional) The intent id
    - Used by I(state=['get'])
    type: str
  tpeExpectations.intent.type:
    description:
    - (Optional) The intent type
    - Used by I(state=['get'])
    type: str
  tpeExpectations.serviceIntent.id:
    description:
    - (Optional) The service intent Id
    - Used by I(state=['get'])
    type: str
author: []
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = [
    "active",
    "adjacencyType",
    "bookingData.lockout",
    "concrete",
    "content",
    "endDateMax",
    "endDateMin",
    "equipmentId",
    "fields",
    "gneSubnetName",
    "id",
    "identifierKey",
    "identifierValue",
    "include",
    "layerRate",
    "limit",
    "location",
    "locationFormat",
    "metaDataFields",
    "metaDataQualifiers",
    "modelType",
    "namedQuery",
    "namedQueryParam1",
    "namedQueryParam2",
    "namedQueryParam3",
    "networkConstruct.id",
    "offset",
    "resourceState",
    "searchFields",
    "searchText",
    "sortBy",
    "startDateMax",
    "startDateMin",
    "structureType",
    "tpeExpectations.equipmentIntent.id",
    "tpeExpectations.intent.id",
    "tpeExpectations.intent.type",
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
    argument_spec["tpeExpectations_serviceIntent_id"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["tpeExpectations_intent_type"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["tpeExpectations_intent_id"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["tpeExpectations_equipmentIntent_id"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["structureType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["state"] = {"type": "str", "choices": ["get"]}
    argument_spec["startDateMin"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["startDateMax"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["sortBy"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["searchText"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["searchFields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["resourceState"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["offset"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["networkConstruct_id"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["namedQueryParam3"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["namedQueryParam2"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["namedQueryParam1"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["namedQuery"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["modelType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["metaDataQualifiers"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["metaDataFields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["locationFormat"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["location"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["limit"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["layerRate"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["include"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["identifierValue"] = {"type": "list", "operationIds": ["get"]}
    argument_spec["identifierKey"] = {"type": "list", "operationIds": ["get"]}
    argument_spec["id"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["gneSubnetName"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["fields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["equipmentId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["endDateMin"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["endDateMax"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["content"] = {
        "type": "str",
        "choices": ["detail", "summary"],
        "operationIds": ["get"],
    }
    argument_spec["concrete"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["bookingData_lockout"] = {
        "type": "str",
        "choices": ["false", "true"],
        "operationIds": ["get"],
    }
    argument_spec["adjacencyType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["active"] = {
        "type": "str",
        "choices": ["false", "true"],
        "operationIds": ["get"],
    }
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
    return "https://{mcp_hostname}/nsi/api/v1/search/tpes".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _get(params, session):
    _url = "https://{mcp_hostname}/nsi/api/v1/search/tpes".format(**params) + gen_args(
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
