##########################################################################
#
#  Copyright (c) 2008-2009, Image Engine Design Inc. All rights reserved.
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

import unittest
import math
import imath
import IECore

class LineSegmentTest( unittest.TestCase ) :

	def testConstructor( self ) :

		l = IECore.LineSegment3f()

		p0 = imath.V3f( 1, 2, 3 )
		p1 = imath.V3f( 4, 5, 6 )
		l = IECore.LineSegment3f( p0, p1 )

		self.assertEqual( l.p0, p0 )
		self.assertEqual( l.p1, p1 )

	def testPointAccess( self ) :

		l = IECore.LineSegment3f()

		l.p0 = imath.V3f( 1, 2, 3 )
		self.assertEqual( l.p0, imath.V3f( 1, 2, 3 ) )

		l.p1 = imath.V3f( 4, 5, 6 )
		self.assertEqual( l.p1, imath.V3f( 4, 5, 6 ) )

	def testCall( self ) :

		l = IECore.LineSegment3f( imath.V3f( 0 ), imath.V3f( 1 ) )

		self.assertEqual( l( 0 ), imath.V3f( 0 ) )
		self.assertEqual( l( 1 ), imath.V3f( 1 ) )
		self.assertEqual( l( 0.5 ), imath.V3f( 0.5 ) )
		self.assertEqual( l( -1 ), imath.V3f( -1 ) )
		self.assertEqual( l( 2 ), imath.V3f( 2 ) )

	def testLength( self ) :

		l = IECore.LineSegment3f( imath.V3f( 1 ), imath.V3f( 2 ) )

		self.assertEqual( l.length(), imath.V3f( 1 ).length() )
		self.assertEqual( l.length2(), imath.V3f( 1 ).length2() )

	def testClosestPointTo( self ) :

		l = IECore.LineSegment3f( imath.V3f( 1 ), imath.V3f( 2 ) )

		r = imath.Rand32( 100 )

		for i in range( 0, 1000 ) :

			p = l( r.nextf( 0, 1 ) )
			self.assertTrue( l.closestPointTo( p ).equalWithAbsError( p, 0.00001 ) )

		for i in range( 0, 1000 ) :

			p = l( r.nextf( -1, 0 ) )
			self.assertTrue( l.closestPointTo( p ).equalWithAbsError( l.p0, 0.00001 ) )

		for i in range( 0, 1000 ) :

			p = l( r.nextf( 1, 2 ) )
			self.assertTrue( l.closestPointTo( p ).equalWithAbsError( l.p1, 0.00001 ) )

		t = l.direction().cross( imath.V3f( 0, 1, 0 ) )
		for i in range( 0, 1000 ) :

			pl = l( r.nextf( 0, 1 ) )
			pt = pl + t * r.nextf( -10, 10 )
			self.assertTrue( l.closestPointTo( pt ).equalWithAbsError( pl, 0.00001 ) )

		for i in range( 0, 1000 ) :

			pl = l( r.nextf( 1, 2 ) )
			pt = pl + t * r.nextf( -10, 10 )
			self.assertTrue( l.closestPointTo( pt ).equalWithAbsError( l.p1, 0.00001 ) )

		for i in range( 0, 1000 ) :

			pl = l( r.nextf( -1, 0 ) )
			pt = pl + t * r.nextf( -10, 10 )
			self.assertTrue( l.closestPointTo( pt ).equalWithAbsError( l.p0, 0.00001 ) )

	def testClosestPoints( self ) :

		r = imath.Rand32( 100 )
		for i in range( 0, 1000 ) :

			x = r.nextf( -10, 10 )
			y = r.nextf( -10, 10 )
			z1 = r.nextf( -10, 10 )
			z2 = r.nextf( -10, 10 )

			l1 = IECore.LineSegment3f( imath.V3f( -10, y, z1 ), imath.V3f( 10, y, z1 ) )
			l2 = IECore.LineSegment3f( imath.V3f( x, -10, z2 ), imath.V3f( x, 10, z2 ) )

			p1, p2 = l1.closestPoints( l2 )
			p3, p4 = l2.closestPoints( l1 )

			self.assertTrue( p1.equalWithAbsError( p4, 0.00001 ) )
			self.assertTrue( p2.equalWithAbsError( p3, 0.00001 ) )

		# |
		# |
		# |  ------
		# |
		# |
		l1 = IECore.LineSegment3f( imath.V3f( 0, 0, 0 ), imath.V3f( 0, 2, 0 ) )
		l2 = IECore.LineSegment3f( imath.V3f( 1, 1, 0 ), imath.V3f( 3, 1, 0 ) )

		p1, p2 = l1.closestPoints( l2 )
		p3, p4 = l2.closestPoints( l1 )
		self.assertEqual( p1, p4 )
		self.assertEqual( p2, p3 )

		self.assertEqual( p1, imath.V3f( 0, 1, 0 ) )
		self.assertEqual( p2, imath.V3f( 1, 1, 0 ) )

		# \
		#  \
		#
		#  /
		# /

		l1 = IECore.LineSegment3f( imath.V3f( 0, 0, 0 ), imath.V3f( 2, 2, 0 ) )
		l2 = IECore.LineSegment3f( imath.V3f( 0, 5, 0 ), imath.V3f( 2, 3, 0 ) )

		p1, p2 = l1.closestPoints( l2 )
		p3, p4 = l2.closestPoints( l1 )
		self.assertEqual( p1, p4 )
		self.assertEqual( p2, p3 )

		self.assertEqual( p1, imath.V3f( 2, 2, 0 ) )
		self.assertEqual( p2, imath.V3f( 2, 3, 0 ) )

	def testTransform( self ) :

		l1 = IECore.LineSegment3f( imath.V3f( 0, 0, 0 ), imath.V3f( 0, 2, 0 ) )
		l2 = IECore.LineSegment3f( l1 )
		self.assertEqual( l1, l2 )

		t = imath.M44f().translate( imath.V3f( 1 ) )

		l3 = l2 * t
		self.assertEqual( l1, l2 )
		self.assertEqual( l3.p0, l2.p0 + imath.V3f( 1 ) )
		self.assertEqual( l3.p1, l2.p1 + imath.V3f( 1 ) )

		l1 *= t
		self.assertEqual( l1.p0, l2.p0 + imath.V3f( 1 ) )
		self.assertEqual( l1.p1, l2.p1 + imath.V3f( 1 ) )

	def testIntersect( self ) :

		l = IECore.LineSegment3f( imath.V3f( 0, -1, 0 ), imath.V3f( 0, 1, 0 ) )
		p = imath.Plane3f( imath.V3f( 0, 1, 0 ), 0 )
		self.assertEqual( l.intersect( p ), ( True, imath.V3f( 0, 0, 0 ) ) )
		self.assertEqual( l.intersectT( p ), ( True, 0.5 ) )

		p = imath.Plane3f( imath.V3f( -1, 0, 0 ), 10 )
		self.assertEqual( l.intersect( p )[0], False )
		self.assertEqual( l.intersectT( p )[0], False )

	def testRepr( self ) :

		p0 = imath.V3f( 0, 0, 0 )
		p1 = imath.V3f( 0, 0, 0 )

		l = IECore.LineSegment3f( p0, p1 )
		self.assertEqual( repr(l), "IECore.LineSegment3f( " + repr(p0) + ", " + repr(p1) + " )" )

	def testDimensions( self ) :

		self.assertEqual( IECore.LineSegment3f.dimensions(), 3 )
		self.assertEqual( IECore.LineSegment3d.dimensions(), 3 )


if __name__ == "__main__":
    unittest.main()
