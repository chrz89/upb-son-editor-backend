'''
Created on 22.07.2016

@author: Jonas
'''
from enum import Enum

WORKSPACES = "workspaces"
PROJECTS = "projects"
PLATFORMS = "platforms"
CATALOGUES = "catalogues"
SERVICES = "services"
VNFS = "vnfs"
DATABASE_SQLITE_FILE = "sqlite:////tmp/test.db"


class Category(Enum):
    project = 1
    catalogue = 2
    platform = 3

def get_parent(request):
    parent = str(request.url_rule).split(sep="/")[3]
    return {
            PROJECTS:Category.project,
            CATALOGUES:Category.catalogue,
            PLATFORMS:Category.platform
    }[parent]