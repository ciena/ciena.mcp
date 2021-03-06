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
module: nsi_api_v1_search_equipment
short_description: Handle resource of type nsi_api_v1_search_equipment
description: Handle resource of type nsi_api_v1_search_equipment
options:
  availabilityState:
    description:
    - '(Optional) List of Equipment availabilityState. The allowed values are: PLANNED,
      AVAILABLE, UNVALIDATED, INUSE'
    - Used by I(state=['get'])
    type: str
  cardType:
    description:
    - (Optional) List of Equipment cardType
    - Used by I(state=['get'])
    type: str
  category:
    description:
    - '(Optional) List of Equipment category. The allowed values are: rack, shelf,
      pluggable, standalone'
    - Used by I(state=['get'])
    type: str
  displayAvailabilityState:
    description:
    - '(Optional) List of equipment displayAvailabilityState values. The allowed values
      are: Planned, Unvalidated, Available, In use'
    - Used by I(state=['get'])
    type: str
  displayState:
    description:
    - '(Optional) List of equipment displayState values. The allowed values are: IS,
      OOS, OOS-AU, OOS-MA, OOS-AUMA'
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
  equipmentExpectations.equipmentIntent.id:
    description:
    - (Optional) Equipment Intent Identifier
    - Used by I(state=['get'])
    type: str
  fields:
    description:
    - (Optional) List of comma separated fields to be included in the response. Fields
      require full path (i.e. data.attributes.field)
    - Used by I(state=['get'])
    type: str
  id:
    description:
    - (Optional) List of equipment Ids
    - Used by I(state=['get'])
    type: str
  include:
    description:
    - '(Optional) List of comma separated resources to be side-loaded. The allowed
      values are: expectations, planned, discovered, networkConstructs, equipmentPlanned,
      equipmentDiscovered'
    - Used by I(state=['get'])
    type: str
  limit:
    description:
    - The size of a returned page
    - Used by I(state=['get'])
    type: str
  maintenanceMode:
    description:
    - '(Optional) List of Equipment maintenanceMode. The allowed values are: true,
      false'
    - Used by I(state=['get'])
    type: str
  metaDataFields:
    description:
    - '(Optional) List of meta data to be included. The allowed values are: specificationMismatch,
      state, availabilityState, reservationState, maintenanceMode, cardType, category,
      ncMacAddress, ncSubnetName, projectName, displayAvailabilityState, displayState'
    - Used by I(state=['get'])
    type: str
  metaDataQualifiers:
    description:
    - '(Optional) List of meta data options. The allowed values are: absoluteTotals'
    - Used by I(state=['get'])
    type: str
  neContactState:
    description:
    - '(Optional) List of neContactState. The allowed values are: IN, OUT'
    - Used by I(state=['get'])
    type: str
  networkConstruct.id:
    description:
    - (Optional) Network Construct identifier
    - Used by I(state=['get'])
    type: str
  networkConstruct.macAddress:
    description:
    - (Optional) Network Construct macAddress
    - Used by I(state=['get'])
    type: str
  networkConstruct.name:
    description:
    - (Optional) Network Construct name
    - Used by I(state=['get'])
    type: str
  networkConstruct.subnetName:
    description:
    - (Optional) Network Construct subnetName
    - Used by I(state=['get'])
    type: str
  offset:
    description:
    - (Optional) Offset for current index of data to return
    - Used by I(state=['get'])
    type: str
  projectName:
    description:
    - (Optional) Project name
    - Used by I(state=['get'])
    type: str
  reservationState:
    description:
    - '(Optional) List of Equipment reservationState. The allowed values are: Unknown,
      Not reserved, Reserved for maintenance, Reserved for facility, Reserved for
      reversion'
    - Used by I(state=['get'])
    type: str
  resourceState:
    description:
    - '(Optional) List of resource states. By default, if no value for this parameter
      is specified, root and unknown states are filtered out. The allowed values are:
      root, planned, discovered, plannedAndDiscovered, unknown'
    - Used by I(state=['get'])
    type: str
  searchFields:
    description:
    - (Optional) List of comma separated fields to search on. If none are specified,
      all supported fields are implied. Fields require full path (e.g. data.attributes.siteName).
      If provided, must also provide searchText parameter
    - Used by I(state=['get'])
    type: str
  searchText:
    description:
    - (Optional) The searchable text
    - Used by I(state=['get'])
    type: str
  shelf:
    description:
    - (Optional) Comma separated list of equipment shelves
    - Used by I(state=['get'])
    type: str
  siteId:
    description:
    - (Optional) Site Identifier for equipment
    - Used by I(state=['get'])
    type: str
  slot:
    description:
    - (Optional) Comma separated list of equipment slots
    - Used by I(state=['get'])
    type: str
  sortBy:
    description:
    - (Optional) List of comma separated fields by which to sort the result. Fields
      require full path (i.e. data.attributes.field). A dash or negative sign before
      a field indicates descending order; by default ascending order is used
    - Used by I(state=['get'])
    type: str
  specificationMismatch:
    description:
    - '(Optional) List of Equipment specificationMismatch. The allowed values are:
      true, false'
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
  subShelf:
    description:
    - (Optional) Comma separated list of equipment sub-shelves
    - Used by I(state=['get'])
    type: str
  subSlot:
    description:
    - (Optional) Comma separated list of equipment sub-slots
    - Used by I(state=['get'])
    type: str
  subsubSlot:
    description:
    - (Optional) Comma separated list of equipment sub-sub-slots
    - Used by I(state=['get'])
    type: str
author: []
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = [
    "availabilityState",
    "cardType",
    "category",
    "displayAvailabilityState",
    "displayState",
    "endDateMax",
    "endDateMin",
    "equipmentExpectations.equipmentIntent.id",
    "fields",
    "id",
    "include",
    "limit",
    "maintenanceMode",
    "metaDataFields",
    "metaDataQualifiers",
    "neContactState",
    "networkConstruct.id",
    "networkConstruct.macAddress",
    "networkConstruct.name",
    "networkConstruct.subnetName",
    "offset",
    "projectName",
    "reservationState",
    "resourceState",
    "searchFields",
    "searchText",
    "shelf",
    "siteId",
    "slot",
    "sortBy",
    "specificationMismatch",
    "startDateMax",
    "startDateMin",
    "subShelf",
    "subSlot",
    "subsubSlot",
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
    argument_spec["subsubSlot"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["subSlot"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["subShelf"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["state"] = {"type": "str", "choices": ["get"]}
    argument_spec["startDateMin"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["startDateMax"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["specificationMismatch"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["sortBy"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["slot"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["siteId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["shelf"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["searchText"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["searchFields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["resourceState"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["reservationState"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["projectName"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["offset"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["networkConstruct_subnetName"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["networkConstruct_name"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["networkConstruct_macAddress"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["networkConstruct_id"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["neContactState"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["metaDataQualifiers"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["metaDataFields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["maintenanceMode"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["limit"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["include"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["id"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["fields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["equipmentExpectations_equipmentIntent_id"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["endDateMin"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["endDateMax"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["displayState"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["displayAvailabilityState"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["category"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["cardType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["availabilityState"] = {"type": "str", "operationIds": ["get"]}
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
    return "https://{mcp_hostname}/nsi/api/v1/search/equipment".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _get(params, session):
    _url = "https://{mcp_hostname}/nsi/api/v1/search/equipment".format(
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
