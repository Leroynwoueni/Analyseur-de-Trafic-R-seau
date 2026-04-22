from models.network import Network
from services.simulator import Simulator

def main():
    network = Network()
    
    # créer quelques nœuds et liens
    network.add_node("A")
    network.add_node("B")
    network.connect_nodes("A", "B")

    simulator = Simulator(network)
    simulator.run(steps=10)

if __name__ == "__main__":
    main()