import modal

stub = modal.Stub("example-get-started")


@stub.function()
def square(x):
    print("This code is running on a remote worker!")
    return x**2


@stub.local_entrypoint()
def main():
    print("the square is", square.call(42))

exit() # 萬一從 terminal 執行，到此為止。下面是用 Jupyter lab 執行的實驗。

# {GitHub}/modal-examples/01_getting_started/hello_world.py
# 在 JupyterLab 中用 scratchpad 方式執行的方式是 with stub.run() 如下： 

    with stub.run():
        print("the square is", square.call(42))
