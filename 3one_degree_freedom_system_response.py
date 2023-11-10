import numpy 
import matplotlib

# Defining system data
mass = 1
damp_ratio = 0.003
stiff = 5*numpy.exp(6)
freq_rad = numpy.sqrt(stiff/mass)
damp = 2*mass*damp_ratio*freq_rad
natural_damp = freq_rad/(2*numpy.pi)

# Defining excitation data
a = 0.7
b = 2.2

excitation_freq = numpy.array([30, freq_rad, 3*freq_rad])
complex_amplitude = (a-1j*b)/2
receptance = 1. / (-mass * excitation_freq * numpy.exp(2) + 1j * excitation_freq * damp + stiff)
response = complex_amplitude*receptance

def get_time():
  step = 0.00431
  number_of_points = 2000
  final_time = step*number_of_points
  index = 0
  time_array = []
  while(index < number_of_points):
    if index == 0:
      time_array.append(0)
      index += 1
    else:
      time_array.append(time_array[index-1] + step)
      index += 1
  return numpy.array(time_array)

time = get_time()

func = [[],[],[]]
x = [[],[],[]]

for i in range(len(func)):
  for j in range(len(time)):
    x[i].append(response[i]*numpy.exp(1j*excitation_freq[i]*time[j])+numpy.conj(response[i])*numpy.exp(-1j*excitation_freq[i]*time[j]))
    func[i].append(complex_amplitude*numpy.exp(1j*excitation_freq[i]*time[j])+numpy.conj(complex_amplitude)*numpy.exp(-1j*excitation_freq[i]*time[j]))


figure, axis = matplotlib.pyplot.subplots(2)
figure.suptitle('F1 and X1')
axis[0].plot(time,func[0])
axis[0].axis([0, 0.5, -3, 3])
axis[0].set_xlabel('Time [s]')
axis[0].set_ylabel('Excitation [EU]')
axis[1].plot(time, x[0])
axis[1].axis([0, 0.5, -5*numpy.exp(-5), 5*numpy.exp(-5)])
axis[1].set_xlabel('Time [s]')
axis[1].set_ylabel('Response [EU]')

figure, axis = matplotlib.pyplot.subplots(2)
figure.suptitle('F2 and X2')
axis[0].plot(time,func[1])
axis[0].axis([0, 0.5, -3, 3])
axis[0].set_xlabel('Time [s]')
axis[0].set_ylabel('Excitation [EU]')
axis[1].plot(time, x[1])
axis[1].axis([0, 0.5, -5*numpy.exp(-5), 5*numpy.exp(-5)])
axis[1].set_xlabel('Time [s]')
axis[1].set_ylabel('Response [EU]')

figure, axis = matplotlib.pyplot.subplots(2)
figure.suptitle('F3 and X3')
axis[0].plot(time,func[2])
axis[0].axis([0, 0.5, -3, 3])
axis[0].set_xlabel('Time [s]')
axis[0].set_ylabel('Excitation [EU]')
axis[1].plot(time, x[2])
axis[1].axis([0, 0.5, -5*numpy.exp(-5), 5*numpy.exp(-5)])
axis[1].set_xlabel('Time [s]')
axis[1].set_ylabel('Response [EU]')

def get_vector():
  step = 0.013
  index = 0
  vector_freq = []
  while (index < 1.2*numpy.max(excitation_freq)):
    vector_freq.append(index+step)
    index += 1
  return numpy.array(vector_freq)

freq_vector = get_vector()
frf_receptance = 1. / -mass * freq_vector * numpy.exp(2) + 1j * freq_vector * damp + stiff

vector_force = numpy.zeroes(1, len(freq_vector))
displacement_vector = numpy.zeroes(1, len(freq_vector))
freq_response = (a-1j*b)/2

figure, axis = matplotlib.pyplot.subplots(3)
figure.suptitle('Receptance, Excitation and Response')
axis[0].plot(freq_vector/(2*numpy.pi), 20*numpy.log10(numpy.abs(frf_receptance)))
axis[0].axis([0, 0.5, -3, 3])
axis[0].set_title('ref=1 [m/N]')
axis[0].set_xlabel('Time [s]')
axis[0].set_ylabel('Receptance')
axis[1].plot(time, x[2])
axis[1].axis([0, 0.5, -5*numpy.exp(-5), 5*numpy.exp(-5)])
axis[1].set_xlabel('Time [s]')
axis[1].set_ylabel('Response [EU]')