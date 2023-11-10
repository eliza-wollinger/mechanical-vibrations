import numpy 
import matplotlib

# Defining variables
A = 10
B = 20

frequency = 3
amplitude = numpy.sqrt(A*numpy.exp(2)+B*numpy.exp(2))
angle_phase = numpy.arctan(-B/A)
complex_amplitude = (A-1j*B)/2
omega = 2*numpy.pi*frequency
step = 0.013

# Defining time
def get_delta_time():
  number_of_points = 2000
  delta = 0.001
  time = []

  for i in range(number_of_points):
    time.append(i*delta)
  return time

time = get_delta_time()

# Defining harmonic equations
def get_model(func):
  model=[]
  for i in time:
    model.append(func(i))
  return model

def get_func_A(i):
  return amplitude*numpy.cos(omega*i+angle_phase)

def get_func_B(i):
  return A*numpy.cos(omega*i)+B*numpy.sin(omega*i)

def get_func_C(i):
  return complex_amplitude*numpy.exp(1j*omega*i)+(complex_amplitude)*numpy.exp(-1j*omega*i)

modelA = get_model(get_func_A)
modelB = get_model(get_func_B)
modelC = get_model(get_func_C)

# Plotting harmonic excitation models
figure, axis = matplotlib.pyplot.subplots(3)
figure.suptitle('Harmonic excitation models')
axis[0].plot(time, modelA)
axis[1].plot(time, modelB)
axis[2].plot(time, modelC)

# Defining angle omega
def get_omega_matrix():
  index = 0
  angles = []

  while (index <= (3*omega)):
    angles.append(index)
    index += step
  return angles

# Defining the lag/divergence
omega_matrix = get_omega_matrix()

def get_lag():
  index = 0
  lag = numpy.zeros(len(omega_matrix), dtype=complex)

  while (index < len(lag)):
    if (numpy.absolute(omega-omega_matrix[index]) <= step):
      lag[index] = complex_amplitude
    index += 1
  return lag

lag = get_lag()

# Plotting spectrum and phase angle
figure, axis = matplotlib.pyplot.subplots(2)
figure.suptitle('Spectrum and Phase Angle')

half_pi = 2/numpy.pi

axis[0].plot([x/half_pi for x in omega_matrix],2*numpy.abs(lag))
axis[0].set_xlabel('Frequency [Hz]')
axis[0].set_ylabel('Spectrum [N]')
axis[0].axis([0,3*omega,0,50])

axis[1].plot([x/half_pi for x in omega_matrix],numpy.angle(lag))
axis[1].set_xlabel('Frequency [Hz]')
axis[1].set_ylabel('Phase angle [rad]')
axis[1].axis([0,3*omega,-numpy.pi,0])
