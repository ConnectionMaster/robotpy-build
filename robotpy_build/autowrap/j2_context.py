#
# These dataclasses hold data to be rendered by the *.j2 files in templates
#

from dataclasses import dataclass, field
from robotpy_build.config.autowrap_yml import ClassData
import typing

Documentation = typing.Optional[typing.List[str]]


@dataclass
class EnumeratorContext:

    #: Name in C++
    cpp_name: str

    #: Name in python
    py_name: str

    #: Documentation
    doc: Documentation


@dataclass
class EnumContext:

    #: Name of parent variable in initializer
    scope_var: str

    #: Name of variable in initializer
    var_name: str

    #: C++ name, including namespace/classname
    full_cpp_name: str

    #: Python name
    py_name: str

    #: Enum values
    values: typing.List[EnumeratorContext]

    #: Documentation
    doc: Documentation


@dataclass
class ClassContext:

    full_cpp_name: str

    #: Name of parent variable in initializer
    scope_var: str

    #: Name of variable in initializer
    var_name: str

    # used for dealing with methods/etc
    cls_key: str
    data: ClassData
    has_trampoline: bool
    final: bool

    # cls_using
    # - typealias
    # - constants

    #: Documentation
    doc: Documentation

    bases: typing.List[BaseClassData]

    # header:

    # extra_includes/extra_includes_first

    trampoline: typing.Optional[TrampolineData]

    # add default constructor
    # {% if not cls.x_has_constructor and not cls.data.nodelete and not cls.data.force_no_default_constructor %}

    # template_params
    #

    # don't add protected things if trampoline not enabled
    # .. more nuance than that

    classes: typing.List["ClassContext"] = field(default_factory=list)

    enums: typing.List[EnumContext] = field(default_factory=list)

    anon_enums: typing.List[EnumContext] = field(default_factory=list)


@dataclass
class TemplateInstanceContext:

    #: Name of parent variable in initializer
    scope_var: str

    #: Name of variable in initializer
    var_name: str

    py_name: str

    #: binding object
    binding_object: str

    params: typing.List[str]

    doc_set: Documentation
    doc_add: Documentation


@dataclass
class HeaderContext:
    #
    rel_fname: str = ""

    # TODO: anon enums?
    enums: typing.List[EnumContext] = field(default_factory=list)

    # classes

    # trampolines

    # template_classes
    template_instances: typing.List[TemplateInstanceContext] = field(
        default_factory=list
    )

    type_caster_includes: typing.List[str] = field(default_factory=list)

    using_ns: typing.List[str] = field(default_factory=list)

    subpackages: typing.Dict[str, str] = field(default_factory=dict)

    # key: class name, value: list of classes this class depends on
    class_hierarchy: typing.Dict[str, typing.List[str]] = field(default_factory=dict)
