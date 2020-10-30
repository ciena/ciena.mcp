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
module: resources_by_resourceid_promote
short_description: Handle resource of type resources_by_resourceid_promote
description: Handle resource of type resources_by_resourceid_promote
options:
  autoClean:
    description:
    - Free up any resources automatically upon any activation failure
    - Used by I(state=['post'])
    type: bool
  createdAt:
    description:
    - Time of creation
    - Used by I(state=['post'])
    type: str
  description:
    description:
    - Detailed description of this resource
    - Used by I(state=['post'])
    type: str
  desiredOrchState:
    description:
    - Desired orchestration state
    - Used by I(state=['post'])
    type: str
  differences:
    description:
    - Differences represent the difference between desired and observed state
    - Used by I(state=['post'])
    type: list
  discovered:
    description:
    - Is this resource discovered
    - Used by I(state=['post'])
    type: bool
  id:
    description:
    - Unique identifier for the resource (optional/ignored on calls to create)
    - Used by I(state=['post'])
    type: str
  label:
    description:
    - Textual label
    - Used by I(state=['post'])
    type: str
  nativeState:
    description:
    - Native (type specific) state
    - Used by I(state=['post'])
    type: str
  orchState:
    description:
    - Current state of the resource in the orchestrator
    - Used by I(state=['post'])
    type: str
  orderId:
    description:
    - If applicable, the order containing this resource
    - Used by I(state=['post'])
    type: str
  productId:
    description:
    - The type of product for this resource
    - Used by I(state=['post'])
    type: str
  properties:
    description:
    - Properties
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    - Used by I(state=['post'])
    type: dict
  providerData:
    description:
    - Provider custom data
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    - Used by I(state=['post'])
    type: dict
  providerResourceId:
    description:
    - Identifier of the resource in provider's context
    - Used by I(state=['post'])
    type: str
  reason:
    description:
    - Reason for the orchestration state
    - Used by I(state=['post'])
    type: str
  resourceId:
    description:
    - Identifier of the resource to promote
    - Required with I(state=['post'])
    - Used by I(state=['post'])
    type: str
  resourceTypeId:
    description:
    - The type of this resource
    - Used by I(state=['post'])
    type: str
  revision:
    description:
    - Strictly increasing revision number, incremented every update including observed
      update
    - Used by I(state=['post'])
    type: int
  shared:
    description:
    - Is resource shared?
    - Used by I(state=['post'])
    type: bool
  sharingPermissionId:
    description:
    - The sharing permission associated with the resource
    - Used by I(state=['post'])
    type: str
  state:
    choices:
    - post
    description: []
    type: str
  subDomainId:
    description:
    - Identifier of the resource's sub-domain
    - Used by I(state=['post'])
    type: str
  tags:
    description:
    - Tags
    - Used by I(state=['post'])
    type: dict
  tenantId:
    description:
    - Owner tenant of the resource?
    - Used by I(state=['post'])
    type: str
  updateCount:
    description:
    - Monotonically increasing count of updates applied to this resource
    - Used by I(state=['post'])
    type: int
  updateReason:
    description:
    - Reason for the update state
    - Used by I(state=['post'])
    type: str
  updateState:
    description:
    - Current state of updating the resource, or `unset`
    - Used by I(state=['post'])
    type: dict
  updatedAt:
    description:
    - Time of last update
    - Used by I(state=['post'])
    type: str
author: []
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = []
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
    argument_spec["updatedAt"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["updateState"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["updateReason"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["updateCount"] = {"type": "int", "operationIds": ["post"]}
    argument_spec["tenantId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["tags"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["subDomainId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["state"] = {"type": "str", "choices": ["post"]}
    argument_spec["sharingPermissionId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["shared"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["revision"] = {"type": "int", "operationIds": ["post"]}
    argument_spec["resourceTypeId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["resourceId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["reason"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["providerResourceId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["providerData"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["properties"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["productId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["orderId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["orchState"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["nativeState"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["label"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["id"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["discovered"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["differences"] = {"type": "list", "operationIds": ["post"]}
    argument_spec["desiredOrchState"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["description"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["createdAt"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["autoClean"] = {"type": "bool", "operationIds": ["post"]}
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
    return "https://{mcp_hostname}/bpocore/market/api/v1/resources/{resourceId}/promote".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _post(params, session):
    accepted_fields = [
        "autoClean",
        "createdAt",
        "description",
        "desiredOrchState",
        "differences",
        "discovered",
        "id",
        "label",
        "nativeState",
        "orchState",
        "orderId",
        "productId",
        "properties",
        "providerData",
        "providerResourceId",
        "reason",
        "resourceId",
        "resourceTypeId",
        "revision",
        "shared",
        "sharingPermissionId",
        "subDomainId",
        "tags",
        "tenantId",
        "updateCount",
        "updateReason",
        "updateState",
        "updatedAt",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i] is not None:
            spec[i] = params[i]
    _url = "https://{mcp_hostname}/bpocore/market/api/v1/resources/{resourceId}/promote".format(
        **params
    ) + gen_args(
        params, IN_QUERY_PARAMETER
    )
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
