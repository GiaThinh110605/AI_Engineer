from qiskit import QuantumCircuit
import matplotlib.pyplot as plt 

# 2 đầu tiên: là số lượng qubit
# 2 thứ hai: là số lượng bit cổ điển, để lưu kết quả khi đo
qc = QuantumCircuit(2, 2)

qc.h(0)

# cnot gate
# control: (qubit: 0), target: (qubit: 1)
# khi qubit 0 có trí 1, thì target đổi 0 -> 1, hoặc 1 -> 0
qc.cx(0, 1)

# qc.measure([qubits], [danh sách bit cổ điển])
# 0 -> 0, 1 -> 1
qc.measure([0, 1], [0, 1])

print(qc.draw())
print("final circuit")
qc.draw("mpl")


