import os

os.system("gnome-terminal -x python3 ./Executive_producer/producer1.py")
os.system("gnome-terminal -x python3 ./Executive_producer/producer2.py")
os.system("gnome-terminal -x python3 ./Executive_producer/producer3.py")
os.system("gnome-terminal -x python3 ./Executive_producer/producer4.py")

os.system("gnome-terminal -x python3 ./consumers/consumer1.py")
os.system("gnome-terminal -x python3 ./consumers/consumer2.py")
os.system("gnome-terminal -x python3 ./consumers/consumer3.py")
os.system("gnome-terminal -x python3 ./consumers/consumer4.py")

os.system("gnome-terminal -x python3 ./consumers/AggregatedConsumer.py")

os.system("gnome-terminal -x echo 'wating'")
os.system("gnome-terminal -x echo 'wating'")
os.system("gnome-terminal -x echo 'wating'")
os.system("gnome-terminal -x echo 'wating'")

os.system("gnome-terminal -x python3 ./Executive_producer/ExecutiveProducer.py")
