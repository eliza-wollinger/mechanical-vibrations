# Mechanical Vibration Analysis Scripts 🛠️📈

Welcome to the Mechanical Vibration Analysis repository! This repository contains a collection of Python and MATLAB scripts designed for analyzing mechanical vibrations.

### Table of Contents
1. [Script 1](https://github.com/eliza-wollinger/mechanical-vibrations/edit/main/README.md#script-1-harmonic-excitation-models-): Harmonic Excitation Models
2. [Script 2](https://github.com/eliza-wollinger/mechanical-vibrations/edit/main/README.md#script-2-frequency-response-function--linear-bode-diagram-%EF%B8%8F): Frequency Response Function
3. [Script 3](https://github.com/eliza-wollinger/mechanical-vibrations/edit/main/README.md#script-3-one-degree-freedom-system-response-): One Degree Freedom System Response
4. [Script 4](https://github.com/eliza-wollinger/mechanical-vibrations/edit/main/README.md#script-4-periodic-excitation-response-): Periodic Excitation Response
5. [Script 5](https://github.com/eliza-wollinger/mechanical-vibrations/edit/main/README.md#script-5-fourier-series-): Fourier Series

## Script 1: Harmonic Excitation Models 🎵

This script provides a simple yet powerful tool for analyzing harmonic excitation models. By utilizing the capabilities of NumPy and Matplotlib in Python, it explores various aspects of harmonic vibrations, including amplitude, frequency, and phase angle.

### Script Overview
####  Variables Definition
- ```A``` and ```B``` are coefficients used in the definition of amplitude and angle calculations.
- ```frequency``` specifies the frequency of the harmonic excitation.
- ```amplitude``` is calculated based on A and B using a predefined formula.
- ```angle_phase``` is the phase angle calculated using the arctangent function.
- ```complex_amplitude``` represents the complex amplitude derived from A and B.
- ```omega``` is the angular frequency calculated from the given frequency.
- ```step``` is a constant used for defining the time and the omega matrix.
  
#### Time Definition
- ```get_delta_time()``` generates time points for the simulation.
- ```time``` stores the time points obtained from the get_delta_time() function.

#### Harmonic Equations and Plots
- Three functions (```get_func_A```, ```get_func_B```, ```get_func_C```) define three different harmonic models (modelA, modelB, modelC) based on the specified equations.
- Three subplots are created to visualize the three harmonic models over time.

#### Angular Frequency Matrix Definition
- ```get_omega_matrix()``` defines an array of angles covering the range of three times the angular frequency.
- ```omega_matrix``` stores the angular frequency matrix.
  
#### Lag/Amplitude Divergence Definition
- ```get_lag()``` calculates the lag/amplitude divergence for each angle in the omega matrix.
- ```lag``` stores the resulting lag/amplitude values.

#### Plotting Spectrum and Phase Angle
- Two subplots display the spectrum and phase angle of the harmonic excitation models.
- The spectrum is plotted against frequency in Hertz.
- The phase angle is plotted against frequency in radians.

## Script 2: Frequency Response Function / Linear Bode Diagram 🎚️
This script facilitates the generation and visualization of linear Bode diagrams for a mechanical system. Using NumPy and Matplotlib in Python, it calculates and plots the receptance (amplitude and phase) over a range of frequencies.

### Script Overview
#### Variables Definition
- ```db_ref``` is the reference value for the logarithmic scale in decibels.
- ```max_circular_frequency``` sets the upper limit for the circular frequency.
- ```frequency_points``` determines the number of frequency points to be generated.
- ```mass```, ```stiff```, ```damp_ratio``` are parameters defining the mechanical system.
- ```rad_freq``` is the natural circular frequency calculated from the system's parameters.
- ```hz_freq``` is the natural frequency in Hertz.
- ```damp represents``` the damping coefficient.
  
#### Frequency Generation
- ```get_frequency()``` generates an array of frequencies within the specified range.
- The result is stored in the ```frequency``` array.

#### Receptance Calculation
- The script calculates the receptance of the system at each frequency point using the defined mechanical parameters.
- The results are stored in the ```receptance``` array.

#### Plotting Linear Bode Diagram
- Two subplots are created to visualize the linear Bode diagram: one for the amplitude spectrum and one for the phase angle.
- The amplitude spectrum is plotted against frequency in Hertz.
- The phase angle is plotted against frequency in radians.
  
#### Plotting dB Bode Diagram
- Another set of two subplots generates a Bode diagram in decibels for better visualization of amplitude variations.
- The amplitude spectrum is plotted in decibels against frequency in Hertz.
- The phase angle remains unchanged.
  
## Script 3: One Degree Freedom System Response 🔄
This script provides a comprehensive analysis of the dynamic response of a system subjected to various excitations. Leveraging NumPy and Matplotlib in Python, it explores the time-domain response and the frequency response of the system.

### Script Overview
#### System Data Definition
- ```mass```: Mass of the system.
- ```damp_ratio```: Damping ratio of the system.
- ```stiff```: Stiffness of the system.
- ```freq_rad```: Angular frequency calculated from the stiffness and mass.
- ```damp```: Damping coefficient.
- ```natural_damp```: Natural damping frequency.
  
#### Excitation Data Definition
- ```a``` and ```b```: Coefficients used to define complex amplitude.
- ```excitation_freq```: Array of excitation frequencies.
- ```complex_amplitude```: Complex amplitude derived from a and b.
- ```receptance```: The system's receptance based on the excitation frequencies.
- ```response```: System response to the excitation.

#### Time Definition
- ```get_time()```: Generates time points for the simulation.
- ```time```: Time array for the analysis.
- 
#### Time-Domain Response and Excitation Plots
The script generates three subplots for each excitation frequency:

- ```F1``` and ```X1```: Plots the excitation and response for the first frequency.
- ```F2``` and ```X2```: Plots the excitation and response for the second frequency.
- ```F3``` and ```X3```: Plots the excitation and response for the third frequency.

#### Frequency Response Function (FRF) Analysis
- ```get_vector()```: Generates a frequency vector for FRF analysis.
- ```freq_vector```: Frequency vector for FRF analysis.
- ```frf_receptance```: Frequency response function receptance.
- ```vector_force``` and ```displacement_vector```: Vectors for force and displacement.
- ```freq_response```: Frequency response of the system.

##### Frequency Response and System Response Plots
The script generates three subplots for FRF, excitation, and system response:

- ```Receptance```, ```Excitation```, and ```Response```: Plots the receptance and compares it with the excitation and system response.

## Script 4: Periodic Excitation Response 🔄📈
Explore how systems respond to periodic excitations. Visualize and analyze the behavior of mechanical systems under repeated forces.

### Script Overview
#### Excitation and System Parameters
- ```amplitude```, ```period_parameter```, ```signal_period```, ```signal_breadth```, and ```terms_number``` define the characteristics of the excitation signal.
- ```mass```, ```stiff```, and ```damp_coeficient``` represent the system's mass, stiffness, and damping coefficient.
- Calculations are performed to obtain the fundamental frequency, no-damping frequency, and other essential system parameters.

#### Time Array Creation
- The ```get_time()``` function generates a time array for the simulation.

#### Fourier Series Computation
- The ```get_fourier_series()``` function computes the Fourier series of the system's response to harmonic excitation.
- It involves the calculation of coefficients and sums to obtain the excitation and response signals.

#### Plotting Graphs
- Two subplots display the excitation and response signals over time.

#### Receptance and Spectrum Analysis
- The script calculates the receptance of the system and plots it against frequency.
- Two additional subplots show the spectrum of the excitation and response signals.

## Script 5: Fourier Series 🔍📉
Understand and compute the Fourier series of signals. Break down complex vibrations into simpler sinusoidal components.

### Script Overview
#### Angle Array Creation
- The ```get_angle()``` function generates an array of angles for the Fourier series visualization.

#### Fourier Series Computation
- The ```get_fourier_series(A, T)``` function computes the Fourier series for a given amplitude (A) and period (T).
- The script calculates five different Fourier series with varying amplitude and period combinations.

#### Plotting Graphs
- The script uses Matplotlib to create a graph and plot the absolute values of the generated Fourier series against the angle array.
- Each Fourier series is represented by a different line on the graph, allowing for easy comparison.
