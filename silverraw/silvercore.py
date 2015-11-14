# ./silvercore.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:124ab58ff634848548cf6d9d1320f856ff23519e
# Generated 2015-11-14 16:58:02.798568 by PyXB version 1.2.4 using Python 2.7.9.final.0
# Namespace http://schemas.xmlsoap.org/soap/envelope/

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
import silvershop as _ImportedBinding_silvershop
import pyxb.binding.datatypes
import silverbook as _ImportedBinding_silverbook

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://schemas.xmlsoap.org/soap/envelope/', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

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
class STD_ANON (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 87, 4)
    _Documentation = None
STD_ANON._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON._CF_pattern.addPattern(pattern='0|1')
STD_ANON._InitializeFacetMap(STD_ANON._CF_pattern)

# List simple type: {http://schemas.xmlsoap.org/soap/envelope/}encodingStyle
# superclasses pyxb.binding.datatypes.anySimpleType
class encodingStyle (pyxb.binding.basis.STD_list):

    """
            'encodingStyle' indicates any canonicalization conventions followed in the contents of the containing element. For example, the value 'http://schemas.xmlsoap.org/soap/encoding/' indicates the pattern described in SOAP specification
        """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'encodingStyle')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 94, 0)
    _Documentation = "\n            'encodingStyle' indicates any canonicalization conventions followed in the contents of the containing element. For example, the value 'http://schemas.xmlsoap.org/soap/encoding/' indicates the pattern described in SOAP specification\n        "

    _ItemType = pyxb.binding.datatypes.anyURI
encodingStyle._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'encodingStyle', encodingStyle)

# Complex type {http://schemas.xmlsoap.org/soap/envelope/}Envelope with content type ELEMENT_ONLY
class Envelope_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.xmlsoap.org/soap/envelope/}Envelope with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Envelope')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 15, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.xmlsoap.org/soap/envelope/}Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Header'), 'Header', '__httpschemas_xmlsoap_orgsoapenvelope_Envelope__httpschemas_xmlsoap_orgsoapenvelopeHeader', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 23, 4), )

    
    Header = property(__Header.value, __Header.set, None, None)

    
    # Element {http://schemas.xmlsoap.org/soap/envelope/}Body uses Python identifier Body
    __Body = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Body'), 'Body', '__httpschemas_xmlsoap_orgsoapenvelope_Envelope__httpschemas_xmlsoap_orgsoapenvelopeBody', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 30, 4), )

    
    Body = property(__Body.value, __Body.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://schemas.xmlsoap.org/soap/envelope/'))
    _HasWildcardElement = True
    _ElementMap.update({
        __Header.name() : __Header,
        __Body.name() : __Body
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Envelope', Envelope_)


# Complex type {http://schemas.xmlsoap.org/soap/envelope/}Header with content type ELEMENT_ONLY
class Header_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.xmlsoap.org/soap/envelope/}Header with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Header')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 24, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://schemas.xmlsoap.org/soap/envelope/'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Header', Header_)


# Complex type {http://schemas.xmlsoap.org/soap/envelope/}Body with content type ELEMENT_ONLY
class Body_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.xmlsoap.org/soap/envelope/}Body with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Body')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 31, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element pointToPointShoppingRequest uses Python identifier pointToPointShoppingRequest
    __pointToPointShoppingRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pointToPointShoppingRequest'), 'pointToPointShoppingRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__pointToPointShoppingRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 33, 12), )

    
    pointToPointShoppingRequest = property(__pointToPointShoppingRequest.value, __pointToPointShoppingRequest.set, None, None)

    
    # Element pointToPointShoppingResponse uses Python identifier pointToPointShoppingResponse
    __pointToPointShoppingResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pointToPointShoppingResponse'), 'pointToPointShoppingResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__pointToPointShoppingResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 34, 12), )

    
    pointToPointShoppingResponse = property(__pointToPointShoppingResponse.value, __pointToPointShoppingResponse.set, None, None)

    
    # Element travelPassShoppingRequest uses Python identifier travelPassShoppingRequest
    __travelPassShoppingRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'travelPassShoppingRequest'), 'travelPassShoppingRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__travelPassShoppingRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 35, 12), )

    
    travelPassShoppingRequest = property(__travelPassShoppingRequest.value, __travelPassShoppingRequest.set, None, None)

    
    # Element travelPassShoppingResponse uses Python identifier travelPassShoppingResponse
    __travelPassShoppingResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'travelPassShoppingResponse'), 'travelPassShoppingResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__travelPassShoppingResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 36, 12), )

    
    travelPassShoppingResponse = property(__travelPassShoppingResponse.value, __travelPassShoppingResponse.set, None, None)

    
    # Element scheduleSearchRequest uses Python identifier scheduleSearchRequest
    __scheduleSearchRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'scheduleSearchRequest'), 'scheduleSearchRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__scheduleSearchRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 37, 12), )

    
    scheduleSearchRequest = property(__scheduleSearchRequest.value, __scheduleSearchRequest.set, None, None)

    
    # Element scheduleSearchResponse uses Python identifier scheduleSearchResponse
    __scheduleSearchResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'scheduleSearchResponse'), 'scheduleSearchResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__scheduleSearchResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 38, 12), )

    
    scheduleSearchResponse = property(__scheduleSearchResponse.value, __scheduleSearchResponse.set, None, None)

    
    # Element addPaymentRequest uses Python identifier addPaymentRequest
    __addPaymentRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'addPaymentRequest'), 'addPaymentRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__addPaymentRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 39, 12), )

    
    addPaymentRequest = property(__addPaymentRequest.value, __addPaymentRequest.set, None, None)

    
    # Element addPaymentResponse uses Python identifier addPaymentResponse
    __addPaymentResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'addPaymentResponse'), 'addPaymentResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__addPaymentResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 40, 12), )

    
    addPaymentResponse = property(__addPaymentResponse.value, __addPaymentResponse.set, None, None)

    
    # Element authenticatePayerRequest uses Python identifier authenticatePayerRequest
    __authenticatePayerRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'authenticatePayerRequest'), 'authenticatePayerRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__authenticatePayerRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 41, 12), )

    
    authenticatePayerRequest = property(__authenticatePayerRequest.value, __authenticatePayerRequest.set, None, None)

    
    # Element authenticatePayerResponse uses Python identifier authenticatePayerResponse
    __authenticatePayerResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'authenticatePayerResponse'), 'authenticatePayerResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__authenticatePayerResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 42, 12), )

    
    authenticatePayerResponse = property(__authenticatePayerResponse.value, __authenticatePayerResponse.set, None, None)

    
    # Element cancelBookingRecordRequest uses Python identifier cancelBookingRecordRequest
    __cancelBookingRecordRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cancelBookingRecordRequest'), 'cancelBookingRecordRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__cancelBookingRecordRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 43, 12), )

    
    cancelBookingRecordRequest = property(__cancelBookingRecordRequest.value, __cancelBookingRecordRequest.set, None, None)

    
    # Element cancelBookingRecordResponse uses Python identifier cancelBookingRecordResponse
    __cancelBookingRecordResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cancelBookingRecordResponse'), 'cancelBookingRecordResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__cancelBookingRecordResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 44, 12), )

    
    cancelBookingRecordResponse = property(__cancelBookingRecordResponse.value, __cancelBookingRecordResponse.set, None, None)

    
    # Element claimValueDocumentRequest uses Python identifier claimValueDocumentRequest
    __claimValueDocumentRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'claimValueDocumentRequest'), 'claimValueDocumentRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__claimValueDocumentRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 45, 12), )

    
    claimValueDocumentRequest = property(__claimValueDocumentRequest.value, __claimValueDocumentRequest.set, None, None)

    
    # Element claimValueDocumentResponse uses Python identifier claimValueDocumentResponse
    __claimValueDocumentResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'claimValueDocumentResponse'), 'claimValueDocumentResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__claimValueDocumentResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 46, 12), )

    
    claimValueDocumentResponse = property(__claimValueDocumentResponse.value, __claimValueDocumentResponse.set, None, None)

    
    # Element confirmBookingRecordRequest uses Python identifier confirmBookingRecordRequest
    __confirmBookingRecordRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'confirmBookingRecordRequest'), 'confirmBookingRecordRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__confirmBookingRecordRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 47, 12), )

    
    confirmBookingRecordRequest = property(__confirmBookingRecordRequest.value, __confirmBookingRecordRequest.set, None, None)

    
    # Element confirmBookingRecordResponse uses Python identifier confirmBookingRecordResponse
    __confirmBookingRecordResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'confirmBookingRecordResponse'), 'confirmBookingRecordResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__confirmBookingRecordResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 48, 12), )

    
    confirmBookingRecordResponse = property(__confirmBookingRecordResponse.value, __confirmBookingRecordResponse.set, None, None)

    
    # Element createBookingRecordRequest uses Python identifier createBookingRecordRequest
    __createBookingRecordRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'createBookingRecordRequest'), 'createBookingRecordRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__createBookingRecordRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 49, 12), )

    
    createBookingRecordRequest = property(__createBookingRecordRequest.value, __createBookingRecordRequest.set, None, None)

    
    # Element createBookingRecordResponse uses Python identifier createBookingRecordResponse
    __createBookingRecordResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'createBookingRecordResponse'), 'createBookingRecordResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__createBookingRecordResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 50, 12), )

    
    createBookingRecordResponse = property(__createBookingRecordResponse.value, __createBookingRecordResponse.set, None, None)

    
    # Element recordFinancialTransactionRequest uses Python identifier recordFinancialTransactionRequest
    __recordFinancialTransactionRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'recordFinancialTransactionRequest'), 'recordFinancialTransactionRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__recordFinancialTransactionRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 51, 12), )

    
    recordFinancialTransactionRequest = property(__recordFinancialTransactionRequest.value, __recordFinancialTransactionRequest.set, None, None)

    
    # Element recordFinancialTransactionResponse uses Python identifier recordFinancialTransactionResponse
    __recordFinancialTransactionResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'recordFinancialTransactionResponse'), 'recordFinancialTransactionResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__recordFinancialTransactionResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 52, 12), )

    
    recordFinancialTransactionResponse = property(__recordFinancialTransactionResponse.value, __recordFinancialTransactionResponse.set, None, None)

    
    # Element redeliverValueDocumentRequest uses Python identifier redeliverValueDocumentRequest
    __redeliverValueDocumentRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'redeliverValueDocumentRequest'), 'redeliverValueDocumentRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__redeliverValueDocumentRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 53, 12), )

    
    redeliverValueDocumentRequest = property(__redeliverValueDocumentRequest.value, __redeliverValueDocumentRequest.set, None, None)

    
    # Element redeliverValueDocumentResponse uses Python identifier redeliverValueDocumentResponse
    __redeliverValueDocumentResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'redeliverValueDocumentResponse'), 'redeliverValueDocumentResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__redeliverValueDocumentResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 54, 12), )

    
    redeliverValueDocumentResponse = property(__redeliverValueDocumentResponse.value, __redeliverValueDocumentResponse.set, None, None)

    
    # Element retrieveBookingRecordRequest uses Python identifier retrieveBookingRecordRequest
    __retrieveBookingRecordRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'retrieveBookingRecordRequest'), 'retrieveBookingRecordRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__retrieveBookingRecordRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 55, 12), )

    
    retrieveBookingRecordRequest = property(__retrieveBookingRecordRequest.value, __retrieveBookingRecordRequest.set, None, None)

    
    # Element retrieveBookingRecordResponse uses Python identifier retrieveBookingRecordResponse
    __retrieveBookingRecordResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'retrieveBookingRecordResponse'), 'retrieveBookingRecordResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__retrieveBookingRecordResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 56, 12), )

    
    retrieveBookingRecordResponse = property(__retrieveBookingRecordResponse.value, __retrieveBookingRecordResponse.set, None, None)

    
    # Element returnValueDocumentRequest uses Python identifier returnValueDocumentRequest
    __returnValueDocumentRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'returnValueDocumentRequest'), 'returnValueDocumentRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__returnValueDocumentRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 57, 12), )

    
    returnValueDocumentRequest = property(__returnValueDocumentRequest.value, __returnValueDocumentRequest.set, None, None)

    
    # Element returnValueDocumentResponse uses Python identifier returnValueDocumentResponse
    __returnValueDocumentResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'returnValueDocumentResponse'), 'returnValueDocumentResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__returnValueDocumentResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 58, 12), )

    
    returnValueDocumentResponse = property(__returnValueDocumentResponse.value, __returnValueDocumentResponse.set, None, None)

    
    # Element searchBookingRecordsRequest uses Python identifier searchBookingRecordsRequest
    __searchBookingRecordsRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'searchBookingRecordsRequest'), 'searchBookingRecordsRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__searchBookingRecordsRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 59, 12), )

    
    searchBookingRecordsRequest = property(__searchBookingRecordsRequest.value, __searchBookingRecordsRequest.set, None, None)

    
    # Element searchBookingRecordsResponse uses Python identifier searchBookingRecordsResponse
    __searchBookingRecordsResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'searchBookingRecordsResponse'), 'searchBookingRecordsResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__searchBookingRecordsResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 60, 12), )

    
    searchBookingRecordsResponse = property(__searchBookingRecordsResponse.value, __searchBookingRecordsResponse.set, None, None)

    
    # Element updateBookingRecordRequest uses Python identifier updateBookingRecordRequest
    __updateBookingRecordRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'updateBookingRecordRequest'), 'updateBookingRecordRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__updateBookingRecordRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 61, 12), )

    
    updateBookingRecordRequest = property(__updateBookingRecordRequest.value, __updateBookingRecordRequest.set, None, None)

    
    # Element updateBookingRecordResponse uses Python identifier updateBookingRecordResponse
    __updateBookingRecordResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'updateBookingRecordResponse'), 'updateBookingRecordResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__updateBookingRecordResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 62, 12), )

    
    updateBookingRecordResponse = property(__updateBookingRecordResponse.value, __updateBookingRecordResponse.set, None, None)

    
    # Element refundBookingRecordRequest uses Python identifier refundBookingRecordRequest
    __refundBookingRecordRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'refundBookingRecordRequest'), 'refundBookingRecordRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__refundBookingRecordRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 63, 12), )

    
    refundBookingRecordRequest = property(__refundBookingRecordRequest.value, __refundBookingRecordRequest.set, None, None)

    
    # Element refundBookingRecordResponse uses Python identifier refundBookingRecordResponse
    __refundBookingRecordResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'refundBookingRecordResponse'), 'refundBookingRecordResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__refundBookingRecordResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 64, 12), )

    
    refundBookingRecordResponse = property(__refundBookingRecordResponse.value, __refundBookingRecordResponse.set, None, None)

    
    # Element validateBookingRecordInformationRequest uses Python identifier validateBookingRecordInformationRequest
    __validateBookingRecordInformationRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'validateBookingRecordInformationRequest'), 'validateBookingRecordInformationRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__validateBookingRecordInformationRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 65, 12), )

    
    validateBookingRecordInformationRequest = property(__validateBookingRecordInformationRequest.value, __validateBookingRecordInformationRequest.set, None, None)

    
    # Element validateBookingRecordInformationResponse uses Python identifier validateBookingRecordInformationResponse
    __validateBookingRecordInformationResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'validateBookingRecordInformationResponse'), 'validateBookingRecordInformationResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__validateBookingRecordInformationResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 66, 12), )

    
    validateBookingRecordInformationResponse = property(__validateBookingRecordInformationResponse.value, __validateBookingRecordInformationResponse.set, None, None)

    
    # Element generatePaymentTokenRequest uses Python identifier generatePaymentTokenRequest
    __generatePaymentTokenRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'generatePaymentTokenRequest'), 'generatePaymentTokenRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__generatePaymentTokenRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 67, 12), )

    
    generatePaymentTokenRequest = property(__generatePaymentTokenRequest.value, __generatePaymentTokenRequest.set, None, None)

    
    # Element generatePaymentTokenResponse uses Python identifier generatePaymentTokenResponse
    __generatePaymentTokenResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'generatePaymentTokenResponse'), 'generatePaymentTokenResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__generatePaymentTokenResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 68, 12), )

    
    generatePaymentTokenResponse = property(__generatePaymentTokenResponse.value, __generatePaymentTokenResponse.set, None, None)

    
    # Element deletePaymentTokenRequest uses Python identifier deletePaymentTokenRequest
    __deletePaymentTokenRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'deletePaymentTokenRequest'), 'deletePaymentTokenRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__deletePaymentTokenRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 69, 12), )

    
    deletePaymentTokenRequest = property(__deletePaymentTokenRequest.value, __deletePaymentTokenRequest.set, None, None)

    
    # Element deletePaymentTokenResponse uses Python identifier deletePaymentTokenResponse
    __deletePaymentTokenResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'deletePaymentTokenResponse'), 'deletePaymentTokenResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__deletePaymentTokenResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 70, 12), )

    
    deletePaymentTokenResponse = property(__deletePaymentTokenResponse.value, __deletePaymentTokenResponse.set, None, None)

    
    # Element retrieveCancellationSummaryRequest uses Python identifier retrieveCancellationSummaryRequest
    __retrieveCancellationSummaryRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'retrieveCancellationSummaryRequest'), 'retrieveCancellationSummaryRequest', '__httpschemas_xmlsoap_orgsoapenvelope_Body__retrieveCancellationSummaryRequest', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 71, 12), )

    
    retrieveCancellationSummaryRequest = property(__retrieveCancellationSummaryRequest.value, __retrieveCancellationSummaryRequest.set, None, None)

    
    # Element retrieveCancellationSummaryResponse uses Python identifier retrieveCancellationSummaryResponse
    __retrieveCancellationSummaryResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'retrieveCancellationSummaryResponse'), 'retrieveCancellationSummaryResponse', '__httpschemas_xmlsoap_orgsoapenvelope_Body__retrieveCancellationSummaryResponse', True, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 72, 12), )

    
    retrieveCancellationSummaryResponse = property(__retrieveCancellationSummaryResponse.value, __retrieveCancellationSummaryResponse.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        __pointToPointShoppingRequest.name() : __pointToPointShoppingRequest,
        __pointToPointShoppingResponse.name() : __pointToPointShoppingResponse,
        __travelPassShoppingRequest.name() : __travelPassShoppingRequest,
        __travelPassShoppingResponse.name() : __travelPassShoppingResponse,
        __scheduleSearchRequest.name() : __scheduleSearchRequest,
        __scheduleSearchResponse.name() : __scheduleSearchResponse,
        __addPaymentRequest.name() : __addPaymentRequest,
        __addPaymentResponse.name() : __addPaymentResponse,
        __authenticatePayerRequest.name() : __authenticatePayerRequest,
        __authenticatePayerResponse.name() : __authenticatePayerResponse,
        __cancelBookingRecordRequest.name() : __cancelBookingRecordRequest,
        __cancelBookingRecordResponse.name() : __cancelBookingRecordResponse,
        __claimValueDocumentRequest.name() : __claimValueDocumentRequest,
        __claimValueDocumentResponse.name() : __claimValueDocumentResponse,
        __confirmBookingRecordRequest.name() : __confirmBookingRecordRequest,
        __confirmBookingRecordResponse.name() : __confirmBookingRecordResponse,
        __createBookingRecordRequest.name() : __createBookingRecordRequest,
        __createBookingRecordResponse.name() : __createBookingRecordResponse,
        __recordFinancialTransactionRequest.name() : __recordFinancialTransactionRequest,
        __recordFinancialTransactionResponse.name() : __recordFinancialTransactionResponse,
        __redeliverValueDocumentRequest.name() : __redeliverValueDocumentRequest,
        __redeliverValueDocumentResponse.name() : __redeliverValueDocumentResponse,
        __retrieveBookingRecordRequest.name() : __retrieveBookingRecordRequest,
        __retrieveBookingRecordResponse.name() : __retrieveBookingRecordResponse,
        __returnValueDocumentRequest.name() : __returnValueDocumentRequest,
        __returnValueDocumentResponse.name() : __returnValueDocumentResponse,
        __searchBookingRecordsRequest.name() : __searchBookingRecordsRequest,
        __searchBookingRecordsResponse.name() : __searchBookingRecordsResponse,
        __updateBookingRecordRequest.name() : __updateBookingRecordRequest,
        __updateBookingRecordResponse.name() : __updateBookingRecordResponse,
        __refundBookingRecordRequest.name() : __refundBookingRecordRequest,
        __refundBookingRecordResponse.name() : __refundBookingRecordResponse,
        __validateBookingRecordInformationRequest.name() : __validateBookingRecordInformationRequest,
        __validateBookingRecordInformationResponse.name() : __validateBookingRecordInformationResponse,
        __generatePaymentTokenRequest.name() : __generatePaymentTokenRequest,
        __generatePaymentTokenResponse.name() : __generatePaymentTokenResponse,
        __deletePaymentTokenRequest.name() : __deletePaymentTokenRequest,
        __deletePaymentTokenResponse.name() : __deletePaymentTokenResponse,
        __retrieveCancellationSummaryRequest.name() : __retrieveCancellationSummaryRequest,
        __retrieveCancellationSummaryResponse.name() : __retrieveCancellationSummaryResponse
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Body', Body_)


# Complex type {http://schemas.xmlsoap.org/soap/envelope/}Fault with content type ELEMENT_ONLY
class Fault_ (pyxb.binding.basis.complexTypeDefinition):
    """Fault reporting structure"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Fault')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 107, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element faultcode uses Python identifier faultcode
    __faultcode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'faultcode'), 'faultcode', '__httpschemas_xmlsoap_orgsoapenvelope_Fault__faultcode', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 112, 8), )

    
    faultcode = property(__faultcode.value, __faultcode.set, None, None)

    
    # Element faultstring uses Python identifier faultstring
    __faultstring = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'faultstring'), 'faultstring', '__httpschemas_xmlsoap_orgsoapenvelope_Fault__faultstring', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 113, 8), )

    
    faultstring = property(__faultstring.value, __faultstring.set, None, None)

    
    # Element faultactor uses Python identifier faultactor
    __faultactor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'faultactor'), 'faultactor', '__httpschemas_xmlsoap_orgsoapenvelope_Fault__faultactor', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 114, 8), )

    
    faultactor = property(__faultactor.value, __faultactor.set, None, None)

    
    # Element detail uses Python identifier detail
    __detail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'detail'), 'detail', '__httpschemas_xmlsoap_orgsoapenvelope_Fault__detail', False, pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 115, 8), )

    
    detail = property(__detail.value, __detail.set, None, None)

    _ElementMap.update({
        __faultcode.name() : __faultcode,
        __faultstring.name() : __faultstring,
        __faultactor.name() : __faultactor,
        __detail.name() : __detail
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Fault', Fault_)


# Complex type {http://schemas.xmlsoap.org/soap/envelope/}detail with content type ELEMENT_ONLY
class detail (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.xmlsoap.org/soap/envelope/}detail with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'detail')
    _XSDLocation = pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 118, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'detail', detail)


Envelope = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Envelope'), Envelope_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 14, 4))
Namespace.addCategoryObject('elementBinding', Envelope.name().localName(), Envelope)

Header = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Header'), Header_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 23, 4))
Namespace.addCategoryObject('elementBinding', Header.name().localName(), Header)

Body = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Body'), Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 30, 4))
Namespace.addCategoryObject('elementBinding', Body.name().localName(), Body)

Fault = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Fault'), Fault_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 106, 0))
Namespace.addCategoryObject('elementBinding', Fault.name().localName(), Fault)



Envelope_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Header'), Header_, scope=Envelope_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 23, 4)))

Envelope_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Body'), Body_, scope=Envelope_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 30, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 17, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 19, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Envelope_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Header')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 17, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Envelope_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Body')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 18, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://schemas.xmlsoap.org/soap/envelope/')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 19, 12))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Envelope_._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 26, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://schemas.xmlsoap.org/soap/envelope/')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 26, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Header_._Automaton = _BuildAutomaton_()




Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pointToPointShoppingRequest'), _ImportedBinding_silvershop.PointToPointShoppingRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 33, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pointToPointShoppingResponse'), _ImportedBinding_silvershop.PointToPointShoppingResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 34, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'travelPassShoppingRequest'), _ImportedBinding_silvershop.TravelPassShoppingRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 35, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'travelPassShoppingResponse'), _ImportedBinding_silvershop.TravelPassShoppingResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 36, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'scheduleSearchRequest'), _ImportedBinding_silvershop.ScheduleSearchRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 37, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'scheduleSearchResponse'), _ImportedBinding_silvershop.ScheduleSearchResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 38, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'addPaymentRequest'), _ImportedBinding_silverbook.AddPaymentRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 39, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'addPaymentResponse'), _ImportedBinding_silverbook.AddPaymentResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 40, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'authenticatePayerRequest'), _ImportedBinding_silverbook.AuthenticatePayerRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 41, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'authenticatePayerResponse'), _ImportedBinding_silverbook.AuthenticatePayerResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 42, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cancelBookingRecordRequest'), _ImportedBinding_silverbook.CancelBookingRecordRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 43, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cancelBookingRecordResponse'), _ImportedBinding_silverbook.CancelBookingRecordResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 44, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'claimValueDocumentRequest'), _ImportedBinding_silverbook.ClaimValueDocumentRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 45, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'claimValueDocumentResponse'), _ImportedBinding_silverbook.ClaimValueDocumentResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 46, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'confirmBookingRecordRequest'), _ImportedBinding_silverbook.ConfirmBookingRecordRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 47, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'confirmBookingRecordResponse'), _ImportedBinding_silverbook.ConfirmBookingRecordResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 48, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'createBookingRecordRequest'), _ImportedBinding_silverbook.CreateBookingRecordRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 49, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'createBookingRecordResponse'), _ImportedBinding_silverbook.CreateBookingRecordResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 50, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'recordFinancialTransactionRequest'), _ImportedBinding_silverbook.RecordFinancialTransactionRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 51, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'recordFinancialTransactionResponse'), _ImportedBinding_silverbook.RecordFinancialTransactionResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 52, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'redeliverValueDocumentRequest'), _ImportedBinding_silverbook.RedeliverValueDocumentRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 53, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'redeliverValueDocumentResponse'), _ImportedBinding_silverbook.RedeliverValueDocumentResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 54, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'retrieveBookingRecordRequest'), _ImportedBinding_silverbook.RetrieveBookingRecordRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 55, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'retrieveBookingRecordResponse'), _ImportedBinding_silverbook.RetrieveBookingRecordResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 56, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'returnValueDocumentRequest'), _ImportedBinding_silverbook.ReturnValueDocumentRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 57, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'returnValueDocumentResponse'), _ImportedBinding_silverbook.ReturnValueDocumentResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 58, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'searchBookingRecordsRequest'), _ImportedBinding_silverbook.SearchBookingRecordsRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 59, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'searchBookingRecordsResponse'), _ImportedBinding_silverbook.SearchBookingRecordsResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 60, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'updateBookingRecordRequest'), _ImportedBinding_silverbook.UpdateBookingRecordRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 61, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'updateBookingRecordResponse'), _ImportedBinding_silverbook.UpdateBookingRecordResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 62, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'refundBookingRecordRequest'), _ImportedBinding_silverbook.RefundBookingRecordRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 63, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'refundBookingRecordResponse'), _ImportedBinding_silverbook.RefundBookingRecordResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 64, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'validateBookingRecordInformationRequest'), _ImportedBinding_silverbook.ValidateBookingRecordInformationRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 65, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'validateBookingRecordInformationResponse'), _ImportedBinding_silverbook.ValidateBookingRecordInformationResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 66, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'generatePaymentTokenRequest'), _ImportedBinding_silverbook.GeneratePaymentTokenRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 67, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'generatePaymentTokenResponse'), _ImportedBinding_silverbook.GeneratePaymentTokenResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 68, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'deletePaymentTokenRequest'), _ImportedBinding_silverbook.DeletePaymentTokenRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 69, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'deletePaymentTokenResponse'), _ImportedBinding_silverbook.DeletePaymentTokenResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 70, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'retrieveCancellationSummaryRequest'), _ImportedBinding_silverbook.RetrieveCancellationSummaryRequestType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 71, 12)))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'retrieveCancellationSummaryResponse'), _ImportedBinding_silverbook.RetrieveCancellationSummaryResponseType, scope=Body_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 72, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 33, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 34, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 35, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 36, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 37, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 38, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 39, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 40, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 41, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 42, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 43, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 44, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 45, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 46, 12))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 47, 12))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 48, 12))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 49, 12))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 50, 12))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 51, 12))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 52, 12))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 53, 12))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 54, 12))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 55, 12))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 56, 12))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 57, 12))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 58, 12))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 59, 12))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 60, 12))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 61, 12))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 62, 12))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 63, 12))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 64, 12))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 65, 12))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 66, 12))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 67, 12))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 68, 12))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 69, 12))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 70, 12))
    counters.add(cc_37)
    cc_38 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 71, 12))
    counters.add(cc_38)
    cc_39 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 72, 12))
    counters.add(cc_39)
    cc_40 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 73, 12))
    counters.add(cc_40)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'pointToPointShoppingRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 33, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'pointToPointShoppingResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 34, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'travelPassShoppingRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 35, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'travelPassShoppingResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 36, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'scheduleSearchRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 37, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'scheduleSearchResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 38, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'addPaymentRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 39, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'addPaymentResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 40, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'authenticatePayerRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 41, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'authenticatePayerResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 42, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'cancelBookingRecordRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 43, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'cancelBookingRecordResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 44, 12))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'claimValueDocumentRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 45, 12))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'claimValueDocumentResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 46, 12))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'confirmBookingRecordRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 47, 12))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'confirmBookingRecordResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 48, 12))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'createBookingRecordRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 49, 12))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'createBookingRecordResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 50, 12))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'recordFinancialTransactionRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 51, 12))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'recordFinancialTransactionResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 52, 12))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'redeliverValueDocumentRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 53, 12))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'redeliverValueDocumentResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 54, 12))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'retrieveBookingRecordRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 55, 12))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'retrieveBookingRecordResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 56, 12))
    st_23 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'returnValueDocumentRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 57, 12))
    st_24 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'returnValueDocumentResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 58, 12))
    st_25 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'searchBookingRecordsRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 59, 12))
    st_26 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'searchBookingRecordsResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 60, 12))
    st_27 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'updateBookingRecordRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 61, 12))
    st_28 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'updateBookingRecordResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 62, 12))
    st_29 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_30, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'refundBookingRecordRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 63, 12))
    st_30 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_31, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'refundBookingRecordResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 64, 12))
    st_31 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_32, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'validateBookingRecordInformationRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 65, 12))
    st_32 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_33, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'validateBookingRecordInformationResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 66, 12))
    st_33 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_34, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'generatePaymentTokenRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 67, 12))
    st_34 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_35, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'generatePaymentTokenResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 68, 12))
    st_35 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_36, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'deletePaymentTokenRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 69, 12))
    st_36 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_37, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'deletePaymentTokenResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 70, 12))
    st_37 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_38, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'retrieveCancellationSummaryRequest')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 71, 12))
    st_38 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_39, False))
    symbol = pyxb.binding.content.ElementUse(Body_._UseForTag(pyxb.namespace.ExpandedName(None, 'retrieveCancellationSummaryResponse')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 72, 12))
    st_39 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_40, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 73, 12))
    st_40 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_40, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_40, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_40, [
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
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_40, [
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
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
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
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
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
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
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
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
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
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_29, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_30, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_30, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_31, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_31, False) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_32, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_32, False) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_33, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_33, False) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_34, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_34, False) ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_35, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_35, False) ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_36, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_36, False) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_37, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_37, False) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_38, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_38, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_39, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_39, False) ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_40, True) ]))
    st_40._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Body_._Automaton = _BuildAutomaton_2()




Fault_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'faultcode'), pyxb.binding.datatypes.QName, scope=Fault_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 112, 8)))

Fault_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'faultstring'), pyxb.binding.datatypes.string, scope=Fault_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 113, 8)))

Fault_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'faultactor'), pyxb.binding.datatypes.anyURI, scope=Fault_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 114, 8)))

Fault_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'detail'), detail, scope=Fault_, location=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 115, 8)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 114, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 115, 8))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Fault_._UseForTag(pyxb.namespace.ExpandedName(None, 'faultcode')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 112, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Fault_._UseForTag(pyxb.namespace.ExpandedName(None, 'faultstring')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 113, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Fault_._UseForTag(pyxb.namespace.ExpandedName(None, 'faultactor')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 114, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Fault_._UseForTag(pyxb.namespace.ExpandedName(None, 'detail')), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 115, 8))
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
Fault_._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 120, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/bloomberglondonrd1/IdeaProjects/silvercore/xsd/all.xsd', 120, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
detail._Automaton = _BuildAutomaton_4()

