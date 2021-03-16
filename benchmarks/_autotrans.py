from matlab.engine import connect_matlab


def simulate_autotrans(_, T, u):
    matlab = connect_matlab()

    matlab.workspace["u"] = u
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

    return results.yout, result.tout
