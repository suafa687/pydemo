import tensorflow as tf
import numpy as np
import pandas as pd
import timeit

# 查看设备
cpu = tf.config.list_physical_devices(device_type="CPU")
gpu = tf.config.list_physical_devices(device_type="GPU")
print( cpu, "\n", gpu)
print("-"*20)

# 设置打印设备日志
# tf.debugging.set_log_device_placement(True)

def multiply():
    a = tf.random.normal([10000,1000])
    b = tf.random.normal([1000,2000])
    c = tf.matmul(a,b)
    return c

def cpu_run():
    with tf.device("/CPU:0"):
        multiply()

def gpu_run():
    with tf.device("/GPU:0"):
        multiply()

gpu_time = timeit.timeit(gpu_run, number=1)
cpu_time = timeit.timeit(cpu_run, number=1)
print("cpu_time:",cpu_time, "\n", "gpu_time:",gpu_time)

gpu_time = timeit.timeit(gpu_run, number=100)
cpu_time = timeit.timeit(cpu_run, number=100)
print("cpu_time:",cpu_time, "\n", "gpu_time:",gpu_time)