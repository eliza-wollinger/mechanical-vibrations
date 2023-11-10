clear all 
clc

% Defining variables
frequency1 = 3.5;
frequency2 = 5;

A1 = 10;
A2 = 0;
B1 = 0;                         
B2 = 20;

amplitud1 = sqrt(A1^2+B1^2);  
phase_angle1=atan(-B1/A1); 
complex_amplitud1 = (A1-1i*B1)/2;

amplitud2 = sqrt(A2^2+B2^2);
phase_angle2 = atan(-B2/A2);
complex_amplitud2 = (A2-1i*B2)/2;

points = 2000;
delta_time = 0.001;
final_time = delta_time*points;
vector_time = 0:delta_time:final_time;

excitation_frequency1 = 2*pi*f1;
excitation_frequency2 = 2*pi*f2;

signal = A1*cos(excitation_frequency1*vector_time)+B1*sin(excitation_frequency1*vector_time)+A2*cos(excitation_frequency2*vector_time)+B2*sin(excitation_frequency2*vector_time);

plot(vector_time, signal)

signal_model1 = amplitud1*cos(excitation_frequency1*vector_time+phase_angle1)+amplitud2*cos(excitation_frequency2*vector_time+phase_angle2);
signal_model2 = A1*cos(excitation_frequency1*vector_time)+B1*sin(excitation_frequency1*vector_time)+A2*cos(excitation_frequency2*vector_time)+B2*sin(excitation_frequency2*vector_time);
signal_model3 = complex_amplitud1*exp(1i*excitation_frequency1*vector_time)+ conj(complex_amplitud1)*exp(-1i*excitation_frequency1*vector_time)+complex_amplitud2*exp(1i*excitation_frequency2*vector_time)+ conj(complex_amplitud2)*exp(-1i*excitation_frequency2*vector_time); % signal with model 3

figure()
subplot(3,1,1)
plot(vector_time, signal_model1)

subplot(3,1,2)
plot(vector_time, signal_model2)
ylabel('Harmonic function [N]')

subplot(3,1,3)
plot(vector_time, signal_model2)
xlabel('Time [s]')

inc = 0.013;
frequency_array = 0:inc:3*excitation_frequency2;

FF1=zeros(length(frequency_array),1);
FF2=zeros(length(frequency_array),1);
for ii=1:length(frequency_array)
    if abs(excitation_frequency1-frequency_array(ii))<=inc 
           FF1(ii)=complex_amplitud1;
    end    
    if abs(excitation_frequency2-frequency_array(ii))<=inc 
           FF2(ii)=complex_amplitud2;
    end   
end


figure(2)
subplot(2,1,1)
plot(frequency_array/2/pi,2*abs(FF1),frequency_array/2/pi,2*abs(FF2))
xlabel('Frequency [Hz]')
ylabel('Spectrum [N]')
axis([0 3*excitation_frequency1 0 50])

subplot(2,1,2)
plot(frequency_array/2/pi,angle(FF1),frequency_array/2/pi,angle(FF2))
xlabel('Frequency [Hz]')
ylabel('Phase angle [rad]')
axis([0 3*excitation_frequency1 -pi 0])