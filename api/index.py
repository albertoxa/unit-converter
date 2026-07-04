from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Callable, Optional
import json

app = FastAPI(title="Universal Converter API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================================================================
# CONVERSION ENGINE
# =============================================================================

class CategoryRegistry:
    def __init__(self):
        self._categories: Dict[str, dict] = {}

    def register(self, category_id: str, units: Dict[str, float], base_unit: str,
                 symbols: Optional[Dict[str, str]] = None,
                 names: Optional[Dict[str, str]] = None,
                 formulas: Optional[Dict[str, Dict[str, Callable]]] = None):
        self._categories[category_id] = {
            "units": units,
            "base_unit": base_unit,
            "symbols": symbols or {},
            "names": names or {u: u.replace("_", " ").title() for u in units},
            "formulas": formulas or {}
        }

    def convert(self, category: str, value: float, from_unit: str, to_unit: str) -> float:
        cat = self._categories[category]
        if from_unit in cat["formulas"] or to_unit in cat["formulas"]:
            return self._formula_convert(cat, value, from_unit, to_unit)
        base_value = value * cat["units"][from_unit]
        return base_value / cat["units"][to_unit]

    def _formula_convert(self, cat, value, from_u, to_u):
        base = cat["base_unit"]
        formulas = cat["formulas"]
        if from_u == base:
            base_val = value
        else:
            base_val = formulas[from_u]["to_base"](value)
        if to_u == base:
            return base_val
        return formulas[to_u]["from_base"](base_val)

    def get_metadata(self) -> Dict:
        return {
            cat_id: {
                "units": [
                    {"id": uid, "symbol": data["symbols"].get(uid, uid),
                     "name": data["names"].get(uid, uid.replace("_", " ").title())}
                    for uid in data["units"]
                ],
                "base_unit": data["base_unit"]
            }
            for cat_id, data in self._categories.items()
        }

registry = CategoryRegistry()

# --- LENGTH ---
registry.register("length",
    units={"meter":1.0,"centimeter":0.01,"millimeter":0.001,"kilometer":1000.0,
           "inch":0.0254,"foot":0.3048,"yard":0.9144,"mile":1609.344,"nautical_mile":1852.0},
    base_unit="meter",
    symbols={"meter":"m","centimeter":"cm","millimeter":"mm","kilometer":"km",
             "inch":"in","foot":"ft","yard":"yd","mile":"mi","nautical_mile":"nmi"})

# --- TEMPERATURE ---
registry.register("temperature",
    units={"celsius":1.0,"fahrenheit":1.0,"kelvin":1.0},
    base_unit="celsius",
    symbols={"celsius":"°C","fahrenheit":"°F","kelvin":"K"},
    formulas={
        "celsius":   {"to_base": lambda x: x,           "from_base": lambda x: x},
        "fahrenheit":{"to_base": lambda x: (x-32)*5/9, "from_base": lambda x: x*9/5+32},
        "kelvin":    {"to_base": lambda x: x-273.15,   "from_base": lambda x: x+273.15}
    })

# --- WEIGHT ---
registry.register("weight",
    units={"gram":1.0,"kilogram":1000.0,"milligram":0.001,"metric_ton":1_000_000.0,
           "pound":453.59237,"ounce":28.3495,"stone":6350.293,"us_ton":907_184.74},
    base_unit="gram",
    symbols={"gram":"g","kilogram":"kg","milligram":"mg","metric_ton":"t",
             "pound":"lb","ounce":"oz","stone":"st","us_ton":"ton (US)"})

# --- VOLUME ---
registry.register("volume",
    units={"liter":1.0,"milliliter":0.001,"cubic_meter":1000.0,
           "gallon_us":3.78541,"quart_us":0.946353,"pint_us":0.473176,"cup_us":0.236588,
           "fluid_ounce_us":0.0295735,"tablespoon_us":0.0147868,"teaspoon_us":0.00492892,
           "gallon_uk":4.54609,"pint_uk":0.568261},
    base_unit="liter",
    symbols={"liter":"L","milliliter":"mL","cubic_meter":"m³","gallon_us":"gal (US)",
             "quart_us":"qt (US)","pint_us":"pt (US)","cup_us":"cup",
             "fluid_ounce_us":"fl oz","tablespoon_us":"tbsp","teaspoon_us":"tsp",
             "gallon_uk":"gal (UK)","pint_uk":"pt (UK)"})

# --- DIGITAL STORAGE ---
registry.register("data",
    units={"byte":1.0,"kilobyte":1024.0,"megabyte":1_048_576.0,"gigabyte":1_073_741_824.0,
           "terabyte":1_099_511_627_776.0,"petabyte":1.1259e15,"bit":0.125},
    base_unit="byte",
    symbols={"byte":"B","kilobyte":"KB","megabyte":"MB","gigabyte":"GB",
             "terabyte":"TB","petabyte":"PB","bit":"b"})

# --- AREA ---
registry.register("area",
    units={"square_meter":1.0,"square_kilometer":1e6,"square_centimeter":0.0001,
           "square_mile":2.59e6,"square_yard":0.836127,"square_foot":0.092903,
           "acre":4046.86,"hectare":10000.0},
    base_unit="square_meter",
    symbols={"square_meter":"m²","square_kilometer":"km²","square_centimeter":"cm²",
             "square_mile":"mi²","square_yard":"yd²","square_foot":"ft²","acre":"ac","hectare":"ha"})

# --- SPEED ---
registry.register("speed",
    units={"meter_per_second":1.0,"kilometer_per_hour":0.277778,
           "mile_per_hour":0.44704,"knot":0.514444,"foot_per_second":0.3048},
    base_unit="meter_per_second",
    symbols={"meter_per_second":"m/s","kilometer_per_hour":"km/h",
             "mile_per_hour":"mph","knot":"kn","foot_per_second":"ft/s"})

# --- TIME ---
registry.register("time",
    units={"second":1.0,"minute":60.0,"hour":3600.0,"day":86400.0,
           "week":604800.0,"month":2.628e6,"year":3.154e7},
    base_unit="second",
    symbols={"second":"s","minute":"min","hour":"h","day":"d","week":"wk","month":"mo","year":"yr"})

# --- PRESSURE ---
registry.register("pressure",
    units={"pascal":1.0,"kilopascal":1000.0,"bar":100000.0,
           "psi":6894.76,"atmosphere":101325.0,"torr":133.322},
    base_unit="pascal",
    symbols={"pascal":"Pa","kilopascal":"kPa","bar":"bar","psi":"psi","atmosphere":"atm","torr":"Torr"})

# --- ENERGY ---
registry.register("energy",
    units={"joule":1.0,"kilojoule":1000.0,"calorie":4.184,"kilocalorie":4184.0,
           "watt_hour":3600.0,"kilowatt_hour":3.6e6,"british_thermal_unit":1055.06,"electronvolt":1.602e-19},
    base_unit="joule",
    symbols={"joule":"J","kilojoule":"kJ","calorie":"cal","kilocalorie":"kcal",
             "watt_hour":"Wh","kilowatt_hour":"kWh","british_thermal_unit":"BTU","electronvolt":"eV"})

# --- LIGHT / LUMINANCE ---
registry.register("luminance",
    units={"lumen":1.0,"lux":1.0,"candela":1.0,"foot_candle":10.764,"nit":1.0},
    base_unit="lumen",
    symbols={"lumen":"lm","lux":"lx","candela":"cd","foot_candle":"fc","nit":"nt"})

# --- POWER ---
registry.register("power",
    units={"watt":1.0,"kilowatt":1000.0,"megawatt":1e6,"horsepower":745.7,
           "british_thermal_unit_per_hour":0.293071},
    base_unit="watt",
    symbols={"watt":"W","kilowatt":"kW","megawatt":"MW","horsepower":"hp","british_thermal_unit_per_hour":"BTU/h"})

# --- ANGLE ---
registry.register("angle",
    units={"degree":1.0,"radian":57.2958,"gradian":0.9,"minute":0.0166667,"second":0.000277778},
    base_unit="degree",
    symbols={"degree":"°","radian":"rad","gradian":"gon","minute":"′","second":"″"})

# =============================================================================
# API ENDPOINTS
# =============================================================================

class ConvertRequest(BaseModel):
    category: str
    value: float
    from_unit: str
    to_unit: str

@app.get("/categories")
def get_categories():
    return registry.get_metadata()

@app.post("/convert")
def convert_units(req: ConvertRequest):
    try:
        result = registry.convert(req.category, req.value, req.from_unit, req.to_unit)
        cat = registry._categories[req.category]
        from_sym = cat["symbols"].get(req.from_unit, req.from_unit)
        to_sym = cat["symbols"].get(req.to_unit, req.to_unit)
        if req.category == "temperature":
            formula = f"{req.value} {from_sym} → {result:.4f} {to_sym}"
        else:
            factor = cat["units"][req.from_unit] / cat["units"][req.to_unit]
            formula = f"{req.value} {from_sym} × {factor:.6g} = {result:.6g} {to_sym}"
        return {"result": result, "formula": formula}
    except Exception as e:
        return {"error": str(e), "result": None}

@app.get("/health")
def health():
    return {"status": "healthy", "categories": len(registry._categories)}
