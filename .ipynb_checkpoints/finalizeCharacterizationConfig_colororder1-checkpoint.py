config.psf_determiner['piff'].spatialOrderPerBand = {
	"u": 2, "g": 2, "r": 2, "i": 2, "z": 2, "y": 2,
}
config.psf_determiner['piff'].zerothOrderInterpNotEnoughStars = False
config.psf_determiner['piff'].piffBasisPolynomialSolver = "cpp"
config.psf_determiner['piff'].piffPixelGridFitCenter = False
config.psf_determiner['piff'].useColor = True
config.psf_determiner['piff'].colorOrder = 1
config.psf_determiner['piff'].color = {
	"u": "g-i", "g": "g-i", "r": "g-i", "i": "g-i", 
	"z": "i-z", "y": "i-z",
}

