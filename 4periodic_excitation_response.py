import numpy
import matplotlib

# Defining excitation data
amplitude = 1
period_parameter = 2
signal_period = numpy.pi / 5
signal_breadhth = signal_period / period_parameter
terms_number = 500

fundamental_frequency_hz = 1 / signal_period
fundamental_frequency_rad = 2 * numpy.pi * fundamental_frequency_hz

# Defining system data
mass = 1
stiff = 10000
damp_coeficient = 0.001

no_damp_frequency_rad = numpy.sqrt(stiff/mass)
no_damp_frequency_hz = no_damp_frequency_rad / (2 * numpy.pi)
damp = 2 * mass * damp_coeficient * no_damp_frequency_rad

half_f = amplitude / period_parameter
half_x = (1 / stiff) * half_f

# Creating time array
def get_time():
  index = 0
  time_array = []
  domain_number = 2000
  time_increment = 0.00131
  while(index < domain_number):
    if index == 0:
      time_array.append(0)
      index += 1
    else:
      time_array.append(time_array[index-1] + time_increment)
      index += 1
  return numpy.array(time_array)

time = get_time()

def get_fourier_series():
  step = numpy.zeros(terms_number, dtype = complex)  
  F = numpy.zeros(terms_number, dtype = complex)
  H = numpy.zeros(terms_number, dtype = complex)
  X = numpy.zeros(terms_number, dtype = complex)
  f = numpy.zeros(len(time), dtype = complex)
  x = numpy.zeros(len(time), dtype = complex)

  i = 1
  while (i < len(time)):
    j = 1
    sum1 = 0.0
    sum2 = 0.0
    while (j < terms_number):
      step[j] = j * fundamental_frequency_rad
      F[j] = amplitude / period_parameter * numpy.sin((step[j]) * signal_breadhth/2) / (step[j]) * signal_breadhth/2
      H[j] = 1 / (-mass * step[j] * numpy.exp(2 + 1j * step[j] * damp + stiff))
      X[j] = H[j] * F[j]
      sum1 = numpy.conj( F[j] * numpy.exp( -1j * step[j] * time[i] ) + F[j] * numpy.exp( 1j * step[j] * damp * stiff ) )
      sum2 = numpy.conj( X[j] * numpy.exp( -1j * step[j] * time[i] ) + X[j] * numpy.exp(1j * step[j] * damp * stiff ))

      j += 1

    f[i] = sum1 + half_f
    x[i] = sum2 + half_x

    i += 1

  params = {
      'F': F,
      'X': X,
      'f': f,
      'x': x,
      'step': step
  }

  return params

fourier_series = get_fourier_series()

# Ploting graphs
figure, axis = matplotlib.pyplot.subplots(2)
axis[0].plot(time, fourier_series['f'])
axis[0].set_xlabel('Time [s]')
axis[0].set_ylabel('Excitation [EU]')
axis[1].plot(time, fourier_series['x'])
axis[1].set_xlabel('Time [s]')
axis[1].set_ylabel('Response [m]')

receptance = 1 / ( -mass * fourier_series['step'] * numpy.power(( 2 + 1j * damp * fourier_series['step'] + stiff)))

figure, axis = matplotlib.pyplot.subplots(3)
axis[0].plot((fourier_series['step'][1:50])/(2/numpy.pi), numpy.abs(receptance[1:50]))
axis[0].set_xlabel('Time [s]')
axis[0].set_ylabel('Receptance [m/N]')
axis[1].plot((fourier_series['step'][1:50])/(2/numpy.pi), fourier_series['F'][1:50])
axis[1].set_xlabel('Time [s]')
axis[1].set_ylabel('Spectrum [N]')
axis[2].plot((fourier_series['step'][1:50])/(2/numpy.pi), fourier_series['F'][1:50])
axis[2].set_xlabel('Frequency [Hz]')
axis[2].set_ylabel('Spectrum [m]')