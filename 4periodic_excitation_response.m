clear all
clc

% Excitation data
amplitude = 1.0;
signal_breadhth = 0.1;
period_parameter = 2;
period = period_parameter*signal_breadhth;
series_terms = 100;

points = 2000;
delta_time = 0.00131;
final_time = delta_time*points;
hz_fundamental_frequency = 1/period;
time_vector = 0:delta_time:final_time;
rad_fundamental_frequency = 2*pi*hz_fundamental_frequency;

% Sistem data   
mass=20;
damping_coeficient = 0.05;
stiffness_parameters = (2.*rad_fundamental_frequency)^2*mass;

rad_non_damped_natural_frequency = sqrt(stiffness_parameters/mass);
damping_coeficient = 2*mass*damping_coeficient*rad_non_damped_natural_frequency;
hz_non_damped_natural_frequency = rad_non_damped_natural_frequency/(2*pi)
half_value_f = amplitude/m;
half_value_x = (1/stiffness_parameters)*half_value_f;

for it=1:length(time_vector)
   sum=0.0;
   sum2=0.0;
  for ii=1:series_terms
    omeg(ii)=ii*rad_fundamental_frequency; 
    F(ii)=amplitude/m*sin(omeg(ii)*signal_breadhth/2)/(omeg(ii)*signal_breadhth/2);
    H(ii)=1/(-mass*omeg(ii)^2+1i*omeg(ii)*damping_coeficient+stiffness_parameters); 
    X(ii)=H(ii)*F(ii); 
    sum=sum+conj(F(ii))*exp(-1i*omeg(ii)*time_vector(it))+F(ii)*exp(1i*omeg(ii)*t(it));
    sum2=sum2+conj(X(ii))*exp(-1i*omeg(ii)*time_vector(it))+X(ii)*exp(1i*omeg(ii)*t(it));
  end
  f(it)=sum+half_value_f;
  x(it)=sum2+half_value_x;
end

figure(1)
subplot(2,1,1)
plot(time_vector,f)
ylabel('Excitation [EU]')

subplot(2,1,2)
plot(time_vector,x)
xlabel('Time [s]')
ylabel('Response [m]')

receptance = 1./(-mass*omeg.^2+1i*damping_coeficient*omeg+stiffness_parameters);

figure(3)
subplot(3,1,1)
plot(omeg(1:50)/2/pi,abs(receptance(1:50)))
ylabel('|Receptance| [m/N]')

subplot(3,1,2)
stem(omeg(1:50)/2/pi,abs(F(1:50)))
ylabel('Spectrum [N]')

subplot(3,1,3)
stem(omeg(1:50)/2/pi,abs(X(1:50)))
ylabel('Spectrum [m]')
xlabel('FRequency [Hz]')
