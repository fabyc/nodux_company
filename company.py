#! -*- coding: utf8 -*-

from trytond.pool import *
import logging
from importlib import import_module
from trytond.model import ModelView, ModelSQL, fields
from trytond.wizard import Wizard, StateTransition, StateView, Button
from trytond.pyson import Bool, Eval, Id
from trytond.transaction import Transaction
import re

__all__ = ['Company']
__metaclass__ = PoolMeta

class Company:
    __name__ = 'company.company'

    logo_footer = fields.Binary('Logo Pie de Pagina')
