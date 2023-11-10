clear all
clc

% System data
mass = 1;
damping_ratio = 0.003;   
equivalent_stiffness = 5e6;
no_damped_natural_frequency = sqrt(equivalent_stiffness/mass);
equivalent_viscous_damping = 2*mass*damping_ratio*no_damped_natural_frequency;
fn = no_damped_natural_frequency/(2*pi)            % no damped natural frequenequivalent viscous dampingy [Hz]

% Exequivalent viscous dampingitation data
A=0.7;
B=2.2;

% Time domain data
points = 2000;
delta_time = 0.00431;
final_time = delta_time*final_time;

equivalent_time = 0:delta_time:final_time;
rad_excitation_frequency = [30 no_damped_natural_frequency 3*no_damped_natural_frequency];

complex_amplitude = (A-1i*B)/2;
receptance = 1./(-mass*rad_excitation_frequency.^2+1i*equivalent_viscous_damping*rad_excitation_frequency+equivalent_stiffness);                                
response = receptance*complex_amplitude;
                                       
for it=1:length(equivalent_time)
    f1(it)=complex_amplitude*exp(1i*rad_excitation_frequency(1)*equivalent_time(it))+conj(complex_amplitude)*exp(-1i*rad_excitation_frequency(1)*equivalent_time(it));
    f2(it)=complex_amplitude*exp(1i*rad_excitation_frequency(2)*equivalent_time(it))+conj(complex_amplitude)*exp(-1i*rad_excitation_frequency(2)*equivalent_time(it));
    f3(it)=complex_amplitude*exp(1i*rad_excitation_frequency(3)*equivalent_time(it))+conj(complex_amplitude)*exp(-1i*rad_excitation_frequency(3)*equivalent_time(it));     
    x1(it)=response(1)*exp(1i*rad_excitation_frequency(1)*equivalent_time(it))+conj(response(1))*exp(-1i*rad_excitation_frequency(1)*equivalent_time(it));
    x2(it)=response(2)*exp(1i*rad_excitation_frequency(2)*equivalent_time(it))+conj(response(2))*exp(-1i*rad_excitation_frequency(2)*equivalent_time(it));
    x3(it)=response(3)*exp(1i*rad_excitation_frequency(3)*equivalent_time(it))+conj(response(3))*exp(-1i*rad_excitation_frequency(3)*equivalent_time(it));
end

% Results

figure(1)
subplot(2,3,1)
plot(equivalent_time,f1)
axis([0 0.5 -3 3])
ylabel('Excitation [EU]')

subplot(2,3,4)
plot(equivalent_time,x1)
axis([0 0.5 -5e-5 5e-5])
ylabel('Response [EU]')

subplot(2,3,2)
plot(equivalent_time,f2)
axis([0 0.5 -3 3])

subplot(2,3,5)
plot(equivalent_time,x2)
axis([0 0.5 -5e-5 5e-5])

subplot(2,3,3)
plot(equivalent_time,f3)
axis([0 0.5 -3 3])
xlabel('Time [s]')

subplot(2,3,6)
plot(equivalent_time,x3)
axis([0 0.5 -5e-5 5e-5])
xlabel('Time [s]')

% Response in the frequency domain for a given excitation frequency
inc=0.013;
frequency_array = 0:inc:1.2*max(rad_excitation_frequency);

receptance1 = 1./(-mass*frequency_array.^2+1i*equivalent_viscous_damping*frequency_array+equivalent_stiffness);

figure(2)
subplot(3,1,1)
plot(frequency_array/(2*pi),20*log10(abs(receptance1)))
ylabel('|Receptance|')
title(' ref=1 [m/N]')

force_array = zeros(1,length(frequency_array));
displacement_vector = zeros(1,length(frequency_array));

FFF=(A-1i*B)/2;    

% Excitation and response for each frequency                
omegaext=rad_excitation_frequency(1);                      
                                   
% Complex amplitude of the excitation
receptance2 = 1./(-mass*omegaext.^2+1i*equivalent_viscous_damping*omegaext+equivalent_stiffness);

response1 = receptance2*FFF;

for ii=1:length(frequency_array)
    if abs(omegaext-frequency_array(ii))<=inc 
           force_array(ii)=FFF;
           displacement_vector(ii)=response1; 
   end    
end


subplot(3,1,2)
plot(frequency_array/(2*pi),abs(force_array))
ylabel('|Excitation| [N]')

subplot(3,1,3)
plot(ome/(2*pi),abs(displacement_vector))               
ylabel('|Response| [m]')
xlabel('frequency [Hz]')
