//////////////////////////////////////////////////////////////////////////
//
//  Copyright (c) 2013, Image Engine Design Inc. All rights reserved.
//
//  Redistribution and use in source and binary forms, with or without
//  modification, are permitted provided that the following conditions are
//  met:
//
//     * Redistributions of source code must retain the above copyright
//       notice, this list of conditions and the following disclaimer.
//
//     * Redistributions in binary form must reproduce the above copyright
//       notice, this list of conditions and the following disclaimer in the
//       documentation and/or other materials provided with the distribution.
//
//     * Neither the name of Image Engine Design nor the names of any
//       other contributors to this software may be used to endorse or
//       promote products derived from this software without specific prior
//       written permission.
//
//  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
//  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
//  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
//  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
//  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
//  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
//  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
//  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
//  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
//  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
//  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
//////////////////////////////////////////////////////////////////////////

#include "boost/python.hpp"

#include "IECorePython/GeometricTypedDataBinding.h"

#include "IECore/GeometricTypedData.h"

using namespace boost;
using namespace boost::python;
using namespace IECore;

namespace IECorePython
{

class GeometricTypedDataHelper
{
};

void bindGeometricTypedData()
{
	scope geometricTypedDataScope = class_<GeometricTypedDataHelper>( "GeometricData" );

	enum_<GeometricData::Interpretation>( "Interpretation" )
		// We would dearly love to bind `None` as `None`.
		.value( "None", GeometricData::None )
		// But Python 3 very inconveniently makes `None`
		// a keyword, making `Interpretation.None` a syntax
		// error. So we bind as `None_` as well, which is
		// ugly but seems to be the general convention when
		// a C++ name clashes with a Python one.
		.value( "None_", GeometricData::None )
		// Of course, for the Northerner, all this is
		// academic.
		.value( "Nowt", GeometricData::None )
		.value( "Numeric", GeometricData::Numeric ) // depreciated, use None instead.
		.value( "Point", GeometricData::Point )
		.value( "Normal", GeometricData::Normal )
		.value( "Vector", GeometricData::Vector )
		.value( "Color", GeometricData::Color )
		.value( "UV", GeometricData::UV )
		.value( "Rational", GeometricData::Rational )
	;
}

} // namespace IECorePython
