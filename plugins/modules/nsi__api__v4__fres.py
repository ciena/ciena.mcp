from __future__ import absolute_import, division, print_function

__metaclass__ = type
import socket
import json

DOCUMENTATION = """
module: nsi__api__v4__fres
short_description: Handle resource of type nsi__api__v4__fres
description: Handle resource of type nsi__api__v4__fres
options:
  active:
    choices:
    - 'false'
    - 'true'
    description:
    - (Optional) The active state of the resource
    type: str
  adminState:
    description:
    - '(Optional) Allow filtering on FRE adminState. This parameter accepts a list
      of comma separated values: enabled, disabled, not applicable, In Service, Out
      of Service'
    type: str
  bookingData.lockout:
    choices:
    - 'false'
    - 'true'
    description:
    - (Optional)  Flag that enables/disables a link from having additional tunnel
      BW being consumed
    type: str
  childFreId:
    description:
    - (Optional) The child FRE identifier to return its parents
    type: str
  concrete:
    description:
    - (Optional) List of concrete FRE identifiers
    type: str
  coroutedFreId:
    description:
    - (Optional) Retrieves all correlated FREs that are co-routed and co-terminated
      with the specified FRE Id
    type: str
  customerName:
    description:
    - (Optional) Search for an exact match on customerName
    type: str
  data:
    description:
    - 'Validate attributes are:'
    - ' - C(attributes) (dict): '
    - ' - C(id) (str): The unique identifier for the FRE resource'
    - ' - C(meta) (dict): A metadata object that contains non-standard meta information'
    - ' - C(relationships) (dict): '
    - ' - C(type) (str): The FRE resource type'
    type: dict
  deploymentState:
    description:
    - (Optional) deploymentState parameter used to filter results
    type: str
  directionality:
    choices:
    - bidirectional
    - unidirectional
    description:
    - (Optional) Indicates if unidirectional or bidirectional FREs should be returned
    type: str
  displayAdminState:
    description:
    - (Optional) Allow filtering on FRE adminState display string
    type: str
  displayOperationState:
    description:
    - (Optional) Allow filtering on FRE operationState display string
    type: str
  displayTopologySource:
    description:
    - (Optional) Allow filtering on FRE topologySource display string. Currently will
      only be set to 'Retained' on Fres
    type: str
  endpoint.tpe.concrete:
    description:
    - Concrete TPE identifier for endpoints
    type: str
  exclude:
    choices:
    - actual
    - expectation
    description:
    - (Optional) The given type would be excluded from get parents call, only combine
      with childFreId
    type: str
  fields:
    description:
    - (Optional) List of comma separated fields to be included in the response. Fields
      require full path (i.e. data.attributes.field)
    type: str
  freExpectations.equipmentIntent.id:
    description:
    - (Optional) The equipment intent Id
    type: str
  freExpectations.serviceIntent.id:
    description:
    - (Optional) The service intent Id
    type: str
  freType:
    description:
    - 'FRE types in comma separated list The allowed values are: explicitRoute, explicitRouteGroup,
      snc, sncGroup'
    type: str
  group:
    choices:
    - dwa
    - infrastructure
    - packet
    - packet_infrastructure
    - tdm
    description:
    - (Optional, Deprecated) FRE group :<ul><li>dwa for all FREs in OTU4 and all top
      level FREs in ETHERNET, DSR, DSR_ETHERNET, OTSi(OCH), ODU2, ODU4, ODUCn, OTUCn<li>infrastructure
      for all FRE-APs representing forwarding constructs between ROADM OTS'<li>packet
      for all L2 nodal and top level FREs in ETHERNET including infrastructure</ul>
    type: str
  id:
    description:
    - (Optional) Comma separated list of FRE identifiers to retrieve
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
      values are: tpes, expectations, networkConstructs, planned, freDiscovered, frePlanned'
    type: str
  included:
    description:
    - Resources related to a FRE, such as FreData, EndPointData, TpeData, EquipmentData,
      EquipmentHolderData, FrePlannedData, FreExpectationData, FreDiscoveredData,
      ResiliencyControllerData, EncapsulatedResiliencyData
    type: list
  layerRate:
    description:
    - 'FRE layer rates in comma separated list.  The allowed values are: ETHERNET,
      OTU1, OTU2, OTU2e, OTU3, OTU4, OTUCn, OTSi, OMS, OS, PHY, OTS, FICON, FC, ODU,
      ODU0, ODU1, ODU2, ODU2e, ODU3, ODU4, ODUCn, DSR, DSR_10GE, DSR_100GE, DSR_ETHERNET,
      ENCAPSULATION, MPLS, MPLS_PROTECTION, MEDIA, LAG, RS, E1, E3, E1_2M, EC1, DSR_2M,
      LINE_OC3_STS3_AND_MS_STM1, SECTION_OC3_STS3_AND_RS_STM1, DSR_OC3_STM1, DSR_OC12_STM4,
      DSR_OC48_STM16, DSR_OC192_STM64, CES_IWF, T1, DSR_1_5M, STS1, STS3C, STS12C,
      STS24C, STS48C, DS0, DS1, DS3, VT15, VT2, NOT_APPLICABLE, ODUFLEX, OTUg, ODUg,
      BGP, IP'
    type: str
  layerRateQualifier:
    description:
    - (Optional) Indicates additional qualification information for a LayerRate. For
      example, for beyond 100G rates (e.g. OTUCn, ODUCn), defines the n multiplier,
      or the n-M subrate value.
    type: str
  limit:
    description:
    - The size of a returned page
    type: str
  links:
    description:
    - Links related to the resource
    - 'Validate attributes are:'
    - ' - C(current) (str): The current page of data'
    - ' - C(first) (str): The first page of data'
    - ' - C(last) (str): The last page of data'
    - ' - C(next) (str): The next page of data'
    - ' - C(prev) (str): The previous page of data'
    - ' - C(self) (str): A `self` member, whose value is a URL for the relationship
      itself (a "relationship URL"). This URL allows the client to directly manipulate
      the relationship. For example, it would allow a client to remove an `author`
      from an `article` without deleting the people resource itself.'
    type: dict
  lqsData.fiber.method:
    choices:
    - osc
    - totalPower
    description:
    - (Optional) Allow filtering on the LQS fiber method. This parameter accepts a
      list of comma separated values
    type: str
  lqsData.fiber.reconciled:
    choices:
    - 'false'
    - 'true'
    description:
    - (Optional) The LQS fiber reconciled state
    type: str
  lqsData.margin.valid:
    choices:
    - 'false'
    - 'true'
    description:
    - (Optional) The LQS margin validity state
    type: str
  lqsData.margin.viableAtEol:
    description:
    - (Optional) A list of LQS margin viable at EOL states
    type: str
  lqsData.status:
    choices:
    - good
    - high
    - low
    - upgrade
    description:
    - (Optional) Allow filtering on the LQS status. This parameter accepts a list
      of comma separated values
    type: str
  managementName:
    description:
    - Management Name
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
    - 'MetaData to be included. The allowed values are: layerRate, layerRateQualifier,
      signalContentType, serviceClass, sncgUserlabel, adminState, operationState,
      lqsData.status, lqsData.margin.valid, lqsData.fiber.reconciled, lqsData.fiber.method,
      lqsData.margin.viableAtEol, displayAdminState, displayOperationState, displayTopologySource,
      customerName'
    type: str
  modelType:
    description:
    - (Optional) modelType parameter used to filter results
    type: str
  namedQuery:
    description:
    - '(Optional) Comma-separated named query id list; The allowed values are: resiliency,
      tdmServices, topologicalLinks, roadmLineSpan'
    type: str
  networkConstruct.id:
    description:
    - Network Construct identifier
    type: str
  networkRole:
    choices:
    - FREAP
    - IFRE
    - IFRECP
    - ROADMLINE
    description:
    - (Optional) Determines if the FRE participates in an internal or external forwarding
      view or involves access points or connection points
    type: str
  offset:
    description:
    - Offset for the second page
    type: str
  operationState:
    description:
    - '(Optional) Allow filtering on FRE operationState. This parameter accepts a
      list of comma separated values: fully operating, not operating, degraded operation,
      Not Applicable, Undetermined, In Service, Degraded, Out of Service External,
      Out of Service'
    type: str
  resourceState:
    description:
    - '(Optional) List of fre planning states. By default, if no value for this parameter
      is specified, root and unknown states are filtered out. The allowed values are:
      root, planned, discovered, plannedAndDiscovered, unknown'
    type: str
  roadmLineId:
    description:
    - (Optional) Find services configured over a roadmline based on the roadmline
      FRE identifier.
    type: str
  searchFields:
    description:
    - (Optional) List of comma separated fields to search with, combined with searchText.
      Fields require full path (i.e. data.attributes.field)
    type: str
  searchText:
    description:
    - (Optional) The searchable text, (default search Fields are name, layerRate,
      tpeLocations if searchFields is not specified.)
    type: str
  serviceClass:
    choices:
    - EAccess
    - ETransit
    - EVC
    - Fiber
    - IP
    - L3VPN
    - LAG
    - LLDP
    - OSRP Line
    - OSRP Link
    - OTU
    - Photonic
    - ROADM Line
    - SNC
    - SNCP
    - TDM
    - Transport Client
    - Tunnel
    - VLAN
    description:
    - (Optional) Allow filtering on the FRE service class. This parameter accepts
      a list of comma separated values
    type: str
  signalContentType:
    description:
    - (Optional) The identifier indicating type of parent to be returned. If specified,
      parent matching the criteria will be returned
    type: str
  sncgUserlabel:
    description:
    - '(Optional) For Control Plane SNCs only: Retrieves all SNCs provided the parent
      SNCG userLabel'
    type: str
  sortBy:
    description:
    - (Optional) List of comma separated fields by which to sort the result. Fields
      require full path (i.e. data.attributes.field). A dash or negative sign before
      a field indicates descending order; by default ascending order is used
    type: str
  srlg:
    description:
    - (Optional) Find roadmlines by srlg values separated by comma. A roadmline is
      a FRE between two SAM cards.
    type: str
  state:
    choices:
    - get
    - post
    description: []
    type: str
  supportedByFreId:
    description:
    - (Optional) Retrieves all supported parent FREs (one serviceClass/layer level
      up) that have a serviceClass designation for the specified FRE Id
    type: str
  supportingFreId:
    description:
    - (Optional) Retrieves all supporting child FREs (one serviceClass/layer level
      down) that have a serviceClass designation for the specified FRE Id
    type: str
  tags:
    description:
    - (Optional) Allow filtering on FRE tags. This parameter accepts a list of comma
      separated strings
    type: str
  tpeId:
    description:
    - TPE identifier for endpoints
    type: str
  tunnelType:
    description:
    - '(Optional) Allow filtering on FRE Tunnel class service. This parameter accepts
      a list of comma separated values: dynamic, static'
    type: str
  type:
    description:
    - 'FRE types in comma separated list. The allowed values are: service, link, roadmline-ap,
      roadmline'
    type: str
  userLabel:
    description:
    - User label
    type: str
author:
- Jeff Groom
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = [
    "active",
    "adminState",
    "bookingData.lockout",
    "childFreId",
    "concrete",
    "coroutedFreId",
    "customerName",
    "deploymentState",
    "directionality",
    "displayAdminState",
    "displayOperationState",
    "displayTopologySource",
    "endpoint.tpe.concrete",
    "exclude",
    "fields",
    "freExpectations.equipmentIntent.id",
    "freExpectations.serviceIntent.id",
    "freType",
    "group",
    "id",
    "identifierKey",
    "identifierValue",
    "include",
    "layerRate",
    "layerRateQualifier",
    "limit",
    "lqsData.fiber.method",
    "lqsData.fiber.reconciled",
    "lqsData.margin.valid",
    "lqsData.margin.viableAtEol",
    "lqsData.status",
    "managementName",
    "metaDataFields",
    "modelType",
    "namedQuery",
    "networkConstruct.id",
    "networkRole",
    "offset",
    "operationState",
    "resourceState",
    "roadmLineId",
    "searchFields",
    "searchText",
    "serviceClass",
    "signalContentType",
    "sncgUserlabel",
    "sortBy",
    "srlg",
    "supportedByFreId",
    "supportingFreId",
    "tags",
    "tpeId",
    "tunnelType",
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
    argument_spec["tunnelType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["tpeId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["tags"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["supportingFreId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["supportedByFreId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["state"] = {"type": "str", "choices": ["get", "post"]}
    argument_spec["srlg"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["sortBy"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["sncgUserlabel"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["signalContentType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["serviceClass"] = {
        "type": "str",
        "choices": [
            "EAccess",
            "ETransit",
            "EVC",
            "Fiber",
            "IP",
            "L3VPN",
            "LAG",
            "LLDP",
            "OSRP Line",
            "OSRP Link",
            "OTU",
            "Photonic",
            "ROADM Line",
            "SNC",
            "SNCP",
            "TDM",
            "Transport Client",
            "Tunnel",
            "VLAN",
        ],
        "operationIds": ["get"],
    }
    argument_spec["searchText"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["searchFields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["roadmLineId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["resourceState"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["operationState"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["offset"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["networkRole"] = {
        "type": "str",
        "choices": ["FREAP", "IFRE", "IFRECP", "ROADMLINE"],
        "operationIds": ["get"],
    }
    argument_spec["networkConstruct.id"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["namedQuery"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["modelType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["metaDataFields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["meta"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["managementName"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["lqsData.status"] = {
        "type": "str",
        "choices": ["good", "high", "low", "upgrade"],
        "operationIds": ["get"],
    }
    argument_spec["lqsData.margin.viableAtEol"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["lqsData.margin.valid"] = {
        "type": "str",
        "choices": ["false", "true"],
        "operationIds": ["get"],
    }
    argument_spec["lqsData.fiber.reconciled"] = {
        "type": "str",
        "choices": ["false", "true"],
        "operationIds": ["get"],
    }
    argument_spec["lqsData.fiber.method"] = {
        "type": "str",
        "choices": ["osc", "totalPower"],
        "operationIds": ["get"],
    }
    argument_spec["links"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["limit"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["layerRateQualifier"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["layerRate"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["included"] = {"type": "list", "operationIds": ["post"]}
    argument_spec["include"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["identifierValue"] = {"type": "list", "operationIds": ["get"]}
    argument_spec["identifierKey"] = {"type": "list", "operationIds": ["get"]}
    argument_spec["id"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["group"] = {
        "type": "str",
        "choices": ["dwa", "infrastructure", "packet", "packet_infrastructure", "tdm"],
        "operationIds": ["get"],
    }
    argument_spec["freType"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["freExpectations.serviceIntent.id"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["freExpectations.equipmentIntent.id"] = {
        "type": "str",
        "operationIds": ["get"],
    }
    argument_spec["fields"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["exclude"] = {
        "type": "str",
        "choices": ["actual", "expectation"],
        "operationIds": ["get"],
    }
    argument_spec["endpoint.tpe.concrete"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["displayTopologySource"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["displayOperationState"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["displayAdminState"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["directionality"] = {
        "type": "str",
        "choices": ["bidirectional", "unidirectional"],
        "operationIds": ["get"],
    }
    argument_spec["deploymentState"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["data"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["customerName"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["coroutedFreId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["concrete"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["childFreId"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["bookingData.lockout"] = {
        "type": "str",
        "choices": ["false", "true"],
        "operationIds": ["get"],
    }
    argument_spec["adminState"] = {"type": "str", "operationIds": ["get"]}
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
    return "https://{mcp_hostname}/nsi/api/v4/fres".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _get(params, session):
    _url = "https://{mcp_hostname}/nsi/api/v4/fres".format(**params) + gen_args(
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
    accepted_fields = ["data", "included", "links", "meta"]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = "https://{mcp_hostname}/nsi/api/v4/fres".format(**params)
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
