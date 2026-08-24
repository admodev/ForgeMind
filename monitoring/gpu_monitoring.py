import pynvml

pynvml.nvmlInit()

handle = pynvml.nvmlDeviceGetHandleByIndex(0)

def GetGPUTemp():
    return pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)

def GetGPUStatus():
    heat = f"{GetGPUTemp()}°C"

    return f"""

🌡️ Heat = {heat}
        """

