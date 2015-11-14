# ./silvershop.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:71576adc579898ffbdc934717b8fadc7cf098128
# Generated 2015-11-14 16:58:02.797987 by PyXB version 1.2.4 using Python 2.7.9.final.0
# Namespace http://railgds.net/ws/shopping [xmlns:shop]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:dd5dc02e-8af0-11e5-954c-7831c1d0cf70')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import silvercom as _ImportedBinding_silvercom

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://railgds.net/ws/shopping', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_com = _ImportedBinding_silvercom.Namespace
_Namespace_com.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 64, 3)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.NONE = STD_ANON._CF_enumeration.addEnumeration(unicode_value='NONE', tag='NONE')
STD_ANON.CHEAPEST = STD_ANON._CF_enumeration.addEnumeration(unicode_value='CHEAPEST', tag='CHEAPEST')
STD_ANON.CHEAPEST_ONEWAY_AND_ROUNDTRIP = STD_ANON._CF_enumeration.addEnumeration(unicode_value='CHEAPEST_ONEWAY_AND_ROUNDTRIP', tag='CHEAPEST_ONEWAY_AND_ROUNDTRIP')
STD_ANON.OPEN = STD_ANON._CF_enumeration.addEnumeration(unicode_value='OPEN', tag='OPEN')
STD_ANON.CHEAPEST_OPEN = STD_ANON._CF_enumeration.addEnumeration(unicode_value='CHEAPEST_OPEN', tag='CHEAPEST_OPEN')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 85, 9)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.CONNECTION_POINTS_ONLY = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='CONNECTION_POINTS_ONLY', tag='CONNECTION_POINTS_ONLY')
STD_ANON_.CONNECTION_POINTS_AND_STOPS = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='CONNECTION_POINTS_AND_STOPS', tag='CONNECTION_POINTS_AND_STOPS')
STD_ANON_.NONE = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='NONE', tag='NONE')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 94, 9)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.ALL = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='ALL', tag='ALL')
STD_ANON_2.PRIVATE_ONLY = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='PRIVATE_ONLY', tag='PRIVATE_ONLY')
STD_ANON_2.PUBLIC_ONLY = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='PUBLIC_ONLY', tag='PUBLIC_ONLY')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 104, 9)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.TICKET = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='TICKET', tag='TICKET')
STD_ANON_3.RESERVATION = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='RESERVATION', tag='RESERVATION')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 195, 6)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.NONE = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='NONE', tag='NONE')
STD_ANON_4.CHEAPEST = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='CHEAPEST', tag='CHEAPEST')
STD_ANON_4.CHEAPEST_ONEWAY_AND_ROUNDTRIP = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='CHEAPEST_ONEWAY_AND_ROUNDTRIP', tag='CHEAPEST_ONEWAY_AND_ROUNDTRIP')
STD_ANON_4.OPEN = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='OPEN', tag='OPEN')
STD_ANON_4.CHEAPEST_OPEN = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='CHEAPEST_OPEN', tag='CHEAPEST_OPEN')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 217, 12)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_5, enum_prefix=None)
STD_ANON_5.ALL = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='ALL', tag='ALL')
STD_ANON_5.PRIVATE_ONLY = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='PRIVATE_ONLY', tag='PRIVATE_ONLY')
STD_ANON_5.PUBLIC_ONLY = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='PUBLIC_ONLY', tag='PUBLIC_ONLY')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 316, 20)
    _Documentation = None
STD_ANON_6._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_6, enum_prefix=None)
STD_ANON_6.SUPPLY_CHANNEL = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='SUPPLY_CHANNEL', tag='SUPPLY_CHANNEL')
STD_ANON_6.CACHE = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='CACHE', tag='CACHE')
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 339, 11)
    _Documentation = None
STD_ANON_7._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_7, enum_prefix=None)
STD_ANON_7.PREFERRED = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='PREFERRED', tag='PREFERRED')
STD_ANON_7.PERMITTED = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='PERMITTED', tag='PERMITTED')
STD_ANON_7.RESTRICTED = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='RESTRICTED', tag='RESTRICTED')
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 361, 11)
    _Documentation = None
STD_ANON_8._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_8, enum_prefix=None)
STD_ANON_8.PERMITTED = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='PERMITTED', tag='PERMITTED')
STD_ANON_8.RESTRICTED = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='RESTRICTED', tag='RESTRICTED')
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_enumeration)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 23, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}travelPointPair uses Python identifier travelPointPair
    __travelPointPair = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'travelPointPair'), 'travelPointPair', '__httprailgds_netwsshopping_CTD_ANON_httprailgds_netwsshoppingtravelPointPair', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 25, 6), )

    
    travelPointPair = property(__travelPointPair.value, __travelPointPair.set, None, None)

    _ElementMap.update({
        __travelPointPair.name() : __travelPointPair
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 30, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}passengerSpec uses Python identifier passengerSpec
    __passengerSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passengerSpec'), 'passengerSpec', '__httprailgds_netwsshopping_CTD_ANON__httprailgds_netwsshoppingpassengerSpec', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 32, 6), )

    
    passengerSpec = property(__passengerSpec.value, __passengerSpec.set, None, None)

    _ElementMap.update({
        __passengerSpec.name() : __passengerSpec
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """passengerFareQualifiers have been deprecated. They have been replaced by loyaltyCards."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 41, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}passengerFareQualifier uses Python identifier passengerFareQualifier
    __passengerFareQualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passengerFareQualifier'), 'passengerFareQualifier', '__httprailgds_netwsshopping_CTD_ANON_2_httprailgds_netwsshoppingpassengerFareQualifier', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 43, 14), )

    
    passengerFareQualifier = property(__passengerFareQualifier.value, __passengerFareQualifier.set, None, None)

    _ElementMap.update({
        __passengerFareQualifier.name() : __passengerFareQualifier
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 56, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}fareQualifier uses Python identifier fareQualifier
    __fareQualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fareQualifier'), 'fareQualifier', '__httprailgds_netwsshopping_CTD_ANON_3_httprailgds_netwsshoppingfareQualifier', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 58, 6), )

    
    fareQualifier = property(__fareQualifier.value, __fareQualifier.set, None, None)

    _ElementMap.update({
        __fareQualifier.name() : __fareQualifier
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 81, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}includeCommissions uses Python identifier includeCommissions
    __includeCommissions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includeCommissions'), 'includeCommissions', '__httprailgds_netwsshopping_CTD_ANON_4_httprailgds_netwsshoppingincludeCommissions', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 83, 8), )

    
    includeCommissions = property(__includeCommissions.value, __includeCommissions.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}intermediatePoints uses Python identifier intermediatePoints
    __intermediatePoints = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'intermediatePoints'), 'intermediatePoints', '__httprailgds_netwsshopping_CTD_ANON_4_httprailgds_netwsshoppingintermediatePoints', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 84, 8), )

    
    intermediatePoints = property(__intermediatePoints.value, __intermediatePoints.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}validFareTypes uses Python identifier validFareTypes
    __validFareTypes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'validFareTypes'), 'validFareTypes', '__httprailgds_netwsshopping_CTD_ANON_4_httprailgds_netwsshoppingvalidFareTypes', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 93, 8), )

    
    validFareTypes = property(__validFareTypes.value, __validFareTypes.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}maximumNumberOfSolutions uses Python identifier maximumNumberOfSolutions
    __maximumNumberOfSolutions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maximumNumberOfSolutions'), 'maximumNumberOfSolutions', '__httprailgds_netwsshopping_CTD_ANON_4_httprailgds_netwsshoppingmaximumNumberOfSolutions', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 102, 8), )

    
    maximumNumberOfSolutions = property(__maximumNumberOfSolutions.value, __maximumNumberOfSolutions.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}productType uses Python identifier productType
    __productType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'productType'), 'productType', '__httprailgds_netwsshopping_CTD_ANON_4_httprailgds_netwsshoppingproductType', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 103, 8), )

    
    productType = property(__productType.value, __productType.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}includeRules uses Python identifier includeRules
    __includeRules = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includeRules'), 'includeRules', '__httprailgds_netwsshopping_CTD_ANON_4_httprailgds_netwsshoppingincludeRules', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 111, 8), )

    
    includeRules = property(__includeRules.value, __includeRules.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}includeOptionalPrices uses Python identifier includeOptionalPrices
    __includeOptionalPrices = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includeOptionalPrices'), 'includeOptionalPrices', '__httprailgds_netwsshopping_CTD_ANON_4_httprailgds_netwsshoppingincludeOptionalPrices', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 112, 32), )

    
    includeOptionalPrices = property(__includeOptionalPrices.value, __includeOptionalPrices.set, None, None)

    _ElementMap.update({
        __includeCommissions.name() : __includeCommissions,
        __intermediatePoints.name() : __intermediatePoints,
        __validFareTypes.name() : __validFareTypes,
        __maximumNumberOfSolutions.name() : __maximumNumberOfSolutions,
        __productType.name() : __productType,
        __includeRules.name() : __includeRules,
        __includeOptionalPrices.name() : __includeOptionalPrices
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 113, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute reservations uses Python identifier reservations
    __reservations = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'reservations'), 'reservations', '__httprailgds_netwsshopping_CTD_ANON_5_reservations', pyxb.binding.datatypes.boolean, required=True)
    __reservations._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 114, 40)
    __reservations._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 114, 40)
    
    reservations = property(__reservations.value, __reservations.set, None, None)

    
    # Attribute accommodations uses Python identifier accommodations
    __accommodations = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accommodations'), 'accommodations', '__httprailgds_netwsshopping_CTD_ANON_5_accommodations', pyxb.binding.datatypes.boolean, required=True)
    __accommodations._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 115, 40)
    __accommodations._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 115, 40)
    
    accommodations = property(__accommodations.value, __accommodations.set, None, None)

    
    # Attribute onboardServices uses Python identifier onboardServices
    __onboardServices = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'onboardServices'), 'onboardServices', '__httprailgds_netwsshopping_CTD_ANON_5_onboardServices', pyxb.binding.datatypes.boolean, required=True)
    __onboardServices._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 116, 40)
    __onboardServices._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 116, 40)
    
    onboardServices = property(__onboardServices.value, __onboardServices.set, None, None)

    
    # Attribute localServices uses Python identifier localServices
    __localServices = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'localServices'), 'localServices', '__httprailgds_netwsshopping_CTD_ANON_5_localServices', pyxb.binding.datatypes.boolean, required=True)
    __localServices._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 117, 40)
    __localServices._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 117, 40)
    
    localServices = property(__localServices.value, __localServices.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __reservations.name() : __reservations,
        __accommodations.name() : __accommodations,
        __onboardServices.name() : __onboardServices,
        __localServices.name() : __localServices
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 132, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}legs uses Python identifier legs
    __legs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legs'), 'legs', '__httprailgds_netwsshopping_CTD_ANON_6_httprailgds_netwsshoppinglegs', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 134, 8), )

    
    legs = property(__legs.value, __legs.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}passengers uses Python identifier passengers
    __passengers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passengers'), 'passengers', '__httprailgds_netwsshopping_CTD_ANON_6_httprailgds_netwsshoppingpassengers', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 141, 8), )

    
    passengers = property(__passengers.value, __passengers.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}fareInformation uses Python identifier fareInformation
    __fareInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fareInformation'), 'fareInformation', '__httprailgds_netwsshopping_CTD_ANON_6_httprailgds_netwsshoppingfareInformation', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 148, 8), )

    
    fareInformation = property(__fareInformation.value, __fareInformation.set, None, None)

    _ElementMap.update({
        __legs.name() : __legs,
        __passengers.name() : __passengers,
        __fareInformation.name() : __fareInformation
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 135, 9)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}leg uses Python identifier leg
    __leg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'leg'), 'leg', '__httprailgds_netwsshopping_CTD_ANON_7_httprailgds_netwsshoppingleg', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 137, 11), )

    
    leg = property(__leg.value, __leg.set, None, None)

    _ElementMap.update({
        __leg.name() : __leg
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 142, 9)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}passenger uses Python identifier passenger
    __passenger = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passenger'), 'passenger', '__httprailgds_netwsshopping_CTD_ANON_8_httprailgds_netwsshoppingpassenger', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 144, 11), )

    
    passenger = property(__passenger.value, __passenger.set, None, None)

    _ElementMap.update({
        __passenger.name() : __passenger
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 149, 9)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}prices uses Python identifier prices
    __prices = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'prices'), 'prices', '__httprailgds_netwsshopping_CTD_ANON_9_httprailgds_netwsshoppingprices', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 151, 11), )

    
    prices = property(__prices.value, __prices.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}transactionFees uses Python identifier transactionFees
    __transactionFees = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionFees'), 'transactionFees', '__httprailgds_netwsshopping_CTD_ANON_9_httprailgds_netwsshoppingtransactionFees', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 158, 11), )

    
    transactionFees = property(__transactionFees.value, __transactionFees.set, None, None)

    _ElementMap.update({
        __prices.name() : __prices,
        __transactionFees.name() : __transactionFees
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 152, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}pointToPointPrice uses Python identifier pointToPointPrice
    __pointToPointPrice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pointToPointPrice'), 'pointToPointPrice', '__httprailgds_netwsshopping_CTD_ANON_10_httprailgds_netwsshoppingpointToPointPrice', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 154, 14), )

    
    pointToPointPrice = property(__pointToPointPrice.value, __pointToPointPrice.set, None, None)

    _ElementMap.update({
        __pointToPointPrice.name() : __pointToPointPrice
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 159, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}transactionFee uses Python identifier transactionFee
    __transactionFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionFee'), 'transactionFee', '__httprailgds_netwsshopping_CTD_ANON_11_httprailgds_netwsshoppingtransactionFee', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 161, 14), )

    
    transactionFee = property(__transactionFee.value, __transactionFee.set, None, None)

    _ElementMap.update({
        __transactionFee.name() : __transactionFee
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 179, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}passengerSpec uses Python identifier passengerSpec
    __passengerSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passengerSpec'), 'passengerSpec', '__httprailgds_netwsshopping_CTD_ANON_12_httprailgds_netwsshoppingpassengerSpec', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 181, 24), )

    
    passengerSpec = property(__passengerSpec.value, __passengerSpec.set, None, None)

    _ElementMap.update({
        __passengerSpec.name() : __passengerSpec
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 186, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}fareQualifier uses Python identifier fareQualifier
    __fareQualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fareQualifier'), 'fareQualifier', '__httprailgds_netwsshopping_CTD_ANON_13_httprailgds_netwsshoppingfareQualifier', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 188, 24), )

    
    fareQualifier = property(__fareQualifier.value, __fareQualifier.set, None, None)

    _ElementMap.update({
        __fareQualifier.name() : __fareQualifier
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 213, 9)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}includeCommissions uses Python identifier includeCommissions
    __includeCommissions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includeCommissions'), 'includeCommissions', '__httprailgds_netwsshopping_CTD_ANON_14_httprailgds_netwsshoppingincludeCommissions', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 215, 11), )

    
    includeCommissions = property(__includeCommissions.value, __includeCommissions.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}validFareTypes uses Python identifier validFareTypes
    __validFareTypes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'validFareTypes'), 'validFareTypes', '__httprailgds_netwsshopping_CTD_ANON_14_httprailgds_netwsshoppingvalidFareTypes', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 216, 11), )

    
    validFareTypes = property(__validFareTypes.value, __validFareTypes.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}maximumNumberOfSolutions uses Python identifier maximumNumberOfSolutions
    __maximumNumberOfSolutions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maximumNumberOfSolutions'), 'maximumNumberOfSolutions', '__httprailgds_netwsshopping_CTD_ANON_14_httprailgds_netwsshoppingmaximumNumberOfSolutions', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 225, 11), )

    
    maximumNumberOfSolutions = property(__maximumNumberOfSolutions.value, __maximumNumberOfSolutions.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}includeRules uses Python identifier includeRules
    __includeRules = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includeRules'), 'includeRules', '__httprailgds_netwsshopping_CTD_ANON_14_httprailgds_netwsshoppingincludeRules', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 226, 11), )

    
    includeRules = property(__includeRules.value, __includeRules.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}includeOptionalPrices uses Python identifier includeOptionalPrices
    __includeOptionalPrices = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includeOptionalPrices'), 'includeOptionalPrices', '__httprailgds_netwsshopping_CTD_ANON_14_httprailgds_netwsshoppingincludeOptionalPrices', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 227, 35), )

    
    includeOptionalPrices = property(__includeOptionalPrices.value, __includeOptionalPrices.set, None, None)

    _ElementMap.update({
        __includeCommissions.name() : __includeCommissions,
        __validFareTypes.name() : __validFareTypes,
        __maximumNumberOfSolutions.name() : __maximumNumberOfSolutions,
        __includeRules.name() : __includeRules,
        __includeOptionalPrices.name() : __includeOptionalPrices
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 228, 39)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute travelPasses uses Python identifier travelPasses
    __travelPasses = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'travelPasses'), 'travelPasses', '__httprailgds_netwsshopping_CTD_ANON_15_travelPasses', pyxb.binding.datatypes.boolean, required=True)
    __travelPasses._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 229, 43)
    __travelPasses._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 229, 43)
    
    travelPasses = property(__travelPasses.value, __travelPasses.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __travelPasses.name() : __travelPasses
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 244, 9)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}passengers uses Python identifier passengers
    __passengers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passengers'), 'passengers', '__httprailgds_netwsshopping_CTD_ANON_16_httprailgds_netwsshoppingpassengers', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 246, 11), )

    
    passengers = property(__passengers.value, __passengers.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}fareInformation uses Python identifier fareInformation
    __fareInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fareInformation'), 'fareInformation', '__httprailgds_netwsshopping_CTD_ANON_16_httprailgds_netwsshoppingfareInformation', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 253, 11), )

    
    fareInformation = property(__fareInformation.value, __fareInformation.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}passengerInformationRequired uses Python identifier passengerInformationRequired
    __passengerInformationRequired = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passengerInformationRequired'), 'passengerInformationRequired', '__httprailgds_netwsshopping_CTD_ANON_16_httprailgds_netwsshoppingpassengerInformationRequired', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 273, 8), )

    
    passengerInformationRequired = property(__passengerInformationRequired.value, __passengerInformationRequired.set, None, None)

    _ElementMap.update({
        __passengers.name() : __passengers,
        __fareInformation.name() : __fareInformation,
        __passengerInformationRequired.name() : __passengerInformationRequired
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 247, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}passenger uses Python identifier passenger
    __passenger = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passenger'), 'passenger', '__httprailgds_netwsshopping_CTD_ANON_17_httprailgds_netwsshoppingpassenger', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 249, 14), )

    
    passenger = property(__passenger.value, __passenger.set, None, None)

    _ElementMap.update({
        __passenger.name() : __passenger
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 254, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}prices uses Python identifier prices
    __prices = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'prices'), 'prices', '__httprailgds_netwsshopping_CTD_ANON_18_httprailgds_netwsshoppingprices', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 256, 14), )

    
    prices = property(__prices.value, __prices.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}transactionFees uses Python identifier transactionFees
    __transactionFees = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionFees'), 'transactionFees', '__httprailgds_netwsshopping_CTD_ANON_18_httprailgds_netwsshoppingtransactionFees', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 263, 14), )

    
    transactionFees = property(__transactionFees.value, __transactionFees.set, None, None)

    _ElementMap.update({
        __prices.name() : __prices,
        __transactionFees.name() : __transactionFees
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 257, 15)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}travelPassPrice uses Python identifier travelPassPrice
    __travelPassPrice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'travelPassPrice'), 'travelPassPrice', '__httprailgds_netwsshopping_CTD_ANON_19_httprailgds_netwsshoppingtravelPassPrice', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 259, 17), )

    
    travelPassPrice = property(__travelPassPrice.value, __travelPassPrice.set, None, None)

    _ElementMap.update({
        __travelPassPrice.name() : __travelPassPrice
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 264, 15)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}transactionFee uses Python identifier transactionFee
    __transactionFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionFee'), 'transactionFee', '__httprailgds_netwsshopping_CTD_ANON_20_httprailgds_netwsshoppingtransactionFee', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 266, 17), )

    
    transactionFee = property(__transactionFee.value, __transactionFee.set, None, None)

    _ElementMap.update({
        __transactionFee.name() : __transactionFee
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 274, 9)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}passengerInformation uses Python identifier passengerInformation
    __passengerInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passengerInformation'), 'passengerInformation', '__httprailgds_netwsshopping_CTD_ANON_21_httprailgds_netwsshoppingpassengerInformation', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 276, 11), )

    
    passengerInformation = property(__passengerInformation.value, __passengerInformation.set, None, None)

    _ElementMap.update({
        __passengerInformation.name() : __passengerInformation
    })
    _AttributeMap.update({
        
    })



# Complex type {http://railgds.net/ws/shopping}ScheduleQueryType with content type ELEMENT_ONLY
class ScheduleQueryType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://railgds.net/ws/shopping}ScheduleQueryType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ScheduleQueryType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 298, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}travelPointPair uses Python identifier travelPointPair
    __travelPointPair = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'travelPointPair'), 'travelPointPair', '__httprailgds_netwsshopping_ScheduleQueryType_httprailgds_netwsshoppingtravelPointPair', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 300, 4), )

    
    travelPointPair = property(__travelPointPair.value, __travelPointPair.set, None, None)

    _ElementMap.update({
        __travelPointPair.name() : __travelPointPair
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ScheduleQueryType', ScheduleQueryType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 308, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}leg uses Python identifier leg
    __leg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'leg'), 'leg', '__httprailgds_netwsshopping_CTD_ANON_22_httprailgds_netwsshoppingleg', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 310, 8), )

    
    leg = property(__leg.value, __leg.set, None, None)

    _ElementMap.update({
        __leg.name() : __leg
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 331, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}carrierRestriction uses Python identifier carrierRestriction
    __carrierRestriction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'carrierRestriction'), 'carrierRestriction', '__httprailgds_netwsshopping_CTD_ANON_23_httprailgds_netwsshoppingcarrierRestriction', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 333, 8), )

    
    carrierRestriction = property(__carrierRestriction.value, __carrierRestriction.set, None, None)

    _ElementMap.update({
        __carrierRestriction.name() : __carrierRestriction
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 353, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}equipmentTypeRestriction uses Python identifier equipmentTypeRestriction
    __equipmentTypeRestriction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'equipmentTypeRestriction'), 'equipmentTypeRestriction', '__httprailgds_netwsshopping_CTD_ANON_24_httprailgds_netwsshoppingequipmentTypeRestriction', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 355, 8), )

    
    equipmentTypeRestriction = property(__equipmentTypeRestriction.value, __equipmentTypeRestriction.set, None, None)

    _ElementMap.update({
        __equipmentTypeRestriction.name() : __equipmentTypeRestriction
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 389, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}legIDRef uses Python identifier legIDRef
    __legIDRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legIDRef'), 'legIDRef', '__httprailgds_netwsshopping_CTD_ANON_25_httprailgds_netwsshoppinglegIDRef', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 391, 8), )

    
    legIDRef = property(__legIDRef.value, __legIDRef.set, None, None)

    
    # Attribute minQuantity uses Python identifier minQuantity
    __minQuantity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minQuantity'), 'minQuantity', '__httprailgds_netwsshopping_CTD_ANON_25_minQuantity', pyxb.binding.datatypes.integer, required=True)
    __minQuantity._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 393, 7)
    __minQuantity._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 393, 7)
    
    minQuantity = property(__minQuantity.value, __minQuantity.set, None, None)

    
    # Attribute maxQuantity uses Python identifier maxQuantity
    __maxQuantity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxQuantity'), 'maxQuantity', '__httprailgds_netwsshopping_CTD_ANON_25_maxQuantity', pyxb.binding.datatypes.integer, required=True)
    __maxQuantity._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 394, 7)
    __maxQuantity._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 394, 7)
    
    maxQuantity = property(__maxQuantity.value, __maxQuantity.set, None, None)

    _ElementMap.update({
        __legIDRef.name() : __legIDRef
    })
    _AttributeMap.update({
        __minQuantity.name() : __minQuantity,
        __maxQuantity.name() : __maxQuantity
    })



# Complex type {http://railgds.net/ws/shopping}PointToPointShoppingQuery with content type ELEMENT_ONLY
class PointToPointShoppingQuery (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://railgds.net/ws/shopping}PointToPointShoppingQuery with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PointToPointShoppingQuery')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 20, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}travelPointPairs uses Python identifier travelPointPairs
    __travelPointPairs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'travelPointPairs'), 'travelPointPairs', '__httprailgds_netwsshopping_PointToPointShoppingQuery_httprailgds_netwsshoppingtravelPointPairs', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 22, 3), )

    
    travelPointPairs = property(__travelPointPairs.value, __travelPointPairs.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}passengerSpecs uses Python identifier passengerSpecs
    __passengerSpecs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passengerSpecs'), 'passengerSpecs', '__httprailgds_netwsshopping_PointToPointShoppingQuery_httprailgds_netwsshoppingpassengerSpecs', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 29, 3), )

    
    passengerSpecs = property(__passengerSpecs.value, __passengerSpecs.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}fareQualifiers uses Python identifier fareQualifiers
    __fareQualifiers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fareQualifiers'), 'fareQualifiers', '__httprailgds_netwsshopping_PointToPointShoppingQuery_httprailgds_netwsshoppingfareQualifiers', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 55, 3), )

    
    fareQualifiers = property(__fareQualifiers.value, __fareQualifiers.set, None, None)

    
    # Attribute fareFilter uses Python identifier fareFilter
    __fareFilter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fareFilter'), 'fareFilter', '__httprailgds_netwsshopping_PointToPointShoppingQuery_fareFilter', STD_ANON)
    __fareFilter._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 63, 2)
    __fareFilter._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 63, 2)
    
    fareFilter = property(__fareFilter.value, __fareFilter.set, None, None)

    _ElementMap.update({
        __travelPointPairs.name() : __travelPointPairs,
        __passengerSpecs.name() : __passengerSpecs,
        __fareQualifiers.name() : __fareQualifiers
    })
    _AttributeMap.update({
        __fareFilter.name() : __fareFilter
    })
Namespace.addCategoryObject('typeBinding', 'PointToPointShoppingQuery', PointToPointShoppingQuery)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26 (_ImportedBinding_silvercom.PassengerSpecType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 33, 7)
    _ElementMap = _ImportedBinding_silvercom.PassengerSpecType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.PassengerSpecType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.PassengerSpecType
    
    # Element age ({http://railgds.net/ws/commontypes}age) inherited from {http://railgds.net/ws/commontypes}PassengerSpecType
    
    # Element dateOfBirth ({http://railgds.net/ws/commontypes}dateOfBirth) inherited from {http://railgds.net/ws/commontypes}PassengerSpecType
    
    # Element residenceInformation ({http://railgds.net/ws/commontypes}residenceInformation) inherited from {http://railgds.net/ws/commontypes}PassengerSpecType
    
    # Element {http://railgds.net/ws/shopping}passengerFareQualifiers uses Python identifier passengerFareQualifiers
    __passengerFareQualifiers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passengerFareQualifiers'), 'passengerFareQualifiers', '__httprailgds_netwsshopping_CTD_ANON_26_httprailgds_netwsshoppingpassengerFareQualifiers', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 37, 11), )

    
    passengerFareQualifiers = property(__passengerFareQualifiers.value, __passengerFareQualifiers.set, None, 'passengerFareQualifiers have been deprecated. They have been replaced by loyaltyCards.')

    
    # Attribute passengerSpecID inherited from {http://railgds.net/ws/commontypes}PassengerSpecType
    _ElementMap.update({
        __passengerFareQualifiers.name() : __passengerFareQualifiers
    })
    _AttributeMap.update({
        
    })



# Complex type {http://railgds.net/ws/shopping}PointToPointShoppingRequestType with content type ELEMENT_ONLY
class PointToPointShoppingRequestType (_ImportedBinding_silvercom.BaseRequestType):
    """Complex type {http://railgds.net/ws/shopping}PointToPointShoppingRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PointToPointShoppingRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 75, 1)
    _ElementMap = _ImportedBinding_silvercom.BaseRequestType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseRequestType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseRequestType
    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element {http://railgds.net/ws/shopping}pointToPointShoppingQuery uses Python identifier pointToPointShoppingQuery
    __pointToPointShoppingQuery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pointToPointShoppingQuery'), 'pointToPointShoppingQuery', '__httprailgds_netwsshopping_PointToPointShoppingRequestType_httprailgds_netwsshoppingpointToPointShoppingQuery', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 79, 5), )

    
    pointToPointShoppingQuery = property(__pointToPointShoppingQuery.value, __pointToPointShoppingQuery.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}responseSpec uses Python identifier responseSpec
    __responseSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), 'responseSpec', '__httprailgds_netwsshopping_PointToPointShoppingRequestType_httprailgds_netwsshoppingresponseSpec', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 80, 5), )

    
    responseSpec = property(__responseSpec.value, __responseSpec.set, None, None)

    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __pointToPointShoppingQuery.name() : __pointToPointShoppingQuery,
        __responseSpec.name() : __responseSpec
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'PointToPointShoppingRequestType', PointToPointShoppingRequestType)


# Complex type {http://railgds.net/ws/shopping}PointToPointShoppingResponseType with content type ELEMENT_ONLY
class PointToPointShoppingResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/shopping}PointToPointShoppingResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PointToPointShoppingResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 127, 1)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Element {http://railgds.net/ws/shopping}results uses Python identifier results
    __results = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'results'), 'results', '__httprailgds_netwsshopping_PointToPointShoppingResponseType_httprailgds_netwsshoppingresults', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 131, 5), )

    
    results = property(__results.value, __results.set, None, None)

    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __results.name() : __results
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'PointToPointShoppingResponseType', PointToPointShoppingResponseType)


# Complex type {http://railgds.net/ws/shopping}TravelPassShoppingQuery with content type ELEMENT_ONLY
class TravelPassShoppingQuery (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://railgds.net/ws/shopping}TravelPassShoppingQuery with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TravelPassShoppingQuery')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 175, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}travelPointPair uses Python identifier travelPointPair
    __travelPointPair = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'travelPointPair'), 'travelPointPair', '__httprailgds_netwsshopping_TravelPassShoppingQuery_httprailgds_netwsshoppingtravelPointPair', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 177, 12), )

    
    travelPointPair = property(__travelPointPair.value, __travelPointPair.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}passengerSpecs uses Python identifier passengerSpecs
    __passengerSpecs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passengerSpecs'), 'passengerSpecs', '__httprailgds_netwsshopping_TravelPassShoppingQuery_httprailgds_netwsshoppingpassengerSpecs', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 178, 12), )

    
    passengerSpecs = property(__passengerSpecs.value, __passengerSpecs.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}fareQualifiers uses Python identifier fareQualifiers
    __fareQualifiers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fareQualifiers'), 'fareQualifiers', '__httprailgds_netwsshopping_TravelPassShoppingQuery_httprailgds_netwsshoppingfareQualifiers', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 185, 12), )

    
    fareQualifiers = property(__fareQualifiers.value, __fareQualifiers.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}issueType uses Python identifier issueType
    __issueType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'issueType'), 'issueType', '__httprailgds_netwsshopping_TravelPassShoppingQuery_httprailgds_netwsshoppingissueType', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 192, 3), )

    
    issueType = property(__issueType.value, __issueType.set, None, None)

    
    # Attribute fareFilter uses Python identifier fareFilter
    __fareFilter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fareFilter'), 'fareFilter', '__httprailgds_netwsshopping_TravelPassShoppingQuery_fareFilter', STD_ANON_4)
    __fareFilter._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 194, 5)
    __fareFilter._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 194, 5)
    
    fareFilter = property(__fareFilter.value, __fareFilter.set, None, None)

    _ElementMap.update({
        __travelPointPair.name() : __travelPointPair,
        __passengerSpecs.name() : __passengerSpecs,
        __fareQualifiers.name() : __fareQualifiers,
        __issueType.name() : __issueType
    })
    _AttributeMap.update({
        __fareFilter.name() : __fareFilter
    })
Namespace.addCategoryObject('typeBinding', 'TravelPassShoppingQuery', TravelPassShoppingQuery)


# Complex type {http://railgds.net/ws/shopping}TravelPassShoppingRequestType with content type ELEMENT_ONLY
class TravelPassShoppingRequestType (_ImportedBinding_silvercom.BaseRequestType):
    """Complex type {http://railgds.net/ws/shopping}TravelPassShoppingRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TravelPassShoppingRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 207, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseRequestType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseRequestType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseRequestType
    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element {http://railgds.net/ws/shopping}travelPassShoppingQuery uses Python identifier travelPassShoppingQuery
    __travelPassShoppingQuery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'travelPassShoppingQuery'), 'travelPassShoppingQuery', '__httprailgds_netwsshopping_TravelPassShoppingRequestType_httprailgds_netwsshoppingtravelPassShoppingQuery', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 211, 8), )

    
    travelPassShoppingQuery = property(__travelPassShoppingQuery.value, __travelPassShoppingQuery.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}responseSpec uses Python identifier responseSpec
    __responseSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), 'responseSpec', '__httprailgds_netwsshopping_TravelPassShoppingRequestType_httprailgds_netwsshoppingresponseSpec', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 212, 8), )

    
    responseSpec = property(__responseSpec.value, __responseSpec.set, None, None)

    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __travelPassShoppingQuery.name() : __travelPassShoppingQuery,
        __responseSpec.name() : __responseSpec
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'TravelPassShoppingRequestType', TravelPassShoppingRequestType)


# Complex type {http://railgds.net/ws/shopping}TravelPassShoppingResponseType with content type ELEMENT_ONLY
class TravelPassShoppingResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/shopping}TravelPassShoppingResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TravelPassShoppingResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 239, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Element {http://railgds.net/ws/shopping}results uses Python identifier results
    __results = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'results'), 'results', '__httprailgds_netwsshopping_TravelPassShoppingResponseType_httprailgds_netwsshoppingresults', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 243, 8), )

    
    results = property(__results.value, __results.set, None, None)

    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __results.name() : __results
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'TravelPassShoppingResponseType', TravelPassShoppingResponseType)


# Complex type {http://railgds.net/ws/shopping}ScheduleSearchRequestType with content type ELEMENT_ONLY
class ScheduleSearchRequestType (_ImportedBinding_silvercom.BaseRequestType):
    """Complex type {http://railgds.net/ws/shopping}ScheduleSearchRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ScheduleSearchRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 289, 1)
    _ElementMap = _ImportedBinding_silvercom.BaseRequestType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseRequestType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseRequestType
    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element {http://railgds.net/ws/shopping}scheduleQuery uses Python identifier scheduleQuery
    __scheduleQuery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scheduleQuery'), 'scheduleQuery', '__httprailgds_netwsshopping_ScheduleSearchRequestType_httprailgds_netwsshoppingscheduleQuery', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 293, 5), )

    
    scheduleQuery = property(__scheduleQuery.value, __scheduleQuery.set, None, None)

    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __scheduleQuery.name() : __scheduleQuery
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ScheduleSearchRequestType', ScheduleSearchRequestType)


# Complex type {http://railgds.net/ws/shopping}ScheduleSearchResponseType with content type ELEMENT_ONLY
class ScheduleSearchResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/shopping}ScheduleSearchResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ScheduleSearchResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 303, 1)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Element {http://railgds.net/ws/shopping}results uses Python identifier results
    __results = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'results'), 'results', '__httprailgds_netwsshopping_ScheduleSearchResponseType_httprailgds_netwsshoppingresults', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 307, 5), )

    
    results = property(__results.value, __results.set, None, None)

    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute source uses Python identifier source
    __source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'source'), 'source', '__httprailgds_netwsshopping_ScheduleSearchResponseType_source', STD_ANON_6)
    __source._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 315, 16)
    __source._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 315, 16)
    
    source = property(__source.value, __source.set, None, None)

    _ElementMap.update({
        __results.name() : __results
    })
    _AttributeMap.update({
        __source.name() : __source
    })
Namespace.addCategoryObject('typeBinding', 'ScheduleSearchResponseType', ScheduleSearchResponseType)


# Complex type {http://railgds.net/ws/shopping}QueryTravelPointPairType with content type ELEMENT_ONLY
class QueryTravelPointPairType (_ImportedBinding_silvercom.TravelPointPairType):
    """Complex type {http://railgds.net/ws/shopping}QueryTravelPointPairType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTravelPointPairType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 326, 1)
    _ElementMap = _ImportedBinding_silvercom.TravelPointPairType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.TravelPointPairType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.TravelPointPairType
    
    # Element originTravelPoint ({http://railgds.net/ws/commontypes}originTravelPoint) inherited from {http://railgds.net/ws/commontypes}TravelPointPairType
    
    # Element destinationTravelPoint ({http://railgds.net/ws/commontypes}destinationTravelPoint) inherited from {http://railgds.net/ws/commontypes}TravelPointPairType
    
    # Element departureDateTimeWindow ({http://railgds.net/ws/commontypes}departureDateTimeWindow) inherited from {http://railgds.net/ws/commontypes}TravelPointPairType
    
    # Element arrivalDateTimeWindow ({http://railgds.net/ws/commontypes}arrivalDateTimeWindow) inherited from {http://railgds.net/ws/commontypes}TravelPointPairType
    
    # Element {http://railgds.net/ws/shopping}carrierRestrictions uses Python identifier carrierRestrictions
    __carrierRestrictions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'carrierRestrictions'), 'carrierRestrictions', '__httprailgds_netwsshopping_QueryTravelPointPairType_httprailgds_netwsshoppingcarrierRestrictions', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 330, 5), )

    
    carrierRestrictions = property(__carrierRestrictions.value, __carrierRestrictions.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}equipmentTypeRestrictions uses Python identifier equipmentTypeRestrictions
    __equipmentTypeRestrictions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'equipmentTypeRestrictions'), 'equipmentTypeRestrictions', '__httprailgds_netwsshopping_QueryTravelPointPairType_httprailgds_netwsshoppingequipmentTypeRestrictions', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 352, 5), )

    
    equipmentTypeRestrictions = property(__equipmentTypeRestrictions.value, __equipmentTypeRestrictions.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}routingRestrictions uses Python identifier routingRestrictions
    __routingRestrictions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'routingRestrictions'), 'routingRestrictions', '__httprailgds_netwsshopping_QueryTravelPointPairType_httprailgds_netwsshoppingroutingRestrictions', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 373, 5), )

    
    routingRestrictions = property(__routingRestrictions.value, __routingRestrictions.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}minimumConnectionTime uses Python identifier minimumConnectionTime
    __minimumConnectionTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'minimumConnectionTime'), 'minimumConnectionTime', '__httprailgds_netwsshopping_QueryTravelPointPairType_httprailgds_netwsshoppingminimumConnectionTime', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 374, 5), )

    
    minimumConnectionTime = property(__minimumConnectionTime.value, __minimumConnectionTime.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}maximumConnectionTime uses Python identifier maximumConnectionTime
    __maximumConnectionTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maximumConnectionTime'), 'maximumConnectionTime', '__httprailgds_netwsshopping_QueryTravelPointPairType_httprailgds_netwsshoppingmaximumConnectionTime', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 375, 5), )

    
    maximumConnectionTime = property(__maximumConnectionTime.value, __maximumConnectionTime.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}maximumPermittedConnections uses Python identifier maximumPermittedConnections
    __maximumPermittedConnections = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maximumPermittedConnections'), 'maximumPermittedConnections', '__httprailgds_netwsshopping_QueryTravelPointPairType_httprailgds_netwsshoppingmaximumPermittedConnections', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 376, 5), )

    
    maximumPermittedConnections = property(__maximumPermittedConnections.value, __maximumPermittedConnections.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}maximumTransitTime uses Python identifier maximumTransitTime
    __maximumTransitTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maximumTransitTime'), 'maximumTransitTime', '__httprailgds_netwsshopping_QueryTravelPointPairType_httprailgds_netwsshoppingmaximumTransitTime', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 377, 5), )

    
    maximumTransitTime = property(__maximumTransitTime.value, __maximumTransitTime.set, None, None)

    _ElementMap.update({
        __carrierRestrictions.name() : __carrierRestrictions,
        __equipmentTypeRestrictions.name() : __equipmentTypeRestrictions,
        __routingRestrictions.name() : __routingRestrictions,
        __minimumConnectionTime.name() : __minimumConnectionTime,
        __maximumConnectionTime.name() : __maximumConnectionTime,
        __maximumPermittedConnections.name() : __maximumPermittedConnections,
        __maximumTransitTime.name() : __maximumTransitTime
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'QueryTravelPointPairType', QueryTravelPointPairType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 334, 9)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}carrier uses Python identifier carrier
    __carrier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'carrier'), 'carrier', '__httprailgds_netwsshopping_CTD_ANON_27_httprailgds_netwsshoppingcarrier', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 336, 11), )

    
    carrier = property(__carrier.value, __carrier.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httprailgds_netwsshopping_CTD_ANON_27_type', STD_ANON_7, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 338, 10)
    __type._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 338, 10)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __carrier.name() : __carrier
    })
    _AttributeMap.update({
        __type.name() : __type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 356, 9)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/shopping}equipmentType uses Python identifier equipmentType
    __equipmentType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'equipmentType'), 'equipmentType', '__httprailgds_netwsshopping_CTD_ANON_28_httprailgds_netwsshoppingequipmentType', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 358, 11), )

    
    equipmentType = property(__equipmentType.value, __equipmentType.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httprailgds_netwsshopping_CTD_ANON_28_type', STD_ANON_8, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 360, 10)
    __type._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 360, 10)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __equipmentType.name() : __equipmentType
    })
    _AttributeMap.update({
        __type.name() : __type
    })



# Complex type {http://railgds.net/ws/shopping}ShoppingTransactionFeeType with content type ELEMENT_ONLY
class ShoppingTransactionFeeType (_ImportedBinding_silvercom.BaseTransactionFeeType):
    """Complex type {http://railgds.net/ws/shopping}ShoppingTransactionFeeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShoppingTransactionFeeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 383, 1)
    _ElementMap = _ImportedBinding_silvercom.BaseTransactionFeeType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseTransactionFeeType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseTransactionFeeType
    
    # Element fee ({http://railgds.net/ws/commontypes}fee) inherited from {http://railgds.net/ws/commontypes}BaseTransactionFeeType
    
    # Element {http://railgds.net/ws/shopping}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httprailgds_netwsshopping_ShoppingTransactionFeeType_httprailgds_netwsshoppingdescription', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 387, 5), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://railgds.net/ws/shopping}applicableLegs uses Python identifier applicableLegs
    __applicableLegs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'applicableLegs'), 'applicableLegs', '__httprailgds_netwsshopping_ShoppingTransactionFeeType_httprailgds_netwsshoppingapplicableLegs', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 388, 5), )

    
    applicableLegs = property(__applicableLegs.value, __applicableLegs.set, None, None)

    
    # Attribute transactionFeeID inherited from {http://railgds.net/ws/commontypes}BaseTransactionFeeType
    
    # Attribute mandatory uses Python identifier mandatory
    __mandatory = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mandatory'), 'mandatory', '__httprailgds_netwsshopping_ShoppingTransactionFeeType_mandatory', pyxb.binding.datatypes.boolean, required=True)
    __mandatory._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 398, 4)
    __mandatory._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 398, 4)
    
    mandatory = property(__mandatory.value, __mandatory.set, None, None)

    _ElementMap.update({
        __description.name() : __description,
        __applicableLegs.name() : __applicableLegs
    })
    _AttributeMap.update({
        __mandatory.name() : __mandatory
    })
Namespace.addCategoryObject('typeBinding', 'ShoppingTransactionFeeType', ShoppingTransactionFeeType)


pointToPointShoppingRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pointToPointShoppingRequest'), PointToPointShoppingRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 13, 1))
Namespace.addCategoryObject('elementBinding', pointToPointShoppingRequest.name().localName(), pointToPointShoppingRequest)

pointToPointShoppingResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pointToPointShoppingResponse'), PointToPointShoppingResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 14, 1))
Namespace.addCategoryObject('elementBinding', pointToPointShoppingResponse.name().localName(), pointToPointShoppingResponse)

travelPassShoppingRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'travelPassShoppingRequest'), TravelPassShoppingRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 15, 4))
Namespace.addCategoryObject('elementBinding', travelPassShoppingRequest.name().localName(), travelPassShoppingRequest)

travelPassShoppingResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'travelPassShoppingResponse'), TravelPassShoppingResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 16, 4))
Namespace.addCategoryObject('elementBinding', travelPassShoppingResponse.name().localName(), travelPassShoppingResponse)

scheduleSearchRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleSearchRequest'), ScheduleSearchRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 17, 1))
Namespace.addCategoryObject('elementBinding', scheduleSearchRequest.name().localName(), scheduleSearchRequest)

scheduleSearchResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleSearchResponse'), ScheduleSearchResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 18, 1))
Namespace.addCategoryObject('elementBinding', scheduleSearchResponse.name().localName(), scheduleSearchResponse)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'travelPointPair'), QueryTravelPointPairType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 25, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'travelPointPair')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 25, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passengerSpec'), CTD_ANON_26, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 32, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passengerSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 32, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passengerFareQualifier'), _ImportedBinding_silvercom.PassengerFareQualifierType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 43, 14)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passengerFareQualifier')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 43, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fareQualifier'), _ImportedBinding_silvercom.FareQualifierType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 58, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fareQualifier')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 58, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includeCommissions'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 83, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'intermediatePoints'), STD_ANON_, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 84, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'validFareTypes'), STD_ANON_2, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 93, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maximumNumberOfSolutions'), pyxb.binding.datatypes.int, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 102, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'productType'), STD_ANON_3, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 103, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includeRules'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 111, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includeOptionalPrices'), CTD_ANON_5, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 112, 32)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 83, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 84, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 93, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 102, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 103, 8))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 111, 8))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 112, 32))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includeCommissions')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 83, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'intermediatePoints')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 84, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validFareTypes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 93, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maximumNumberOfSolutions')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 102, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'productType')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 103, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includeRules')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 111, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includeOptionalPrices')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 112, 32))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legs'), CTD_ANON_7, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 134, 8)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passengers'), CTD_ANON_8, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 141, 8)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fareInformation'), CTD_ANON_9, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 148, 8)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legs')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 134, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passengers')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 141, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fareInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 148, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_5()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'leg'), _ImportedBinding_silvercom.LegType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 137, 11)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'leg')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 137, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_6()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passenger'), _ImportedBinding_silvercom.PassengerSpecType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 144, 11)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passenger')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 144, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_7()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'prices'), CTD_ANON_10, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 151, 11)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionFees'), CTD_ANON_11, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 158, 11)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 158, 11))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prices')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 151, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionFees')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 158, 11))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_8()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pointToPointPrice'), _ImportedBinding_silvercom.PointToPointPriceType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 154, 14)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pointToPointPrice')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 154, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_9()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionFee'), ShoppingTransactionFeeType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 161, 14)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionFee')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 161, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_10()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passengerSpec'), _ImportedBinding_silvercom.PassengerSpecType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 181, 24)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passengerSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 181, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_11()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fareQualifier'), _ImportedBinding_silvercom.FareQualifierType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 188, 24)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fareQualifier')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 188, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_12()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includeCommissions'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 215, 11)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'validFareTypes'), STD_ANON_5, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 216, 11)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maximumNumberOfSolutions'), pyxb.binding.datatypes.int, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 225, 11)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includeRules'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 226, 11)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includeOptionalPrices'), CTD_ANON_15, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 227, 35)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 215, 11))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 216, 11))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 225, 11))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 226, 11))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 227, 35))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includeCommissions')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 215, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validFareTypes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 216, 11))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maximumNumberOfSolutions')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 225, 11))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includeRules')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 226, 11))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includeOptionalPrices')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 227, 35))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_13()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passengers'), CTD_ANON_17, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 246, 11)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fareInformation'), CTD_ANON_18, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 253, 11)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passengerInformationRequired'), CTD_ANON_21, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 273, 8)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 273, 8))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passengers')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 246, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fareInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 253, 11))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passengerInformationRequired')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 273, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_14()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passenger'), _ImportedBinding_silvercom.PassengerSpecType, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 249, 14)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passenger')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 249, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_15()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'prices'), CTD_ANON_19, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 256, 14)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionFees'), CTD_ANON_20, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 263, 14)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 263, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prices')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 256, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionFees')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 263, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_16()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'travelPassPrice'), _ImportedBinding_silvercom.PassPriceType, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 259, 17)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'travelPassPrice')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 259, 17))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_17()




CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionFee'), ShoppingTransactionFeeType, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 266, 17)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionFee')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 266, 17))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_18()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passengerInformation'), _ImportedBinding_silvercom.PassengerInformationType, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 276, 11)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passengerInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 276, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_19()




ScheduleQueryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'travelPointPair'), QueryTravelPointPairType, scope=ScheduleQueryType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 300, 4)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ScheduleQueryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'travelPointPair')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 300, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ScheduleQueryType._Automaton = _BuildAutomaton_20()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'leg'), _ImportedBinding_silvercom.LegType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 310, 8)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'leg')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 310, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_21()




CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'carrierRestriction'), CTD_ANON_27, scope=CTD_ANON_23, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 333, 8)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'carrierRestriction')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 333, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_22()




CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'equipmentTypeRestriction'), CTD_ANON_28, scope=CTD_ANON_24, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 355, 8)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'equipmentTypeRestriction')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 355, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_23()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legIDRef'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 391, 8)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legIDRef')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 391, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_24()




PointToPointShoppingQuery._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'travelPointPairs'), CTD_ANON, scope=PointToPointShoppingQuery, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 22, 3)))

PointToPointShoppingQuery._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passengerSpecs'), CTD_ANON_, scope=PointToPointShoppingQuery, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 29, 3)))

PointToPointShoppingQuery._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fareQualifiers'), CTD_ANON_3, scope=PointToPointShoppingQuery, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 55, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 55, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PointToPointShoppingQuery._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'travelPointPairs')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 22, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PointToPointShoppingQuery._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passengerSpecs')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 29, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PointToPointShoppingQuery._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fareQualifiers')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 55, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PointToPointShoppingQuery._Automaton = _BuildAutomaton_25()




CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passengerFareQualifiers'), CTD_ANON_2, scope=CTD_ANON_26, documentation='passengerFareQualifiers have been deprecated. They have been replaced by loyaltyCards.', location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 37, 11)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 1546, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 37, 11))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'age')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 1543, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'dateOfBirth')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 1544, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'residenceInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 1546, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passengerFareQualifiers')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 37, 11))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_26()




PointToPointShoppingRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pointToPointShoppingQuery'), PointToPointShoppingQuery, scope=PointToPointShoppingRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 79, 5)))

PointToPointShoppingRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), CTD_ANON_4, scope=PointToPointShoppingRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 80, 5)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 80, 5))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PointToPointShoppingRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PointToPointShoppingRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PointToPointShoppingRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pointToPointShoppingQuery')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 79, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PointToPointShoppingRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 80, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PointToPointShoppingRequestType._Automaton = _BuildAutomaton_27()




PointToPointShoppingResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'results'), CTD_ANON_6, scope=PointToPointShoppingResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 131, 5)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 131, 5))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PointToPointShoppingResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PointToPointShoppingResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'results')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 131, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PointToPointShoppingResponseType._Automaton = _BuildAutomaton_28()




TravelPassShoppingQuery._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'travelPointPair'), _ImportedBinding_silvercom.QueryTravelPointPairPassType, scope=TravelPassShoppingQuery, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 177, 12)))

TravelPassShoppingQuery._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passengerSpecs'), CTD_ANON_12, scope=TravelPassShoppingQuery, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 178, 12)))

TravelPassShoppingQuery._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fareQualifiers'), CTD_ANON_13, scope=TravelPassShoppingQuery, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 185, 12)))

TravelPassShoppingQuery._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'issueType'), _ImportedBinding_silvercom.IssueType, scope=TravelPassShoppingQuery, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 192, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 185, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 192, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TravelPassShoppingQuery._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'travelPointPair')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 177, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TravelPassShoppingQuery._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passengerSpecs')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 178, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TravelPassShoppingQuery._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fareQualifiers')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 185, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TravelPassShoppingQuery._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'issueType')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 192, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TravelPassShoppingQuery._Automaton = _BuildAutomaton_29()




TravelPassShoppingRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'travelPassShoppingQuery'), TravelPassShoppingQuery, scope=TravelPassShoppingRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 211, 8)))

TravelPassShoppingRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), CTD_ANON_14, scope=TravelPassShoppingRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 212, 8)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 212, 8))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TravelPassShoppingRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TravelPassShoppingRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TravelPassShoppingRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'travelPassShoppingQuery')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 211, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TravelPassShoppingRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 212, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TravelPassShoppingRequestType._Automaton = _BuildAutomaton_30()




TravelPassShoppingResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'results'), CTD_ANON_16, scope=TravelPassShoppingResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 243, 8)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 243, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TravelPassShoppingResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TravelPassShoppingResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'results')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 243, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TravelPassShoppingResponseType._Automaton = _BuildAutomaton_31()




ScheduleSearchRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleQuery'), ScheduleQueryType, scope=ScheduleSearchRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 293, 5)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ScheduleSearchRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ScheduleSearchRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ScheduleSearchRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleQuery')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 293, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ScheduleSearchRequestType._Automaton = _BuildAutomaton_32()




ScheduleSearchResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'results'), CTD_ANON_22, scope=ScheduleSearchResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 307, 5)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 307, 5))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ScheduleSearchResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ScheduleSearchResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'results')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 307, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ScheduleSearchResponseType._Automaton = _BuildAutomaton_33()




QueryTravelPointPairType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'carrierRestrictions'), CTD_ANON_23, scope=QueryTravelPointPairType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 330, 5)))

QueryTravelPointPairType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'equipmentTypeRestrictions'), CTD_ANON_24, scope=QueryTravelPointPairType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 352, 5)))

QueryTravelPointPairType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'routingRestrictions'), _ImportedBinding_silvercom.RoutingRestrictionsType, scope=QueryTravelPointPairType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 373, 5)))

QueryTravelPointPairType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'minimumConnectionTime'), pyxb.binding.datatypes.duration, scope=QueryTravelPointPairType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 374, 5)))

QueryTravelPointPairType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maximumConnectionTime'), pyxb.binding.datatypes.duration, scope=QueryTravelPointPairType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 375, 5)))

QueryTravelPointPairType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maximumPermittedConnections'), pyxb.binding.datatypes.int, scope=QueryTravelPointPairType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 376, 5)))

QueryTravelPointPairType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maximumTransitTime'), pyxb.binding.datatypes.duration, scope=QueryTravelPointPairType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 377, 5)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 2301, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 2302, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 330, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 352, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 373, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 374, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 375, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 376, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 377, 5))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QueryTravelPointPairType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'originTravelPoint')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 2299, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTravelPointPairType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'destinationTravelPoint')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 2300, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTravelPointPairType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'departureDateTimeWindow')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 2301, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(QueryTravelPointPairType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'arrivalDateTimeWindow')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 2302, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(QueryTravelPointPairType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'carrierRestrictions')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 330, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(QueryTravelPointPairType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'equipmentTypeRestrictions')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 352, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(QueryTravelPointPairType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'routingRestrictions')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 373, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(QueryTravelPointPairType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'minimumConnectionTime')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 374, 5))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(QueryTravelPointPairType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maximumConnectionTime')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 375, 5))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(QueryTravelPointPairType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maximumPermittedConnections')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 376, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(QueryTravelPointPairType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maximumTransitTime')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 377, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTravelPointPairType._Automaton = _BuildAutomaton_34()




CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'carrier'), _ImportedBinding_silvercom.CarrierType, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 336, 11)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'carrier')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 336, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_35()




CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'equipmentType'), _ImportedBinding_silvercom.EquipmentTypeType, scope=CTD_ANON_28, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 358, 11)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'equipmentType')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 358, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_36()




ShoppingTransactionFeeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=ShoppingTransactionFeeType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 387, 5)))

ShoppingTransactionFeeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'applicableLegs'), CTD_ANON_25, scope=ShoppingTransactionFeeType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 388, 5)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ShoppingTransactionFeeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'fee')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 2578, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ShoppingTransactionFeeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 387, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ShoppingTransactionFeeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'applicableLegs')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/ShoppingServicesSchema_2_65.xsd', 388, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ShoppingTransactionFeeType._Automaton = _BuildAutomaton_37()

