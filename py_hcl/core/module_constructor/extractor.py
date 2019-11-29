from py_hcl.core.module_constructor import ModuleError
from py_hcl.dsl.expr.expression import Expression


def extract(dct, name):
    res = {}

    for k, v in dct.items():
        if isinstance(v, Expression):
            res[k] = v

    check_io_exist(res, name)

    return res


def check_io_exist(res, name):
    if 'io' not in res:
        raise ModuleError.not_contains_io(
            'module {} lack of io attribute'.format(name))