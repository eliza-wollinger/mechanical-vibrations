import numpy
import matplotlib.pyplot as plt

def get_angle():
  index = 0
  angle_array = []
  number_of_points = 10000
  angle_domain = 5000
  while (index < angle_domain):
    angle_array.append(index)
    index += angle_domain/(number_of_points-1)
  return numpy.array(angle_array)

angle = get_angle()
print(angle)

def get_fourier_series(A, T):
  omega = angle*T
  amp = A*T/2
  fourier_series = (amp/numpy.pi) * numpy.sin(omega/2) / (omega/2)
  return numpy.array(fourier_series)

fourier1 = get_fourier_series(1, 1)
fourier2 = get_fourier_series(10, 0.1)
fourier3 = get_fourier_series(100, 0.01)
fourier4 = get_fourier_series(1000, 0.001)
fourier5 = get_fourier_series(10000, 0.0001)

graph = plt.gca()
graph.set_facecolor((0.11, 0.11, 0.125))
graph.set_xlabel('Frequency [Hz]')
graph.set_ylabel('| F |')
graph.plot(angle, abs(fourier1))
graph.plot(angle, abs(fourier2))
graph.plot(angle, abs(fourier3))
graph.plot(angle, abs(fourier4))
graph.plot(angle, abs(fourier5))
graph.legend(['A=1 T=1', 'A=10 T=0.1', 'A=100 T=0.01', 'A=1000 T=0.001', 'A=10000 T=0.0001'], loc=1)