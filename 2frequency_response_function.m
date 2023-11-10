clear all
clc

db_ref = 1e-6;
maximum_circular_value = 3000;
discretization_points = 10000;

beam_lenght = 0.4;
material_elasticity_modulus = 20e10;
material_density = 7850;
material_width = 40e-3;
material_height = 10e-3;

beam_mass = material_width*material_height*beam_lenght*material_density;
second_moment = material_width*material_height^3/12;
kb=3*material_elasticity_modulus*second_moment/beam_lenght^3;
k=kb%+keq1

system_mass = 0.203*beam_mass
damping_ratio = 0.1;

rad_undamped_natural_frequency = sqrt(k/system_mass);
hz_undamped_natural_frequency = rad_undamped_natural_frequency/2/pi;
damping = 2*m*damping_ratio*rad_undamped_natural_frequency

Domega = maximum_circular_value / discretization_points;
array_frequency = 0:Domega:maximum_circular_value;

receptance = 1./(-system_mass*array_frequency.^2+1i*array_frequency*damping+k);

figure(1) % Linear Bode diagram
subplot(2,1,1)
plot(array_frequency/(2*pi),abs(receptance))
xlabel('Frequency [Hz]')
ylabel('Receptance [m/N]')
title('Spectrum')
subplot(2,1,2)
plot(array_frequency/(2*pi),angle(receptance))
xlabel('Frequency [Hz]')
ylabel('Phase angle [rad]')
xlabel('frequency [Hz]')