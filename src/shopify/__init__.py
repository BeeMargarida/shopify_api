#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Shopify API
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive Shopify API.
#
# Hive Shopify API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Shopify API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Shopify API. If not, see <http://www.apache.org/licenses/>.

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

from . import base
from . import cart
from . import order
from . import product
from . import shop
from . import smart_collection
from . import webhook

from .base import API, OAuthAPI
from .cart import CartAPI
from .order import OrderAPI
from .product import ProductAPI
from .shop import ShopAPI
from .smart_collection import SmartCollectionAPI
from .webhook import WebhookAPI
