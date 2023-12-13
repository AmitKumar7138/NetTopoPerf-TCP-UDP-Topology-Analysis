
# Comparative analysis of TCP/UDP performace in diverse network topology

In this project we are going through a thorough analysis of different network topologies starting from basic topologies to a hybrid network systems using mininet and miniedit GUI interface in the linux environment setup.




## Prerequisite
You would need to have a linux machine or a VM installed to have a linux runtime.
Have the git setup on this linux system to clone and install mininet. 
## Terminal commands to have mininet installed after starting your Linux setup

#### Check python version

```http
  sudo apt-get install python
  python --version
```


#### Get git

```http
  sudo apt install git
```

#### Navigate to the Downloads directory and install mininet

```http
  git clone https://github.com/mininet/mininet
  util/install.sh -a
  
```
##### Save your Python scripts (provided with the asignments) at the desired location. (Suggested: Save in the "Downloads/mininet/mininet/examples/" location)
### Run custom scripts

```http
  sudo mn --custom <python_file_name> --topo <topology_name>
  
```
topology_name can be identified by the key of the dictionary where the topologies are saved in the script.
### Once your scripts run successfully, and you enter the mininet environment:
#### ping test and rtt values:
```http
  pingall
  ping <host_name> <destination_host_name>
```
#### xterm host terminal and analyse host properties, jitter, throughput and latency from host terminal:
```http
  xterm <first_host_name_acting_as_the_server>
  xterm <second_host_name_acting_as_the_clinet>
  ifconfig
  qperf 
  iperf -s  

  OR

  iperf -s -u
```
#### One client host terminal analyse the network attributes
```http
  qperf -vvs <server_ip> tcp_lat
  qperf -vvs <server_ip> udp_lat

  
  iperf -c <server_ip> -t 10
  iperf -c <server_ip> -u -t 10 
```
![Logo](https://1000logos.net/wp-content/uploads/2022/07/University-of-Florida-Logo.png)

