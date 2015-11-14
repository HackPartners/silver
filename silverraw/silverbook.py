# ./silverbook.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:846b4fb611d42d5772c6e937231ac0b1d13a4e8c
# Generated 2015-11-14 16:58:02.798289 by PyXB version 1.2.4 using Python 2.7.9.final.0
# Namespace http://railgds.net/ws/booking [xmlns:book]

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
Namespace = pyxb.namespace.NamespaceForURI('http://railgds.net/ws/booking', create_if_missing=True)
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 670, 68)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.SEAT = STD_ANON._CF_enumeration.addEnumeration(unicode_value='SEAT', tag='SEAT')
STD_ANON.TICKET = STD_ANON._CF_enumeration.addEnumeration(unicode_value='TICKET', tag='TICKET')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 686, 36)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.FULL = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='FULL', tag='FULL')
STD_ANON_.PARTIAL = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='PARTIAL', tag='PARTIAL')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1084, 20)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.CC = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='CC', tag='CC')
STD_ANON_2.DB = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='DB', tag='DB')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 53, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}formOfPayment uses Python identifier formOfPayment
    __formOfPayment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'formOfPayment'), 'formOfPayment', '__httprailgds_netwsbooking_CTD_ANON_httprailgds_netwsbookingformOfPayment', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 55, 32), )

    
    formOfPayment = property(__formOfPayment.value, __formOfPayment.set, None, None)

    
    # Element {http://railgds.net/ws/booking}creditCard uses Python identifier creditCard
    __creditCard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'creditCard'), 'creditCard', '__httprailgds_netwsbooking_CTD_ANON_httprailgds_netwsbookingcreditCard', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 57, 36), )

    
    creditCard = property(__creditCard.value, __creditCard.set, None, None)

    
    # Element {http://railgds.net/ws/booking}check uses Python identifier check
    __check = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'check'), 'check', '__httprailgds_netwsbooking_CTD_ANON_httprailgds_netwsbookingcheck', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 59, 36), )

    
    check = property(__check.value, __check.set, None, None)

    
    # Element {http://railgds.net/ws/booking}onAccount uses Python identifier onAccount
    __onAccount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'onAccount'), 'onAccount', '__httprailgds_netwsbooking_CTD_ANON_httprailgds_netwsbookingonAccount', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 60, 36), )

    
    onAccount = property(__onAccount.value, __onAccount.set, None, None)

    
    # Element {http://railgds.net/ws/booking}debitCard uses Python identifier debitCard
    __debitCard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'debitCard'), 'debitCard', '__httprailgds_netwsbooking_CTD_ANON_httprailgds_netwsbookingdebitCard', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 61, 36), )

    
    debitCard = property(__debitCard.value, __debitCard.set, None, None)

    
    # Element {http://railgds.net/ws/booking}voucher uses Python identifier voucher
    __voucher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'voucher'), 'voucher', '__httprailgds_netwsbooking_CTD_ANON_httprailgds_netwsbookingvoucher', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 62, 36), )

    
    voucher = property(__voucher.value, __voucher.set, None, None)

    
    # Element {http://railgds.net/ws/booking}eCheck uses Python identifier eCheck
    __eCheck = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eCheck'), 'eCheck', '__httprailgds_netwsbooking_CTD_ANON_httprailgds_netwsbookingeCheck', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 63, 36), )

    
    eCheck = property(__eCheck.value, __eCheck.set, None, None)

    
    # Element {http://railgds.net/ws/booking}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'amount'), 'amount', '__httprailgds_netwsbooking_CTD_ANON_httprailgds_netwsbookingamount', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 65, 32), )

    
    amount = property(__amount.value, __amount.set, None, None)

    _ElementMap.update({
        __formOfPayment.name() : __formOfPayment,
        __creditCard.name() : __creditCard,
        __check.name() : __check,
        __onAccount.name() : __onAccount,
        __debitCard.name() : __debitCard,
        __voucher.name() : __voucher,
        __eCheck.name() : __eCheck,
        __amount.name() : __amount
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 97, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}confirmBooking uses Python identifier confirmBooking
    __confirmBooking = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'confirmBooking'), 'confirmBooking', '__httprailgds_netwsbooking_CTD_ANON__httprailgds_netwsbookingconfirmBooking', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 99, 32), )

    
    confirmBooking = property(__confirmBooking.value, __confirmBooking.set, None, None)

    _ElementMap.update({
        __confirmBooking.name() : __confirmBooking
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 108, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}returnReservationDetails uses Python identifier returnReservationDetails
    __returnReservationDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), 'returnReservationDetails', '__httprailgds_netwsbooking_CTD_ANON_2_httprailgds_netwsbookingreturnReservationDetails', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 110, 32), )

    
    returnReservationDetails = property(__returnReservationDetails.value, __returnReservationDetails.set, None, None)

    _ElementMap.update({
        __returnReservationDetails.name() : __returnReservationDetails
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 117, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}payerAuthenticationResponse uses Python identifier payerAuthenticationResponse
    __payerAuthenticationResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'payerAuthenticationResponse'), 'payerAuthenticationResponse', '__httprailgds_netwsbooking_CTD_ANON_3_httprailgds_netwsbookingpayerAuthenticationResponse', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 119, 32), )

    
    payerAuthenticationResponse = property(__payerAuthenticationResponse.value, __payerAuthenticationResponse.set, None, None)

    _ElementMap.update({
        __payerAuthenticationResponse.name() : __payerAuthenticationResponse
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 146, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}returnReservationDetails uses Python identifier returnReservationDetails
    __returnReservationDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), 'returnReservationDetails', '__httprailgds_netwsbooking_CTD_ANON_4_httprailgds_netwsbookingreturnReservationDetails', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 148, 32), )

    
    returnReservationDetails = property(__returnReservationDetails.value, __returnReservationDetails.set, None, None)

    _ElementMap.update({
        __returnReservationDetails.name() : __returnReservationDetails
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 162, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}isEnrolled uses Python identifier isEnrolled
    __isEnrolled = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'isEnrolled'), 'isEnrolled', '__httprailgds_netwsbooking_CTD_ANON_5_httprailgds_netwsbookingisEnrolled', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 164, 32), )

    
    isEnrolled = property(__isEnrolled.value, __isEnrolled.set, None, None)

    
    # Element {http://railgds.net/ws/booking}processor uses Python identifier processor
    __processor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'processor'), 'processor', '__httprailgds_netwsbooking_CTD_ANON_5_httprailgds_netwsbookingprocessor', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 165, 32), )

    
    processor = property(__processor.value, __processor.set, None, None)

    
    # Element {http://railgds.net/ws/booking}accessControlServerUrl uses Python identifier accessControlServerUrl
    __accessControlServerUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accessControlServerUrl'), 'accessControlServerUrl', '__httprailgds_netwsbooking_CTD_ANON_5_httprailgds_netwsbookingaccessControlServerUrl', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 166, 32), )

    
    accessControlServerUrl = property(__accessControlServerUrl.value, __accessControlServerUrl.set, None, None)

    
    # Element {http://railgds.net/ws/booking}payerAuthenticationRequest uses Python identifier payerAuthenticationRequest
    __payerAuthenticationRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'payerAuthenticationRequest'), 'payerAuthenticationRequest', '__httprailgds_netwsbooking_CTD_ANON_5_httprailgds_netwsbookingpayerAuthenticationRequest', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 168, 32), )

    
    payerAuthenticationRequest = property(__payerAuthenticationRequest.value, __payerAuthenticationRequest.set, None, None)

    _ElementMap.update({
        __isEnrolled.name() : __isEnrolled,
        __processor.name() : __processor,
        __accessControlServerUrl.name() : __accessControlServerUrl,
        __payerAuthenticationRequest.name() : __payerAuthenticationRequest
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 183, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}externalId uses Python identifier externalId
    __externalId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'externalId'), 'externalId', '__httprailgds_netwsbooking_CTD_ANON_6_httprailgds_netwsbookingexternalId', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 185, 32), )

    
    externalId = property(__externalId.value, __externalId.set, None, None)

    
    # Element {http://railgds.net/ws/booking}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httprailgds_netwsbooking_CTD_ANON_6_httprailgds_netwsbookingname', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 186, 32), )

    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __externalId.name() : __externalId,
        __name.name() : __name
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 200, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}note uses Python identifier note
    __note = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'note'), 'note', '__httprailgds_netwsbooking_CTD_ANON_7_httprailgds_netwsbookingnote', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 202, 32), )

    
    note = property(__note.value, __note.set, None, None)

    _ElementMap.update({
        __note.name() : __note
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 208, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}orderNote uses Python identifier orderNote
    __orderNote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderNote'), 'orderNote', '__httprailgds_netwsbooking_CTD_ANON_8_httprailgds_netwsbookingorderNote', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 210, 32), )

    
    orderNote = property(__orderNote.value, __orderNote.set, None, None)

    _ElementMap.update({
        __orderNote.name() : __orderNote
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 227, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}ticketableFareLocator uses Python identifier ticketableFareLocator
    __ticketableFareLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ticketableFareLocator'), 'ticketableFareLocator', '__httprailgds_netwsbooking_CTD_ANON_9_httprailgds_netwsbookingticketableFareLocator', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 229, 32), )

    
    ticketableFareLocator = property(__ticketableFareLocator.value, __ticketableFareLocator.set, None, None)

    _ElementMap.update({
        __ticketableFareLocator.name() : __ticketableFareLocator
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 235, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}alwaysAcceptCancellationFee uses Python identifier alwaysAcceptCancellationFee
    __alwaysAcceptCancellationFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'alwaysAcceptCancellationFee'), 'alwaysAcceptCancellationFee', '__httprailgds_netwsbooking_CTD_ANON_10_httprailgds_netwsbookingalwaysAcceptCancellationFee', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 237, 32), )

    
    alwaysAcceptCancellationFee = property(__alwaysAcceptCancellationFee.value, __alwaysAcceptCancellationFee.set, None, None)

    _ElementMap.update({
        __alwaysAcceptCancellationFee.name() : __alwaysAcceptCancellationFee
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 243, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}returnReservationDetails uses Python identifier returnReservationDetails
    __returnReservationDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), 'returnReservationDetails', '__httprailgds_netwsbooking_CTD_ANON_11_httprailgds_netwsbookingreturnReservationDetails', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 245, 32), )

    
    returnReservationDetails = property(__returnReservationDetails.value, __returnReservationDetails.set, None, None)

    _ElementMap.update({
        __returnReservationDetails.name() : __returnReservationDetails
    })
    _AttributeMap.update({
        
    })



# Complex type {http://railgds.net/ws/booking}RefundInformationType with content type ELEMENT_ONLY
class RefundInformationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://railgds.net/ws/booking}RefundInformationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RefundInformationType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 261, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}processRefundWithCancel uses Python identifier processRefundWithCancel
    __processRefundWithCancel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'processRefundWithCancel'), 'processRefundWithCancel', '__httprailgds_netwsbooking_RefundInformationType_httprailgds_netwsbookingprocessRefundWithCancel', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 263, 12), )

    
    processRefundWithCancel = property(__processRefundWithCancel.value, __processRefundWithCancel.set, None, None)

    
    # Element {http://railgds.net/ws/booking}receiptNumber uses Python identifier receiptNumber
    __receiptNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'receiptNumber'), 'receiptNumber', '__httprailgds_netwsbooking_RefundInformationType_httprailgds_netwsbookingreceiptNumber', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 264, 12), )

    
    receiptNumber = property(__receiptNumber.value, __receiptNumber.set, None, None)

    
    # Element {http://railgds.net/ws/booking}refundAmount uses Python identifier refundAmount
    __refundAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'refundAmount'), 'refundAmount', '__httprailgds_netwsbooking_RefundInformationType_httprailgds_netwsbookingrefundAmount', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 266, 12), )

    
    refundAmount = property(__refundAmount.value, __refundAmount.set, None, None)

    
    # Element {http://railgds.net/ws/booking}refundReason uses Python identifier refundReason
    __refundReason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'refundReason'), 'refundReason', '__httprailgds_netwsbooking_RefundInformationType_httprailgds_netwsbookingrefundReason', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 267, 12), )

    
    refundReason = property(__refundReason.value, __refundReason.set, None, None)

    _ElementMap.update({
        __processRefundWithCancel.name() : __processRefundWithCancel,
        __receiptNumber.name() : __receiptNumber,
        __refundAmount.name() : __refundAmount,
        __refundReason.name() : __refundReason
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RefundInformationType', RefundInformationType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 291, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}returnReservationDetails uses Python identifier returnReservationDetails
    __returnReservationDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), 'returnReservationDetails', '__httprailgds_netwsbooking_CTD_ANON_12_httprailgds_netwsbookingreturnReservationDetails', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 293, 32), )

    
    returnReservationDetails = property(__returnReservationDetails.value, __returnReservationDetails.set, None, None)

    _ElementMap.update({
        __returnReservationDetails.name() : __returnReservationDetails
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 329, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}returnReservationDetails uses Python identifier returnReservationDetails
    __returnReservationDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), 'returnReservationDetails', '__httprailgds_netwsbooking_CTD_ANON_13_httprailgds_netwsbookingreturnReservationDetails', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 331, 32), )

    
    returnReservationDetails = property(__returnReservationDetails.value, __returnReservationDetails.set, None, None)

    _ElementMap.update({
        __returnReservationDetails.name() : __returnReservationDetails
    })
    _AttributeMap.update({
        
    })



# Complex type {http://railgds.net/ws/booking}ClaimValueDocumentResultType with content type ELEMENT_ONLY
class ClaimValueDocumentResultType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://railgds.net/ws/booking}ClaimValueDocumentResultType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClaimValueDocumentResultType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 355, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}result uses Python identifier result
    __result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'result'), 'result', '__httprailgds_netwsbooking_ClaimValueDocumentResultType_httprailgds_netwsbookingresult', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 357, 12), )

    
    result = property(__result.value, __result.set, None, None)

    
    # Element {http://railgds.net/ws/booking}claimValueDocumentUrl uses Python identifier claimValueDocumentUrl
    __claimValueDocumentUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'claimValueDocumentUrl'), 'claimValueDocumentUrl', '__httprailgds_netwsbooking_ClaimValueDocumentResultType_httprailgds_netwsbookingclaimValueDocumentUrl', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 358, 12), )

    
    claimValueDocumentUrl = property(__claimValueDocumentUrl.value, __claimValueDocumentUrl.set, None, None)

    _ElementMap.update({
        __result.name() : __result,
        __claimValueDocumentUrl.name() : __claimValueDocumentUrl
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ClaimValueDocumentResultType', ClaimValueDocumentResultType)


# Complex type {http://railgds.net/ws/booking}ConfirmationInformationType with content type ELEMENT_ONLY
class ConfirmationInformationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://railgds.net/ws/booking}ConfirmationInformationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConfirmationInformationType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 362, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}valueDocumentRetrievalInformation uses Python identifier valueDocumentRetrievalInformation
    __valueDocumentRetrievalInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueDocumentRetrievalInformation'), 'valueDocumentRetrievalInformation', '__httprailgds_netwsbooking_ConfirmationInformationType_httprailgds_netwsbookingvalueDocumentRetrievalInformation', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 365, 16), )

    
    valueDocumentRetrievalInformation = property(__valueDocumentRetrievalInformation.value, __valueDocumentRetrievalInformation.set, None, None)

    
    # Element {http://railgds.net/ws/booking}selectedConfirmationOption uses Python identifier selectedConfirmationOption
    __selectedConfirmationOption = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'selectedConfirmationOption'), 'selectedConfirmationOption', '__httprailgds_netwsbooking_ConfirmationInformationType_httprailgds_netwsbookingselectedConfirmationOption', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 386, 16), )

    
    selectedConfirmationOption = property(__selectedConfirmationOption.value, __selectedConfirmationOption.set, None, None)

    
    # Element {http://railgds.net/ws/booking}selectedTicketLanguage uses Python identifier selectedTicketLanguage
    __selectedTicketLanguage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'selectedTicketLanguage'), 'selectedTicketLanguage', '__httprailgds_netwsbooking_ConfirmationInformationType_httprailgds_netwsbookingselectedTicketLanguage', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 389, 12), )

    
    selectedTicketLanguage = property(__selectedTicketLanguage.value, __selectedTicketLanguage.set, None, None)

    _ElementMap.update({
        __valueDocumentRetrievalInformation.name() : __valueDocumentRetrievalInformation,
        __selectedConfirmationOption.name() : __selectedConfirmationOption,
        __selectedTicketLanguage.name() : __selectedTicketLanguage
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ConfirmationInformationType', ConfirmationInformationType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 367, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}customer uses Python identifier customer
    __customer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customer'), 'customer', '__httprailgds_netwsbooking_CTD_ANON_14_httprailgds_netwsbookingcustomer', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 369, 28), )

    
    customer = property(__customer.value, __customer.set, None, None)

    
    # Element {http://railgds.net/ws/booking}creditCardNumber uses Python identifier creditCardNumber
    __creditCardNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'creditCardNumber'), 'creditCardNumber', '__httprailgds_netwsbooking_CTD_ANON_14_httprailgds_netwsbookingcreditCardNumber', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 379, 28), )

    
    creditCardNumber = property(__creditCardNumber.value, __creditCardNumber.set, None, None)

    
    # Element {http://railgds.net/ws/booking}expirationDate uses Python identifier expirationDate
    __expirationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expirationDate'), 'expirationDate', '__httprailgds_netwsbooking_CTD_ANON_14_httprailgds_netwsbookingexpirationDate', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 380, 28), )

    
    expirationDate = property(__expirationDate.value, __expirationDate.set, None, None)

    _ElementMap.update({
        __customer.name() : __customer,
        __creditCardNumber.name() : __creditCardNumber,
        __expirationDate.name() : __expirationDate
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 370, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}nameLast uses Python identifier nameLast
    __nameLast = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nameLast'), 'nameLast', '__httprailgds_netwsbooking_CTD_ANON_15_httprailgds_netwsbookingnameLast', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 372, 40), )

    
    nameLast = property(__nameLast.value, __nameLast.set, None, None)

    
    # Element {http://railgds.net/ws/booking}nameFirst uses Python identifier nameFirst
    __nameFirst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nameFirst'), 'nameFirst', '__httprailgds_netwsbooking_CTD_ANON_15_httprailgds_netwsbookingnameFirst', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 373, 40), )

    
    nameFirst = property(__nameFirst.value, __nameFirst.set, None, None)

    
    # Element {http://railgds.net/ws/booking}nameMiddle uses Python identifier nameMiddle
    __nameMiddle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nameMiddle'), 'nameMiddle', '__httprailgds_netwsbooking_CTD_ANON_15_httprailgds_netwsbookingnameMiddle', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 374, 40), )

    
    nameMiddle = property(__nameMiddle.value, __nameMiddle.set, None, None)

    _ElementMap.update({
        __nameLast.name() : __nameLast,
        __nameFirst.name() : __nameFirst,
        __nameMiddle.name() : __nameMiddle
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 405, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}passenger uses Python identifier passenger
    __passenger = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passenger'), 'passenger', '__httprailgds_netwsbooking_CTD_ANON_16_httprailgds_netwsbookingpassenger', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 407, 32), )

    
    passenger = property(__passenger.value, __passenger.set, None, None)

    _ElementMap.update({
        __passenger.name() : __passenger
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 414, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}pointToPointPrice uses Python identifier pointToPointPrice
    __pointToPointPrice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pointToPointPrice'), 'pointToPointPrice', '__httprailgds_netwsbooking_CTD_ANON_17_httprailgds_netwsbookingpointToPointPrice', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 416, 36), )

    
    pointToPointPrice = property(__pointToPointPrice.value, __pointToPointPrice.set, None, None)

    _ElementMap.update({
        __pointToPointPrice.name() : __pointToPointPrice
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 423, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}transactionFee uses Python identifier transactionFee
    __transactionFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionFee'), 'transactionFee', '__httprailgds_netwsbooking_CTD_ANON_18_httprailgds_netwsbookingtransactionFee', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 425, 32), )

    
    transactionFee = property(__transactionFee.value, __transactionFee.set, None, None)

    _ElementMap.update({
        __transactionFee.name() : __transactionFee
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 431, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}priceAcceptance uses Python identifier priceAcceptance
    __priceAcceptance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'priceAcceptance'), 'priceAcceptance', '__httprailgds_netwsbooking_CTD_ANON_19_httprailgds_netwsbookingpriceAcceptance', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 433, 32), )

    
    priceAcceptance = property(__priceAcceptance.value, __priceAcceptance.set, None, None)

    
    # Element {http://railgds.net/ws/booking}shopAncillary uses Python identifier shopAncillary
    __shopAncillary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shopAncillary'), 'shopAncillary', '__httprailgds_netwsbooking_CTD_ANON_19_httprailgds_netwsbookingshopAncillary', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 446, 32), )

    
    shopAncillary = property(__shopAncillary.value, __shopAncillary.set, None, None)

    _ElementMap.update({
        __priceAcceptance.name() : __priceAcceptance,
        __shopAncillary.name() : __shopAncillary
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 434, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}acceptAny uses Python identifier acceptAny
    __acceptAny = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'acceptAny'), 'acceptAny', '__httprailgds_netwsbooking_CTD_ANON_20_httprailgds_netwsbookingacceptAny', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 436, 44), )

    
    acceptAny = property(__acceptAny.value, __acceptAny.set, None, None)

    
    # Element {http://railgds.net/ws/booking}acceptHigher uses Python identifier acceptHigher
    __acceptHigher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'acceptHigher'), 'acceptHigher', '__httprailgds_netwsbooking_CTD_ANON_20_httprailgds_netwsbookingacceptHigher', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 438, 48), )

    
    acceptHigher = property(__acceptHigher.value, __acceptHigher.set, None, None)

    
    # Element {http://railgds.net/ws/booking}acceptLower uses Python identifier acceptLower
    __acceptLower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'acceptLower'), 'acceptLower', '__httprailgds_netwsbooking_CTD_ANON_20_httprailgds_netwsbookingacceptLower', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 440, 48), )

    
    acceptLower = property(__acceptLower.value, __acceptLower.set, None, None)

    _ElementMap.update({
        __acceptAny.name() : __acceptAny,
        __acceptHigher.name() : __acceptHigher,
        __acceptLower.name() : __acceptLower
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 451, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}returnReservationDetails uses Python identifier returnReservationDetails
    __returnReservationDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), 'returnReservationDetails', '__httprailgds_netwsbooking_CTD_ANON_21_httprailgds_netwsbookingreturnReservationDetails', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 453, 32), )

    
    returnReservationDetails = property(__returnReservationDetails.value, __returnReservationDetails.set, None, None)

    _ElementMap.update({
        __returnReservationDetails.name() : __returnReservationDetails
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 461, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}fareQualifier uses Python identifier fareQualifier
    __fareQualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fareQualifier'), 'fareQualifier', '__httprailgds_netwsbooking_CTD_ANON_22_httprailgds_netwsbookingfareQualifier', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 463, 32), )

    
    fareQualifier = property(__fareQualifier.value, __fareQualifier.set, None, None)

    _ElementMap.update({
        __fareQualifier.name() : __fareQualifier
    })
    _AttributeMap.update({
        
    })



# Complex type {http://railgds.net/ws/booking}TravelPassQuery with content type ELEMENT_ONLY
class TravelPassQuery (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://railgds.net/ws/booking}TravelPassQuery with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TravelPassQuery')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 485, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}travelPointPair uses Python identifier travelPointPair
    __travelPointPair = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'travelPointPair'), 'travelPointPair', '__httprailgds_netwsbooking_TravelPassQuery_httprailgds_netwsbookingtravelPointPair', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 487, 12), )

    
    travelPointPair = property(__travelPointPair.value, __travelPointPair.set, None, None)

    
    # Element {http://railgds.net/ws/booking}passPrices uses Python identifier passPrices
    __passPrices = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passPrices'), 'passPrices', '__httprailgds_netwsbooking_TravelPassQuery_httprailgds_netwsbookingpassPrices', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 488, 12), )

    
    passPrices = property(__passPrices.value, __passPrices.set, None, None)

    
    # Element {http://railgds.net/ws/booking}passIssueType uses Python identifier passIssueType
    __passIssueType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passIssueType'), 'passIssueType', '__httprailgds_netwsbooking_TravelPassQuery_httprailgds_netwsbookingpassIssueType', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 496, 12), )

    
    passIssueType = property(__passIssueType.value, __passIssueType.set, None, None)

    _ElementMap.update({
        __travelPointPair.name() : __travelPointPair,
        __passPrices.name() : __passPrices,
        __passIssueType.name() : __passIssueType
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'TravelPassQuery', TravelPassQuery)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 489, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}travelPassPrice uses Python identifier travelPassPrice
    __travelPassPrice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'travelPassPrice'), 'travelPassPrice', '__httprailgds_netwsbooking_CTD_ANON_23_httprailgds_netwsbookingtravelPassPrice', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 491, 24), )

    
    travelPassPrice = property(__travelPassPrice.value, __travelPassPrice.set, None, None)

    _ElementMap.update({
        __travelPassPrice.name() : __travelPassPrice
    })
    _AttributeMap.update({
        
    })



# Complex type {http://railgds.net/ws/booking}FulfillmentInformationType with content type ELEMENT_ONLY
class FulfillmentInformationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://railgds.net/ws/booking}FulfillmentInformationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FulfillmentInformationType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 499, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}ticketOption uses Python identifier ticketOption
    __ticketOption = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ticketOption'), 'ticketOption', '__httprailgds_netwsbooking_FulfillmentInformationType_httprailgds_netwsbookingticketOption', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 501, 12), )

    
    ticketOption = property(__ticketOption.value, __ticketOption.set, None, None)

    
    # Element {http://railgds.net/ws/booking}shippingName uses Python identifier shippingName
    __shippingName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shippingName'), 'shippingName', '__httprailgds_netwsbooking_FulfillmentInformationType_httprailgds_netwsbookingshippingName', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 502, 12), )

    
    shippingName = property(__shippingName.value, __shippingName.set, None, None)

    
    # Element {http://railgds.net/ws/booking}shippingAddress uses Python identifier shippingAddress
    __shippingAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shippingAddress'), 'shippingAddress', '__httprailgds_netwsbooking_FulfillmentInformationType_httprailgds_netwsbookingshippingAddress', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 503, 12), )

    
    shippingAddress = property(__shippingAddress.value, __shippingAddress.set, None, None)

    
    # Element {http://railgds.net/ws/booking}phoneNumber uses Python identifier phoneNumber
    __phoneNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'phoneNumber'), 'phoneNumber', '__httprailgds_netwsbooking_FulfillmentInformationType_httprailgds_netwsbookingphoneNumber', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 504, 12), )

    
    phoneNumber = property(__phoneNumber.value, __phoneNumber.set, None, None)

    _ElementMap.update({
        __ticketOption.name() : __ticketOption,
        __shippingName.name() : __shippingName,
        __shippingAddress.name() : __shippingAddress,
        __phoneNumber.name() : __phoneNumber
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'FulfillmentInformationType', FulfillmentInformationType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 526, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}order uses Python identifier order
    __order = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'order'), 'order', '__httprailgds_netwsbooking_CTD_ANON_24_httprailgds_netwsbookingorder', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 528, 32), )

    
    order = property(__order.value, __order.set, None, None)

    _ElementMap.update({
        __order.name() : __order
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 529, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}alternativeTicketPickupLocation uses Python identifier alternativeTicketPickupLocation
    __alternativeTicketPickupLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'alternativeTicketPickupLocation'), 'alternativeTicketPickupLocation', '__httprailgds_netwsbooking_CTD_ANON_25_httprailgds_netwsbookingalternativeTicketPickupLocation', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 531, 44), )

    
    alternativeTicketPickupLocation = property(__alternativeTicketPickupLocation.value, __alternativeTicketPickupLocation.set, None, None)

    
    # Attribute orderNumber uses Python identifier orderNumber
    __orderNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'orderNumber'), 'orderNumber', '__httprailgds_netwsbooking_CTD_ANON_25_orderNumber', pyxb.binding.datatypes.string, required=True)
    __orderNumber._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 534, 40)
    __orderNumber._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 534, 40)
    
    orderNumber = property(__orderNumber.value, __orderNumber.set, None, None)

    _ElementMap.update({
        __alternativeTicketPickupLocation.name() : __alternativeTicketPickupLocation
    })
    _AttributeMap.update({
        __orderNumber.name() : __orderNumber
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 542, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}includeOrderDetails uses Python identifier includeOrderDetails
    __includeOrderDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includeOrderDetails'), 'includeOrderDetails', '__httprailgds_netwsbooking_CTD_ANON_26_httprailgds_netwsbookingincludeOrderDetails', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 544, 32), )

    
    includeOrderDetails = property(__includeOrderDetails.value, __includeOrderDetails.set, None, None)

    
    # Element {http://railgds.net/ws/booking}includeOrderCosts uses Python identifier includeOrderCosts
    __includeOrderCosts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includeOrderCosts'), 'includeOrderCosts', '__httprailgds_netwsbooking_CTD_ANON_26_httprailgds_netwsbookingincludeOrderCosts', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 546, 32), )

    
    includeOrderCosts = property(__includeOrderCosts.value, __includeOrderCosts.set, None, None)

    
    # Element {http://railgds.net/ws/booking}includePassengerDetails uses Python identifier includePassengerDetails
    __includePassengerDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includePassengerDetails'), 'includePassengerDetails', '__httprailgds_netwsbooking_CTD_ANON_26_httprailgds_netwsbookingincludePassengerDetails', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 547, 32), )

    
    includePassengerDetails = property(__includePassengerDetails.value, __includePassengerDetails.set, None, None)

    
    # Element {http://railgds.net/ws/booking}includeFinancials uses Python identifier includeFinancials
    __includeFinancials = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includeFinancials'), 'includeFinancials', '__httprailgds_netwsbooking_CTD_ANON_26_httprailgds_netwsbookingincludeFinancials', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 549, 32), )

    
    includeFinancials = property(__includeFinancials.value, __includeFinancials.set, None, None)

    
    # Element {http://railgds.net/ws/booking}includePaymentRequirements uses Python identifier includePaymentRequirements
    __includePaymentRequirements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includePaymentRequirements'), 'includePaymentRequirements', '__httprailgds_netwsbooking_CTD_ANON_26_httprailgds_netwsbookingincludePaymentRequirements', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 550, 32), )

    
    includePaymentRequirements = property(__includePaymentRequirements.value, __includePaymentRequirements.set, None, None)

    
    # Element {http://railgds.net/ws/booking}includeTicketingOptions uses Python identifier includeTicketingOptions
    __includeTicketingOptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includeTicketingOptions'), 'includeTicketingOptions', '__httprailgds_netwsbooking_CTD_ANON_26_httprailgds_netwsbookingincludeTicketingOptions', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 552, 32), )

    
    includeTicketingOptions = property(__includeTicketingOptions.value, __includeTicketingOptions.set, None, None)

    
    # Element {http://railgds.net/ws/booking}includeNotes uses Python identifier includeNotes
    __includeNotes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includeNotes'), 'includeNotes', '__httprailgds_netwsbooking_CTD_ANON_26_httprailgds_netwsbookingincludeNotes', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 554, 32), )

    
    includeNotes = property(__includeNotes.value, __includeNotes.set, None, None)

    
    # Element {http://railgds.net/ws/booking}includeFulfillmentInformation uses Python identifier includeFulfillmentInformation
    __includeFulfillmentInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includeFulfillmentInformation'), 'includeFulfillmentInformation', '__httprailgds_netwsbooking_CTD_ANON_26_httprailgds_netwsbookingincludeFulfillmentInformation', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 555, 32), )

    
    includeFulfillmentInformation = property(__includeFulfillmentInformation.value, __includeFulfillmentInformation.set, None, None)

    _ElementMap.update({
        __includeOrderDetails.name() : __includeOrderDetails,
        __includeOrderCosts.name() : __includeOrderCosts,
        __includePassengerDetails.name() : __includePassengerDetails,
        __includeFinancials.name() : __includeFinancials,
        __includePaymentRequirements.name() : __includePaymentRequirements,
        __includeTicketingOptions.name() : __includeTicketingOptions,
        __includeNotes.name() : __includeNotes,
        __includeFulfillmentInformation.name() : __includeFulfillmentInformation
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 570, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}note uses Python identifier note
    __note = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'note'), 'note', '__httprailgds_netwsbooking_CTD_ANON_27_httprailgds_netwsbookingnote', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 572, 32), )

    
    note = property(__note.value, __note.set, None, None)

    _ElementMap.update({
        __note.name() : __note
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 594, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}returnReservationDetails uses Python identifier returnReservationDetails
    __returnReservationDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), 'returnReservationDetails', '__httprailgds_netwsbooking_CTD_ANON_28_httprailgds_netwsbookingreturnReservationDetails', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 596, 32), )

    
    returnReservationDetails = property(__returnReservationDetails.value, __returnReservationDetails.set, None, None)

    _ElementMap.update({
        __returnReservationDetails.name() : __returnReservationDetails
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 611, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}directDeliveryRequested uses Python identifier directDeliveryRequested
    __directDeliveryRequested = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'directDeliveryRequested'), 'directDeliveryRequested', '__httprailgds_netwsbooking_CTD_ANON_29_httprailgds_netwsbookingdirectDeliveryRequested', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 613, 32), )

    
    directDeliveryRequested = property(__directDeliveryRequested.value, __directDeliveryRequested.set, None, None)

    
    # Element {http://railgds.net/ws/booking}valueDocumentURL uses Python identifier valueDocumentURL
    __valueDocumentURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueDocumentURL'), 'valueDocumentURL', '__httprailgds_netwsbooking_CTD_ANON_29_httprailgds_netwsbookingvalueDocumentURL', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 614, 32), )

    
    valueDocumentURL = property(__valueDocumentURL.value, __valueDocumentURL.set, None, None)

    
    # Element {http://railgds.net/ws/booking}valueDocumentPDF uses Python identifier valueDocumentPDF
    __valueDocumentPDF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueDocumentPDF'), 'valueDocumentPDF', '__httprailgds_netwsbooking_CTD_ANON_29_httprailgds_netwsbookingvalueDocumentPDF', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 624, 32), )

    
    valueDocumentPDF = property(__valueDocumentPDF.value, __valueDocumentPDF.set, None, None)

    _ElementMap.update({
        __directDeliveryRequested.name() : __directDeliveryRequested,
        __valueDocumentURL.name() : __valueDocumentURL,
        __valueDocumentPDF.name() : __valueDocumentPDF
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 615, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute expirationDateTime uses Python identifier expirationDateTime
    __expirationDateTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'expirationDateTime'), 'expirationDateTime', '__httprailgds_netwsbooking_CTD_ANON_30_expirationDateTime', pyxb.binding.datatypes.dateTime)
    __expirationDateTime._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 618, 48)
    __expirationDateTime._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 618, 48)
    
    expirationDateTime = property(__expirationDateTime.value, __expirationDateTime.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __expirationDateTime.name() : __expirationDateTime
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 625, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute encoding uses Python identifier encoding
    __encoding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'encoding'), 'encoding', '__httprailgds_netwsbooking_CTD_ANON_31_encoding', pyxb.binding.datatypes.string)
    __encoding._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 628, 48)
    __encoding._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 628, 48)
    
    encoding = property(__encoding.value, __encoding.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __encoding.name() : __encoding
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 655, 40)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}coupon uses Python identifier coupon
    __coupon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coupon'), 'coupon', '__httprailgds_netwsbooking_CTD_ANON_32_httprailgds_netwsbookingcoupon', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 657, 48), )

    
    coupon = property(__coupon.value, __coupon.set, None, None)

    _ElementMap.update({
        __coupon.name() : __coupon
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_33 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 696, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}coupons uses Python identifier coupons
    __coupons = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coupons'), 'coupons', '__httprailgds_netwsbooking_CTD_ANON_33_httprailgds_netwsbookingcoupons', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 698, 36), )

    
    coupons = property(__coupons.value, __coupons.set, None, None)

    
    # Element {http://railgds.net/ws/booking}reverseRevenue uses Python identifier reverseRevenue
    __reverseRevenue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reverseRevenue'), 'reverseRevenue', '__httprailgds_netwsbooking_CTD_ANON_33_httprailgds_netwsbookingreverseRevenue', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 725, 36), )

    
    reverseRevenue = property(__reverseRevenue.value, __reverseRevenue.set, None, None)

    
    # Element {http://railgds.net/ws/booking}reverseCost uses Python identifier reverseCost
    __reverseCost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reverseCost'), 'reverseCost', '__httprailgds_netwsbooking_CTD_ANON_33_httprailgds_netwsbookingreverseCost', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 733, 36), )

    
    reverseCost = property(__reverseCost.value, __reverseCost.set, None, None)

    
    # Element {http://railgds.net/ws/booking}cancellationPenalty uses Python identifier cancellationPenalty
    __cancellationPenalty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cancellationPenalty'), 'cancellationPenalty', '__httprailgds_netwsbooking_CTD_ANON_33_httprailgds_netwsbookingcancellationPenalty', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 741, 36), )

    
    cancellationPenalty = property(__cancellationPenalty.value, __cancellationPenalty.set, None, None)

    _ElementMap.update({
        __coupons.name() : __coupons,
        __reverseRevenue.name() : __reverseRevenue,
        __reverseCost.name() : __reverseCost,
        __cancellationPenalty.name() : __cancellationPenalty
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_34 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 699, 40)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}coupon uses Python identifier coupon
    __coupon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coupon'), 'coupon', '__httprailgds_netwsbooking_CTD_ANON_34_httprailgds_netwsbookingcoupon', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 701, 48), )

    
    coupon = property(__coupon.value, __coupon.set, None, None)

    _ElementMap.update({
        __coupon.name() : __coupon
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_35 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 709, 50)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__httprailgds_netwsbooking_CTD_ANON_35_code', pyxb.binding.datatypes.string)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 712, 50)
    __code._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 712, 50)
    
    code = property(__code.value, __code.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __code.name() : __code
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_36 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 726, 40)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'amount'), 'amount', '__httprailgds_netwsbooking_CTD_ANON_36_httprailgds_netwsbookingamount', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 728, 48), )

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://railgds.net/ws/booking}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httprailgds_netwsbooking_CTD_ANON_36_httprailgds_netwsbookingdescription', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 729, 48), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __amount.name() : __amount,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_37 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 734, 40)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'amount'), 'amount', '__httprailgds_netwsbooking_CTD_ANON_37_httprailgds_netwsbookingamount', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 736, 48), )

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://railgds.net/ws/booking}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httprailgds_netwsbooking_CTD_ANON_37_httprailgds_netwsbookingdescription', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 737, 48), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __amount.name() : __amount,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_38 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 748, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}returnReservationDetails uses Python identifier returnReservationDetails
    __returnReservationDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), 'returnReservationDetails', '__httprailgds_netwsbooking_CTD_ANON_38_httprailgds_netwsbookingreturnReservationDetails', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 750, 32), )

    
    returnReservationDetails = property(__returnReservationDetails.value, __returnReservationDetails.set, None, None)

    _ElementMap.update({
        __returnReservationDetails.name() : __returnReservationDetails
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_39 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 779, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}passengerLastName uses Python identifier passengerLastName
    __passengerLastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passengerLastName'), 'passengerLastName', '__httprailgds_netwsbooking_CTD_ANON_39_httprailgds_netwsbookingpassengerLastName', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 781, 32), )

    
    passengerLastName = property(__passengerLastName.value, __passengerLastName.set, None, None)

    
    # Element {http://railgds.net/ws/booking}emailAddress uses Python identifier emailAddress
    __emailAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'emailAddress'), 'emailAddress', '__httprailgds_netwsbooking_CTD_ANON_39_httprailgds_netwsbookingemailAddress', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 782, 32), )

    
    emailAddress = property(__emailAddress.value, __emailAddress.set, None, None)

    
    # Element {http://railgds.net/ws/booking}supplyChannelLocator uses Python identifier supplyChannelLocator
    __supplyChannelLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supplyChannelLocator'), 'supplyChannelLocator', '__httprailgds_netwsbooking_CTD_ANON_39_httprailgds_netwsbookingsupplyChannelLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 783, 32), )

    
    supplyChannelLocator = property(__supplyChannelLocator.value, __supplyChannelLocator.set, None, None)

    _ElementMap.update({
        __passengerLastName.name() : __passengerLastName,
        __emailAddress.name() : __emailAddress,
        __supplyChannelLocator.name() : __supplyChannelLocator
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_40 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 800, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}bookingRecord uses Python identifier bookingRecord
    __bookingRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), 'bookingRecord', '__httprailgds_netwsbooking_CTD_ANON_40_httprailgds_netwsbookingbookingRecord', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 802, 32), )

    
    bookingRecord = property(__bookingRecord.value, __bookingRecord.set, None, None)

    _ElementMap.update({
        __bookingRecord.name() : __bookingRecord
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_41 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 824, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_42 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 832, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}passengers uses Python identifier passengers
    __passengers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passengers'), 'passengers', '__httprailgds_netwsbooking_CTD_ANON_42_httprailgds_netwsbookingpassengers', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 834, 32), )

    
    passengers = property(__passengers.value, __passengers.set, None, None)

    
    # Element {http://railgds.net/ws/booking}legSolutions uses Python identifier legSolutions
    __legSolutions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legSolutions'), 'legSolutions', '__httprailgds_netwsbooking_CTD_ANON_42_httprailgds_netwsbookinglegSolutions', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 842, 32), )

    
    legSolutions = property(__legSolutions.value, __legSolutions.set, None, None)

    
    # Element {http://railgds.net/ws/booking}prices uses Python identifier prices
    __prices = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'prices'), 'prices', '__httprailgds_netwsbooking_CTD_ANON_42_httprailgds_netwsbookingprices', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 843, 32), )

    
    prices = property(__prices.value, __prices.set, None, None)

    
    # Element {http://railgds.net/ws/booking}parameters uses Python identifier parameters
    __parameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameters'), 'parameters', '__httprailgds_netwsbooking_CTD_ANON_42_httprailgds_netwsbookingparameters', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 852, 32), )

    
    parameters = property(__parameters.value, __parameters.set, None, None)

    _ElementMap.update({
        __passengers.name() : __passengers,
        __legSolutions.name() : __legSolutions,
        __prices.name() : __prices,
        __parameters.name() : __parameters
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_43 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 835, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}passenger uses Python identifier passenger
    __passenger = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passenger'), 'passenger', '__httprailgds_netwsbooking_CTD_ANON_43_httprailgds_netwsbookingpassenger', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 837, 44), )

    
    passenger = property(__passenger.value, __passenger.set, None, None)

    _ElementMap.update({
        __passenger.name() : __passenger
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_44 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 844, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}pointToPointPrice uses Python identifier pointToPointPrice
    __pointToPointPrice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pointToPointPrice'), 'pointToPointPrice', '__httprailgds_netwsbooking_CTD_ANON_44_httprailgds_netwsbookingpointToPointPrice', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 846, 44), )

    
    pointToPointPrice = property(__pointToPointPrice.value, __pointToPointPrice.set, None, None)

    _ElementMap.update({
        __pointToPointPrice.name() : __pointToPointPrice
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_45 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 853, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}priceAcceptance uses Python identifier priceAcceptance
    __priceAcceptance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'priceAcceptance'), 'priceAcceptance', '__httprailgds_netwsbooking_CTD_ANON_45_httprailgds_netwsbookingpriceAcceptance', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 855, 44), )

    
    priceAcceptance = property(__priceAcceptance.value, __priceAcceptance.set, None, None)

    
    # Element {http://railgds.net/ws/booking}shopAncillary uses Python identifier shopAncillary
    __shopAncillary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shopAncillary'), 'shopAncillary', '__httprailgds_netwsbooking_CTD_ANON_45_httprailgds_netwsbookingshopAncillary', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 868, 44), )

    
    shopAncillary = property(__shopAncillary.value, __shopAncillary.set, None, None)

    _ElementMap.update({
        __priceAcceptance.name() : __priceAcceptance,
        __shopAncillary.name() : __shopAncillary
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_46 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 856, 48)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}acceptAny uses Python identifier acceptAny
    __acceptAny = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'acceptAny'), 'acceptAny', '__httprailgds_netwsbooking_CTD_ANON_46_httprailgds_netwsbookingacceptAny', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 858, 50), )

    
    acceptAny = property(__acceptAny.value, __acceptAny.set, None, None)

    
    # Element {http://railgds.net/ws/booking}acceptHigher uses Python identifier acceptHigher
    __acceptHigher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'acceptHigher'), 'acceptHigher', '__httprailgds_netwsbooking_CTD_ANON_46_httprailgds_netwsbookingacceptHigher', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 860, 50), )

    
    acceptHigher = property(__acceptHigher.value, __acceptHigher.set, None, None)

    
    # Element {http://railgds.net/ws/booking}acceptLower uses Python identifier acceptLower
    __acceptLower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'acceptLower'), 'acceptLower', '__httprailgds_netwsbooking_CTD_ANON_46_httprailgds_netwsbookingacceptLower', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 862, 50), )

    
    acceptLower = property(__acceptLower.value, __acceptLower.set, None, None)

    _ElementMap.update({
        __acceptAny.name() : __acceptAny,
        __acceptHigher.name() : __acceptHigher,
        __acceptLower.name() : __acceptLower
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_47 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 877, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}passenger uses Python identifier passenger
    __passenger = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passenger'), 'passenger', '__httprailgds_netwsbooking_CTD_ANON_47_httprailgds_netwsbookingpassenger', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 879, 32), )

    
    passenger = property(__passenger.value, __passenger.set, None, None)

    _ElementMap.update({
        __passenger.name() : __passenger
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_48 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 885, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}returnReservationDetails uses Python identifier returnReservationDetails
    __returnReservationDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), 'returnReservationDetails', '__httprailgds_netwsbooking_CTD_ANON_48_httprailgds_netwsbookingreturnReservationDetails', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 887, 32), )

    
    returnReservationDetails = property(__returnReservationDetails.value, __returnReservationDetails.set, None, None)

    _ElementMap.update({
        __returnReservationDetails.name() : __returnReservationDetails
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_49 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 916, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}refund uses Python identifier refund
    __refund = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'refund'), 'refund', '__httprailgds_netwsbooking_CTD_ANON_49_httprailgds_netwsbookingrefund', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 918, 32), )

    
    refund = property(__refund.value, __refund.set, None, None)

    _ElementMap.update({
        __refund.name() : __refund
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_50 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 919, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}receiptNumber uses Python identifier receiptNumber
    __receiptNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'receiptNumber'), 'receiptNumber', '__httprailgds_netwsbooking_CTD_ANON_50_httprailgds_netwsbookingreceiptNumber', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 921, 44), )

    
    receiptNumber = property(__receiptNumber.value, __receiptNumber.set, None, None)

    
    # Element {http://railgds.net/ws/booking}refundAmount uses Python identifier refundAmount
    __refundAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'refundAmount'), 'refundAmount', '__httprailgds_netwsbooking_CTD_ANON_50_httprailgds_netwsbookingrefundAmount', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 923, 44), )

    
    refundAmount = property(__refundAmount.value, __refundAmount.set, None, None)

    
    # Element {http://railgds.net/ws/booking}refundReason uses Python identifier refundReason
    __refundReason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'refundReason'), 'refundReason', '__httprailgds_netwsbooking_CTD_ANON_50_httprailgds_netwsbookingrefundReason', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 924, 44), )

    
    refundReason = property(__refundReason.value, __refundReason.set, None, None)

    
    # Element {http://railgds.net/ws/booking}paymentProcessorInfo uses Python identifier paymentProcessorInfo
    __paymentProcessorInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentProcessorInfo'), 'paymentProcessorInfo', '__httprailgds_netwsbooking_CTD_ANON_50_httprailgds_netwsbookingpaymentProcessorInfo', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 926, 44), )

    
    paymentProcessorInfo = property(__paymentProcessorInfo.value, __paymentProcessorInfo.set, None, None)

    _ElementMap.update({
        __receiptNumber.name() : __receiptNumber,
        __refundAmount.name() : __refundAmount,
        __refundReason.name() : __refundReason,
        __paymentProcessorInfo.name() : __paymentProcessorInfo
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_51 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 935, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}returnReservationDetails uses Python identifier returnReservationDetails
    __returnReservationDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), 'returnReservationDetails', '__httprailgds_netwsbooking_CTD_ANON_51_httprailgds_netwsbookingreturnReservationDetails', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 937, 32), )

    
    returnReservationDetails = property(__returnReservationDetails.value, __returnReservationDetails.set, None, None)

    _ElementMap.update({
        __returnReservationDetails.name() : __returnReservationDetails
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_52 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 964, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}returnReservationDetails uses Python identifier returnReservationDetails
    __returnReservationDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), 'returnReservationDetails', '__httprailgds_netwsbooking_CTD_ANON_52_httprailgds_netwsbookingreturnReservationDetails', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 966, 32), )

    
    returnReservationDetails = property(__returnReservationDetails.value, __returnReservationDetails.set, None, None)

    _ElementMap.update({
        __returnReservationDetails.name() : __returnReservationDetails
    })
    _AttributeMap.update({
        
    })



# Complex type {http://railgds.net/ws/booking}BookingNotesType with content type ELEMENT_ONLY
class BookingNotesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://railgds.net/ws/booking}BookingNotesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BookingNotesType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 990, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}note uses Python identifier note
    __note = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'note'), 'note', '__httprailgds_netwsbooking_BookingNotesType_httprailgds_netwsbookingnote', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 992, 12), )

    
    note = property(__note.value, __note.set, None, None)

    _ElementMap.update({
        __note.name() : __note
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BookingNotesType', BookingNotesType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_53 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1006, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}orderInformationSet uses Python identifier orderInformationSet
    __orderInformationSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderInformationSet'), 'orderInformationSet', '__httprailgds_netwsbooking_CTD_ANON_53_httprailgds_netwsbookingorderInformationSet', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1008, 32), )

    
    orderInformationSet = property(__orderInformationSet.value, __orderInformationSet.set, None, None)

    
    # Element {http://railgds.net/ws/booking}paymentRequirements uses Python identifier paymentRequirements
    __paymentRequirements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentRequirements'), 'paymentRequirements', '__httprailgds_netwsbooking_CTD_ANON_53_httprailgds_netwsbookingpaymentRequirements', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1063, 32), )

    
    paymentRequirements = property(__paymentRequirements.value, __paymentRequirements.set, None, None)

    
    # Element {http://railgds.net/ws/booking}serviceFeeAllowed uses Python identifier serviceFeeAllowed
    __serviceFeeAllowed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serviceFeeAllowed'), 'serviceFeeAllowed', '__httprailgds_netwsbooking_CTD_ANON_53_httprailgds_netwsbookingserviceFeeAllowed', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1065, 32), )

    
    serviceFeeAllowed = property(__serviceFeeAllowed.value, __serviceFeeAllowed.set, None, None)

    _ElementMap.update({
        __orderInformationSet.name() : __orderInformationSet,
        __paymentRequirements.name() : __paymentRequirements,
        __serviceFeeAllowed.name() : __serviceFeeAllowed
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_54 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1009, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}orderInformation uses Python identifier orderInformation
    __orderInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderInformation'), 'orderInformation', '__httprailgds_netwsbooking_CTD_ANON_54_httprailgds_netwsbookingorderInformation', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1011, 44), )

    
    orderInformation = property(__orderInformation.value, __orderInformation.set, None, None)

    _ElementMap.update({
        __orderInformation.name() : __orderInformation
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_55 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1013, 48)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}travelSegments uses Python identifier travelSegments
    __travelSegments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'travelSegments'), 'travelSegments', '__httprailgds_netwsbooking_CTD_ANON_55_httprailgds_netwsbookingtravelSegments', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1015, 56), )

    
    travelSegments = property(__travelSegments.value, __travelSegments.set, None, None)

    
    # Element {http://railgds.net/ws/booking}ticketingOptions uses Python identifier ticketingOptions
    __ticketingOptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ticketingOptions'), 'ticketingOptions', '__httprailgds_netwsbooking_CTD_ANON_55_httprailgds_netwsbookingticketingOptions', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1026, 56), )

    
    ticketingOptions = property(__ticketingOptions.value, __ticketingOptions.set, None, None)

    
    # Element {http://railgds.net/ws/booking}confirmationOptions uses Python identifier confirmationOptions
    __confirmationOptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'confirmationOptions'), 'confirmationOptions', '__httprailgds_netwsbooking_CTD_ANON_55_httprailgds_netwsbookingconfirmationOptions', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1036, 56), )

    
    confirmationOptions = property(__confirmationOptions.value, __confirmationOptions.set, None, None)

    
    # Element {http://railgds.net/ws/booking}confirmationInformationRequired uses Python identifier confirmationInformationRequired
    __confirmationInformationRequired = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'confirmationInformationRequired'), 'confirmationInformationRequired', '__httprailgds_netwsbooking_CTD_ANON_55_httprailgds_netwsbookingconfirmationInformationRequired', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1039, 56), )

    
    confirmationInformationRequired = property(__confirmationInformationRequired.value, __confirmationInformationRequired.set, None, None)

    
    # Element {http://railgds.net/ws/booking}paymentCardRequiredForConfirmationInformation uses Python identifier paymentCardRequiredForConfirmationInformation
    __paymentCardRequiredForConfirmationInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentCardRequiredForConfirmationInformation'), 'paymentCardRequiredForConfirmationInformation', '__httprailgds_netwsbooking_CTD_ANON_55_httprailgds_netwsbookingpaymentCardRequiredForConfirmationInformation', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1041, 56), )

    
    paymentCardRequiredForConfirmationInformation = property(__paymentCardRequiredForConfirmationInformation.value, __paymentCardRequiredForConfirmationInformation.set, None, None)

    
    # Element {http://railgds.net/ws/booking}availableTicketLanguages uses Python identifier availableTicketLanguages
    __availableTicketLanguages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'availableTicketLanguages'), 'availableTicketLanguages', '__httprailgds_netwsbooking_CTD_ANON_55_httprailgds_netwsbookingavailableTicketLanguages', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1044, 56), )

    
    availableTicketLanguages = property(__availableTicketLanguages.value, __availableTicketLanguages.set, None, None)

    
    # Element {http://railgds.net/ws/booking}externalBookingUrl uses Python identifier externalBookingUrl
    __externalBookingUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'externalBookingUrl'), 'externalBookingUrl', '__httprailgds_netwsbooking_CTD_ANON_55_httprailgds_netwsbookingexternalBookingUrl', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1053, 56), )

    
    externalBookingUrl = property(__externalBookingUrl.value, __externalBookingUrl.set, None, None)

    
    # Element {http://railgds.net/ws/booking}commercialAgentName uses Python identifier commercialAgentName
    __commercialAgentName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'commercialAgentName'), 'commercialAgentName', '__httprailgds_netwsbooking_CTD_ANON_55_httprailgds_netwsbookingcommercialAgentName', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1055, 56), )

    
    commercialAgentName = property(__commercialAgentName.value, __commercialAgentName.set, None, None)

    _ElementMap.update({
        __travelSegments.name() : __travelSegments,
        __ticketingOptions.name() : __ticketingOptions,
        __confirmationOptions.name() : __confirmationOptions,
        __confirmationInformationRequired.name() : __confirmationInformationRequired,
        __paymentCardRequiredForConfirmationInformation.name() : __paymentCardRequiredForConfirmationInformation,
        __availableTicketLanguages.name() : __availableTicketLanguages,
        __externalBookingUrl.name() : __externalBookingUrl,
        __commercialAgentName.name() : __commercialAgentName
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_56 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1017, 60)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}travelSegment uses Python identifier travelSegment
    __travelSegment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'travelSegment'), 'travelSegment', '__httprailgds_netwsbooking_CTD_ANON_56_httprailgds_netwsbookingtravelSegment', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1019, 68), )

    
    travelSegment = property(__travelSegment.value, __travelSegment.set, None, None)

    _ElementMap.update({
        __travelSegment.name() : __travelSegment
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_57 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1028, 60)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}ticketingOption uses Python identifier ticketingOption
    __ticketingOption = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ticketingOption'), 'ticketingOption', '__httprailgds_netwsbooking_CTD_ANON_57_httprailgds_netwsbookingticketingOption', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1030, 68), )

    
    ticketingOption = property(__ticketingOption.value, __ticketingOption.set, None, None)

    _ElementMap.update({
        __ticketingOption.name() : __ticketingOption
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_58 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1046, 60)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'language'), 'language', '__httprailgds_netwsbooking_CTD_ANON_58_httprailgds_netwsbookinglanguage', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1048, 68), )

    
    language = property(__language.value, __language.set, None, None)

    _ElementMap.update({
        __language.name() : __language
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_59 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1101, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}formOfPayment uses Python identifier formOfPayment
    __formOfPayment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'formOfPayment'), 'formOfPayment', '__httprailgds_netwsbooking_CTD_ANON_59_httprailgds_netwsbookingformOfPayment', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1103, 32), )

    
    formOfPayment = property(__formOfPayment.value, __formOfPayment.set, None, None)

    
    # Element {http://railgds.net/ws/booking}creditCard uses Python identifier creditCard
    __creditCard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'creditCard'), 'creditCard', '__httprailgds_netwsbooking_CTD_ANON_59_httprailgds_netwsbookingcreditCard', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1105, 36), )

    
    creditCard = property(__creditCard.value, __creditCard.set, None, None)

    
    # Element {http://railgds.net/ws/booking}debitCard uses Python identifier debitCard
    __debitCard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'debitCard'), 'debitCard', '__httprailgds_netwsbooking_CTD_ANON_59_httprailgds_netwsbookingdebitCard', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1107, 36), )

    
    debitCard = property(__debitCard.value, __debitCard.set, None, None)

    
    # Element {http://railgds.net/ws/booking}customerIpAddress uses Python identifier customerIpAddress
    __customerIpAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerIpAddress'), 'customerIpAddress', '__httprailgds_netwsbooking_CTD_ANON_59_httprailgds_netwsbookingcustomerIpAddress', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1109, 32), )

    
    customerIpAddress = property(__customerIpAddress.value, __customerIpAddress.set, None, None)

    _ElementMap.update({
        __formOfPayment.name() : __formOfPayment,
        __creditCard.name() : __creditCard,
        __debitCard.name() : __debitCard,
        __customerIpAddress.name() : __customerIpAddress
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_60 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1155, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}ticketableFareLocator uses Python identifier ticketableFareLocator
    __ticketableFareLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ticketableFareLocator'), 'ticketableFareLocator', '__httprailgds_netwsbooking_CTD_ANON_60_httprailgds_netwsbookingticketableFareLocator', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1157, 32), )

    
    ticketableFareLocator = property(__ticketableFareLocator.value, __ticketableFareLocator.set, None, None)

    _ElementMap.update({
        __ticketableFareLocator.name() : __ticketableFareLocator
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_61 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1171, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}order uses Python identifier order
    __order = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'order'), 'order', '__httprailgds_netwsbooking_CTD_ANON_61_httprailgds_netwsbookingorder', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1173, 32), )

    
    order = property(__order.value, __order.set, None, None)

    _ElementMap.update({
        __order.name() : __order
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_62 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1174, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}cancellationSummary uses Python identifier cancellationSummary
    __cancellationSummary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cancellationSummary'), 'cancellationSummary', '__httprailgds_netwsbooking_CTD_ANON_62_httprailgds_netwsbookingcancellationSummary', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1176, 44), )

    
    cancellationSummary = property(__cancellationSummary.value, __cancellationSummary.set, None, None)

    
    # Attribute orderID uses Python identifier orderID
    __orderID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'orderID'), 'orderID', '__httprailgds_netwsbooking_CTD_ANON_62_orderID', pyxb.binding.datatypes.anySimpleType, required=True)
    __orderID._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1178, 40)
    __orderID._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1178, 40)
    
    orderID = property(__orderID.value, __orderID.set, None, None)

    _ElementMap.update({
        __cancellationSummary.name() : __cancellationSummary
    })
    _AttributeMap.update({
        __orderID.name() : __orderID
    })



# Complex type {http://railgds.net/ws/booking}AddPaymentResponseType with content type ELEMENT_ONLY
class AddPaymentResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}AddPaymentResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddPaymentResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 127, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}recordLocator uses Python identifier recordLocator
    __recordLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), 'recordLocator', '__httprailgds_netwsbooking_AddPaymentResponseType_httprailgds_netwsbookingrecordLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 131, 20), )

    
    recordLocator = property(__recordLocator.value, __recordLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}bookingRecord uses Python identifier bookingRecord
    __bookingRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), 'bookingRecord', '__httprailgds_netwsbooking_AddPaymentResponseType_httprailgds_netwsbookingbookingRecord', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 133, 20), )

    
    bookingRecord = property(__bookingRecord.value, __bookingRecord.set, None, None)

    
    # Element {http://railgds.net/ws/booking}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httprailgds_netwsbooking_AddPaymentResponseType_httprailgds_netwsbookingnotes', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 134, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://railgds.net/ws/booking}paymentToken uses Python identifier paymentToken
    __paymentToken = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentToken'), 'paymentToken', '__httprailgds_netwsbooking_AddPaymentResponseType_httprailgds_netwsbookingpaymentToken', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 135, 20), )

    
    paymentToken = property(__paymentToken.value, __paymentToken.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __recordLocator.name() : __recordLocator,
        __bookingRecord.name() : __bookingRecord,
        __notes.name() : __notes,
        __paymentToken.name() : __paymentToken
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AddPaymentResponseType', AddPaymentResponseType)


# Complex type {http://railgds.net/ws/booking}AuthenticatePayerResponseType with content type ELEMENT_ONLY
class AuthenticatePayerResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}AuthenticatePayerResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AuthenticatePayerResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 157, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}threeDeeSecureAuthenticatePayer uses Python identifier threeDeeSecureAuthenticatePayer
    __threeDeeSecureAuthenticatePayer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'threeDeeSecureAuthenticatePayer'), 'threeDeeSecureAuthenticatePayer', '__httprailgds_netwsbooking_AuthenticatePayerResponseType_httprailgds_netwsbookingthreeDeeSecureAuthenticatePayer', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 161, 20), )

    
    threeDeeSecureAuthenticatePayer = property(__threeDeeSecureAuthenticatePayer.value, __threeDeeSecureAuthenticatePayer.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __threeDeeSecureAuthenticatePayer.name() : __threeDeeSecureAuthenticatePayer
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AuthenticatePayerResponseType', AuthenticatePayerResponseType)


# Complex type {http://railgds.net/ws/booking}AuditableRequestType with content type ELEMENT_ONLY
class AuditableRequestType (_ImportedBinding_silvercom.BaseRequestType):
    """Complex type {http://railgds.net/ws/booking}AuditableRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AuditableRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 178, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseRequestType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseRequestType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseRequestType
    
    # Element {http://railgds.net/ws/booking}agentInformation uses Python identifier agentInformation
    __agentInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'agentInformation'), 'agentInformation', '__httprailgds_netwsbooking_AuditableRequestType_httprailgds_netwsbookingagentInformation', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20), )

    
    agentInformation = property(__agentInformation.value, __agentInformation.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __agentInformation.name() : __agentInformation
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AuditableRequestType', AuditableRequestType)


# Complex type {http://railgds.net/ws/booking}CancelBookingRecordResponseType with content type ELEMENT_ONLY
class CancelBookingRecordResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}CancelBookingRecordResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CancelBookingRecordResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 271, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}bookingRecord uses Python identifier bookingRecord
    __bookingRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), 'bookingRecord', '__httprailgds_netwsbooking_CancelBookingRecordResponseType_httprailgds_netwsbookingbookingRecord', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 275, 20), )

    
    bookingRecord = property(__bookingRecord.value, __bookingRecord.set, None, None)

    
    # Element {http://railgds.net/ws/booking}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httprailgds_netwsbooking_CancelBookingRecordResponseType_httprailgds_netwsbookingnotes', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 276, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://railgds.net/ws/booking}refundStatus uses Python identifier refundStatus
    __refundStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'refundStatus'), 'refundStatus', '__httprailgds_netwsbooking_CancelBookingRecordResponseType_httprailgds_netwsbookingrefundStatus', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 277, 20), )

    
    refundStatus = property(__refundStatus.value, __refundStatus.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __bookingRecord.name() : __bookingRecord,
        __notes.name() : __notes,
        __refundStatus.name() : __refundStatus
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CancelBookingRecordResponseType', CancelBookingRecordResponseType)


# Complex type {http://railgds.net/ws/booking}ClaimValueDocumentResponseType with content type ELEMENT_ONLY
class ClaimValueDocumentResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}ClaimValueDocumentResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClaimValueDocumentResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 303, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}valueDocument uses Python identifier valueDocument
    __valueDocument = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueDocument'), 'valueDocument', '__httprailgds_netwsbooking_ClaimValueDocumentResponseType_httprailgds_netwsbookingvalueDocument', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 307, 20), )

    
    valueDocument = property(__valueDocument.value, __valueDocument.set, None, None)

    
    # Element {http://railgds.net/ws/booking}bookingRecord uses Python identifier bookingRecord
    __bookingRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), 'bookingRecord', '__httprailgds_netwsbooking_ClaimValueDocumentResponseType_httprailgds_netwsbookingbookingRecord', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 308, 20), )

    
    bookingRecord = property(__bookingRecord.value, __bookingRecord.set, None, None)

    
    # Element {http://railgds.net/ws/booking}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httprailgds_netwsbooking_ClaimValueDocumentResponseType_httprailgds_netwsbookingnotes', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 309, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __valueDocument.name() : __valueDocument,
        __bookingRecord.name() : __bookingRecord,
        __notes.name() : __notes
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ClaimValueDocumentResponseType', ClaimValueDocumentResponseType)


# Complex type {http://railgds.net/ws/booking}ConfirmBookingRecordResponseType with content type ELEMENT_ONLY
class ConfirmBookingRecordResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}ConfirmBookingRecordResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConfirmBookingRecordResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 342, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}bookingRecord uses Python identifier bookingRecord
    __bookingRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), 'bookingRecord', '__httprailgds_netwsbooking_ConfirmBookingRecordResponseType_httprailgds_netwsbookingbookingRecord', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 346, 20), )

    
    bookingRecord = property(__bookingRecord.value, __bookingRecord.set, None, None)

    
    # Element {http://railgds.net/ws/booking}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httprailgds_netwsbooking_ConfirmBookingRecordResponseType_httprailgds_netwsbookingnotes', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 347, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://railgds.net/ws/booking}claimValueDocumentResult uses Python identifier claimValueDocumentResult
    __claimValueDocumentResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'claimValueDocumentResult'), 'claimValueDocumentResult', '__httprailgds_netwsbooking_ConfirmBookingRecordResponseType_httprailgds_netwsbookingclaimValueDocumentResult', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 348, 20), )

    
    claimValueDocumentResult = property(__claimValueDocumentResult.value, __claimValueDocumentResult.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __bookingRecord.name() : __bookingRecord,
        __notes.name() : __notes,
        __claimValueDocumentResult.name() : __claimValueDocumentResult
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ConfirmBookingRecordResponseType', ConfirmBookingRecordResponseType)


# Complex type {http://railgds.net/ws/booking}BookingTransactionFeeType with content type ELEMENT_ONLY
class BookingTransactionFeeType (_ImportedBinding_silvercom.BaseTransactionFeeType):
    """Complex type {http://railgds.net/ws/booking}BookingTransactionFeeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BookingTransactionFeeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 393, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseTransactionFeeType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseTransactionFeeType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseTransactionFeeType
    
    # Element fee ({http://railgds.net/ws/commontypes}fee) inherited from {http://railgds.net/ws/commontypes}BaseTransactionFeeType
    
    # Attribute transactionFeeID inherited from {http://railgds.net/ws/commontypes}BaseTransactionFeeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BookingTransactionFeeType', BookingTransactionFeeType)


# Complex type {http://railgds.net/ws/booking}CreateBookingRecordResponseType with content type ELEMENT_ONLY
class CreateBookingRecordResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}CreateBookingRecordResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CreateBookingRecordResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 472, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}recordLocator uses Python identifier recordLocator
    __recordLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), 'recordLocator', '__httprailgds_netwsbooking_CreateBookingRecordResponseType_httprailgds_netwsbookingrecordLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 476, 20), )

    
    recordLocator = property(__recordLocator.value, __recordLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}lastHoldDateTime uses Python identifier lastHoldDateTime
    __lastHoldDateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastHoldDateTime'), 'lastHoldDateTime', '__httprailgds_netwsbooking_CreateBookingRecordResponseType_httprailgds_netwsbookinglastHoldDateTime', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 478, 20), )

    
    lastHoldDateTime = property(__lastHoldDateTime.value, __lastHoldDateTime.set, None, None)

    
    # Element {http://railgds.net/ws/booking}bookingRecord uses Python identifier bookingRecord
    __bookingRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), 'bookingRecord', '__httprailgds_netwsbooking_CreateBookingRecordResponseType_httprailgds_netwsbookingbookingRecord', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 479, 20), )

    
    bookingRecord = property(__bookingRecord.value, __bookingRecord.set, None, None)

    
    # Element {http://railgds.net/ws/booking}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httprailgds_netwsbooking_CreateBookingRecordResponseType_httprailgds_netwsbookingnotes', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 480, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __recordLocator.name() : __recordLocator,
        __lastHoldDateTime.name() : __lastHoldDateTime,
        __bookingRecord.name() : __bookingRecord,
        __notes.name() : __notes
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CreateBookingRecordResponseType', CreateBookingRecordResponseType)


# Complex type {http://railgds.net/ws/booking}PriceAcceptanceType with content type SIMPLE
class PriceAcceptanceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://railgds.net/ws/booking}PriceAcceptanceType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.boolean
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PriceAcceptanceType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 507, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.boolean
    
    # Attribute threshold uses Python identifier threshold
    __threshold = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'threshold'), 'threshold', '__httprailgds_netwsbooking_PriceAcceptanceType_threshold', _ImportedBinding_silvercom.MoneyValueType)
    __threshold._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 510, 16)
    __threshold._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 510, 16)
    
    threshold = property(__threshold.value, __threshold.set, None, None)

    
    # Attribute currency uses Python identifier currency
    __currency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'currency'), 'currency', '__httprailgds_netwsbooking_PriceAcceptanceType_currency', pyxb.binding.datatypes.string)
    __currency._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 511, 16)
    __currency._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 511, 16)
    
    currency = property(__currency.value, __currency.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __threshold.name() : __threshold,
        __currency.name() : __currency
    })
Namespace.addCategoryObject('typeBinding', 'PriceAcceptanceType', PriceAcceptanceType)


# Complex type {http://railgds.net/ws/booking}RetrieveBookingRecordResponseType with content type ELEMENT_ONLY
class RetrieveBookingRecordResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}RetrieveBookingRecordResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RetrieveBookingRecordResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 564, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}bookingRecord uses Python identifier bookingRecord
    __bookingRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), 'bookingRecord', '__httprailgds_netwsbooking_RetrieveBookingRecordResponseType_httprailgds_netwsbookingbookingRecord', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 568, 20), )

    
    bookingRecord = property(__bookingRecord.value, __bookingRecord.set, None, None)

    
    # Element {http://railgds.net/ws/booking}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httprailgds_netwsbooking_RetrieveBookingRecordResponseType_httprailgds_netwsbookingnotes', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 569, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __bookingRecord.name() : __bookingRecord,
        __notes.name() : __notes
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RetrieveBookingRecordResponseType', RetrieveBookingRecordResponseType)


# Complex type {http://railgds.net/ws/booking}RedeliverValueDocumentResponseType with content type ELEMENT_ONLY
class RedeliverValueDocumentResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}RedeliverValueDocumentResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RedeliverValueDocumentResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 606, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}deliveryStatus uses Python identifier deliveryStatus
    __deliveryStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'deliveryStatus'), 'deliveryStatus', '__httprailgds_netwsbooking_RedeliverValueDocumentResponseType_httprailgds_netwsbookingdeliveryStatus', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 610, 20), )

    
    deliveryStatus = property(__deliveryStatus.value, __deliveryStatus.set, None, None)

    
    # Element {http://railgds.net/ws/booking}bookingRecord uses Python identifier bookingRecord
    __bookingRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), 'bookingRecord', '__httprailgds_netwsbooking_RedeliverValueDocumentResponseType_httprailgds_netwsbookingbookingRecord', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 636, 20), )

    
    bookingRecord = property(__bookingRecord.value, __bookingRecord.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __deliveryStatus.name() : __deliveryStatus,
        __bookingRecord.name() : __bookingRecord
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RedeliverValueDocumentResponseType', RedeliverValueDocumentResponseType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_63 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 652, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://railgds.net/ws/booking}coupons uses Python identifier coupons
    __coupons = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coupons'), 'coupons', '__httprailgds_netwsbooking_CTD_ANON_63_httprailgds_netwsbookingcoupons', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 654, 36), )

    
    coupons = property(__coupons.value, __coupons.set, None, None)

    
    # Attribute returnType uses Python identifier returnType
    __returnType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'returnType'), 'returnType', '__httprailgds_netwsbooking_CTD_ANON_63_returnType', STD_ANON_, required=True)
    __returnType._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 685, 32)
    __returnType._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 685, 32)
    
    returnType = property(__returnType.value, __returnType.set, None, None)

    _ElementMap.update({
        __coupons.name() : __coupons
    })
    _AttributeMap.update({
        __returnType.name() : __returnType
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_64 (_ImportedBinding_silvercom.CouponType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 658, 52)
    _ElementMap = _ImportedBinding_silvercom.CouponType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.CouponType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.CouponType
    
    # Element {http://railgds.net/ws/booking}couponReceivedDate uses Python identifier couponReceivedDate
    __couponReceivedDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'couponReceivedDate'), 'couponReceivedDate', '__httprailgds_netwsbooking_CTD_ANON_64_httprailgds_netwsbookingcouponReceivedDate', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 662, 68), )

    
    couponReceivedDate = property(__couponReceivedDate.value, __couponReceivedDate.set, None, None)

    
    # Element {http://railgds.net/ws/booking}origin uses Python identifier origin
    __origin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'origin'), 'origin', '__httprailgds_netwsbooking_CTD_ANON_64_httprailgds_netwsbookingorigin', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 664, 68), )

    
    origin = property(__origin.value, __origin.set, None, None)

    
    # Element {http://railgds.net/ws/booking}destination uses Python identifier destination
    __destination = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'destination'), 'destination', '__httprailgds_netwsbooking_CTD_ANON_64_httprailgds_netwsbookingdestination', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 666, 68), )

    
    destination = property(__destination.value, __destination.set, None, None)

    
    # Element couponNumber ({http://railgds.net/ws/commontypes}couponNumber) inherited from {http://railgds.net/ws/commontypes}CouponType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httprailgds_netwsbooking_CTD_ANON_64_type', STD_ANON)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 669, 64)
    __type._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 669, 64)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __couponReceivedDate.name() : __couponReceivedDate,
        __origin.name() : __origin,
        __destination.name() : __destination
    })
    _AttributeMap.update({
        __type.name() : __type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_65 (_ImportedBinding_silvercom.CouponType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 702, 50)
    _ElementMap = _ImportedBinding_silvercom.CouponType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.CouponType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.CouponType
    
    # Element {http://railgds.net/ws/booking}refundApprovedDate uses Python identifier refundApprovedDate
    __refundApprovedDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'refundApprovedDate'), 'refundApprovedDate', '__httprailgds_netwsbooking_CTD_ANON_65_httprailgds_netwsbookingrefundApprovedDate', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 706, 50), )

    
    refundApprovedDate = property(__refundApprovedDate.value, __refundApprovedDate.set, None, None)

    
    # Element {http://railgds.net/ws/booking}authorization uses Python identifier authorization
    __authorization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'authorization'), 'authorization', '__httprailgds_netwsbooking_CTD_ANON_65_httprailgds_netwsbookingauthorization', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 708, 50), )

    
    authorization = property(__authorization.value, __authorization.set, None, None)

    
    # Element couponNumber ({http://railgds.net/ws/commontypes}couponNumber) inherited from {http://railgds.net/ws/commontypes}CouponType
    _ElementMap.update({
        __refundApprovedDate.name() : __refundApprovedDate,
        __authorization.name() : __authorization
    })
    _AttributeMap.update({
        
    })



# Complex type {http://railgds.net/ws/booking}ReturnValueDocumentResponseType with content type ELEMENT_ONLY
class ReturnValueDocumentResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}ReturnValueDocumentResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReturnValueDocumentResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 760, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}bookingRecord uses Python identifier bookingRecord
    __bookingRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), 'bookingRecord', '__httprailgds_netwsbooking_ReturnValueDocumentResponseType_httprailgds_netwsbookingbookingRecord', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 764, 20), )

    
    bookingRecord = property(__bookingRecord.value, __bookingRecord.set, None, None)

    
    # Element {http://railgds.net/ws/booking}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httprailgds_netwsbooking_ReturnValueDocumentResponseType_httprailgds_netwsbookingnotes', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 765, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __bookingRecord.name() : __bookingRecord,
        __notes.name() : __notes
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ReturnValueDocumentResponseType', ReturnValueDocumentResponseType)


# Complex type {http://railgds.net/ws/booking}SearchBookingRecordsRequestType with content type ELEMENT_ONLY
class SearchBookingRecordsRequestType (_ImportedBinding_silvercom.BaseRequestType):
    """SearchBookingRecordsRequestType is deprecated. Please use search-ws instead"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SearchBookingRecordsRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 771, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseRequestType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseRequestType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseRequestType
    
    # Element {http://railgds.net/ws/booking}searchCriteria uses Python identifier searchCriteria
    __searchCriteria = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'searchCriteria'), 'searchCriteria', '__httprailgds_netwsbooking_SearchBookingRecordsRequestType_httprailgds_netwsbookingsearchCriteria', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 778, 20), )

    
    searchCriteria = property(__searchCriteria.value, __searchCriteria.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __searchCriteria.name() : __searchCriteria
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SearchBookingRecordsRequestType', SearchBookingRecordsRequestType)


# Complex type {http://railgds.net/ws/booking}SearchBookingRecordsResponseType with content type ELEMENT_ONLY
class SearchBookingRecordsResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """SearchBookingRecordsResponseType is deprecated. Please use search-ws instead"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SearchBookingRecordsResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 792, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}bookingRecords uses Python identifier bookingRecords
    __bookingRecords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookingRecords'), 'bookingRecords', '__httprailgds_netwsbooking_SearchBookingRecordsResponseType_httprailgds_netwsbookingbookingRecords', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 799, 20), )

    
    bookingRecords = property(__bookingRecords.value, __bookingRecords.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __bookingRecords.name() : __bookingRecords
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SearchBookingRecordsResponseType', SearchBookingRecordsResponseType)


# Complex type {http://railgds.net/ws/booking}UpdateBookingRecordResponseType with content type ELEMENT_ONLY
class UpdateBookingRecordResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}UpdateBookingRecordResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UpdateBookingRecordResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 899, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}bookingRecord uses Python identifier bookingRecord
    __bookingRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), 'bookingRecord', '__httprailgds_netwsbooking_UpdateBookingRecordResponseType_httprailgds_netwsbookingbookingRecord', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 903, 20), )

    
    bookingRecord = property(__bookingRecord.value, __bookingRecord.set, None, None)

    
    # Element {http://railgds.net/ws/booking}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httprailgds_netwsbooking_UpdateBookingRecordResponseType_httprailgds_netwsbookingnotes', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 904, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __bookingRecord.name() : __bookingRecord,
        __notes.name() : __notes
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'UpdateBookingRecordResponseType', UpdateBookingRecordResponseType)


# Complex type {http://railgds.net/ws/booking}RecordFinancialTransactionResponseType with content type ELEMENT_ONLY
class RecordFinancialTransactionResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}RecordFinancialTransactionResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RecordFinancialTransactionResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 947, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}bookingRecord uses Python identifier bookingRecord
    __bookingRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), 'bookingRecord', '__httprailgds_netwsbooking_RecordFinancialTransactionResponseType_httprailgds_netwsbookingbookingRecord', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 951, 20), )

    
    bookingRecord = property(__bookingRecord.value, __bookingRecord.set, None, None)

    
    # Element {http://railgds.net/ws/booking}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httprailgds_netwsbooking_RecordFinancialTransactionResponseType_httprailgds_netwsbookingnotes', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 952, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __bookingRecord.name() : __bookingRecord,
        __notes.name() : __notes
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RecordFinancialTransactionResponseType', RecordFinancialTransactionResponseType)


# Complex type {http://railgds.net/ws/booking}RefundBookingRecordResponseType with content type ELEMENT_ONLY
class RefundBookingRecordResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}RefundBookingRecordResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RefundBookingRecordResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 979, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}bookingRecord uses Python identifier bookingRecord
    __bookingRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), 'bookingRecord', '__httprailgds_netwsbooking_RefundBookingRecordResponseType_httprailgds_netwsbookingbookingRecord', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 983, 20), )

    
    bookingRecord = property(__bookingRecord.value, __bookingRecord.set, None, None)

    
    # Element {http://railgds.net/ws/booking}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httprailgds_netwsbooking_RefundBookingRecordResponseType_httprailgds_netwsbookingnotes', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 984, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __bookingRecord.name() : __bookingRecord,
        __notes.name() : __notes
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RefundBookingRecordResponseType', RefundBookingRecordResponseType)


# Complex type {http://railgds.net/ws/booking}ValidateBookingRecordInformationResponseType with content type ELEMENT_ONLY
class ValidateBookingRecordInformationResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}ValidateBookingRecordInformationResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValidateBookingRecordInformationResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1001, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}bookingRecordInformation uses Python identifier bookingRecordInformation
    __bookingRecordInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookingRecordInformation'), 'bookingRecordInformation', '__httprailgds_netwsbooking_ValidateBookingRecordInformationResponseType_httprailgds_netwsbookingbookingRecordInformation', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1005, 20), )

    
    bookingRecordInformation = property(__bookingRecordInformation.value, __bookingRecordInformation.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __bookingRecordInformation.name() : __bookingRecordInformation
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ValidateBookingRecordInformationResponseType', ValidateBookingRecordInformationResponseType)


# Complex type {http://railgds.net/ws/booking}TokenPaymentType with content type SIMPLE
class TokenPaymentType (pyxb.binding.basis.complexTypeDefinition):
    """Acceptable Values for 'CC' type: AX, CA, VI, DI, UA, MCAcceptable Values for 'DB' type: DS, DV, DM"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TokenPaymentType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1076, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httprailgds_netwsbooking_TokenPaymentType_type', STD_ANON_2)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1083, 16)
    __type._UseLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1083, 16)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'TokenPaymentType', TokenPaymentType)


# Complex type {http://railgds.net/ws/booking}GeneratePaymentTokenResponseType with content type ELEMENT_ONLY
class GeneratePaymentTokenResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}GeneratePaymentTokenResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeneratePaymentTokenResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1118, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}paymentToken uses Python identifier paymentToken
    __paymentToken = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentToken'), 'paymentToken', '__httprailgds_netwsbooking_GeneratePaymentTokenResponseType_httprailgds_netwsbookingpaymentToken', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1122, 20), )

    
    paymentToken = property(__paymentToken.value, __paymentToken.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __paymentToken.name() : __paymentToken
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GeneratePaymentTokenResponseType', GeneratePaymentTokenResponseType)


# Complex type {http://railgds.net/ws/booking}DeletePaymentTokenResponseType with content type ELEMENT_ONLY
class DeletePaymentTokenResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}DeletePaymentTokenResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeletePaymentTokenResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1141, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DeletePaymentTokenResponseType', DeletePaymentTokenResponseType)


# Complex type {http://railgds.net/ws/booking}RetrieveCancellationSummaryResponseType with content type ELEMENT_ONLY
class RetrieveCancellationSummaryResponseType (_ImportedBinding_silvercom.BaseResponseType):
    """Complex type {http://railgds.net/ws/booking}RetrieveCancellationSummaryResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RetrieveCancellationSummaryResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1166, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseResponseType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseResponseType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseResponseType
    
    # Element {http://railgds.net/ws/booking}orders uses Python identifier orders
    __orders = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orders'), 'orders', '__httprailgds_netwsbooking_RetrieveCancellationSummaryResponseType_httprailgds_netwsbookingorders', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1170, 20), )

    
    orders = property(__orders.value, __orders.set, None, None)

    
    # Element requestStatus ({http://railgds.net/ws/commontypes}requestStatus) inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseResponseType
    _ElementMap.update({
        __orders.name() : __orders
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RetrieveCancellationSummaryResponseType', RetrieveCancellationSummaryResponseType)


# Complex type {http://railgds.net/ws/booking}AddPaymentCreditCardType with content type ELEMENT_ONLY
class AddPaymentCreditCardType (_ImportedBinding_silvercom.BaseCreditCardType):
    """Complex type {http://railgds.net/ws/booking}AddPaymentCreditCardType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddPaymentCreditCardType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 73, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseCreditCardType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseCreditCardType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseCreditCardType
    
    # Element {http://railgds.net/ws/booking}validationNumber uses Python identifier validationNumber
    __validationNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'validationNumber'), 'validationNumber', '__httprailgds_netwsbooking_AddPaymentCreditCardType_httprailgds_netwsbookingvalidationNumber', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 77, 20), )

    
    validationNumber = property(__validationNumber.value, __validationNumber.set, None, None)

    
    # Element number ({http://railgds.net/ws/commontypes}number) inherited from {http://railgds.net/ws/commontypes}BaseCreditCardType
    
    # Element expirationYearMonth ({http://railgds.net/ws/commontypes}expirationYearMonth) inherited from {http://railgds.net/ws/commontypes}BaseCreditCardType
    
    # Element cardholderName ({http://railgds.net/ws/commontypes}cardholderName) inherited from {http://railgds.net/ws/commontypes}BaseCreditCardType
    
    # Element billingAddress ({http://railgds.net/ws/commontypes}billingAddress) inherited from {http://railgds.net/ws/commontypes}BaseCreditCardType
    
    # Element siteCard ({http://railgds.net/ws/commontypes}siteCard) inherited from {http://railgds.net/ws/commontypes}BaseCreditCardType
    
    # Element paymentToken ({http://railgds.net/ws/commontypes}paymentToken) inherited from {http://railgds.net/ws/commontypes}BaseCreditCardType
    
    # Attribute type inherited from {http://railgds.net/ws/commontypes}BaseCreditCardType
    _ElementMap.update({
        __validationNumber.name() : __validationNumber
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AddPaymentCreditCardType', AddPaymentCreditCardType)


# Complex type {http://railgds.net/ws/booking}AddPaymentDebitCardType with content type ELEMENT_ONLY
class AddPaymentDebitCardType (_ImportedBinding_silvercom.BaseDebitCardType):
    """Complex type {http://railgds.net/ws/booking}AddPaymentDebitCardType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddPaymentDebitCardType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 82, 4)
    _ElementMap = _ImportedBinding_silvercom.BaseDebitCardType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_silvercom.BaseDebitCardType._AttributeMap.copy()
    # Base type is _ImportedBinding_silvercom.BaseDebitCardType
    
    # Element {http://railgds.net/ws/booking}issueNumber uses Python identifier issueNumber
    __issueNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'issueNumber'), 'issueNumber', '__httprailgds_netwsbooking_AddPaymentDebitCardType_httprailgds_netwsbookingissueNumber', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 86, 20), )

    
    issueNumber = property(__issueNumber.value, __issueNumber.set, None, None)

    
    # Element {http://railgds.net/ws/booking}validationNumber uses Python identifier validationNumber
    __validationNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'validationNumber'), 'validationNumber', '__httprailgds_netwsbooking_AddPaymentDebitCardType_httprailgds_netwsbookingvalidationNumber', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 87, 20), )

    
    validationNumber = property(__validationNumber.value, __validationNumber.set, None, None)

    
    # Element number ({http://railgds.net/ws/commontypes}number) inherited from {http://railgds.net/ws/commontypes}BaseDebitCardType
    
    # Element startYearMonth ({http://railgds.net/ws/commontypes}startYearMonth) inherited from {http://railgds.net/ws/commontypes}BaseDebitCardType
    
    # Element expirationYearMonth ({http://railgds.net/ws/commontypes}expirationYearMonth) inherited from {http://railgds.net/ws/commontypes}BaseDebitCardType
    
    # Element cardholderName ({http://railgds.net/ws/commontypes}cardholderName) inherited from {http://railgds.net/ws/commontypes}BaseDebitCardType
    
    # Element billingAddress ({http://railgds.net/ws/commontypes}billingAddress) inherited from {http://railgds.net/ws/commontypes}BaseDebitCardType
    
    # Element paymentToken ({http://railgds.net/ws/commontypes}paymentToken) inherited from {http://railgds.net/ws/commontypes}BaseDebitCardType
    
    # Attribute type inherited from {http://railgds.net/ws/commontypes}BaseDebitCardType
    _ElementMap.update({
        __issueNumber.name() : __issueNumber,
        __validationNumber.name() : __validationNumber
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AddPaymentDebitCardType', AddPaymentDebitCardType)


# Complex type {http://railgds.net/ws/booking}BaseBookingRequestType with content type ELEMENT_ONLY
class BaseBookingRequestType (AuditableRequestType):
    """Complex type {http://railgds.net/ws/booking}BaseBookingRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BaseBookingRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 195, 4)
    _ElementMap = AuditableRequestType._ElementMap.copy()
    _AttributeMap = AuditableRequestType._AttributeMap.copy()
    # Base type is AuditableRequestType
    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element {http://railgds.net/ws/booking}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httprailgds_netwsbooking_BaseBookingRequestType_httprailgds_netwsbookingnotes', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://railgds.net/ws/booking}orderNotes uses Python identifier orderNotes
    __orderNotes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderNotes'), 'orderNotes', '__httprailgds_netwsbooking_BaseBookingRequestType_httprailgds_netwsbookingorderNotes', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20), )

    
    orderNotes = property(__orderNotes.value, __orderNotes.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __notes.name() : __notes,
        __orderNotes.name() : __orderNotes
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BaseBookingRequestType', BaseBookingRequestType)


# Complex type {http://railgds.net/ws/booking}RetrieveBookingRecordRequestType with content type ELEMENT_ONLY
class RetrieveBookingRecordRequestType (AuditableRequestType):
    """Complex type {http://railgds.net/ws/booking}RetrieveBookingRecordRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RetrieveBookingRecordRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 515, 4)
    _ElementMap = AuditableRequestType._ElementMap.copy()
    _AttributeMap = AuditableRequestType._AttributeMap.copy()
    # Base type is AuditableRequestType
    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element {http://railgds.net/ws/booking}recordLocator uses Python identifier recordLocator
    __recordLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), 'recordLocator', '__httprailgds_netwsbooking_RetrieveBookingRecordRequestType_httprailgds_netwsbookingrecordLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 520, 24), )

    
    recordLocator = property(__recordLocator.value, __recordLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}supplyChannelRecordLocator uses Python identifier supplyChannelRecordLocator
    __supplyChannelRecordLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supplyChannelRecordLocator'), 'supplyChannelRecordLocator', '__httprailgds_netwsbooking_RetrieveBookingRecordRequestType_httprailgds_netwsbookingsupplyChannelRecordLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 521, 24), )

    
    supplyChannelRecordLocator = property(__supplyChannelRecordLocator.value, __supplyChannelRecordLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}valueDocumentLocator uses Python identifier valueDocumentLocator
    __valueDocumentLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueDocumentLocator'), 'valueDocumentLocator', '__httprailgds_netwsbooking_RetrieveBookingRecordRequestType_httprailgds_netwsbookingvalueDocumentLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 523, 24), )

    
    valueDocumentLocator = property(__valueDocumentLocator.value, __valueDocumentLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}orders uses Python identifier orders
    __orders = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orders'), 'orders', '__httprailgds_netwsbooking_RetrieveBookingRecordRequestType_httprailgds_netwsbookingorders', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 525, 20), )

    
    orders = property(__orders.value, __orders.set, None, None)

    
    # Element {http://railgds.net/ws/booking}responseSpec uses Python identifier responseSpec
    __responseSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), 'responseSpec', '__httprailgds_netwsbooking_RetrieveBookingRecordRequestType_httprailgds_netwsbookingresponseSpec', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 541, 20), )

    
    responseSpec = property(__responseSpec.value, __responseSpec.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __recordLocator.name() : __recordLocator,
        __supplyChannelRecordLocator.name() : __supplyChannelRecordLocator,
        __valueDocumentLocator.name() : __valueDocumentLocator,
        __orders.name() : __orders,
        __responseSpec.name() : __responseSpec
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RetrieveBookingRecordRequestType', RetrieveBookingRecordRequestType)


# Complex type {http://railgds.net/ws/booking}GeneratePaymentTokenRequestType with content type ELEMENT_ONLY
class GeneratePaymentTokenRequestType (AuditableRequestType):
    """Complex type {http://railgds.net/ws/booking}GeneratePaymentTokenRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeneratePaymentTokenRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1095, 4)
    _ElementMap = AuditableRequestType._ElementMap.copy()
    _AttributeMap = AuditableRequestType._AttributeMap.copy()
    # Base type is AuditableRequestType
    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element {http://railgds.net/ws/booking}payment uses Python identifier payment
    __payment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'payment'), 'payment', '__httprailgds_netwsbooking_GeneratePaymentTokenRequestType_httprailgds_netwsbookingpayment', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1100, 20), )

    
    payment = property(__payment.value, __payment.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __payment.name() : __payment
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GeneratePaymentTokenRequestType', GeneratePaymentTokenRequestType)


# Complex type {http://railgds.net/ws/booking}DeletePaymentTokenRequestType with content type ELEMENT_ONLY
class DeletePaymentTokenRequestType (AuditableRequestType):
    """Complex type {http://railgds.net/ws/booking}DeletePaymentTokenRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeletePaymentTokenRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1128, 4)
    _ElementMap = AuditableRequestType._ElementMap.copy()
    _AttributeMap = AuditableRequestType._AttributeMap.copy()
    # Base type is AuditableRequestType
    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element {http://railgds.net/ws/booking}paymentToken uses Python identifier paymentToken
    __paymentToken = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paymentToken'), 'paymentToken', '__httprailgds_netwsbooking_DeletePaymentTokenRequestType_httprailgds_netwsbookingpaymentToken', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1133, 20), )

    
    paymentToken = property(__paymentToken.value, __paymentToken.set, None, None)

    
    # Element {http://railgds.net/ws/booking}accountHolderFirstName uses Python identifier accountHolderFirstName
    __accountHolderFirstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accountHolderFirstName'), 'accountHolderFirstName', '__httprailgds_netwsbooking_DeletePaymentTokenRequestType_httprailgds_netwsbookingaccountHolderFirstName', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1134, 20), )

    
    accountHolderFirstName = property(__accountHolderFirstName.value, __accountHolderFirstName.set, None, None)

    
    # Element {http://railgds.net/ws/booking}accountHolderLastName uses Python identifier accountHolderLastName
    __accountHolderLastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accountHolderLastName'), 'accountHolderLastName', '__httprailgds_netwsbooking_DeletePaymentTokenRequestType_httprailgds_netwsbookingaccountHolderLastName', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1135, 20), )

    
    accountHolderLastName = property(__accountHolderLastName.value, __accountHolderLastName.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __paymentToken.name() : __paymentToken,
        __accountHolderFirstName.name() : __accountHolderFirstName,
        __accountHolderLastName.name() : __accountHolderLastName
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DeletePaymentTokenRequestType', DeletePaymentTokenRequestType)


# Complex type {http://railgds.net/ws/booking}RetrieveCancellationSummaryRequestType with content type ELEMENT_ONLY
class RetrieveCancellationSummaryRequestType (AuditableRequestType):
    """Complex type {http://railgds.net/ws/booking}RetrieveCancellationSummaryRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RetrieveCancellationSummaryRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1148, 4)
    _ElementMap = AuditableRequestType._ElementMap.copy()
    _AttributeMap = AuditableRequestType._AttributeMap.copy()
    # Base type is AuditableRequestType
    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element {http://railgds.net/ws/booking}recordLocator uses Python identifier recordLocator
    __recordLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), 'recordLocator', '__httprailgds_netwsbooking_RetrieveCancellationSummaryRequestType_httprailgds_netwsbookingrecordLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1152, 20), )

    
    recordLocator = property(__recordLocator.value, __recordLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}orderLocator uses Python identifier orderLocator
    __orderLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderLocator'), 'orderLocator', '__httprailgds_netwsbooking_RetrieveCancellationSummaryRequestType_httprailgds_netwsbookingorderLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1153, 20), )

    
    orderLocator = property(__orderLocator.value, __orderLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}ticketableFareLocators uses Python identifier ticketableFareLocators
    __ticketableFareLocators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ticketableFareLocators'), 'ticketableFareLocators', '__httprailgds_netwsbooking_RetrieveCancellationSummaryRequestType_httprailgds_netwsbookingticketableFareLocators', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1154, 20), )

    
    ticketableFareLocators = property(__ticketableFareLocators.value, __ticketableFareLocators.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __recordLocator.name() : __recordLocator,
        __orderLocator.name() : __orderLocator,
        __ticketableFareLocators.name() : __ticketableFareLocators
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RetrieveCancellationSummaryRequestType', RetrieveCancellationSummaryRequestType)


# Complex type {http://railgds.net/ws/booking}AbstractPaymentRequestType with content type ELEMENT_ONLY
class AbstractPaymentRequestType (BaseBookingRequestType):
    """Complex type {http://railgds.net/ws/booking}AbstractPaymentRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractPaymentRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 47, 4)
    _ElementMap = BaseBookingRequestType._ElementMap.copy()
    _AttributeMap = BaseBookingRequestType._AttributeMap.copy()
    # Base type is BaseBookingRequestType
    
    # Element {http://railgds.net/ws/booking}recordLocator uses Python identifier recordLocator
    __recordLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), 'recordLocator', '__httprailgds_netwsbooking_AbstractPaymentRequestType_httprailgds_netwsbookingrecordLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 51, 20), )

    
    recordLocator = property(__recordLocator.value, __recordLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}payment uses Python identifier payment
    __payment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'payment'), 'payment', '__httprailgds_netwsbooking_AbstractPaymentRequestType_httprailgds_netwsbookingpayment', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 52, 20), )

    
    payment = property(__payment.value, __payment.set, None, None)

    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element notes ({http://railgds.net/ws/booking}notes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element orderNotes ({http://railgds.net/ws/booking}orderNotes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __recordLocator.name() : __recordLocator,
        __payment.name() : __payment
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AbstractPaymentRequestType', AbstractPaymentRequestType)


# Complex type {http://railgds.net/ws/booking}CancelBookingRecordRequestType with content type ELEMENT_ONLY
class CancelBookingRecordRequestType (BaseBookingRequestType):
    """Complex type {http://railgds.net/ws/booking}CancelBookingRecordRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CancelBookingRecordRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 220, 4)
    _ElementMap = BaseBookingRequestType._ElementMap.copy()
    _AttributeMap = BaseBookingRequestType._AttributeMap.copy()
    # Base type is BaseBookingRequestType
    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element notes ({http://railgds.net/ws/booking}notes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element orderNotes ({http://railgds.net/ws/booking}orderNotes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element {http://railgds.net/ws/booking}recordLocator uses Python identifier recordLocator
    __recordLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), 'recordLocator', '__httprailgds_netwsbooking_CancelBookingRecordRequestType_httprailgds_netwsbookingrecordLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 224, 20), )

    
    recordLocator = property(__recordLocator.value, __recordLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}orderLocator uses Python identifier orderLocator
    __orderLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderLocator'), 'orderLocator', '__httprailgds_netwsbooking_CancelBookingRecordRequestType_httprailgds_netwsbookingorderLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 225, 20), )

    
    orderLocator = property(__orderLocator.value, __orderLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}ticketableFareLocators uses Python identifier ticketableFareLocators
    __ticketableFareLocators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ticketableFareLocators'), 'ticketableFareLocators', '__httprailgds_netwsbooking_CancelBookingRecordRequestType_httprailgds_netwsbookingticketableFareLocators', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 226, 20), )

    
    ticketableFareLocators = property(__ticketableFareLocators.value, __ticketableFareLocators.set, None, None)

    
    # Element {http://railgds.net/ws/booking}expectedCancellationFee uses Python identifier expectedCancellationFee
    __expectedCancellationFee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'expectedCancellationFee'), 'expectedCancellationFee', '__httprailgds_netwsbooking_CancelBookingRecordRequestType_httprailgds_netwsbookingexpectedCancellationFee', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 233, 20), )

    
    expectedCancellationFee = property(__expectedCancellationFee.value, __expectedCancellationFee.set, None, None)

    
    # Element {http://railgds.net/ws/booking}parameters uses Python identifier parameters
    __parameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameters'), 'parameters', '__httprailgds_netwsbooking_CancelBookingRecordRequestType_httprailgds_netwsbookingparameters', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 234, 20), )

    
    parameters = property(__parameters.value, __parameters.set, None, None)

    
    # Element {http://railgds.net/ws/booking}responseSpec uses Python identifier responseSpec
    __responseSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), 'responseSpec', '__httprailgds_netwsbooking_CancelBookingRecordRequestType_httprailgds_netwsbookingresponseSpec', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 242, 20), )

    
    responseSpec = property(__responseSpec.value, __responseSpec.set, None, None)

    
    # Element {http://railgds.net/ws/booking}cancellationReason uses Python identifier cancellationReason
    __cancellationReason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cancellationReason'), 'cancellationReason', '__httprailgds_netwsbooking_CancelBookingRecordRequestType_httprailgds_netwsbookingcancellationReason', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 250, 20), )

    
    cancellationReason = property(__cancellationReason.value, __cancellationReason.set, None, None)

    
    # Element {http://railgds.net/ws/booking}refundInformation uses Python identifier refundInformation
    __refundInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'refundInformation'), 'refundInformation', '__httprailgds_netwsbooking_CancelBookingRecordRequestType_httprailgds_netwsbookingrefundInformation', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 252, 20), )

    
    refundInformation = property(__refundInformation.value, __refundInformation.set, None, None)

    
    # Element {http://railgds.net/ws/booking}selectedCancellationOption uses Python identifier selectedCancellationOption
    __selectedCancellationOption = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'selectedCancellationOption'), 'selectedCancellationOption', '__httprailgds_netwsbooking_CancelBookingRecordRequestType_httprailgds_netwsbookingselectedCancellationOption', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 254, 20), )

    
    selectedCancellationOption = property(__selectedCancellationOption.value, __selectedCancellationOption.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __recordLocator.name() : __recordLocator,
        __orderLocator.name() : __orderLocator,
        __ticketableFareLocators.name() : __ticketableFareLocators,
        __expectedCancellationFee.name() : __expectedCancellationFee,
        __parameters.name() : __parameters,
        __responseSpec.name() : __responseSpec,
        __cancellationReason.name() : __cancellationReason,
        __refundInformation.name() : __refundInformation,
        __selectedCancellationOption.name() : __selectedCancellationOption
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CancelBookingRecordRequestType', CancelBookingRecordRequestType)


# Complex type {http://railgds.net/ws/booking}ClaimValueDocumentRequestType with content type ELEMENT_ONLY
class ClaimValueDocumentRequestType (BaseBookingRequestType):
    """Complex type {http://railgds.net/ws/booking}ClaimValueDocumentRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClaimValueDocumentRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 283, 4)
    _ElementMap = BaseBookingRequestType._ElementMap.copy()
    _AttributeMap = BaseBookingRequestType._AttributeMap.copy()
    # Base type is BaseBookingRequestType
    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element notes ({http://railgds.net/ws/booking}notes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element orderNotes ({http://railgds.net/ws/booking}orderNotes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element {http://railgds.net/ws/booking}recordLocator uses Python identifier recordLocator
    __recordLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), 'recordLocator', '__httprailgds_netwsbooking_ClaimValueDocumentRequestType_httprailgds_netwsbookingrecordLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 287, 20), )

    
    recordLocator = property(__recordLocator.value, __recordLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}orderLocator uses Python identifier orderLocator
    __orderLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderLocator'), 'orderLocator', '__httprailgds_netwsbooking_ClaimValueDocumentRequestType_httprailgds_netwsbookingorderLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 288, 20), )

    
    orderLocator = property(__orderLocator.value, __orderLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}responseSpec uses Python identifier responseSpec
    __responseSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), 'responseSpec', '__httprailgds_netwsbooking_ClaimValueDocumentRequestType_httprailgds_netwsbookingresponseSpec', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 290, 20), )

    
    responseSpec = property(__responseSpec.value, __responseSpec.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __recordLocator.name() : __recordLocator,
        __orderLocator.name() : __orderLocator,
        __responseSpec.name() : __responseSpec
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ClaimValueDocumentRequestType', ClaimValueDocumentRequestType)


# Complex type {http://railgds.net/ws/booking}ConfirmBookingRecordRequestType with content type ELEMENT_ONLY
class ConfirmBookingRecordRequestType (BaseBookingRequestType):
    """Complex type {http://railgds.net/ws/booking}ConfirmBookingRecordRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConfirmBookingRecordRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 317, 4)
    _ElementMap = BaseBookingRequestType._ElementMap.copy()
    _AttributeMap = BaseBookingRequestType._AttributeMap.copy()
    # Base type is BaseBookingRequestType
    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element notes ({http://railgds.net/ws/booking}notes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element orderNotes ({http://railgds.net/ws/booking}orderNotes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element {http://railgds.net/ws/booking}recordLocator uses Python identifier recordLocator
    __recordLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), 'recordLocator', '__httprailgds_netwsbooking_ConfirmBookingRecordRequestType_httprailgds_netwsbookingrecordLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 321, 20), )

    
    recordLocator = property(__recordLocator.value, __recordLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}orderLocator uses Python identifier orderLocator
    __orderLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderLocator'), 'orderLocator', '__httprailgds_netwsbooking_ConfirmBookingRecordRequestType_httprailgds_netwsbookingorderLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 322, 20), )

    
    orderLocator = property(__orderLocator.value, __orderLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}confirmationInformation uses Python identifier confirmationInformation
    __confirmationInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'confirmationInformation'), 'confirmationInformation', '__httprailgds_netwsbooking_ConfirmBookingRecordRequestType_httprailgds_netwsbookingconfirmationInformation', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 324, 20), )

    
    confirmationInformation = property(__confirmationInformation.value, __confirmationInformation.set, None, None)

    
    # Element {http://railgds.net/ws/booking}fulfillmentInformation uses Python identifier fulfillmentInformation
    __fulfillmentInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fulfillmentInformation'), 'fulfillmentInformation', '__httprailgds_netwsbooking_ConfirmBookingRecordRequestType_httprailgds_netwsbookingfulfillmentInformation', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 326, 20), )

    
    fulfillmentInformation = property(__fulfillmentInformation.value, __fulfillmentInformation.set, None, None)

    
    # Element {http://railgds.net/ws/booking}responseSpec uses Python identifier responseSpec
    __responseSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), 'responseSpec', '__httprailgds_netwsbooking_ConfirmBookingRecordRequestType_httprailgds_netwsbookingresponseSpec', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 328, 20), )

    
    responseSpec = property(__responseSpec.value, __responseSpec.set, None, None)

    
    # Element {http://railgds.net/ws/booking}returnClaimValueDocument uses Python identifier returnClaimValueDocument
    __returnClaimValueDocument = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'returnClaimValueDocument'), 'returnClaimValueDocument', '__httprailgds_netwsbooking_ConfirmBookingRecordRequestType_httprailgds_netwsbookingreturnClaimValueDocument', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 336, 20), )

    
    returnClaimValueDocument = property(__returnClaimValueDocument.value, __returnClaimValueDocument.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __recordLocator.name() : __recordLocator,
        __orderLocator.name() : __orderLocator,
        __confirmationInformation.name() : __confirmationInformation,
        __fulfillmentInformation.name() : __fulfillmentInformation,
        __responseSpec.name() : __responseSpec,
        __returnClaimValueDocument.name() : __returnClaimValueDocument
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ConfirmBookingRecordRequestType', ConfirmBookingRecordRequestType)


# Complex type {http://railgds.net/ws/booking}CreateBookingRecordRequestType with content type ELEMENT_ONLY
class CreateBookingRecordRequestType (BaseBookingRequestType):
    """Complex type {http://railgds.net/ws/booking}CreateBookingRecordRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CreateBookingRecordRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 400, 4)
    _ElementMap = BaseBookingRequestType._ElementMap.copy()
    _AttributeMap = BaseBookingRequestType._AttributeMap.copy()
    # Base type is BaseBookingRequestType
    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element notes ({http://railgds.net/ws/booking}notes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element orderNotes ({http://railgds.net/ws/booking}orderNotes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element {http://railgds.net/ws/booking}passengers uses Python identifier passengers
    __passengers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passengers'), 'passengers', '__httprailgds_netwsbooking_CreateBookingRecordRequestType_httprailgds_netwsbookingpassengers', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 404, 20), )

    
    passengers = property(__passengers.value, __passengers.set, None, None)

    
    # Element {http://railgds.net/ws/booking}legSolutions uses Python identifier legSolutions
    __legSolutions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legSolutions'), 'legSolutions', '__httprailgds_netwsbooking_CreateBookingRecordRequestType_httprailgds_netwsbookinglegSolutions', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 412, 20), )

    
    legSolutions = property(__legSolutions.value, __legSolutions.set, None, None)

    
    # Element {http://railgds.net/ws/booking}prices uses Python identifier prices
    __prices = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'prices'), 'prices', '__httprailgds_netwsbooking_CreateBookingRecordRequestType_httprailgds_netwsbookingprices', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 413, 20), )

    
    prices = property(__prices.value, __prices.set, None, None)

    
    # Element {http://railgds.net/ws/booking}travelPassQuery uses Python identifier travelPassQuery
    __travelPassQuery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'travelPassQuery'), 'travelPassQuery', '__httprailgds_netwsbooking_CreateBookingRecordRequestType_httprailgds_netwsbookingtravelPassQuery', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 421, 20), )

    
    travelPassQuery = property(__travelPassQuery.value, __travelPassQuery.set, None, None)

    
    # Element {http://railgds.net/ws/booking}transactionFees uses Python identifier transactionFees
    __transactionFees = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionFees'), 'transactionFees', '__httprailgds_netwsbooking_CreateBookingRecordRequestType_httprailgds_netwsbookingtransactionFees', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 422, 20), )

    
    transactionFees = property(__transactionFees.value, __transactionFees.set, None, None)

    
    # Element {http://railgds.net/ws/booking}parameters uses Python identifier parameters
    __parameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameters'), 'parameters', '__httprailgds_netwsbooking_CreateBookingRecordRequestType_httprailgds_netwsbookingparameters', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 430, 20), )

    
    parameters = property(__parameters.value, __parameters.set, None, None)

    
    # Element {http://railgds.net/ws/booking}responseSpec uses Python identifier responseSpec
    __responseSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), 'responseSpec', '__httprailgds_netwsbooking_CreateBookingRecordRequestType_httprailgds_netwsbookingresponseSpec', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 450, 20), )

    
    responseSpec = property(__responseSpec.value, __responseSpec.set, None, None)

    
    # Element {http://railgds.net/ws/booking}externalIdentification uses Python identifier externalIdentification
    __externalIdentification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'externalIdentification'), 'externalIdentification', '__httprailgds_netwsbooking_CreateBookingRecordRequestType_httprailgds_netwsbookingexternalIdentification', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 458, 20), )

    
    externalIdentification = property(__externalIdentification.value, __externalIdentification.set, None, None)

    
    # Element {http://railgds.net/ws/booking}fareQualifiers uses Python identifier fareQualifiers
    __fareQualifiers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fareQualifiers'), 'fareQualifiers', '__httprailgds_netwsbooking_CreateBookingRecordRequestType_httprailgds_netwsbookingfareQualifiers', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 460, 20), )

    
    fareQualifiers = property(__fareQualifiers.value, __fareQualifiers.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __passengers.name() : __passengers,
        __legSolutions.name() : __legSolutions,
        __prices.name() : __prices,
        __travelPassQuery.name() : __travelPassQuery,
        __transactionFees.name() : __transactionFees,
        __parameters.name() : __parameters,
        __responseSpec.name() : __responseSpec,
        __externalIdentification.name() : __externalIdentification,
        __fareQualifiers.name() : __fareQualifiers
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CreateBookingRecordRequestType', CreateBookingRecordRequestType)


# Complex type {http://railgds.net/ws/booking}RedeliverValueDocumentRequestType with content type ELEMENT_ONLY
class RedeliverValueDocumentRequestType (BaseBookingRequestType):
    """Complex type {http://railgds.net/ws/booking}RedeliverValueDocumentRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RedeliverValueDocumentRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 582, 4)
    _ElementMap = BaseBookingRequestType._ElementMap.copy()
    _AttributeMap = BaseBookingRequestType._AttributeMap.copy()
    # Base type is BaseBookingRequestType
    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element notes ({http://railgds.net/ws/booking}notes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element orderNotes ({http://railgds.net/ws/booking}orderNotes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element {http://railgds.net/ws/booking}recordLocator uses Python identifier recordLocator
    __recordLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), 'recordLocator', '__httprailgds_netwsbooking_RedeliverValueDocumentRequestType_httprailgds_netwsbookingrecordLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 586, 20), )

    
    recordLocator = property(__recordLocator.value, __recordLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}orderLocator uses Python identifier orderLocator
    __orderLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderLocator'), 'orderLocator', '__httprailgds_netwsbooking_RedeliverValueDocumentRequestType_httprailgds_netwsbookingorderLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 587, 20), )

    
    orderLocator = property(__orderLocator.value, __orderLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}emailAddress uses Python identifier emailAddress
    __emailAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'emailAddress'), 'emailAddress', '__httprailgds_netwsbooking_RedeliverValueDocumentRequestType_httprailgds_netwsbookingemailAddress', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 589, 24), )

    
    emailAddress = property(__emailAddress.value, __emailAddress.set, None, None)

    
    # Element {http://railgds.net/ws/booking}phoneNumber uses Python identifier phoneNumber
    __phoneNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'phoneNumber'), 'phoneNumber', '__httprailgds_netwsbooking_RedeliverValueDocumentRequestType_httprailgds_netwsbookingphoneNumber', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 590, 24), )

    
    phoneNumber = property(__phoneNumber.value, __phoneNumber.set, None, None)

    
    # Element {http://railgds.net/ws/booking}language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'language'), 'language', '__httprailgds_netwsbooking_RedeliverValueDocumentRequestType_httprailgds_netwsbookinglanguage', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 592, 20), )

    
    language = property(__language.value, __language.set, None, None)

    
    # Element {http://railgds.net/ws/booking}responseSpec uses Python identifier responseSpec
    __responseSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), 'responseSpec', '__httprailgds_netwsbooking_RedeliverValueDocumentRequestType_httprailgds_netwsbookingresponseSpec', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 593, 20), )

    
    responseSpec = property(__responseSpec.value, __responseSpec.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __recordLocator.name() : __recordLocator,
        __orderLocator.name() : __orderLocator,
        __emailAddress.name() : __emailAddress,
        __phoneNumber.name() : __phoneNumber,
        __language.name() : __language,
        __responseSpec.name() : __responseSpec
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RedeliverValueDocumentRequestType', RedeliverValueDocumentRequestType)


# Complex type {http://railgds.net/ws/booking}ReturnValueDocumentRequestType with content type ELEMENT_ONLY
class ReturnValueDocumentRequestType (BaseBookingRequestType):
    """Complex type {http://railgds.net/ws/booking}ReturnValueDocumentRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReturnValueDocumentRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 642, 4)
    _ElementMap = BaseBookingRequestType._ElementMap.copy()
    _AttributeMap = BaseBookingRequestType._AttributeMap.copy()
    # Base type is BaseBookingRequestType
    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element notes ({http://railgds.net/ws/booking}notes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element orderNotes ({http://railgds.net/ws/booking}orderNotes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element {http://railgds.net/ws/booking}recordLocator uses Python identifier recordLocator
    __recordLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), 'recordLocator', '__httprailgds_netwsbooking_ReturnValueDocumentRequestType_httprailgds_netwsbookingrecordLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 646, 20), )

    
    recordLocator = property(__recordLocator.value, __recordLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}orderLocator uses Python identifier orderLocator
    __orderLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderLocator'), 'orderLocator', '__httprailgds_netwsbooking_ReturnValueDocumentRequestType_httprailgds_netwsbookingorderLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 647, 20), )

    
    orderLocator = property(__orderLocator.value, __orderLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}valueDocumentLocator uses Python identifier valueDocumentLocator
    __valueDocumentLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueDocumentLocator'), 'valueDocumentLocator', '__httprailgds_netwsbooking_ReturnValueDocumentRequestType_httprailgds_netwsbookingvalueDocumentLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 649, 20), )

    
    valueDocumentLocator = property(__valueDocumentLocator.value, __valueDocumentLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}receiveCoupons uses Python identifier receiveCoupons
    __receiveCoupons = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'receiveCoupons'), 'receiveCoupons', '__httprailgds_netwsbooking_ReturnValueDocumentRequestType_httprailgds_netwsbookingreceiveCoupons', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 651, 24), )

    
    receiveCoupons = property(__receiveCoupons.value, __receiveCoupons.set, None, None)

    
    # Element {http://railgds.net/ws/booking}authorizeRefund uses Python identifier authorizeRefund
    __authorizeRefund = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'authorizeRefund'), 'authorizeRefund', '__httprailgds_netwsbooking_ReturnValueDocumentRequestType_httprailgds_netwsbookingauthorizeRefund', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 695, 24), )

    
    authorizeRefund = property(__authorizeRefund.value, __authorizeRefund.set, None, None)

    
    # Element {http://railgds.net/ws/booking}responseSpec uses Python identifier responseSpec
    __responseSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), 'responseSpec', '__httprailgds_netwsbooking_ReturnValueDocumentRequestType_httprailgds_netwsbookingresponseSpec', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 747, 20), )

    
    responseSpec = property(__responseSpec.value, __responseSpec.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __recordLocator.name() : __recordLocator,
        __orderLocator.name() : __orderLocator,
        __valueDocumentLocator.name() : __valueDocumentLocator,
        __receiveCoupons.name() : __receiveCoupons,
        __authorizeRefund.name() : __authorizeRefund,
        __responseSpec.name() : __responseSpec
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ReturnValueDocumentRequestType', ReturnValueDocumentRequestType)


# Complex type {http://railgds.net/ws/booking}UpdateBookingRecordRequestType with content type ELEMENT_ONLY
class UpdateBookingRecordRequestType (BaseBookingRequestType):
    """Complex type {http://railgds.net/ws/booking}UpdateBookingRecordRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UpdateBookingRecordRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 812, 4)
    _ElementMap = BaseBookingRequestType._ElementMap.copy()
    _AttributeMap = BaseBookingRequestType._AttributeMap.copy()
    # Base type is BaseBookingRequestType
    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element notes ({http://railgds.net/ws/booking}notes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element orderNotes ({http://railgds.net/ws/booking}orderNotes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element {http://railgds.net/ws/booking}recordLocator uses Python identifier recordLocator
    __recordLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), 'recordLocator', '__httprailgds_netwsbooking_UpdateBookingRecordRequestType_httprailgds_netwsbookingrecordLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 816, 20), )

    
    recordLocator = property(__recordLocator.value, __recordLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}orderLocator uses Python identifier orderLocator
    __orderLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderLocator'), 'orderLocator', '__httprailgds_netwsbooking_UpdateBookingRecordRequestType_httprailgds_netwsbookingorderLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 817, 20), )

    
    orderLocator = property(__orderLocator.value, __orderLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}serviceFees uses Python identifier serviceFees
    __serviceFees = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serviceFees'), 'serviceFees', '__httprailgds_netwsbooking_UpdateBookingRecordRequestType_httprailgds_netwsbookingserviceFees', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 819, 20), )

    
    serviceFees = property(__serviceFees.value, __serviceFees.set, None, None)

    
    # Element {http://railgds.net/ws/booking}fulfillmentInformation uses Python identifier fulfillmentInformation
    __fulfillmentInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fulfillmentInformation'), 'fulfillmentInformation', '__httprailgds_netwsbooking_UpdateBookingRecordRequestType_httprailgds_netwsbookingfulfillmentInformation', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 821, 24), )

    
    fulfillmentInformation = property(__fulfillmentInformation.value, __fulfillmentInformation.set, None, None)

    
    # Element {http://railgds.net/ws/booking}removeSelectedTicketingOption uses Python identifier removeSelectedTicketingOption
    __removeSelectedTicketingOption = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'removeSelectedTicketingOption'), 'removeSelectedTicketingOption', '__httprailgds_netwsbooking_UpdateBookingRecordRequestType_httprailgds_netwsbookingremoveSelectedTicketingOption', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 823, 24), )

    
    removeSelectedTicketingOption = property(__removeSelectedTicketingOption.value, __removeSelectedTicketingOption.set, None, None)

    
    # Element {http://railgds.net/ws/booking}customInformation uses Python identifier customInformation
    __customInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customInformation'), 'customInformation', '__httprailgds_netwsbooking_UpdateBookingRecordRequestType_httprailgds_netwsbookingcustomInformation', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 827, 20), )

    
    customInformation = property(__customInformation.value, __customInformation.set, None, None)

    
    # Element {http://railgds.net/ws/booking}shipmentTracking uses Python identifier shipmentTracking
    __shipmentTracking = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shipmentTracking'), 'shipmentTracking', '__httprailgds_netwsbooking_UpdateBookingRecordRequestType_httprailgds_netwsbookingshipmentTracking', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 829, 20), )

    
    shipmentTracking = property(__shipmentTracking.value, __shipmentTracking.set, None, None)

    
    # Element {http://railgds.net/ws/booking}order uses Python identifier order
    __order = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'order'), 'order', '__httprailgds_netwsbooking_UpdateBookingRecordRequestType_httprailgds_netwsbookingorder', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 831, 20), )

    
    order = property(__order.value, __order.set, None, None)

    
    # Element {http://railgds.net/ws/booking}passengers uses Python identifier passengers
    __passengers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passengers'), 'passengers', '__httprailgds_netwsbooking_UpdateBookingRecordRequestType_httprailgds_netwsbookingpassengers', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 876, 20), )

    
    passengers = property(__passengers.value, __passengers.set, None, None)

    
    # Element {http://railgds.net/ws/booking}responseSpec uses Python identifier responseSpec
    __responseSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), 'responseSpec', '__httprailgds_netwsbooking_UpdateBookingRecordRequestType_httprailgds_netwsbookingresponseSpec', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 884, 20), )

    
    responseSpec = property(__responseSpec.value, __responseSpec.set, None, None)

    
    # Element {http://railgds.net/ws/booking}externalIdentification uses Python identifier externalIdentification
    __externalIdentification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'externalIdentification'), 'externalIdentification', '__httprailgds_netwsbooking_UpdateBookingRecordRequestType_httprailgds_netwsbookingexternalIdentification', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 892, 20), )

    
    externalIdentification = property(__externalIdentification.value, __externalIdentification.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __recordLocator.name() : __recordLocator,
        __orderLocator.name() : __orderLocator,
        __serviceFees.name() : __serviceFees,
        __fulfillmentInformation.name() : __fulfillmentInformation,
        __removeSelectedTicketingOption.name() : __removeSelectedTicketingOption,
        __customInformation.name() : __customInformation,
        __shipmentTracking.name() : __shipmentTracking,
        __order.name() : __order,
        __passengers.name() : __passengers,
        __responseSpec.name() : __responseSpec,
        __externalIdentification.name() : __externalIdentification
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'UpdateBookingRecordRequestType', UpdateBookingRecordRequestType)


# Complex type {http://railgds.net/ws/booking}RecordFinancialTransactionRequestType with content type ELEMENT_ONLY
class RecordFinancialTransactionRequestType (BaseBookingRequestType):
    """Complex type {http://railgds.net/ws/booking}RecordFinancialTransactionRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RecordFinancialTransactionRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 910, 4)
    _ElementMap = BaseBookingRequestType._ElementMap.copy()
    _AttributeMap = BaseBookingRequestType._AttributeMap.copy()
    # Base type is BaseBookingRequestType
    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element notes ({http://railgds.net/ws/booking}notes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element orderNotes ({http://railgds.net/ws/booking}orderNotes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element {http://railgds.net/ws/booking}recordLocator uses Python identifier recordLocator
    __recordLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), 'recordLocator', '__httprailgds_netwsbooking_RecordFinancialTransactionRequestType_httprailgds_netwsbookingrecordLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 914, 20), )

    
    recordLocator = property(__recordLocator.value, __recordLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}refunds uses Python identifier refunds
    __refunds = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'refunds'), 'refunds', '__httprailgds_netwsbooking_RecordFinancialTransactionRequestType_httprailgds_netwsbookingrefunds', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 915, 20), )

    
    refunds = property(__refunds.value, __refunds.set, None, None)

    
    # Element {http://railgds.net/ws/booking}responseSpec uses Python identifier responseSpec
    __responseSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), 'responseSpec', '__httprailgds_netwsbooking_RecordFinancialTransactionRequestType_httprailgds_netwsbookingresponseSpec', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 934, 20), )

    
    responseSpec = property(__responseSpec.value, __responseSpec.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __recordLocator.name() : __recordLocator,
        __refunds.name() : __refunds,
        __responseSpec.name() : __responseSpec
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RecordFinancialTransactionRequestType', RecordFinancialTransactionRequestType)


# Complex type {http://railgds.net/ws/booking}RefundBookingRecordRequestType with content type ELEMENT_ONLY
class RefundBookingRecordRequestType (BaseBookingRequestType):
    """Complex type {http://railgds.net/ws/booking}RefundBookingRecordRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RefundBookingRecordRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 958, 4)
    _ElementMap = BaseBookingRequestType._ElementMap.copy()
    _AttributeMap = BaseBookingRequestType._AttributeMap.copy()
    # Base type is BaseBookingRequestType
    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element notes ({http://railgds.net/ws/booking}notes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element orderNotes ({http://railgds.net/ws/booking}orderNotes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element {http://railgds.net/ws/booking}recordLocator uses Python identifier recordLocator
    __recordLocator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), 'recordLocator', '__httprailgds_netwsbooking_RefundBookingRecordRequestType_httprailgds_netwsbookingrecordLocator', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 962, 20), )

    
    recordLocator = property(__recordLocator.value, __recordLocator.set, None, None)

    
    # Element {http://railgds.net/ws/booking}responseSpec uses Python identifier responseSpec
    __responseSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), 'responseSpec', '__httprailgds_netwsbooking_RefundBookingRecordRequestType_httprailgds_netwsbookingresponseSpec', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 963, 20), )

    
    responseSpec = property(__responseSpec.value, __responseSpec.set, None, None)

    
    # Element {http://railgds.net/ws/booking}receiptNumber uses Python identifier receiptNumber
    __receiptNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'receiptNumber'), 'receiptNumber', '__httprailgds_netwsbooking_RefundBookingRecordRequestType_httprailgds_netwsbookingreceiptNumber', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 971, 20), )

    
    receiptNumber = property(__receiptNumber.value, __receiptNumber.set, None, None)

    
    # Element {http://railgds.net/ws/booking}refundAmount uses Python identifier refundAmount
    __refundAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'refundAmount'), 'refundAmount', '__httprailgds_netwsbooking_RefundBookingRecordRequestType_httprailgds_netwsbookingrefundAmount', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 972, 20), )

    
    refundAmount = property(__refundAmount.value, __refundAmount.set, None, None)

    
    # Element {http://railgds.net/ws/booking}refundReason uses Python identifier refundReason
    __refundReason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'refundReason'), 'refundReason', '__httprailgds_netwsbooking_RefundBookingRecordRequestType_httprailgds_netwsbookingrefundReason', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 973, 20), )

    
    refundReason = property(__refundReason.value, __refundReason.set, None, None)

    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __recordLocator.name() : __recordLocator,
        __responseSpec.name() : __responseSpec,
        __receiptNumber.name() : __receiptNumber,
        __refundAmount.name() : __refundAmount,
        __refundReason.name() : __refundReason
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RefundBookingRecordRequestType', RefundBookingRecordRequestType)


# Complex type {http://railgds.net/ws/booking}AddPaymentRequestType with content type ELEMENT_ONLY
class AddPaymentRequestType (AbstractPaymentRequestType):
    """Complex type {http://railgds.net/ws/booking}AddPaymentRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddPaymentRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 92, 4)
    _ElementMap = AbstractPaymentRequestType._ElementMap.copy()
    _AttributeMap = AbstractPaymentRequestType._AttributeMap.copy()
    # Base type is AbstractPaymentRequestType
    
    # Element recordLocator ({http://railgds.net/ws/booking}recordLocator) inherited from {http://railgds.net/ws/booking}AbstractPaymentRequestType
    
    # Element payment ({http://railgds.net/ws/booking}payment) inherited from {http://railgds.net/ws/booking}AbstractPaymentRequestType
    
    # Element {http://railgds.net/ws/booking}parameters uses Python identifier parameters
    __parameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameters'), 'parameters', '__httprailgds_netwsbooking_AddPaymentRequestType_httprailgds_netwsbookingparameters', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 96, 20), )

    
    parameters = property(__parameters.value, __parameters.set, None, None)

    
    # Element {http://railgds.net/ws/booking}confirmationInformation uses Python identifier confirmationInformation
    __confirmationInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'confirmationInformation'), 'confirmationInformation', '__httprailgds_netwsbooking_AddPaymentRequestType_httprailgds_netwsbookingconfirmationInformation', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 103, 20), )

    
    confirmationInformation = property(__confirmationInformation.value, __confirmationInformation.set, None, None)

    
    # Element {http://railgds.net/ws/booking}fulfillmentInformation uses Python identifier fulfillmentInformation
    __fulfillmentInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fulfillmentInformation'), 'fulfillmentInformation', '__httprailgds_netwsbooking_AddPaymentRequestType_httprailgds_netwsbookingfulfillmentInformation', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 105, 20), )

    
    fulfillmentInformation = property(__fulfillmentInformation.value, __fulfillmentInformation.set, None, None)

    
    # Element {http://railgds.net/ws/booking}responseSpec uses Python identifier responseSpec
    __responseSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), 'responseSpec', '__httprailgds_netwsbooking_AddPaymentRequestType_httprailgds_netwsbookingresponseSpec', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 107, 20), )

    
    responseSpec = property(__responseSpec.value, __responseSpec.set, None, None)

    
    # Element {http://railgds.net/ws/booking}customerIpAddress uses Python identifier customerIpAddress
    __customerIpAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerIpAddress'), 'customerIpAddress', '__httprailgds_netwsbooking_AddPaymentRequestType_httprailgds_netwsbookingcustomerIpAddress', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 115, 20), )

    
    customerIpAddress = property(__customerIpAddress.value, __customerIpAddress.set, None, None)

    
    # Element {http://railgds.net/ws/booking}threeDeeAuthenticatePayer uses Python identifier threeDeeAuthenticatePayer
    __threeDeeAuthenticatePayer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'threeDeeAuthenticatePayer'), 'threeDeeAuthenticatePayer', '__httprailgds_netwsbooking_AddPaymentRequestType_httprailgds_netwsbookingthreeDeeAuthenticatePayer', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 116, 20), )

    
    threeDeeAuthenticatePayer = property(__threeDeeAuthenticatePayer.value, __threeDeeAuthenticatePayer.set, None, None)

    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element notes ({http://railgds.net/ws/booking}notes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element orderNotes ({http://railgds.net/ws/booking}orderNotes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __parameters.name() : __parameters,
        __confirmationInformation.name() : __confirmationInformation,
        __fulfillmentInformation.name() : __fulfillmentInformation,
        __responseSpec.name() : __responseSpec,
        __customerIpAddress.name() : __customerIpAddress,
        __threeDeeAuthenticatePayer.name() : __threeDeeAuthenticatePayer
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AddPaymentRequestType', AddPaymentRequestType)


# Complex type {http://railgds.net/ws/booking}AuthenticatePayerRequestType with content type ELEMENT_ONLY
class AuthenticatePayerRequestType (AbstractPaymentRequestType):
    """Complex type {http://railgds.net/ws/booking}AuthenticatePayerRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AuthenticatePayerRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 140, 4)
    _ElementMap = AbstractPaymentRequestType._ElementMap.copy()
    _AttributeMap = AbstractPaymentRequestType._AttributeMap.copy()
    # Base type is AbstractPaymentRequestType
    
    # Element recordLocator ({http://railgds.net/ws/booking}recordLocator) inherited from {http://railgds.net/ws/booking}AbstractPaymentRequestType
    
    # Element payment ({http://railgds.net/ws/booking}payment) inherited from {http://railgds.net/ws/booking}AbstractPaymentRequestType
    
    # Element {http://railgds.net/ws/booking}customerIpAddress uses Python identifier customerIpAddress
    __customerIpAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerIpAddress'), 'customerIpAddress', '__httprailgds_netwsbooking_AuthenticatePayerRequestType_httprailgds_netwsbookingcustomerIpAddress', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 144, 20), )

    
    customerIpAddress = property(__customerIpAddress.value, __customerIpAddress.set, None, None)

    
    # Element {http://railgds.net/ws/booking}responseSpec uses Python identifier responseSpec
    __responseSpec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), 'responseSpec', '__httprailgds_netwsbooking_AuthenticatePayerRequestType_httprailgds_netwsbookingresponseSpec', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 145, 20), )

    
    responseSpec = property(__responseSpec.value, __responseSpec.set, None, None)

    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element notes ({http://railgds.net/ws/booking}notes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element orderNotes ({http://railgds.net/ws/booking}orderNotes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        __customerIpAddress.name() : __customerIpAddress,
        __responseSpec.name() : __responseSpec
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AuthenticatePayerRequestType', AuthenticatePayerRequestType)


# Complex type {http://railgds.net/ws/booking}ValidateBookingRecordInformationRequestType with content type ELEMENT_ONLY
class ValidateBookingRecordInformationRequestType (CreateBookingRecordRequestType):
    """Complex type {http://railgds.net/ws/booking}ValidateBookingRecordInformationRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValidateBookingRecordInformationRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 996, 4)
    _ElementMap = CreateBookingRecordRequestType._ElementMap.copy()
    _AttributeMap = CreateBookingRecordRequestType._AttributeMap.copy()
    # Base type is CreateBookingRecordRequestType
    
    # Element agentInformation ({http://railgds.net/ws/booking}agentInformation) inherited from {http://railgds.net/ws/booking}AuditableRequestType
    
    # Element notes ({http://railgds.net/ws/booking}notes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element orderNotes ({http://railgds.net/ws/booking}orderNotes) inherited from {http://railgds.net/ws/booking}BaseBookingRequestType
    
    # Element passengers ({http://railgds.net/ws/booking}passengers) inherited from {http://railgds.net/ws/booking}CreateBookingRecordRequestType
    
    # Element legSolutions ({http://railgds.net/ws/booking}legSolutions) inherited from {http://railgds.net/ws/booking}CreateBookingRecordRequestType
    
    # Element prices ({http://railgds.net/ws/booking}prices) inherited from {http://railgds.net/ws/booking}CreateBookingRecordRequestType
    
    # Element travelPassQuery ({http://railgds.net/ws/booking}travelPassQuery) inherited from {http://railgds.net/ws/booking}CreateBookingRecordRequestType
    
    # Element transactionFees ({http://railgds.net/ws/booking}transactionFees) inherited from {http://railgds.net/ws/booking}CreateBookingRecordRequestType
    
    # Element parameters ({http://railgds.net/ws/booking}parameters) inherited from {http://railgds.net/ws/booking}CreateBookingRecordRequestType
    
    # Element responseSpec ({http://railgds.net/ws/booking}responseSpec) inherited from {http://railgds.net/ws/booking}CreateBookingRecordRequestType
    
    # Element externalIdentification ({http://railgds.net/ws/booking}externalIdentification) inherited from {http://railgds.net/ws/booking}CreateBookingRecordRequestType
    
    # Element fareQualifiers ({http://railgds.net/ws/booking}fareQualifiers) inherited from {http://railgds.net/ws/booking}CreateBookingRecordRequestType
    
    # Element context ({http://railgds.net/ws/commontypes}context) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Element overrides ({http://railgds.net/ws/commontypes}overrides) inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute conversationToken inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute version inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    
    # Attribute dateTime inherited from {http://railgds.net/ws/commontypes}BaseRequestType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ValidateBookingRecordInformationRequestType', ValidateBookingRecordInformationRequestType)


addPaymentResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addPaymentResponse'), AddPaymentResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 11, 4))
Namespace.addCategoryObject('elementBinding', addPaymentResponse.name().localName(), addPaymentResponse)

authenticatePayerResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authenticatePayerResponse'), AuthenticatePayerResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 13, 4))
Namespace.addCategoryObject('elementBinding', authenticatePayerResponse.name().localName(), authenticatePayerResponse)

cancelBookingRecordResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cancelBookingRecordResponse'), CancelBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 15, 4))
Namespace.addCategoryObject('elementBinding', cancelBookingRecordResponse.name().localName(), cancelBookingRecordResponse)

claimValueDocumentResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'claimValueDocumentResponse'), ClaimValueDocumentResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 17, 4))
Namespace.addCategoryObject('elementBinding', claimValueDocumentResponse.name().localName(), claimValueDocumentResponse)

confirmBookingRecordResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'confirmBookingRecordResponse'), ConfirmBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 19, 4))
Namespace.addCategoryObject('elementBinding', confirmBookingRecordResponse.name().localName(), confirmBookingRecordResponse)

createBookingRecordResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'createBookingRecordResponse'), CreateBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 21, 4))
Namespace.addCategoryObject('elementBinding', createBookingRecordResponse.name().localName(), createBookingRecordResponse)

recordFinancialTransactionResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordFinancialTransactionResponse'), RecordFinancialTransactionResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 24, 4))
Namespace.addCategoryObject('elementBinding', recordFinancialTransactionResponse.name().localName(), recordFinancialTransactionResponse)

redeliverValueDocumentResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'redeliverValueDocumentResponse'), RedeliverValueDocumentResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 27, 4))
Namespace.addCategoryObject('elementBinding', redeliverValueDocumentResponse.name().localName(), redeliverValueDocumentResponse)

retrieveBookingRecordResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'retrieveBookingRecordResponse'), RetrieveBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 29, 4))
Namespace.addCategoryObject('elementBinding', retrieveBookingRecordResponse.name().localName(), retrieveBookingRecordResponse)

returnValueDocumentResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnValueDocumentResponse'), ReturnValueDocumentResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 31, 4))
Namespace.addCategoryObject('elementBinding', returnValueDocumentResponse.name().localName(), returnValueDocumentResponse)

searchBookingRecordsRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'searchBookingRecordsRequest'), SearchBookingRecordsRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 32, 4))
Namespace.addCategoryObject('elementBinding', searchBookingRecordsRequest.name().localName(), searchBookingRecordsRequest)

searchBookingRecordsResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'searchBookingRecordsResponse'), SearchBookingRecordsResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 33, 4))
Namespace.addCategoryObject('elementBinding', searchBookingRecordsResponse.name().localName(), searchBookingRecordsResponse)

updateBookingRecordResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'updateBookingRecordResponse'), UpdateBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 35, 4))
Namespace.addCategoryObject('elementBinding', updateBookingRecordResponse.name().localName(), updateBookingRecordResponse)

refundBookingRecordResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'refundBookingRecordResponse'), RefundBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 37, 4))
Namespace.addCategoryObject('elementBinding', refundBookingRecordResponse.name().localName(), refundBookingRecordResponse)

validateBookingRecordInformationResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'validateBookingRecordInformationResponse'), ValidateBookingRecordInformationResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 39, 4))
Namespace.addCategoryObject('elementBinding', validateBookingRecordInformationResponse.name().localName(), validateBookingRecordInformationResponse)

generatePaymentTokenResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'generatePaymentTokenResponse'), GeneratePaymentTokenResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 41, 4))
Namespace.addCategoryObject('elementBinding', generatePaymentTokenResponse.name().localName(), generatePaymentTokenResponse)

deletePaymentTokenResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'deletePaymentTokenResponse'), DeletePaymentTokenResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 43, 4))
Namespace.addCategoryObject('elementBinding', deletePaymentTokenResponse.name().localName(), deletePaymentTokenResponse)

retrieveCancellationSummaryResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'retrieveCancellationSummaryResponse'), RetrieveCancellationSummaryResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 45, 4))
Namespace.addCategoryObject('elementBinding', retrieveCancellationSummaryResponse.name().localName(), retrieveCancellationSummaryResponse)

retrieveBookingRecordRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'retrieveBookingRecordRequest'), RetrieveBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 28, 4))
Namespace.addCategoryObject('elementBinding', retrieveBookingRecordRequest.name().localName(), retrieveBookingRecordRequest)

generatePaymentTokenRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'generatePaymentTokenRequest'), GeneratePaymentTokenRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 40, 4))
Namespace.addCategoryObject('elementBinding', generatePaymentTokenRequest.name().localName(), generatePaymentTokenRequest)

deletePaymentTokenRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'deletePaymentTokenRequest'), DeletePaymentTokenRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 42, 4))
Namespace.addCategoryObject('elementBinding', deletePaymentTokenRequest.name().localName(), deletePaymentTokenRequest)

retrieveCancellationSummaryRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'retrieveCancellationSummaryRequest'), RetrieveCancellationSummaryRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 44, 4))
Namespace.addCategoryObject('elementBinding', retrieveCancellationSummaryRequest.name().localName(), retrieveCancellationSummaryRequest)

cancelBookingRecordRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cancelBookingRecordRequest'), CancelBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 14, 4))
Namespace.addCategoryObject('elementBinding', cancelBookingRecordRequest.name().localName(), cancelBookingRecordRequest)

claimValueDocumentRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'claimValueDocumentRequest'), ClaimValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 16, 4))
Namespace.addCategoryObject('elementBinding', claimValueDocumentRequest.name().localName(), claimValueDocumentRequest)

confirmBookingRecordRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'confirmBookingRecordRequest'), ConfirmBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 18, 4))
Namespace.addCategoryObject('elementBinding', confirmBookingRecordRequest.name().localName(), confirmBookingRecordRequest)

createBookingRecordRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'createBookingRecordRequest'), CreateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 20, 4))
Namespace.addCategoryObject('elementBinding', createBookingRecordRequest.name().localName(), createBookingRecordRequest)

recordFinancialTransactionRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordFinancialTransactionRequest'), RecordFinancialTransactionRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 22, 4))
Namespace.addCategoryObject('elementBinding', recordFinancialTransactionRequest.name().localName(), recordFinancialTransactionRequest)

redeliverValueDocumentRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'redeliverValueDocumentRequest'), RedeliverValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 26, 4))
Namespace.addCategoryObject('elementBinding', redeliverValueDocumentRequest.name().localName(), redeliverValueDocumentRequest)

returnValueDocumentRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnValueDocumentRequest'), ReturnValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 30, 4))
Namespace.addCategoryObject('elementBinding', returnValueDocumentRequest.name().localName(), returnValueDocumentRequest)

updateBookingRecordRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'updateBookingRecordRequest'), UpdateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 34, 4))
Namespace.addCategoryObject('elementBinding', updateBookingRecordRequest.name().localName(), updateBookingRecordRequest)

refundBookingRecordRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'refundBookingRecordRequest'), RefundBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 36, 4))
Namespace.addCategoryObject('elementBinding', refundBookingRecordRequest.name().localName(), refundBookingRecordRequest)

addPaymentRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addPaymentRequest'), AddPaymentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 10, 4))
Namespace.addCategoryObject('elementBinding', addPaymentRequest.name().localName(), addPaymentRequest)

authenticatePayerRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authenticatePayerRequest'), AuthenticatePayerRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 12, 4))
Namespace.addCategoryObject('elementBinding', authenticatePayerRequest.name().localName(), authenticatePayerRequest)

validateBookingRecordInformationRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'validateBookingRecordInformationRequest'), ValidateBookingRecordInformationRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 38, 4))
Namespace.addCategoryObject('elementBinding', validateBookingRecordInformationRequest.name().localName(), validateBookingRecordInformationRequest)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'formOfPayment'), _ImportedBinding_silvercom.FormOfPaymentType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 55, 32)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'creditCard'), AddPaymentCreditCardType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 57, 36)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'check'), _ImportedBinding_silvercom.CheckType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 59, 36)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'onAccount'), _ImportedBinding_silvercom.OnAccountType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 60, 36)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'debitCard'), AddPaymentDebitCardType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 61, 36)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'voucher'), _ImportedBinding_silvercom.VoucherType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 62, 36)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eCheck'), _ImportedBinding_silvercom.BaseECheckType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 63, 36)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'amount'), _ImportedBinding_silvercom.MoneyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 65, 32)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'formOfPayment')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 55, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'creditCard')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 57, 36))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'check')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 59, 36))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'onAccount')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 60, 36))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'debitCard')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 61, 36))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'voucher')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 62, 36))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eCheck')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 63, 36))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'amount')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 65, 32))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
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
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'confirmBooking'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 99, 32)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 99, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'confirmBooking')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 99, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 110, 32)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 110, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 110, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'payerAuthenticationResponse'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 119, 32)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'payerAuthenticationResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 119, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 148, 32)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 148, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 148, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'isEnrolled'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 164, 32)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'processor'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 165, 32)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accessControlServerUrl'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 166, 32)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'payerAuthenticationRequest'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 168, 32)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 165, 32))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 166, 32))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 168, 32))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isEnrolled')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 164, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'processor')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 165, 32))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accessControlServerUrl')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 166, 32))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'payerAuthenticationRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 168, 32))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'externalId'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 185, 32)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 186, 32)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 185, 32))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 186, 32))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'externalId')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 185, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 186, 32))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'note'), _ImportedBinding_silvercom.BookingNoteType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 202, 32)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'note')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 202, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderNote'), _ImportedBinding_silvercom.AddedOrderNoteType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 210, 32)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNote')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 210, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_8()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ticketableFareLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 229, 32)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ticketableFareLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 229, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_9()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'alwaysAcceptCancellationFee'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 237, 32)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 237, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'alwaysAcceptCancellationFee')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 237, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_10()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 245, 32)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 245, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 245, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_11()




RefundInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'processRefundWithCancel'), pyxb.binding.datatypes.boolean, scope=RefundInformationType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 263, 12), unicode_default='false'))

RefundInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'receiptNumber'), _ImportedBinding_silvercom.AnorakReceiptLocatorType, scope=RefundInformationType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 264, 12)))

RefundInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'refundAmount'), _ImportedBinding_silvercom.MoneyType, scope=RefundInformationType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 266, 12)))

RefundInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'refundReason'), pyxb.binding.datatypes.string, scope=RefundInformationType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 267, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 264, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 266, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 267, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RefundInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'processRefundWithCancel')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 263, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RefundInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'receiptNumber')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 264, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RefundInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refundAmount')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 266, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RefundInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refundReason')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 267, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RefundInformationType._Automaton = _BuildAutomaton_12()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 293, 32)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 293, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 293, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_13()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 331, 32)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 331, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 331, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_14()




ClaimValueDocumentResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'result'), _ImportedBinding_silvercom.RequestStatusType, scope=ClaimValueDocumentResultType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 357, 12)))

ClaimValueDocumentResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'claimValueDocumentUrl'), pyxb.binding.datatypes.string, scope=ClaimValueDocumentResultType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 358, 12)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 358, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ClaimValueDocumentResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'result')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 357, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClaimValueDocumentResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'claimValueDocumentUrl')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 358, 12))
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
ClaimValueDocumentResultType._Automaton = _BuildAutomaton_15()




ConfirmationInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueDocumentRetrievalInformation'), CTD_ANON_14, scope=ConfirmationInformationType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 365, 16)))

ConfirmationInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'selectedConfirmationOption'), _ImportedBinding_silvercom.selectedConfirmationOptionType, scope=ConfirmationInformationType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 386, 16)))

ConfirmationInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'selectedTicketLanguage'), pyxb.binding.datatypes.string, scope=ConfirmationInformationType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 389, 12)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 365, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 386, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 389, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ConfirmationInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueDocumentRetrievalInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 365, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ConfirmationInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'selectedConfirmationOption')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 386, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ConfirmationInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'selectedTicketLanguage')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 389, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ConfirmationInformationType._Automaton = _BuildAutomaton_16()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customer'), CTD_ANON_15, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 369, 28)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'creditCardNumber'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 379, 28)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expirationDate'), pyxb.binding.datatypes.gYearMonth, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 380, 28)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 380, 28))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customer')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 369, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'creditCardNumber')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 379, 28))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expirationDate')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 380, 28))
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
CTD_ANON_14._Automaton = _BuildAutomaton_17()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nameLast'), pyxb.binding.datatypes.string, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 372, 40)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nameFirst'), pyxb.binding.datatypes.string, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 373, 40)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nameMiddle'), pyxb.binding.datatypes.string, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 374, 40)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 373, 40))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 374, 40))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nameLast')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 372, 40))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nameFirst')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 373, 40))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nameMiddle')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 374, 40))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_18()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passenger'), _ImportedBinding_silvercom.PassengerType, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 407, 32)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passenger')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 407, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_19()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pointToPointPrice'), _ImportedBinding_silvercom.PointToPointPriceType, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 416, 36)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pointToPointPrice')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 416, 36))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_20()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionFee'), BookingTransactionFeeType, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 425, 32)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionFee')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 425, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_21()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'priceAcceptance'), CTD_ANON_20, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 433, 32)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shopAncillary'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 446, 32)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 433, 32))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 446, 32))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'priceAcceptance')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 433, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shopAncillary')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 446, 32))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_22()




CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'acceptAny'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 436, 44)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'acceptHigher'), PriceAcceptanceType, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 438, 48)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'acceptLower'), PriceAcceptanceType, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 440, 48)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 438, 48))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 440, 48))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'acceptAny')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 436, 44))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'acceptHigher')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 438, 48))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'acceptLower')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 440, 48))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_23()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 453, 32)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 453, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 453, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_24()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fareQualifier'), _ImportedBinding_silvercom.FareQualifierType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 463, 32)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fareQualifier')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 463, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_25()




TravelPassQuery._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'travelPointPair'), _ImportedBinding_silvercom.QueryTravelPointPairPassType, scope=TravelPassQuery, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 487, 12)))

TravelPassQuery._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passPrices'), CTD_ANON_23, scope=TravelPassQuery, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 488, 12)))

TravelPassQuery._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passIssueType'), _ImportedBinding_silvercom.IssueType, scope=TravelPassQuery, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 496, 12)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TravelPassQuery._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'travelPointPair')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 487, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TravelPassQuery._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passPrices')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 488, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TravelPassQuery._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passIssueType')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 496, 12))
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
TravelPassQuery._Automaton = _BuildAutomaton_26()




CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'travelPassPrice'), _ImportedBinding_silvercom.PassPriceType, scope=CTD_ANON_23, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 491, 24)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'travelPassPrice')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 491, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_27()




FulfillmentInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ticketOption'), _ImportedBinding_silvercom.TicketingOptionType, scope=FulfillmentInformationType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 501, 12)))

FulfillmentInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shippingName'), pyxb.binding.datatypes.string, scope=FulfillmentInformationType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 502, 12)))

FulfillmentInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shippingAddress'), _ImportedBinding_silvercom.AddressType, scope=FulfillmentInformationType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 503, 12)))

FulfillmentInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'phoneNumber'), _ImportedBinding_silvercom.FulfillmentPhoneNumberType, scope=FulfillmentInformationType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 504, 12)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 502, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 503, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 504, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FulfillmentInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ticketOption')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 501, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FulfillmentInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shippingName')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 502, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(FulfillmentInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shippingAddress')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 503, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(FulfillmentInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'phoneNumber')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 504, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FulfillmentInformationType._Automaton = _BuildAutomaton_28()




CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'order'), CTD_ANON_25, scope=CTD_ANON_24, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 528, 32)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'order')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 528, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_29()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'alternativeTicketPickupLocation'), _ImportedBinding_silvercom.TravelPointType, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 531, 44)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 531, 44))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'alternativeTicketPickupLocation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 531, 44))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_30()




CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includeOrderDetails'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 544, 32)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includeOrderCosts'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 546, 32)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includePassengerDetails'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 547, 32)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includeFinancials'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 549, 32)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includePaymentRequirements'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 550, 32)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includeTicketingOptions'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 552, 32)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includeNotes'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 554, 32)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includeFulfillmentInformation'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 555, 32)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 544, 32))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 546, 32))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 547, 32))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 549, 32))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 550, 32))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 552, 32))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 554, 32))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 555, 32))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includeOrderDetails')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 544, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includeOrderCosts')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 546, 32))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includePassengerDetails')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 547, 32))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includeFinancials')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 549, 32))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includePaymentRequirements')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 550, 32))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includeTicketingOptions')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 552, 32))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includeNotes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 554, 32))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includeFulfillmentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 555, 32))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_31()




CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'note'), _ImportedBinding_silvercom.BookingNoteType, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 572, 32)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'note')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 572, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_32()




CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_28, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 596, 32)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 596, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 596, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_33()




CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'directDeliveryRequested'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 613, 32)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueDocumentURL'), CTD_ANON_30, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 614, 32)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueDocumentPDF'), CTD_ANON_31, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 624, 32)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 612, 28))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'directDeliveryRequested')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 613, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueDocumentURL')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 614, 32))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueDocumentPDF')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 624, 32))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_29._Automaton = _BuildAutomaton_34()




CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coupon'), CTD_ANON_64, scope=CTD_ANON_32, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 657, 48)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coupon')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 657, 48))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_32._Automaton = _BuildAutomaton_35()




CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coupons'), CTD_ANON_34, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 698, 36)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reverseRevenue'), CTD_ANON_36, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 725, 36)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reverseCost'), CTD_ANON_37, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 733, 36)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cancellationPenalty'), _ImportedBinding_silvercom.MoneyType, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 741, 36)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 725, 36))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 733, 36))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 741, 36))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coupons')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 698, 36))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reverseRevenue')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 725, 36))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reverseCost')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 733, 36))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cancellationPenalty')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 741, 36))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_33._Automaton = _BuildAutomaton_36()




CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coupon'), CTD_ANON_65, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 701, 48)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coupon')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 701, 48))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_34._Automaton = _BuildAutomaton_37()




CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'amount'), _ImportedBinding_silvercom.MoneyType, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 728, 48)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 729, 48)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'amount')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 728, 48))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 729, 48))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_36._Automaton = _BuildAutomaton_38()




CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'amount'), _ImportedBinding_silvercom.MoneyType, scope=CTD_ANON_37, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 736, 48)))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_37, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 737, 48)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'amount')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 736, 48))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 737, 48))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_37._Automaton = _BuildAutomaton_39()




CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_38, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 750, 32)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 750, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 750, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_38._Automaton = _BuildAutomaton_40()




CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passengerLastName'), pyxb.binding.datatypes.string, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 781, 32)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'emailAddress'), pyxb.binding.datatypes.string, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 782, 32)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supplyChannelLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 783, 32)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 781, 32))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 782, 32))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 783, 32))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passengerLastName')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 781, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'emailAddress')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 782, 32))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supplyChannelLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 783, 32))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_39._Automaton = _BuildAutomaton_41()




CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), _ImportedBinding_silvercom.BookingRecordType, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 802, 32)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 802, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 802, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_40._Automaton = _BuildAutomaton_42()




CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passengers'), CTD_ANON_43, scope=CTD_ANON_42, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 834, 32)))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legSolutions'), _ImportedBinding_silvercom.LegSolutionsType, scope=CTD_ANON_42, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 842, 32)))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'prices'), CTD_ANON_44, scope=CTD_ANON_42, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 843, 32)))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameters'), CTD_ANON_45, scope=CTD_ANON_42, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 852, 32)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 852, 32))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passengers')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 834, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legSolutions')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 842, 32))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prices')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 843, 32))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameters')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 852, 32))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_42._Automaton = _BuildAutomaton_43()




CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passenger'), _ImportedBinding_silvercom.PassengerType, scope=CTD_ANON_43, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 837, 44)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passenger')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 837, 44))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_43._Automaton = _BuildAutomaton_44()




CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pointToPointPrice'), _ImportedBinding_silvercom.PointToPointPriceType, scope=CTD_ANON_44, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 846, 44)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pointToPointPrice')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 846, 44))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_44._Automaton = _BuildAutomaton_45()




CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'priceAcceptance'), CTD_ANON_46, scope=CTD_ANON_45, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 855, 44)))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shopAncillary'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_45, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 868, 44)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 855, 44))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 868, 44))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'priceAcceptance')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 855, 44))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shopAncillary')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 868, 44))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_45._Automaton = _BuildAutomaton_46()




CTD_ANON_46._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'acceptAny'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_46, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 858, 50)))

CTD_ANON_46._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'acceptHigher'), PriceAcceptanceType, scope=CTD_ANON_46, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 860, 50)))

CTD_ANON_46._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'acceptLower'), PriceAcceptanceType, scope=CTD_ANON_46, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 862, 50)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 860, 50))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 862, 50))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_46._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'acceptAny')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 858, 50))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_46._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'acceptHigher')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 860, 50))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_46._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'acceptLower')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 862, 50))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_46._Automaton = _BuildAutomaton_47()




CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passenger'), _ImportedBinding_silvercom.PassengerType, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 879, 32)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passenger')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 879, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_47._Automaton = _BuildAutomaton_48()




CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_48, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 887, 32)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 887, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 887, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_48._Automaton = _BuildAutomaton_49()




CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'refund'), CTD_ANON_50, scope=CTD_ANON_49, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 918, 32)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refund')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 918, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_49._Automaton = _BuildAutomaton_50()




CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'receiptNumber'), _ImportedBinding_silvercom.AnorakReceiptLocatorType, scope=CTD_ANON_50, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 921, 44)))

CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'refundAmount'), _ImportedBinding_silvercom.MoneyType, scope=CTD_ANON_50, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 923, 44)))

CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'refundReason'), pyxb.binding.datatypes.string, scope=CTD_ANON_50, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 924, 44)))

CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentProcessorInfo'), _ImportedBinding_silvercom.PaymentProcessorInfoType, scope=CTD_ANON_50, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 926, 44)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 924, 44))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 926, 44))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'receiptNumber')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 921, 44))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refundAmount')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 923, 44))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refundReason')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 924, 44))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentProcessorInfo')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 926, 44))
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
CTD_ANON_50._Automaton = _BuildAutomaton_51()




CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_51, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 937, 32)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 937, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 937, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_51._Automaton = _BuildAutomaton_52()




CTD_ANON_52._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_52, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 966, 32)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 966, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_52._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'returnReservationDetails')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 966, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_52._Automaton = _BuildAutomaton_53()




BookingNotesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'note'), _ImportedBinding_silvercom.BookingNoteType, scope=BookingNotesType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 992, 12)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BookingNotesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'note')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 992, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BookingNotesType._Automaton = _BuildAutomaton_54()




CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderInformationSet'), CTD_ANON_54, scope=CTD_ANON_53, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1008, 32)))

CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentRequirements'), _ImportedBinding_silvercom.PaymentRequirementsType, scope=CTD_ANON_53, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1063, 32)))

CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serviceFeeAllowed'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_53, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1065, 32)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1065, 32))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderInformationSet')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1008, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentRequirements')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1063, 32))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serviceFeeAllowed')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1065, 32))
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
CTD_ANON_53._Automaton = _BuildAutomaton_55()




CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderInformation'), CTD_ANON_55, scope=CTD_ANON_54, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1011, 44)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1011, 44))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_54._Automaton = _BuildAutomaton_56()




CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'travelSegments'), CTD_ANON_56, scope=CTD_ANON_55, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1015, 56)))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ticketingOptions'), CTD_ANON_57, scope=CTD_ANON_55, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1026, 56)))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'confirmationOptions'), _ImportedBinding_silvercom.ConfirmationOptionsType, scope=CTD_ANON_55, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1036, 56)))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'confirmationInformationRequired'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_55, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1039, 56)))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentCardRequiredForConfirmationInformation'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_55, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1041, 56)))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'availableTicketLanguages'), CTD_ANON_58, scope=CTD_ANON_55, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1044, 56)))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'externalBookingUrl'), pyxb.binding.datatypes.string, scope=CTD_ANON_55, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1053, 56)))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'commercialAgentName'), pyxb.binding.datatypes.string, scope=CTD_ANON_55, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1055, 56)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1036, 56))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1044, 56))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1053, 56))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1055, 56))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'travelSegments')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1015, 56))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ticketingOptions')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1026, 56))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'confirmationOptions')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1036, 56))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'confirmationInformationRequired')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1039, 56))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentCardRequiredForConfirmationInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1041, 56))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'availableTicketLanguages')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1044, 56))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'externalBookingUrl')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1053, 56))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'commercialAgentName')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1055, 56))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_55._Automaton = _BuildAutomaton_57()




CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'travelSegment'), _ImportedBinding_silvercom.TravelSegmentType, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1019, 68)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1019, 68))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'travelSegment')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1019, 68))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_56._Automaton = _BuildAutomaton_58()




CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ticketingOption'), _ImportedBinding_silvercom.TicketingOptionType, scope=CTD_ANON_57, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1030, 68)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ticketingOption')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1030, 68))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_57._Automaton = _BuildAutomaton_59()




CTD_ANON_58._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'language'), pyxb.binding.datatypes.string, scope=CTD_ANON_58, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1048, 68)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_58._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'language')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1048, 68))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_58._Automaton = _BuildAutomaton_60()




CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'formOfPayment'), TokenPaymentType, scope=CTD_ANON_59, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1103, 32)))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'creditCard'), AddPaymentCreditCardType, scope=CTD_ANON_59, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1105, 36)))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'debitCard'), AddPaymentDebitCardType, scope=CTD_ANON_59, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1107, 36)))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerIpAddress'), pyxb.binding.datatypes.string, scope=CTD_ANON_59, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1109, 32)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1109, 32))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'formOfPayment')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1103, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'creditCard')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1105, 36))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'debitCard')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1107, 36))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerIpAddress')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1109, 32))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_59._Automaton = _BuildAutomaton_61()




CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ticketableFareLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=CTD_ANON_60, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1157, 32)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ticketableFareLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1157, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_60._Automaton = _BuildAutomaton_62()




CTD_ANON_61._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'order'), CTD_ANON_62, scope=CTD_ANON_61, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1173, 32)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_61._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'order')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1173, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_61._Automaton = _BuildAutomaton_63()




CTD_ANON_62._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cancellationSummary'), _ImportedBinding_silvercom.CancellationSummaryType, scope=CTD_ANON_62, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1176, 44)))

def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_62._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cancellationSummary')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1176, 44))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_62._Automaton = _BuildAutomaton_64()




AddPaymentResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=AddPaymentResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 131, 20)))

AddPaymentResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), _ImportedBinding_silvercom.BookingRecordType, scope=AddPaymentResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 133, 20)))

AddPaymentResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), BookingNotesType, scope=AddPaymentResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 134, 20)))

AddPaymentResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentToken'), pyxb.binding.datatypes.string, scope=AddPaymentResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 135, 20)))

def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 131, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 133, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 134, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 135, 20))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AddPaymentResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AddPaymentResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 131, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AddPaymentResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 133, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AddPaymentResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 134, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AddPaymentResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentToken')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 135, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AddPaymentResponseType._Automaton = _BuildAutomaton_65()




AuthenticatePayerResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'threeDeeSecureAuthenticatePayer'), CTD_ANON_5, scope=AuthenticatePayerResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 161, 20)))

def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 160, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AuthenticatePayerResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AuthenticatePayerResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'threeDeeSecureAuthenticatePayer')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 161, 20))
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
AuthenticatePayerResponseType._Automaton = _BuildAutomaton_66()




AuditableRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agentInformation'), CTD_ANON_6, scope=AuditableRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20)))

def _BuildAutomaton_67 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AuditableRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AuditableRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AuditableRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AuditableRequestType._Automaton = _BuildAutomaton_67()




CancelBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), _ImportedBinding_silvercom.BookingRecordType, scope=CancelBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 275, 20)))

CancelBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), BookingNotesType, scope=CancelBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 276, 20)))

CancelBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'refundStatus'), _ImportedBinding_silvercom.RequestStatusType, scope=CancelBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 277, 20)))

def _BuildAutomaton_68 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 275, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 276, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 277, 20))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 275, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 276, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refundStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 277, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CancelBookingRecordResponseType._Automaton = _BuildAutomaton_68()




ClaimValueDocumentResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueDocument'), _ImportedBinding_silvercom.ValueDocumentType, scope=ClaimValueDocumentResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 307, 20)))

ClaimValueDocumentResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), _ImportedBinding_silvercom.BookingRecordType, scope=ClaimValueDocumentResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 308, 20)))

ClaimValueDocumentResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), BookingNotesType, scope=ClaimValueDocumentResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 309, 20)))

def _BuildAutomaton_69 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 307, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 308, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 309, 20))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ClaimValueDocumentResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClaimValueDocumentResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueDocument')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 307, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ClaimValueDocumentResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 308, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ClaimValueDocumentResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 309, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ClaimValueDocumentResponseType._Automaton = _BuildAutomaton_69()




ConfirmBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), _ImportedBinding_silvercom.BookingRecordType, scope=ConfirmBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 346, 20)))

ConfirmBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), BookingNotesType, scope=ConfirmBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 347, 20)))

ConfirmBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'claimValueDocumentResult'), ClaimValueDocumentResultType, scope=ConfirmBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 348, 20)))

def _BuildAutomaton_70 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 346, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 347, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 348, 20))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConfirmBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ConfirmBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 346, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ConfirmBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 347, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ConfirmBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'claimValueDocumentResult')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 348, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ConfirmBookingRecordResponseType._Automaton = _BuildAutomaton_70()




def _BuildAutomaton_71 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BookingTransactionFeeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'fee')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 2578, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BookingTransactionFeeType._Automaton = _BuildAutomaton_71()




CreateBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=CreateBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 476, 20)))

CreateBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastHoldDateTime'), pyxb.binding.datatypes.dateTime, scope=CreateBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 478, 20)))

CreateBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), _ImportedBinding_silvercom.BookingRecordType, scope=CreateBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 479, 20)))

CreateBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), BookingNotesType, scope=CreateBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 480, 20)))

def _BuildAutomaton_72 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 476, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 478, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 479, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 480, 20))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 476, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastHoldDateTime')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 478, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 479, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 480, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CreateBookingRecordResponseType._Automaton = _BuildAutomaton_72()




RetrieveBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), _ImportedBinding_silvercom.BookingRecordType, scope=RetrieveBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 568, 20)))

RetrieveBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), CTD_ANON_27, scope=RetrieveBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 569, 20)))

def _BuildAutomaton_73 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_73
    del _BuildAutomaton_73
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 568, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 569, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RetrieveBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RetrieveBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 568, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RetrieveBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 569, 20))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RetrieveBookingRecordResponseType._Automaton = _BuildAutomaton_73()




RedeliverValueDocumentResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'deliveryStatus'), CTD_ANON_29, scope=RedeliverValueDocumentResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 610, 20)))

RedeliverValueDocumentResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), _ImportedBinding_silvercom.BookingRecordType, scope=RedeliverValueDocumentResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 636, 20)))

def _BuildAutomaton_74 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 610, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 636, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RedeliverValueDocumentResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RedeliverValueDocumentResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deliveryStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 610, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RedeliverValueDocumentResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 636, 20))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RedeliverValueDocumentResponseType._Automaton = _BuildAutomaton_74()




CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coupons'), CTD_ANON_32, scope=CTD_ANON_63, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 654, 36)))

def _BuildAutomaton_75 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coupons')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 654, 36))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_63._Automaton = _BuildAutomaton_75()




CTD_ANON_64._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'couponReceivedDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_64, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 662, 68)))

CTD_ANON_64._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'origin'), _ImportedBinding_silvercom.TravelPointType, scope=CTD_ANON_64, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 664, 68)))

CTD_ANON_64._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'destination'), _ImportedBinding_silvercom.TravelPointType, scope=CTD_ANON_64, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 666, 68)))

def _BuildAutomaton_76 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76
    del _BuildAutomaton_76
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 637, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 664, 68))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 666, 68))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_64._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'couponNumber')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 637, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_64._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'couponReceivedDate')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 662, 68))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_64._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'origin')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 664, 68))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_64._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'destination')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 666, 68))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
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
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_64._Automaton = _BuildAutomaton_76()




CTD_ANON_65._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'refundApprovedDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_65, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 706, 50)))

CTD_ANON_65._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authorization'), CTD_ANON_35, scope=CTD_ANON_65, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 708, 50)))

def _BuildAutomaton_77 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_77
    del _BuildAutomaton_77
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 637, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_65._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'couponNumber')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 637, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_65._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refundApprovedDate')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 706, 50))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_65._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'authorization')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 708, 50))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_65._Automaton = _BuildAutomaton_77()




ReturnValueDocumentResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), _ImportedBinding_silvercom.BookingRecordType, scope=ReturnValueDocumentResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 764, 20)))

ReturnValueDocumentResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), BookingNotesType, scope=ReturnValueDocumentResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 765, 20)))

def _BuildAutomaton_78 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_78
    del _BuildAutomaton_78
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 764, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 765, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReturnValueDocumentResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReturnValueDocumentResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 764, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ReturnValueDocumentResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 765, 20))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReturnValueDocumentResponseType._Automaton = _BuildAutomaton_78()




SearchBookingRecordsRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'searchCriteria'), CTD_ANON_39, scope=SearchBookingRecordsRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 778, 20)))

def _BuildAutomaton_79 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_79
    del _BuildAutomaton_79
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SearchBookingRecordsRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SearchBookingRecordsRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SearchBookingRecordsRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'searchCriteria')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 778, 20))
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
SearchBookingRecordsRequestType._Automaton = _BuildAutomaton_79()




SearchBookingRecordsResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookingRecords'), CTD_ANON_40, scope=SearchBookingRecordsResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 799, 20)))

def _BuildAutomaton_80 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_80
    del _BuildAutomaton_80
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SearchBookingRecordsResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SearchBookingRecordsResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookingRecords')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 799, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SearchBookingRecordsResponseType._Automaton = _BuildAutomaton_80()




UpdateBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), _ImportedBinding_silvercom.BookingRecordType, scope=UpdateBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 903, 20)))

UpdateBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), BookingNotesType, scope=UpdateBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 904, 20)))

def _BuildAutomaton_81 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_81
    del _BuildAutomaton_81
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 903, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 904, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 903, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 904, 20))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UpdateBookingRecordResponseType._Automaton = _BuildAutomaton_81()




RecordFinancialTransactionResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), _ImportedBinding_silvercom.BookingRecordType, scope=RecordFinancialTransactionResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 951, 20)))

RecordFinancialTransactionResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), BookingNotesType, scope=RecordFinancialTransactionResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 952, 20)))

def _BuildAutomaton_82 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_82
    del _BuildAutomaton_82
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 951, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 952, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RecordFinancialTransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RecordFinancialTransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 951, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RecordFinancialTransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 952, 20))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RecordFinancialTransactionResponseType._Automaton = _BuildAutomaton_82()




RefundBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord'), _ImportedBinding_silvercom.BookingRecordType, scope=RefundBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 983, 20)))

RefundBookingRecordResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), BookingNotesType, scope=RefundBookingRecordResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 984, 20)))

def _BuildAutomaton_83 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_83
    del _BuildAutomaton_83
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 983, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 984, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RefundBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RefundBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookingRecord')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 983, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RefundBookingRecordResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 984, 20))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RefundBookingRecordResponseType._Automaton = _BuildAutomaton_83()




ValidateBookingRecordInformationResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookingRecordInformation'), CTD_ANON_53, scope=ValidateBookingRecordInformationResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1005, 20)))

def _BuildAutomaton_84 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_84
    del _BuildAutomaton_84
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1005, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookingRecordInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1005, 20))
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
ValidateBookingRecordInformationResponseType._Automaton = _BuildAutomaton_84()




GeneratePaymentTokenResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentToken'), pyxb.binding.datatypes.string, scope=GeneratePaymentTokenResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1122, 20)))

def _BuildAutomaton_85 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_85
    del _BuildAutomaton_85
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1122, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeneratePaymentTokenResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeneratePaymentTokenResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentToken')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1122, 20))
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
GeneratePaymentTokenResponseType._Automaton = _BuildAutomaton_85()




def _BuildAutomaton_86 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_86
    del _BuildAutomaton_86
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DeletePaymentTokenResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DeletePaymentTokenResponseType._Automaton = _BuildAutomaton_86()




RetrieveCancellationSummaryResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orders'), CTD_ANON_61, scope=RetrieveCancellationSummaryResponseType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1170, 20)))

def _BuildAutomaton_87 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_87
    del _BuildAutomaton_87
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1170, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RetrieveCancellationSummaryResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'requestStatus')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RetrieveCancellationSummaryResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orders')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1170, 20))
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
RetrieveCancellationSummaryResponseType._Automaton = _BuildAutomaton_87()




AddPaymentCreditCardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'validationNumber'), pyxb.binding.datatypes.string, scope=AddPaymentCreditCardType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 77, 20)))

def _BuildAutomaton_88 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_88
    del _BuildAutomaton_88
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 81, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 85, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 86, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentCreditCardType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'number')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 81, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentCreditCardType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'expirationYearMonth')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 82, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentCreditCardType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'cardholderName')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 83, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentCreditCardType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'billingAddress')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 84, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentCreditCardType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'siteCard')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 85, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentCreditCardType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'paymentToken')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 86, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AddPaymentCreditCardType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validationNumber')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 77, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AddPaymentCreditCardType._Automaton = _BuildAutomaton_88()




AddPaymentDebitCardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'issueNumber'), pyxb.binding.datatypes.string, scope=AddPaymentDebitCardType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 86, 20)))

AddPaymentDebitCardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'validationNumber'), pyxb.binding.datatypes.string, scope=AddPaymentDebitCardType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 87, 20)))

def _BuildAutomaton_89 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_89
    del _BuildAutomaton_89
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 104, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 105, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 109, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 86, 20))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentDebitCardType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'number')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 104, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentDebitCardType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'startYearMonth')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 105, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentDebitCardType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'expirationYearMonth')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 106, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentDebitCardType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'cardholderName')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 107, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentDebitCardType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'billingAddress')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 108, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentDebitCardType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'paymentToken')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 109, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentDebitCardType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'issueNumber')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 86, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AddPaymentDebitCardType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'validationNumber')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 87, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AddPaymentDebitCardType._Automaton = _BuildAutomaton_89()




BaseBookingRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), CTD_ANON_7, scope=BaseBookingRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20)))

BaseBookingRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderNotes'), CTD_ANON_8, scope=BaseBookingRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20)))

def _BuildAutomaton_90 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_90
    del _BuildAutomaton_90
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BaseBookingRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BaseBookingRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BaseBookingRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BaseBookingRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BaseBookingRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNotes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BaseBookingRequestType._Automaton = _BuildAutomaton_90()




RetrieveBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=RetrieveBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 520, 24)))

RetrieveBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supplyChannelRecordLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=RetrieveBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 521, 24)))

RetrieveBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueDocumentLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=RetrieveBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 523, 24)))

RetrieveBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orders'), CTD_ANON_24, scope=RetrieveBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 525, 20)))

RetrieveBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), CTD_ANON_26, scope=RetrieveBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 541, 20)))

def _BuildAutomaton_91 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_91
    del _BuildAutomaton_91
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 525, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 541, 20))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RetrieveBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RetrieveBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RetrieveBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RetrieveBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 520, 24))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RetrieveBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supplyChannelRecordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 521, 24))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RetrieveBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueDocumentLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 523, 24))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RetrieveBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orders')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 525, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RetrieveBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 541, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RetrieveBookingRecordRequestType._Automaton = _BuildAutomaton_91()




GeneratePaymentTokenRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'payment'), CTD_ANON_59, scope=GeneratePaymentTokenRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1100, 20)))

def _BuildAutomaton_92 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_92
    del _BuildAutomaton_92
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeneratePaymentTokenRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeneratePaymentTokenRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeneratePaymentTokenRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeneratePaymentTokenRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'payment')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1100, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GeneratePaymentTokenRequestType._Automaton = _BuildAutomaton_92()




DeletePaymentTokenRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paymentToken'), pyxb.binding.datatypes.string, scope=DeletePaymentTokenRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1133, 20)))

DeletePaymentTokenRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accountHolderFirstName'), pyxb.binding.datatypes.string, scope=DeletePaymentTokenRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1134, 20)))

DeletePaymentTokenRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accountHolderLastName'), pyxb.binding.datatypes.string, scope=DeletePaymentTokenRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1135, 20)))

def _BuildAutomaton_93 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_93
    del _BuildAutomaton_93
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DeletePaymentTokenRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DeletePaymentTokenRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DeletePaymentTokenRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DeletePaymentTokenRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paymentToken')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1133, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DeletePaymentTokenRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accountHolderFirstName')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1134, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DeletePaymentTokenRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accountHolderLastName')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1135, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DeletePaymentTokenRequestType._Automaton = _BuildAutomaton_93()




RetrieveCancellationSummaryRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=RetrieveCancellationSummaryRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1152, 20)))

RetrieveCancellationSummaryRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=RetrieveCancellationSummaryRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1153, 20)))

RetrieveCancellationSummaryRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ticketableFareLocators'), CTD_ANON_60, scope=RetrieveCancellationSummaryRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1154, 20)))

def _BuildAutomaton_94 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_94
    del _BuildAutomaton_94
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1153, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1154, 20))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RetrieveCancellationSummaryRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RetrieveCancellationSummaryRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RetrieveCancellationSummaryRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RetrieveCancellationSummaryRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1152, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RetrieveCancellationSummaryRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1153, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RetrieveCancellationSummaryRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ticketableFareLocators')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 1154, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RetrieveCancellationSummaryRequestType._Automaton = _BuildAutomaton_94()




AbstractPaymentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=AbstractPaymentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 51, 20)))

AbstractPaymentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'payment'), CTD_ANON, scope=AbstractPaymentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 52, 20)))

def _BuildAutomaton_95 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_95
    del _BuildAutomaton_95
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNotes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 51, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AbstractPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'payment')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 52, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AbstractPaymentRequestType._Automaton = _BuildAutomaton_95()




CancelBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=CancelBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 224, 20)))

CancelBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=CancelBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 225, 20)))

CancelBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ticketableFareLocators'), CTD_ANON_9, scope=CancelBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 226, 20)))

CancelBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'expectedCancellationFee'), _ImportedBinding_silvercom.MoneyType, scope=CancelBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 233, 20)))

CancelBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameters'), CTD_ANON_10, scope=CancelBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 234, 20)))

CancelBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), CTD_ANON_11, scope=CancelBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 242, 20)))

CancelBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cancellationReason'), _ImportedBinding_silvercom.CancellationReasonType, scope=CancelBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 250, 20)))

CancelBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'refundInformation'), RefundInformationType, scope=CancelBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 252, 20)))

CancelBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'selectedCancellationOption'), _ImportedBinding_silvercom.SelectedCancellationOptionType, scope=CancelBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 254, 20)))

def _BuildAutomaton_96 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_96
    del _BuildAutomaton_96
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 225, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 226, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 234, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 242, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 250, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 252, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 254, 20))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNotes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 224, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 225, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ticketableFareLocators')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 226, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'expectedCancellationFee')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 233, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameters')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 234, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 242, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cancellationReason')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 250, 20))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refundInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 252, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CancelBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'selectedCancellationOption')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 254, 20))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CancelBookingRecordRequestType._Automaton = _BuildAutomaton_96()




ClaimValueDocumentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=ClaimValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 287, 20)))

ClaimValueDocumentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=ClaimValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 288, 20)))

ClaimValueDocumentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), CTD_ANON_12, scope=ClaimValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 290, 20)))

def _BuildAutomaton_97 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_97
    del _BuildAutomaton_97
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 288, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 290, 20))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ClaimValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ClaimValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ClaimValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ClaimValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ClaimValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNotes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ClaimValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 287, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ClaimValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 288, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ClaimValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 290, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ClaimValueDocumentRequestType._Automaton = _BuildAutomaton_97()




ConfirmBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=ConfirmBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 321, 20)))

ConfirmBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderLocator'), _ImportedBinding_silvercom.AnorakReceiptLocatorType, scope=ConfirmBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 322, 20)))

ConfirmBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'confirmationInformation'), ConfirmationInformationType, scope=ConfirmBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 324, 20)))

ConfirmBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fulfillmentInformation'), FulfillmentInformationType, scope=ConfirmBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 326, 20)))

ConfirmBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), CTD_ANON_13, scope=ConfirmBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 328, 20)))

ConfirmBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'returnClaimValueDocument'), pyxb.binding.datatypes.boolean, scope=ConfirmBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 336, 20)))

def _BuildAutomaton_98 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_98
    del _BuildAutomaton_98
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 322, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 324, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 326, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 328, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 336, 20))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConfirmBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConfirmBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConfirmBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConfirmBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConfirmBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNotes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConfirmBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 321, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ConfirmBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 322, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ConfirmBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'confirmationInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 324, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ConfirmBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fulfillmentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 326, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(ConfirmBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 328, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(ConfirmBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'returnClaimValueDocument')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 336, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
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
ConfirmBookingRecordRequestType._Automaton = _BuildAutomaton_98()




CreateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passengers'), CTD_ANON_16, scope=CreateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 404, 20)))

CreateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legSolutions'), _ImportedBinding_silvercom.LegSolutionsType, scope=CreateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 412, 20)))

CreateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'prices'), CTD_ANON_17, scope=CreateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 413, 20)))

CreateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'travelPassQuery'), TravelPassQuery, scope=CreateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 421, 20)))

CreateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionFees'), CTD_ANON_18, scope=CreateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 422, 20)))

CreateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameters'), CTD_ANON_19, scope=CreateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 430, 20)))

CreateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), CTD_ANON_21, scope=CreateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 450, 20)))

CreateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'externalIdentification'), _ImportedBinding_silvercom.ExternalIdentificationType, scope=CreateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 458, 20)))

CreateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fareQualifiers'), CTD_ANON_22, scope=CreateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 460, 20)))

def _BuildAutomaton_99 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_99
    del _BuildAutomaton_99
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 412, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 413, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 421, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 422, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 430, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 450, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 458, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 460, 20))
    counters.add(cc_11)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNotes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passengers')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 404, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legSolutions')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 412, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prices')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 413, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'travelPassQuery')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 421, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionFees')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 422, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameters')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 430, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 450, 20))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'externalIdentification')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 458, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CreateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fareQualifiers')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 460, 20))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
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
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
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
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
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
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CreateBookingRecordRequestType._Automaton = _BuildAutomaton_99()




RedeliverValueDocumentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=RedeliverValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 586, 20)))

RedeliverValueDocumentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=RedeliverValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 587, 20)))

RedeliverValueDocumentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'emailAddress'), pyxb.binding.datatypes.string, scope=RedeliverValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 589, 24)))

RedeliverValueDocumentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'phoneNumber'), _ImportedBinding_silvercom.FulfillmentPhoneNumberType, scope=RedeliverValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 590, 24)))

RedeliverValueDocumentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'language'), pyxb.binding.datatypes.string, scope=RedeliverValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 592, 20)))

RedeliverValueDocumentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), CTD_ANON_28, scope=RedeliverValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 593, 20)))

def _BuildAutomaton_100 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_100
    del _BuildAutomaton_100
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 587, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 588, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 592, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 593, 20))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RedeliverValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RedeliverValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RedeliverValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RedeliverValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RedeliverValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNotes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RedeliverValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 586, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RedeliverValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 587, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RedeliverValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'emailAddress')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 589, 24))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RedeliverValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'phoneNumber')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 590, 24))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(RedeliverValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'language')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 592, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(RedeliverValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 593, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
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
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RedeliverValueDocumentRequestType._Automaton = _BuildAutomaton_100()




ReturnValueDocumentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=ReturnValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 646, 20)))

ReturnValueDocumentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=ReturnValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 647, 20)))

ReturnValueDocumentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueDocumentLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=ReturnValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 649, 20)))

ReturnValueDocumentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'receiveCoupons'), CTD_ANON_63, scope=ReturnValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 651, 24)))

ReturnValueDocumentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authorizeRefund'), CTD_ANON_33, scope=ReturnValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 695, 24)))

ReturnValueDocumentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), CTD_ANON_38, scope=ReturnValueDocumentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 747, 20)))

def _BuildAutomaton_101 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_101
    del _BuildAutomaton_101
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 647, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 747, 20))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReturnValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReturnValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReturnValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReturnValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReturnValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNotes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReturnValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 646, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReturnValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 647, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReturnValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueDocumentLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 649, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReturnValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'receiveCoupons')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 651, 24))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReturnValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'authorizeRefund')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 695, 24))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ReturnValueDocumentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 747, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReturnValueDocumentRequestType._Automaton = _BuildAutomaton_101()




UpdateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=UpdateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 816, 20)))

UpdateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderLocator'), _ImportedBinding_silvercom.AnorakReceiptLocatorType, scope=UpdateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 817, 20)))

UpdateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serviceFees'), _ImportedBinding_silvercom.FeesType, scope=UpdateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 819, 20)))

UpdateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fulfillmentInformation'), FulfillmentInformationType, scope=UpdateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 821, 24)))

UpdateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'removeSelectedTicketingOption'), CTD_ANON_41, scope=UpdateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 823, 24)))

UpdateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customInformation'), _ImportedBinding_silvercom.CustomInformationType, scope=UpdateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 827, 20)))

UpdateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shipmentTracking'), _ImportedBinding_silvercom.ShipmentTrackingType, scope=UpdateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 829, 20)))

UpdateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'order'), CTD_ANON_42, scope=UpdateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 831, 20)))

UpdateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passengers'), CTD_ANON_47, scope=UpdateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 876, 20)))

UpdateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), CTD_ANON_48, scope=UpdateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 884, 20)))

UpdateBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'externalIdentification'), _ImportedBinding_silvercom.ExternalIdentificationType, scope=UpdateBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 892, 20)))

def _BuildAutomaton_102 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_102
    del _BuildAutomaton_102
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 817, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 819, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 821, 24))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 823, 24))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 827, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 829, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 831, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 876, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 884, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 892, 20))
    counters.add(cc_13)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNotes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 816, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 817, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serviceFees')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 819, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fulfillmentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 821, 24))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'removeSelectedTicketingOption')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 823, 24))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 827, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shipmentTracking')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 829, 20))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'order')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 831, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passengers')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 876, 20))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 884, 20))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(UpdateBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'externalIdentification')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 892, 20))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
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
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
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
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
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
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UpdateBookingRecordRequestType._Automaton = _BuildAutomaton_102()




RecordFinancialTransactionRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=RecordFinancialTransactionRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 914, 20)))

RecordFinancialTransactionRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'refunds'), CTD_ANON_49, scope=RecordFinancialTransactionRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 915, 20)))

RecordFinancialTransactionRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), CTD_ANON_51, scope=RecordFinancialTransactionRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 934, 20)))

def _BuildAutomaton_103 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_103
    del _BuildAutomaton_103
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 915, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 934, 20))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RecordFinancialTransactionRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RecordFinancialTransactionRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RecordFinancialTransactionRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RecordFinancialTransactionRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RecordFinancialTransactionRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNotes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RecordFinancialTransactionRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 914, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RecordFinancialTransactionRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refunds')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 915, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RecordFinancialTransactionRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 934, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RecordFinancialTransactionRequestType._Automaton = _BuildAutomaton_103()




RefundBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recordLocator'), _ImportedBinding_silvercom.AnorakRecordLocatorType, scope=RefundBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 962, 20)))

RefundBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), CTD_ANON_52, scope=RefundBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 963, 20)))

RefundBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'receiptNumber'), _ImportedBinding_silvercom.AnorakReceiptLocatorType, scope=RefundBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 971, 20)))

RefundBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'refundAmount'), _ImportedBinding_silvercom.MoneyType, scope=RefundBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 972, 20)))

RefundBookingRecordRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'refundReason'), pyxb.binding.datatypes.string, scope=RefundBookingRecordRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 973, 20)))

def _BuildAutomaton_104 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_104
    del _BuildAutomaton_104
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 963, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 973, 20))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefundBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefundBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefundBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefundBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefundBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNotes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefundBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 962, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefundBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 963, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefundBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'receiptNumber')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 971, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RefundBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refundAmount')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 972, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RefundBookingRecordRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refundReason')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 973, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RefundBookingRecordRequestType._Automaton = _BuildAutomaton_104()




AddPaymentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameters'), CTD_ANON_, scope=AddPaymentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 96, 20)))

AddPaymentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'confirmationInformation'), ConfirmationInformationType, scope=AddPaymentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 103, 20)))

AddPaymentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fulfillmentInformation'), FulfillmentInformationType, scope=AddPaymentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 105, 20)))

AddPaymentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), CTD_ANON_2, scope=AddPaymentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 107, 20)))

AddPaymentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerIpAddress'), pyxb.binding.datatypes.string, scope=AddPaymentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 115, 20)))

AddPaymentRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'threeDeeAuthenticatePayer'), CTD_ANON_3, scope=AddPaymentRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 116, 20)))

def _BuildAutomaton_105 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_105
    del _BuildAutomaton_105
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 96, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 103, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 105, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 107, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 115, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 116, 20))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNotes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 51, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AddPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'payment')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 52, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AddPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameters')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 96, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AddPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'confirmationInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 103, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AddPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fulfillmentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 105, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AddPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 107, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(AddPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerIpAddress')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 115, 20))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(AddPaymentRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'threeDeeAuthenticatePayer')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 116, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AddPaymentRequestType._Automaton = _BuildAutomaton_105()




AuthenticatePayerRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerIpAddress'), pyxb.binding.datatypes.string, scope=AuthenticatePayerRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 144, 20)))

AuthenticatePayerRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseSpec'), CTD_ANON_4, scope=AuthenticatePayerRequestType, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 145, 20)))

def _BuildAutomaton_106 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_106
    del _BuildAutomaton_106
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 144, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 145, 20))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AuthenticatePayerRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AuthenticatePayerRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AuthenticatePayerRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AuthenticatePayerRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AuthenticatePayerRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNotes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AuthenticatePayerRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recordLocator')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 51, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AuthenticatePayerRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'payment')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 52, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AuthenticatePayerRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerIpAddress')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 144, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AuthenticatePayerRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 145, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AuthenticatePayerRequestType._Automaton = _BuildAutomaton_106()




def _BuildAutomaton_107 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_107
    del _BuildAutomaton_107
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 412, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 413, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 421, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 422, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 430, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 450, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 458, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 460, 20))
    counters.add(cc_11)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'context')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationRequestType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_com, 'overrides')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/CommonTypes_2_65.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentInformation')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 199, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderNotes')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 207, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passengers')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 404, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legSolutions')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 412, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prices')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 413, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'travelPassQuery')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 421, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionFees')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 422, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameters')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 430, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseSpec')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 450, 20))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'externalIdentification')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 458, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(ValidateBookingRecordInformationRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fareQualifiers')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/BookingServicesSchema_2_65.xsd', 460, 20))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
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
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
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
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
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
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ValidateBookingRecordInformationRequestType._Automaton = _BuildAutomaton_107()

