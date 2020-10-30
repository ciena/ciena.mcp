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
module: ifd_api_v1_serviceintents
short_description: Handle resource of type ifd_api_v1_serviceintents
description: Handle resource of type ifd_api_v1_serviceintents
options:
  data:
    description:
    - Resource to specify intent to design and fulfill one service.
    - 'Validate attributes are:'
    - ' - C(attributes) (dict): Attributes of the Service Intent Request. All supported
      services are PointToPoint at this time.'
    - Used by I(state=['post'])
    type: dict
  label:
    description:
    - (Optional) Retrieve service intents with the specified service user label
    - Used by I(state=['get'])
    type: str
  layerRates:
    description:
    - (Optional) Retrieve service intents that operate at the given layer rate(s)
    - Used by I(state=['get'])
    type: list
  roadmLineName:
    description:
    - (Optional) Retrieve service intents that utilize the named ROADM Line
    - Used by I(state=['get'])
    type: str
  state:
    choices:
    - get
    - post
    description: []
    type: str
  supportingServiceName:
    description:
    - (Optional) Retrieve all client service intents for the specified supporting
      (infrastructure) service name
    - Used by I(state=['get'])
    type: str
author: []
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = ["label", "layerRates", "roadmLineName", "supportingServiceName"]
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
    argument_spec["supportingServiceName"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["state"] = {"type": "str", "choices": ["get", "post"]}
    argument_spec["roadmLineName"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["layerRates"] = {"type": "list", "operationIds": ["get"]}
    argument_spec["label"] = {"type": "str", "operationIds": ["get"]}
    argument_spec["data"] = {"type": "dict", "operationIds": ["post"]}
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
    return "https://{mcp_hostname}/ifd/api/v1/serviceIntents".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _get(params, session):
    _url = "https://{mcp_hostname}/ifd/api/v1/serviceIntents".format(
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
        if params[i] is not None:
            spec[i] = params[i]
    _url = "https://{mcp_hostname}/ifd/api/v1/serviceIntents".format(
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