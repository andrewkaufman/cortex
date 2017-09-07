##########################################################################
#
#  Copyright (c) 2017, Image Engine Design Inc. All rights reserved.
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
import warnings
import sys

import IECore
import IECoreImage

warnings.simplefilter( "error", DeprecationWarning )

from ImagePrimitiveTest import ImagePrimitiveTest
from ImageReaderTest import ImageReaderTest
from ImageWriterTest import ImageWriterTest
from ClampOpTest import ClampOpTest
from ColorAlgoTest import ColorAlgoTest
from CurveTracerTest import CurveTracerTest
from DisplayDriverServerTest import DisplayDriverServerTest
from EnvMapSamplerTest import EnvMapSamplerTest
from FontTest import FontTest
from ImageCropOpTest import ImageCropOpTest
from ImageDiffOpTest import ImageDiffOpTest
from ImageThinnerTest import ImageThinnerTest
from LensDistortOpTest import LensDistortOpTest
from LuminanceOpTest import LuminanceOpTest
from MedianCutSamplerTest import MedianCutSamplerTest
from SplineToImageTest import SplineToImageTest
from SummedAreaOpTest import SummedAreaOpTest
from ImageDisplayDriverTest import *

unittest.TestProgram(
	testRunner = unittest.TextTestRunner(
		stream = IECore.CompoundStream(
			[
				sys.stderr,
				open( "test/IECoreImage/results.txt", "w" )
			]
		),
		verbosity = 2
	)
)