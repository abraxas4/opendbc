import os
import capnp
from opendbc.car.common.basedir import BASEDIR

try:
  from openpilot.cereal import car   # new openpilot package structure (cereal pre-loads car)
except ImportError:
  try:
    from cereal import car           # standalone / old structure
  except ImportError:
    capnp.remove_import_hook()
    car = capnp.load(os.path.join(BASEDIR, "car.capnp"), imports=[BASEDIR])

CarState = car.CarState
RadarData = car.RadarData
CarControl = car.CarControl
CarParams = car.CarParams

CarStateT = capnp.lib.capnp._StructModule
RadarDataT = capnp.lib.capnp._StructModule
CarControlT = capnp.lib.capnp._StructModule
CarParamsT = capnp.lib.capnp._StructModule
