//////////////////////////////////////////////////////////////////////////
//
//  Copyright (c) 2017, Image Engine Design Inc. All rights reserved.
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

#include "IECoreAlembic/PrimitiveWriter.h"

#include "IECoreScene/CurvesPrimitive.h"

#include "IECore/MessageHandler.h"

#include "Alembic/AbcGeom/OCurves.h"

using namespace IECore;
using namespace IECoreScene;
using namespace IECoreAlembic;
using namespace Alembic::AbcGeom;

namespace
{

BasisType basisType( const IECore::CubicBasisf &basis )
{
	if( basis == CubicBasisf::linear() )
	{
		return kNoBasis;
	}
	else if( basis == CubicBasisf::bezier() )
	{
		return kBezierBasis;
	}
	else if( basis == CubicBasisf::catmullRom() )
	{
		return kCatmullromBasis;
	}
	else if( basis == CubicBasisf::bSpline() )
	{
		return kBsplineBasis;
	}
	else
	{
		IECore::msg( IECore::Msg::Warning, "CurvesWriter", "Unsupported basis" );
		return kBsplineBasis;
	}
}

class CurvesWriter : public PrimitiveWriter
{

	public :

		CurvesWriter( Alembic::Abc::OObject &parent, const std::string &name )
			:	m_curves( parent, name )
		{
		}

		void writeSample( const IECore::Object *object ) override
		{
			const CurvesPrimitive *curvesPrimitive = runTimeCast<const CurvesPrimitive>( object );
			if( !curvesPrimitive )
			{
				throw IECore::Exception( "CurvesWriter expected a CurvesPrimitive" );
			}

			OCurvesSchema::Sample sample;

			sample.setCurvesNumVertices(
				Abc::Int32ArraySample( curvesPrimitive->verticesPerCurve()->readable() )
			);

			sample.setWrap( curvesPrimitive->periodic() ? kPeriodic : kNonPeriodic );

			const BasisType basis = basisType( curvesPrimitive->basis() );
			if( basis == kNoBasis )
			{
				sample.setType( kLinear );
			}
			else
			{
				sample.setType( kCubic );
				sample.setBasis( basis );
			}

			if( const V3fVectorData *p = curvesPrimitive->variableData<V3fVectorData>( "P" ) )
			{
				sample.setPositions(
					Abc::P3fArraySample( p->readable() )
				);
			}

			if( const V3fVectorData *v = curvesPrimitive->variableData<V3fVectorData>( "velocity" ) )
			{
				sample.setVelocities(
					Abc::V3fArraySample( v->readable() )
				);
			}

			auto widthIt = curvesPrimitive->variables.find( "width" );
			if( widthIt != curvesPrimitive->variables.end() )
			{
				sample.setWidths( geomParamSample<FloatVectorData, OFloatGeomParam>( widthIt->second ) );
			}

			auto uvIt = curvesPrimitive->variables.find( "uv" );
			if( uvIt != curvesPrimitive->variables.end() )
			{
				sample.setUVs( geomParamSample<V2fVectorData, OV2fGeomParam>( uvIt->second ) );
			}

			auto nIt = curvesPrimitive->variables.find( "N" );
			if( nIt != curvesPrimitive->variables.end() )
			{
				sample.setNormals( geomParamSample<V3fVectorData, ON3fGeomParam>( nIt->second ) );
			}

			const char *namesToIgnore[] = { "P", "velocity", "width", "uv", "N", nullptr };
			OCompoundProperty geomParams = m_curves.getSchema().getArbGeomParams();
			writeArbGeomParams( curvesPrimitive, geomParams, namesToIgnore );

			m_curves.getSchema().set( sample );
		}

		void writeTimeSampling( const Alembic::AbcCoreAbstract::TimeSamplingPtr &timeSampling ) override
		{
			m_curves.getSchema().setTimeSampling( timeSampling );
		}

	private :

		Alembic::AbcGeom::OCurves m_curves;

		static Description<CurvesWriter> g_description;

};

IECoreAlembic::ObjectWriter::Description<CurvesWriter> CurvesWriter::g_description( IECoreScene::CurvesPrimitive::staticTypeId() );

} // namespace

