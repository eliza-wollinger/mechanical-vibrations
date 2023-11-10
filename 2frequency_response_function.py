import numpy 
import matplotlib

# Defining variables
db_ref = 1*numpy.exp(-6)
max_circular_frequency = 1000
frequency_points = 10000

mass = 10
stiff = 3.16*numpy.exp(5)
damp_ratio = 0.01
rad_freq = numpy.sqrt(stiff/mass)
hz_freq = rad_freq/(2*numpy.pi)
damp = 2*mass*damp_ratio

def get_frequency():
  frequencies = []
  domain_frequency = max_circular_frequency/frequency_points
  index = 0
  while(index < max_circular_frequency):
    frequencies.append(index)
    index += domain_frequency
  return numpy.array(frequencies)

print(get_frequency())

frequency = get_frequency()
receptance = 1. / (-mass * frequency * numpy.exp(2) + 1j * frequency * damp + stiff)
print(receptance)

figure, axis = matplotlib.pyplot.subplots(2)
figure.suptitle('Linear Bode Diagram')
axis[0].plot(frequency/(2*numpy.pi), numpy.abs(receptance))
axis[0].set_xlabel('Frequency [Hz]')
axis[0].set_ylabel('Receptance [m/N]')
axis[0].set_title('Spectrum')
axis[1].plot(frequency/(2*numpy.pi), numpy.angle(receptance))
axis[1].set_xlabel('Frequency [Hz]')
axis[1].set_ylabel('Phase Angle [rad]')

figure, axis = matplotlib.pyplot.subplots(2)
figure.suptitle('dB Bode Diagram')
axis[0].plot(frequency/(2*numpy.pi), 10*numpy.log10(numpy.abs(receptance)/db_ref))
axis[0].set_xlabel('Frequency [Hz]')
axis[0].set_ylabel('Receptance [m/N]')
axis[0].set_title('Spectrum')
axis[1].plot(frequency/(2*numpy.pi), numpy.angle(receptance))
axis[1].set_xlabel('Frequency [Hz]')
axis[1].set_ylabel('Phase Angle [rad]')