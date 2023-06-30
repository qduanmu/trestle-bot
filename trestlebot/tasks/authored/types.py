#!/usr/bin/python

#    Copyright 2023 Red Hat, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Trestle Bot authoring type information"""

from enum import Enum

from trestle.common import const

from trestlebot.tasks.authored.base_authored import (
    AuthoredObjectException,
    AuthorObjectBase,
)
from trestlebot.tasks.authored.catalog import AuthoredCatalog
from trestlebot.tasks.authored.compdef import AuthoredComponentsDefinition
from trestlebot.tasks.authored.profile import AuthoredProfile
from trestlebot.tasks.authored.ssp import AuthoredSSP, SSPIndex


class AuthoredType(Enum):
    """Top-level OSCAL models that have authoring support"""

    CATALOG = "catalog"
    PROFILE = "profile"
    SSP = "ssp"
    COMPDEF = "compdef"


def get_authored_object(
    input_type: str, working_dir: str, ssp_index_path: str = ""
) -> AuthorObjectBase:
    """Determine and configure author object context"""
    if input_type == AuthoredType.CATALOG.value:
        return AuthoredCatalog(working_dir)
    elif input_type == AuthoredType.PROFILE.value:
        return AuthoredProfile(working_dir)
    elif input_type == AuthoredType.COMPDEF.value:
        return AuthoredComponentsDefinition(working_dir)
    elif input_type is AuthoredType.SSP.value:
        ssp_index: SSPIndex = SSPIndex(ssp_index_path)
        return AuthoredSSP(working_dir, ssp_index)
    else:
        raise AuthoredObjectException(f"Invalid authored type {input_type}")


def get_trestle_model_dir(input_type: str) -> str:
    """Determine directory for JSON content in trestle"""
    if input_type == AuthoredType.CATALOG.value:
        return const.MODEL_DIR_CATALOG
    elif input_type == AuthoredType.PROFILE.value:
        return const.MODEL_DIR_PROFILE
    elif input_type == AuthoredType.COMPDEF.value:
        return const.MODEL_DIR_COMPDEF
    elif input_type is AuthoredType.SSP.value:
        return const.MODEL_DIR_SSP
    else:
        raise AuthoredObjectException(f"Invalid authored type {input_type}")
