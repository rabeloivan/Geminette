from .ex00.test_ex00 import run_C02_ex00
from .ex01.test_ex01 import run_C02_ex01
from .ex02.test_ex02 import run_C02_ex02
from .ex03.test_ex03 import run_C02_ex03
from .ex04.test_ex04 import run_C02_ex04
from .ex05.test_ex05 import run_C02_ex05
from .ex06.test_ex06 import run_C02_ex06
from .ex07.test_ex07 import run_C02_ex07
from .ex08.test_ex08 import run_C02_ex08
from .ex09.test_ex09 import run_C02_ex09
from .ex10.test_ex10 import run_C02_ex10
from .ex11.test_ex11 import run_C02_ex11
from .ex12.test_ex12 import run_C02_ex12


def get_mapping():
    return {
        "ex00/ft_strcpy.c": ("ex00", None),
        "ex01/ft_strncpy.c": ("ex01", None),
        "ex02/ft_str_is_alpha.c": ("ex02", None),
        "ex03/ft_str_is_numeric.c": ("ex03", None),
        "ex04/ft_str_is_lowercase.c": ("ex04", None),
        "ex05/ft_str_is_uppercase.c": ("ex05", None),
        "ex06/ft_str_is_printable.c": ("ex06", None),
        "ex07/ft_strupcase.c": ("ex07", None),
        "ex08/ft_strlowcase.c": ("ex08", None),
        "ex09/ft_strcapitalize.c": ("ex08", None),
        "ex10/ft_strlcpy.c": ("ex08", None),
        "ex11/ft_putstr_non_printable.c": ("ex08", None),
        "ex12/ft_print_memory.c": ("ex08", None),
    }
