export const FALLBACK_CATEGORIES = {
  length: {
    base_unit: "meter",
    units: [
      {id:"meter",symbol:"m",name:"Meter"},
      {id:"centimeter",symbol:"cm",name:"Centimeter"},
      {id:"millimeter",symbol:"mm",name:"Millimeter"},
      {id:"kilometer",symbol:"km",name:"Kilometer"},
      {id:"inch",symbol:"in",name:"Inch"},
      {id:"foot",symbol:"ft",name:"Foot"},
      {id:"yard",symbol:"yd",name:"Yard"},
      {id:"mile",symbol:"mi",name:"Mile"},
      {id:"nautical_mile",symbol:"nmi",name:"Nautical Mile"},
    ]
  },
  temperature: {
    base_unit: "celsius",
    units: [
      {id:"celsius",symbol:"°C",name:"Celsius"},
      {id:"fahrenheit",symbol:"°F",name:"Fahrenheit"},
      {id:"kelvin",symbol:"K",name:"Kelvin"},
    ]
  },
  weight: {
    base_unit: "gram",
    units: [
      {id:"gram",symbol:"g",name:"Gram"},
      {id:"kilogram",symbol:"kg",name:"Kilogram"},
      {id:"milligram",symbol:"mg",name:"Milligram"},
      {id:"metric_ton",symbol:"t",name:"Metric Ton"},
      {id:"pound",symbol:"lb",name:"Pound"},
      {id:"ounce",symbol:"oz",name:"Ounce"},
      {id:"stone",symbol:"st",name:"Stone"},
      {id:"us_ton",symbol:"ton (US)",name:"US Ton"},
    ]
  },
  volume: {
    base_unit: "liter",
    units: [
      {id:"liter",symbol:"L",name:"Liter"},
      {id:"milliliter",symbol:"mL",name:"Milliliter"},
      {id:"cubic_meter",symbol:"m³",name:"Cubic Meter"},
      {id:"gallon_us",symbol:"gal (US)",name:"Gallon (US)"},
      {id:"quart_us",symbol:"qt (US)",name:"Quart (US)"},
      {id:"pint_us",symbol:"pt (US)",name:"Pint (US)"},
      {id:"cup_us",symbol:"cup",name:"Cup (US)"},
      {id:"fluid_ounce_us",symbol:"fl oz",name:"Fluid Ounce (US)"},
      {id:"tablespoon_us",symbol:"tbsp",name:"Tablespoon (US)"},
      {id:"teaspoon_us",symbol:"tsp",name:"Teaspoon (US)"},
      {id:"gallon_uk",symbol:"gal (UK)",name:"Gallon (UK)"},
      {id:"pint_uk",symbol:"pt (UK)",name:"Pint (UK)"},
    ]
  },
  data: {
    base_unit: "byte",
    units: [
      {id:"byte",symbol:"B",name:"Byte"},
      {id:"kilobyte",symbol:"KB",name:"Kilobyte"},
      {id:"megabyte",symbol:"MB",name:"Megabyte"},
      {id:"gigabyte",symbol:"GB",name:"Gigabyte"},
      {id:"terabyte",symbol:"TB",name:"Terabyte"},
      {id:"petabyte",symbol:"PB",name:"Petabyte"},
      {id:"bit",symbol:"b",name:"Bit"},
    ]
  },
  area: {
    base_unit: "square_meter",
    units: [
      {id:"square_meter",symbol:"m²",name:"Square Meter"},
      {id:"square_kilometer",symbol:"km²",name:"Square Kilometer"},
      {id:"square_centimeter",symbol:"cm²",name:"Square Centimeter"},
      {id:"square_mile",symbol:"mi²",name:"Square Mile"},
      {id:"square_yard",symbol:"yd²",name:"Square Yard"},
      {id:"square_foot",symbol:"ft²",name:"Square Foot"},
      {id:"acre",symbol:"ac",name:"Acre"},
      {id:"hectare",symbol:"ha",name:"Hectare"},
    ]
  },
  speed: {
    base_unit: "meter_per_second",
    units: [
      {id:"meter_per_second",symbol:"m/s",name:"Meter per Second"},
      {id:"kilometer_per_hour",symbol:"km/h",name:"Kilometer per Hour"},
      {id:"mile_per_hour",symbol:"mph",name:"Mile per Hour"},
      {id:"knot",symbol:"kn",name:"Knot"},
      {id:"foot_per_second",symbol:"ft/s",name:"Foot per Second"},
    ]
  },
  time: {
    base_unit: "second",
    units: [
      {id:"second",symbol:"s",name:"Second"},
      {id:"minute",symbol:"min",name:"Minute"},
      {id:"hour",symbol:"h",name:"Hour"},
      {id:"day",symbol:"d",name:"Day"},
      {id:"week",symbol:"wk",name:"Week"},
      {id:"month",symbol:"mo",name:"Month"},
      {id:"year",symbol:"yr",name:"Year"},
    ]
  },
  pressure: {
    base_unit: "pascal",
    units: [
      {id:"pascal",symbol:"Pa",name:"Pascal"},
      {id:"kilopascal",symbol:"kPa",name:"Kilopascal"},
      {id:"bar",symbol:"bar",name:"Bar"},
      {id:"psi",symbol:"psi",name:"PSI"},
      {id:"atmosphere",symbol:"atm",name:"Atmosphere"},
      {id:"torr",symbol:"Torr",name:"Torr"},
    ]
  },
  energy: {
    base_unit: "joule",
    units: [
      {id:"joule",symbol:"J",name:"Joule"},
      {id:"kilojoule",symbol:"kJ",name:"Kilojoule"},
      {id:"calorie",symbol:"cal",name:"Calorie"},
      {id:"kilocalorie",symbol:"kcal",name:"Kilocalorie"},
      {id:"watt_hour",symbol:"Wh",name:"Watt Hour"},
      {id:"kilowatt_hour",symbol:"kWh",name:"Kilowatt Hour"},
      {id:"british_thermal_unit",symbol:"BTU",name:"BTU"},
      {id:"electronvolt",symbol:"eV",name:"Electronvolt"},
    ]
  },
  luminance: {
    base_unit: "lumen",
    units: [
      {id:"lumen",symbol:"lm",name:"Lumen"},
      {id:"lux",symbol:"lx",name:"Lux"},
      {id:"candela",symbol:"cd",name:"Candela"},
      {id:"foot_candle",symbol:"fc",name:"Foot Candle"},
      {id:"nit",symbol:"nt",name:"Nit"},
    ]
  },
  power: {
    base_unit: "watt",
    units: [
      {id:"watt",symbol:"W",name:"Watt"},
      {id:"kilowatt",symbol:"kW",name:"Kilowatt"},
      {id:"megawatt",symbol:"MW",name:"Megawatt"},
      {id:"horsepower",symbol:"hp",name:"Horsepower"},
      {id:"british_thermal_unit_per_hour",symbol:"BTU/h",name:"BTU per Hour"},
    ]
  },
  angle: {
    base_unit: "degree",
    units: [
      {id:"degree",symbol:"°",name:"Degree"},
      {id:"radian",symbol:"rad",name:"Radian"},
      {id:"gradian",symbol:"gon",name:"Gradian"},
      {id:"minute",symbol:"′",name:"Arcminute"},
      {id:"second",symbol:"″",name:"Arcsecond"},
    ]
  },
};

export const CATEGORY_NAMES: Record<string, string> = {
  length: "Length",
  temperature: "Temperature",
  weight: "Weight",
  volume: "Volume",
  data: "Digital Storage",
  area: "Area",
  speed: "Speed",
  time: "Time",
  pressure: "Pressure",
  energy: "Energy",
  luminance: "Light / Luminance",
  power: "Power",
  angle: "Angle",
};
