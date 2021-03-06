##########################################################################
#
#  Copyright (c) 2007-2013, Image Engine Design Inc. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#     * Neither the name of Image Engine Design nor the names of any
#       other contributors to this software may be used to endorse or
#       promote products derived from this software without specific prior
#       written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

"""Unit test for FloatVectorData binding"""

import IECore

import math
import unittest
import imath

from VectorData import BaseVectorDataTest

class V2fVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.V2fVectorData, imath.V2f)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test V2fVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test V2fVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test V2fVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test V2fVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test V2fVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test V2fVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test V2fVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test V2fVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test V2fVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test V2fVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test V2fVectorData sum operations"""
		BaseVectorDataTest.testSumOperations(self)

	def testSubOperations(self):
		"""Test V2fVectorData subtraction operations"""
		BaseVectorDataTest.testSubOperations(self)

	def testMultOperations(self):
		"""Test V2fVectorData multiplication operations"""
		BaseVectorDataTest.testMultOperations(self)

	def testDivOperations(self):
		"""Test V2fVectorData division operations"""
		BaseVectorDataTest.testDivOperations(self)

	def testByValueItem(self):
		"""Test V2fVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

	def testRepr(self):
		enumTypeName = "IECore.GeometricData.Interpretation"

		self.assertEqual( repr( IECore.V2fVectorData() ) , "IECore.V2fVectorData( [  ], {0}.None_)".format(enumTypeName) )
		self.assertEqual( repr( IECore.V2fVectorData([], IECore.GeometricData.Interpretation.Point) ) , "IECore.V2fVectorData( [  ], {0}.Point)".format(enumTypeName) )
		self.assertEqual( repr( IECore.V2fVectorData([], IECore.GeometricData.Interpretation.Normal) ) , "IECore.V2fVectorData( [  ], {0}.Normal)".format(enumTypeName) )
		self.assertEqual( repr( IECore.V2fVectorData([], IECore.GeometricData.Interpretation.Vector) ) , "IECore.V2fVectorData( [  ], {0}.Vector)".format(enumTypeName) )
		self.assertEqual( repr( IECore.V2fVectorData([], IECore.GeometricData.Interpretation.Color) ) , "IECore.V2fVectorData( [  ], {0}.Color)".format(enumTypeName) )
		self.assertEqual( repr( IECore.V2fVectorData([], IECore.GeometricData.Interpretation.UV) ) , "IECore.V2fVectorData( [  ], {0}.UV)".format(enumTypeName) )

class V2dVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.V2dVectorData, imath.V2d)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test V2dVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test V2dVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test V2dVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test V2dVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test V2dVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test V2dVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test V2dVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test V2dVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test V2dVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test V2dVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test V2dVectorData sum operations"""
		BaseVectorDataTest.testSumOperations(self)

	def testSubOperations(self):
		"""Test V2dVectorData subtraction operations"""
		BaseVectorDataTest.testSubOperations(self)

	def testMultOperations(self):
		"""Test V2dVectorData multiplication operations"""
		BaseVectorDataTest.testMultOperations(self)

	def testDivOperations(self):
		"""Test V2dVectorData division operations"""
		BaseVectorDataTest.testDivOperations(self)

	def testByValueItem(self):
		"""Test V2dVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

class V2iVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.V2iVectorData, imath.V2i)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test V2iVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test V2iVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test V2iVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test V2iVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test V2iVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test V2iVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test V2iVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test V2iVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test V2iVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test V2iVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test V2iVectorData sum operations"""
		BaseVectorDataTest.testSumOperations(self)

	def testSubOperations(self):
		"""Test V2iVectorData subtraction operations"""
		BaseVectorDataTest.testSubOperations(self)

	def testMultOperations(self):
		"""Test V2iVectorData multiplication operations"""
		BaseVectorDataTest.testMultOperations(self)

	def testDivOperations(self):
		"""Test V2iVectorData division operations"""
		BaseVectorDataTest.testDivOperations(self)

	def testByValueItem(self):
		"""Test V2iVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

class V3fVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.V3fVectorData, imath.V3f)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test V3fVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test V3fVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test V3fVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test V3fVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test V3fVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test V3fVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test V3fVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test V3fVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test V3fVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test V3fVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test V3fVectorData sum operations"""
		BaseVectorDataTest.testSumOperations(self)

	def testSubOperations(self):
		"""Test V3fVectorData subtraction operations"""
		BaseVectorDataTest.testSubOperations(self)

	def testMultOperations(self):
		"""Test V3fVectorData multiplication operations"""
		BaseVectorDataTest.testMultOperations(self)

	def testDivOperations(self):
		"""Test V3fVectorData division operations"""
		BaseVectorDataTest.testDivOperations(self)

	def testByValueItem(self):
		"""Test V3fVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

	def testOperatedInterpretation( self ) :

		v = IECore.V3fVectorData( [ imath.V3f(1), imath.V3f(2), imath.V3f(3) ], IECore.GeometricData.Interpretation.Vector )
		self.assertEqual( v.getInterpretation(), IECore.GeometricData.Interpretation.Vector )

		# add and iadd
		v2 = v + IECore.V3fVectorData( [ imath.V3f(4), imath.V3f(5), imath.V3f(6) ] )
		self.assertEqual( v2.getInterpretation(), IECore.GeometricData.Interpretation.Vector )
		v2 += IECore.V3fVectorData( [ imath.V3f(7), imath.V3f(8), imath.V3f(9) ], IECore.GeometricData.Interpretation.Normal )
		self.assertEqual( v2.getInterpretation(), IECore.GeometricData.Interpretation.Vector )

		# sub and isub
		v3 = v - IECore.V3fVectorData( [ imath.V3f(4), imath.V3f(5), imath.V3f(6) ], IECore.GeometricData.Interpretation.Normal )
		self.assertEqual( v3.getInterpretation(), IECore.GeometricData.Interpretation.Vector )
		v3 -= IECore.V3fVectorData( [ imath.V3f(7), imath.V3f(8), imath.V3f(9) ] )
		self.assertEqual( v3.getInterpretation(), IECore.GeometricData.Interpretation.Vector )

		# mul and imul
		v4 = v * IECore.V3fVectorData( [ imath.V3f(4), imath.V3f(5), imath.V3f(6) ] )
		self.assertEqual( v4.getInterpretation(), IECore.GeometricData.Interpretation.Vector )
		v4 *= IECore.V3fVectorData( [ imath.V3f(7), imath.V3f(8), imath.V3f(9) ], IECore.GeometricData.Interpretation.Point )
		self.assertEqual( v4.getInterpretation(), IECore.GeometricData.Interpretation.Vector )

		# div and idiv
		v5 = v / IECore.V3fVectorData( [ imath.V3f(4), imath.V3f(5), imath.V3f(6) ] )
		self.assertEqual( v5.getInterpretation(), IECore.GeometricData.Interpretation.Vector )
		v5 /= IECore.V3fVectorData( [ imath.V3f(7), imath.V3f(8), imath.V3f(9) ], IECore.GeometricData.Interpretation.Color )
		self.assertEqual( v5.getInterpretation(), IECore.GeometricData.Interpretation.Vector )

		# slices
		v6 = v[:]
		self.assertEqual( v6.getInterpretation(), IECore.GeometricData.Interpretation.Vector )
		v6 = v[2:]
		self.assertEqual( v6.getInterpretation(), IECore.GeometricData.Interpretation.Vector )
		v6 = v[:2]
		self.assertEqual( v6.getInterpretation(), IECore.GeometricData.Interpretation.Vector )
		v6 = v[:-1]
		self.assertEqual( v6.getInterpretation(), IECore.GeometricData.Interpretation.Vector )

class V3dVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.V3dVectorData, imath.V3d)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test V3dVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test V3dVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test V3dVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test V3dVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test V3dVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test V3dVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test V3dVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test V3dVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test V3dVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test V3dVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test V3dVectorData sum operations"""
		BaseVectorDataTest.testSumOperations(self)

	def testSubOperations(self):
		"""Test V3dVectorData subtraction operations"""
		BaseVectorDataTest.testSubOperations(self)

	def testMultOperations(self):
		"""Test V3dVectorData multiplication operations"""
		BaseVectorDataTest.testMultOperations(self)

	def testDivOperations(self):
		"""Test V3dVectorData division operations"""
		BaseVectorDataTest.testDivOperations(self)

	def testByValueItem(self):
		"""Test V3dVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

class V3iVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.V3iVectorData, imath.V3i)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test V3iVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test V3iVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test V3iVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test V3iVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test V3iVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test V3iVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test V3iVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test V3iVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test V3iVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test V3iVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test V3iVectorData sum operations"""
		BaseVectorDataTest.testSumOperations(self)

	def testSubOperations(self):
		"""Test V3iVectorData subtraction operations"""
		BaseVectorDataTest.testSubOperations(self)

	def testMultOperations(self):
		"""Test V3iVectorData multiplication operations"""
		BaseVectorDataTest.testMultOperations(self)

	def testDivOperations(self):
		"""Test V3iVectorData division operations"""
		BaseVectorDataTest.testDivOperations(self)

	def testByValueItem(self):
		"""Test V3iVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

def createBox3f(value):
     return imath.Box3f(imath.V3f(value))

class Box3fVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.Box3fVectorData, createBox3f)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test Box3fVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test Box3fVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test Box3fVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test Box3fVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test Box3fVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test Box3fVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test Box3fVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test Box3fVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test Box3fVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test Box3fVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test Box3fVectorData sum operations"""
		pass

	def testSubOperations(self):
		"""Test Box3fVectorData subtraction operations"""
		pass

	def testMultOperations(self):
		"""Test Box3fVectorData multiplication operations"""
		pass

	def testDivOperations(self):
		"""Test Box3fVectorData division operations"""
		pass

	def testByValueItem(self):
		"""Test Box3fVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

def createBox3d(value):
     return imath.Box3d(imath.V3d(value))

class Box3dVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.Box3dVectorData, createBox3d)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test Box3dVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test Box3dVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test Box3dVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test Box3dVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test Box3dVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test Box3dVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test Box3dVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test Box3dVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test Box3dVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test Box3dVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test Box3dVectorData sum operations"""
		pass

	def testSubOperations(self):
		"""Test Box3dVectorData subtraction operations"""
		pass

	def testMultOperations(self):
		"""Test Box3dVectorData multiplication operations"""
		pass

	def testDivOperations(self):
		"""Test Box3dVectorData division operations"""
		pass

	def testByValueItem(self):
		"""Test Box3dVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

class M33fVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.M33fVectorData, imath.M33f)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test M33fVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test M33fVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test M33fVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test M33fVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test M33fVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test M33fVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test M33fVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test M33fVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test M33fVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test M33fVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test M33fVectorData sum operations"""
		BaseVectorDataTest.testSumOperations(self)

	def testSubOperations(self):
		"""Test M33fVectorData subtraction operations"""
		BaseVectorDataTest.testSubOperations(self)

	def testMultOperations(self):
		"""Test M33fVectorData multiplication operations"""
		_vector = self.vectorFactory
		_c = self.valueFactory
		v1 = _vector([_c(1), _c(2), _c(3), _c(4), _c(5)])
		v2 = v1 * _c(2)
		self.assertTrue(v1 == _vector([_c(1), _c(2), _c(3), _c(4), _c(5)]))
		self.assertTrue(v2 == _vector([_c(2*3), _c(4*3), _c(6*3), _c(8*3), _c(10*3)]))
		v2 = _vector(v1)
		v2 *= _c(2)
		self.assertTrue(v2 == _vector([_c(2*3), _c(4*3), _c(6*3), _c(8*3), _c(10*3)]))
		v3 = v1 * v2
		self.assertTrue(v3 == _vector([_c(2*9), _c(8*9), _c(18*9), _c(32*9), _c(50*9)]))
		v3 = _vector(v1)
		v3 *= v2
		self.assertTrue(v3 == _vector([_c(2*9), _c(8*9), _c(18*9), _c(32*9), _c(50*9)]))

	def testDivOperations(self):
		"""Test M33fVectorData division operations"""
		pass

	def testByValueItem(self):
		"""Test M33fVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

class M33dVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.M33dVectorData, imath.M33d)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test M33dVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test M33dVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test M33dVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test M33dVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test M33dVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test M33dVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test M33dVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test M33dVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test M33dVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test M33dVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test M33dVectorData sum operations"""
		BaseVectorDataTest.testSumOperations(self)

	def testSubOperations(self):
		"""Test M33dVectorData subtraction operations"""
		BaseVectorDataTest.testSubOperations(self)

	def testMultOperations(self):
		"""Test M33dVectorData multiplication operations"""
		_vector = self.vectorFactory
		_c = self.valueFactory
		v1 = _vector([_c(1), _c(2), _c(3), _c(4), _c(5)])
		v2 = v1 * _c(2)
		self.assertTrue(v1 == _vector([_c(1), _c(2), _c(3), _c(4), _c(5)]))
		self.assertTrue(v2 == _vector([_c(2*3), _c(4*3), _c(6*3), _c(8*3), _c(10*3)]))
		v2 = _vector(v1)
		v2 *= _c(2)
		self.assertTrue(v2 == _vector([_c(2*3), _c(4*3), _c(6*3), _c(8*3), _c(10*3)]))
		v3 = v1 * v2
		self.assertTrue(v3 == _vector([_c(2*9), _c(8*9), _c(18*9), _c(32*9), _c(50*9)]))
		v3 = _vector(v1)
		v3 *= v2
		self.assertTrue(v3 == _vector([_c(2*9), _c(8*9), _c(18*9), _c(32*9), _c(50*9)]))

	def testDivOperations(self):
		"""Test M33dVectorData division operations"""
		pass

	def testByValueItem(self):
		"""Test M33dVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

class M44fVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.M44fVectorData, imath.M44f)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test M44fVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test M44fVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test M44fVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test M44fVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test M44fVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test M44fVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test M44fVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test M44fVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test M44fVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test M44fVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test M44fVectorData sum operations"""
		BaseVectorDataTest.testSumOperations(self)

	def testSubOperations(self):
		"""Test M44fVectorData subtraction operations"""
		BaseVectorDataTest.testSubOperations(self)

	def testMultOperations(self):
		"""Test M44fVectorData multiplication operations"""
		_vector = self.vectorFactory
		_c = self.valueFactory
		v1 = _vector([_c(1), _c(2), _c(3), _c(4), _c(5)])
		v2 = v1 * _c(2)
		self.assertTrue(v1 == _vector([_c(1), _c(2), _c(3), _c(4), _c(5)]))
		self.assertTrue(v2 == _vector([_c(2*4), _c(4*4), _c(6*4), _c(8*4), _c(10*4)]))
		v2 = _vector(v1)
		v2 *= _c(2)
		self.assertTrue(v2 == _vector([_c(2*4), _c(4*4), _c(6*4), _c(8*4), _c(10*4)]))
		v3 = v1 * v2
		self.assertTrue(v3 == _vector([_c(2*16), _c(8*16), _c(18*16), _c(32*16), _c(50*16)]))
		v3 = _vector(v1)
		v3 *= v2
		self.assertTrue(v3 == _vector([_c(2*16), _c(8*16), _c(18*16), _c(32*16), _c(50*16)]))

	def testDivOperations(self):
		"""Test M44fVectorData division operations"""
		pass

	def testByValueItem(self):
		"""Test M44fVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

class M44dVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.M44dVectorData, imath.M44d)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test M44dVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test M44dVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test M44dVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test M44dVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test M44dVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test M44dVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test M44dVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test M44dVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test M44dVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test M44dVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test M44dVectorData sum operations"""
		BaseVectorDataTest.testSumOperations(self)

	def testSubOperations(self):
		"""Test M44dVectorData subtraction operations"""
		BaseVectorDataTest.testSubOperations(self)

	def testMultOperations(self):
		"""Test M44dVectorData multiplication operations"""
		_vector = self.vectorFactory
		_c = self.valueFactory
		v1 = _vector([_c(1), _c(2), _c(3), _c(4), _c(5)])
		v2 = v1 * _c(2)
		self.assertTrue(v1 == _vector([_c(1), _c(2), _c(3), _c(4), _c(5)]))
		self.assertTrue(v2 == _vector([_c(2*4), _c(4*4), _c(6*4), _c(8*4), _c(10*4)]))
		v2 = _vector(v1)
		v2 *= _c(2)
		self.assertTrue(v2 == _vector([_c(2*4), _c(4*4), _c(6*4), _c(8*4), _c(10*4)]))
		v3 = v1 * v2
		self.assertTrue(v3 == _vector([_c(2*16), _c(8*16), _c(18*16), _c(32*16), _c(50*16)]))
		v3 = _vector(v1)
		v3 *= v2
		self.assertTrue(v3 == _vector([_c(2*16), _c(8*16), _c(18*16), _c(32*16), _c(50*16)]))

	def testDivOperations(self):
		"""Test M44dVectorData division operations"""
		pass

	def testByValueItem(self):
		"""Test M44dVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

def createQuatf(value):
	return imath.Quatf(value, 0, 0, 0)

class QuatfVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.QuatfVectorData, createQuatf)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test QuatfVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test QuatfVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test QuatfVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test QuatfVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test QuatfVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test QuatfVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test QuatfVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test QuatfVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test QuatfVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test QuatfVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test QuatfVectorData sum operations"""
		BaseVectorDataTest.testSumOperations(self)

	def testSubOperations(self):
		"""Test QuatfVectorData subtraction operations"""
		BaseVectorDataTest.testSubOperations(self)

	def testMultOperations(self):
		"""Test QuatfVectorData multiplication operations"""
		BaseVectorDataTest.testMultOperations(self)

	def testDivOperations(self):
		"""Test QuatfVectorData division operations"""
		pass

	def testByValueItem(self):
		"""Test QuatfVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

def createQuatd(value):
	return imath.Quatd(value, 0, 0, 0)

class QuatdVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.QuatdVectorData, createQuatd)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test QuatdVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test QuatdVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test QuatdVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test QuatdVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test QuatdVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test QuatdVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test QuatdVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test QuatdVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test QuatdVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test QuatdVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test QuatdVectorData sum operations"""
		BaseVectorDataTest.testSumOperations(self)

	def testSubOperations(self):
		"""Test QuatdVectorData subtraction operations"""
		BaseVectorDataTest.testSubOperations(self)

	def testMultOperations(self):
		"""Test QuatdVectorData multiplication operations"""
		BaseVectorDataTest.testMultOperations(self)

	def testDivOperations(self):
		"""Test QuatdVectorData division operations"""
		pass

	def testByValueItem(self):
		"""Test QuatdVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

class Color3fVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.Color3fVectorData, imath.Color3f)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test Color3fVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test Color3fVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test Color3fVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test Color3fVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test Color3fVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test Color3fVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test Color3fVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test Color3fVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test Color3fVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test Color3fVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test Color3fVectorData sum operations"""
		BaseVectorDataTest.testSumOperations(self)

	def testSubOperations(self):
		"""Test Color3fVectorData subtraction operations"""
		BaseVectorDataTest.testSubOperations(self)

	def testMultOperations(self):
		"""Test Color3fVectorData multiplication operations"""
		BaseVectorDataTest.testMultOperations(self)

	def testDivOperations(self):
		"""Test Color3fVectorData division operations"""
		BaseVectorDataTest.testDivOperations(self)

	def testByValueItem(self):
		"""Test Color3fVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

class Color4fVectorDataTest(BaseVectorDataTest, unittest.TestCase):

	def __init__(self, param1):
		BaseVectorDataTest.__init__(self, IECore.Color4fVectorData, imath.Color4f)
		unittest.TestCase.__init__(self, param1)

	def testConstructors(self):
		"""Test Color4fVectorData constructors"""
		BaseVectorDataTest.testConstructors(self)

	def testResize(self):
		"""Test Color4fVectorData resizing"""
		BaseVectorDataTest.testResize(self)

	def testAssignment(self):
		"""Test Color4fVectorData assignment"""
		BaseVectorDataTest.testAssignment(self)

	def testNegativeIndexing(self):
		"""Test Color4fVectorData negative indexing"""
		BaseVectorDataTest.testNegativeIndexing(self)

	def testCopyOnWrite(self):
		"""Test Color4fVectorData copy-on-write behavior"""
		BaseVectorDataTest.testCopyOnWrite(self)

	def testContains(self):
		"""Test Color4fVectorData contains function"""
		BaseVectorDataTest.testContains(self)

	def testExtend(self):
		"""Test Color4fVectorData extend function"""
		BaseVectorDataTest.testExtend(self)

	def testSlices(self):
		"""Test Color4fVectorData slicing behavior"""
		BaseVectorDataTest.testSlices(self)

	def testEquality(self):
		"""Test Color4fVectorData equality function"""
		BaseVectorDataTest.testEquality(self)

	def testComparison(self):
		"""Test Color4fVectorData comparison function"""
		pass

	def testSumOperations(self):
		"""Test Color4fVectorData sum operations"""
		BaseVectorDataTest.testSumOperations(self)

	def testSubOperations(self):
		"""Test Color4fVectorData subtraction operations"""
		BaseVectorDataTest.testSubOperations(self)

	def testMultOperations(self):
		"""Test Color4fVectorData multiplication operations"""
		BaseVectorDataTest.testMultOperations(self)

	def testDivOperations(self):
		"""Test Color4fVectorData division operations"""
		BaseVectorDataTest.testDivOperations(self)

	def testByValueItem(self):
		"""Test Color4fVectorData by value return type"""
		BaseVectorDataTest.testByValueItem(self)

# class Color3dVectorDataTest(BaseVectorDataTest, unittest.TestCase):

# 	def __init__(self, param1):
# 		BaseVectorDataTest.__init__(self, IECore.Color3dVectorData, IECore.Color3d)
# 		unittest.TestCase.__init__(self, param1)

# 	def testConstructors(self):
# 		"""Test Color3dVectorData constructors"""
# 		BaseVectorDataTest.testConstructors(self)

# 	def testResize(self):
# 		"""Test Color3dVectorData resizing"""
# 		BaseVectorDataTest.testResize(self)

# 	def testAssignment(self):
# 		"""Test Color3dVectorData assignment"""
# 		BaseVectorDataTest.testAssignment(self)

# 	def testNegativeIndexing(self):
# 		"""Test Color3dVectorData negative indexing"""
# 		BaseVectorDataTest.testNegativeIndexing(self)

# 	def testCopyOnWrite(self):
# 		"""Test Color3dVectorData copy-on-write behavior"""
# 		BaseVectorDataTest.testCopyOnWrite(self)

# 	def testContains(self):
# 		"""Test Color3dVectorData contains function"""
# 		BaseVectorDataTest.testContains(self)

# 	def testExtend(self):
# 		"""Test Color3dVectorData extend function"""
# 		BaseVectorDataTest.testExtend(self)

# 	def testSlices(self):
# 		"""Test Color3dVectorData slicing behavior"""
# 		BaseVectorDataTest.testSlices(self)

# 	def testEquality(self):
# 		"""Test Color3dVectorData equality function"""
# 		BaseVectorDataTest.testEquality(self)

# 	def testComparison(self):
# 		"""Test Color3dVectorData comparison function"""
# 		pass

# 	def testSumOperations(self):
# 		"""Test Color3dVectorData sum operations"""
# 		BaseVectorDataTest.testSumOperations(self)

# 	def testSubOperations(self):
# 		"""Test Color3dVectorData subtraction operations"""
# 		BaseVectorDataTest.testSubOperations(self)

# 	def testMultOperations(self):
# 		"""Test Color3dVectorData multiplication operations"""
# 		BaseVectorDataTest.testMultOperations(self)

# 	def testDivOperations(self):
# 		"""Test Color3dVectorData division operations"""
# 		BaseVectorDataTest.testDivOperations(self)

# 	def testByValueItem(self):
# 		"""Test Color3dVectorData by value return type"""
# 		BaseVectorDataTest.testByValueItem(self)

# class Color4dVectorDataTest(BaseVectorDataTest, unittest.TestCase):

# 	def __init__(self, param1):
# 		BaseVectorDataTest.__init__(self, IECore.Color4dVectorData, IECore.Color4d)
# 		unittest.TestCase.__init__(self, param1)

# 	def testConstructors(self):
# 		"""Test Color4dVectorData constructors"""
# 		BaseVectorDataTest.testConstructors(self)

# 	def testResize(self):
# 		"""Test Color4dVectorData resizing"""
# 		BaseVectorDataTest.testResize(self)

# 	def testAssignment(self):
# 		"""Test Color4dVectorData assignment"""
# 		BaseVectorDataTest.testAssignment(self)

# 	def testNegativeIndexing(self):
# 		"""Test Color4dVectorData negative indexing"""
# 		BaseVectorDataTest.testNegativeIndexing(self)

# 	def testCopyOnWrite(self):
# 		"""Test Color4dVectorData copy-on-write behavior"""
# 		BaseVectorDataTest.testCopyOnWrite(self)

# 	def testContains(self):
# 		"""Test Color4dVectorData contains function"""
# 		BaseVectorDataTest.testContains(self)

# 	def testExtend(self):
# 		"""Test Color4dVectorData extend function"""
# 		BaseVectorDataTest.testExtend(self)

# 	def testSlices(self):
# 		"""Test Color4dVectorData slicing behavior"""
# 		BaseVectorDataTest.testSlices(self)

# 	def testEquality(self):
# 		"""Test Color4dVectorData equality function"""
# 		BaseVectorDataTest.testEquality(self)

# 	def testComparison(self):
# 		"""Test Color4dVectorData comparison function"""
# 		pass

# 	def testSumOperations(self):
# 		"""Test Color4dVectorData sum operations"""
# 		BaseVectorDataTest.testSumOperations(self)

# 	def testSubOperations(self):
# 		"""Test Color4dVectorData subtraction operations"""
# 		BaseVectorDataTest.testSubOperations(self)

# 	def testMultOperations(self):
# 		"""Test Color4dVectorData multiplication operations"""
# 		BaseVectorDataTest.testMultOperations(self)

# 	def testDivOperations(self):
# 		"""Test Color4dVectorData division operations"""
# 		BaseVectorDataTest.testDivOperations(self)

# 	def testByValueItem(self):
# 		"""Test Color4dVectorData by value return type"""
# 		BaseVectorDataTest.testByValueItem(self)

if __name__ == "__main__":
    unittest.main()

