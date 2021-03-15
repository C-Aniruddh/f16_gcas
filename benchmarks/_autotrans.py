from matlab.engine import start_matlab


def simulate_autotrans(_, T, u):
    matlab = start_matlab()

    matlab.workspace["U"] = u
    matlab.workspace["T"] = T
    result = matlab.sim(
        "autotrans_shift",
        "StopTime",
        "T",
        "LoadExternalInput",
        "on",
        "ExternalInput",
        "u",
        "SaveTime",
        "on",
        "TimeSaveName",
        "tout",
        "SaveOutput",
        "on",
        "OutputSaveName",
        "yout",
        "SaveFormat",
        "Array",
    )

    return result.tout, result.yout
