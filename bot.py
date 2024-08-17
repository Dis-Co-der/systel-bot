import requests
import os
from dotenv import load_dotenv
import psutil
import GPUtil
from pynvml import nvmlInit, nvmlDeviceGetHandleByIndex, nvmlDeviceGetPowerUsage

load_dotenv('.venv/.env')

bot_key=os.environ['BOT_KEY']
chat_id=os.environ['CHAT_ID']

# Initialize NVML
nvmlInit()

# Function to get GPU information
def get_gpu_info():
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        gpu_id = gpu.id
        handle = nvmlDeviceGetHandleByIndex(gpu_id)
        power_usage = nvmlDeviceGetPowerUsage(handle) / 1000 
        return {
            "id": gpu_id,
            "name": gpu.name,
            "load": gpu.load * 100,
            "temperature": gpu.temperature,
            "memory_used": gpu.memoryUsed / 1024,  
            "memory_total": gpu.memoryTotal / 1024,
            "power_usage": power_usage
        }

# Function to get system information
def get_system_info():
    return {
        "cpu_percent": psutil.cpu_percent(),
        "ram_used": psutil.virtual_memory().used / (1024 ** 3),  
        "ram_total": psutil.virtual_memory().total / (1024 ** 3) 
    }

# Function to send a message via Telegram
def send_telegram_message(message):
    bot_token = bot_key  
    bot_chatID = chat_id  
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&text={message}'
    response = requests.get(send_text)
    return response.json()

# Function to monitor and send updates
def monitor_and_notify():
    gpu_info = get_gpu_info()
    system_info = get_system_info()

    message = (
        f"GPU: {gpu_info['name']}\n"
        f"Temperature: {gpu_info['temperature']}°C\n"
        f"Power Usage: {gpu_info['power_usage']}W\n"
        f"GPU Load: {gpu_info['load']}%\n"
        f"GPU Memory: {gpu_info['memory_used']}/{gpu_info['memory_total']} GB\n\n"
        f"CPU Usage: {system_info['cpu_percent']}%\n"
        f"RAM Usage: {system_info['ram_used']}/{system_info['ram_total']} GB"
    )

    send_telegram_message(message)

#Monitor and notify every 30 minutes
if __name__ == "__main__":
    import schedule
    import time
    
    print("Bot is now live and monitoring system...")

    # Schedule the task_you can change the value accordingly
    schedule.every(30).minutes.do(monitor_and_notify)

    while True:
        schedule.run_pending()
        time.sleep(1)
