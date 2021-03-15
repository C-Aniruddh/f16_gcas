from matlab.engine import start_matlab


def simulate_autotrans(X, U):
    matlab = start_matlab()
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
