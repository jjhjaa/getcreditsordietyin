import cx_Freeze

executables = [cx_Freeze.Executable("peli.py")]

cx_Freeze.setup(
    name="Get nobs or die tryin",
    options={"build_exe": {"packages":["pygame"],
                "included_files":['lobo.png', 'beer.png', "dice.png", "kela.PNG", "joonaskali.wav",
                "joonakalii.wav", "joonaskaliii.wav", "maijumauu.wav",
              "matuhavisit.wav"]}},

    executables=executables
)